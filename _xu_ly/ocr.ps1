$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType=WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType=WindowsRuntime]
$asTask = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' } | Select-Object -First 1
function Await($op, $type) {
    $task = $asTask.MakeGenericMethod($type).Invoke($null, @($op))
    $task.Wait()
    return $task.Result
}
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language, Windows.Globalization, ContentType=WindowsRuntime]::new('en-US'))
$baseDir = $PSScriptRoot
$outDir = Join-Path $baseDir 'ocr'
New-Item -ItemType Directory -Path $outDir -Force | Out-Null
foreach ($img in (Get-ChildItem -LiteralPath (Join-Path $baseDir 'pages') -Filter '*.png' | Sort-Object Name)) {
    $outFile = Join-Path $outDir ($img.BaseName + '.json')
    if (Test-Path -LiteralPath $outFile) { continue }
    $file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($img.FullName)) ([Windows.Storage.StorageFile])
    $stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    $decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bitmap = Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $result = Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
    $lines = @($result.Lines | ForEach-Object {
        $words = @($_.Words | ForEach-Object { @{text=$_.Text; x=$_.BoundingRect.X; y=$_.BoundingRect.Y; w=$_.BoundingRect.Width; h=$_.BoundingRect.Height} })
        @{text=$_.Text; words=$words}
    })
    @{page=[int]$img.BaseName; width=$bitmap.PixelWidth; height=$bitmap.PixelHeight; text=$result.Text; lines=$lines} | ConvertTo-Json -Depth 8 -Compress | Set-Content -LiteralPath $outFile -Encoding UTF8
    $bitmap.Dispose()
    $stream.Dispose()
    Write-Output ('OCR page ' + $img.BaseName)
}
