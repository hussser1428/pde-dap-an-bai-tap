# Bài tập phương trình đạo hàm riêng (PDE)

Bộ tài liệu tiếng Việt gồm **336 mục**: 99 ví dụ, 233 bài tập thực hành và 4 bài nâng cao. Mỗi mục có bản Markdown để đọc trong IDE và bản PDF. Đề gốc giữ bằng ảnh; lời giải bổ sung được soạn bằng LaTeX.

**[Mở mục lục và chọn bài](MUC_LUC_PDE.md)** · [Kiến thức và phương pháp](PDE_Tach_bai_va_loi_giai/00_Kien_thuc_va_phuong_phap.md) · [Hướng dẫn sử dụng](PDE_Tach_bai_va_loi_giai/HUONG_DAN.md) · [PDF lời giải tổng hợp](loi_giai_tong_hop.pdf)

## Nội dung

| Chương | Chủ đề | Tình trạng |
|---|---|---|
| 1 | Phương trình cấp một | 93 mục có kiến thức và lời giải chi tiết |
| 2 | Phương trình cấp hai | 27 mục có kiến thức và lời giải chi tiết |
| 3 | Phương trình sóng | 85 mục có kiến thức và lời giải chi tiết |
| 4 | Phương trình nhiệt | 50 mục có kiến thức và lời giải chi tiết |
| 5 | Phương trình Laplace | Giữ nội dung đã biên soạn |
| 6 | Chuỗi Fourier | Giữ nội dung đã biên soạn |

Lời giải Chương 1–4 trình bày cách chọn phương pháp, các phép tính trung gian, cách dùng dữ liệu đầu/biên và kiểm tra kết quả. Những đề có ký hiệu không thống nhất, thiếu dữ kiện hoặc kết luận sai được phân tích ngay trong từng bài. Chuỗi và tích phân xác định được giữ khi đó là dạng tự nhiên của nghiệm.

Có **322 mục với lời giải bổ sung bằng chữ** trong PDF tổng hợp 469 trang. Các ví dụ còn lại giữ phần trình bày gốc bằng ảnh. Đây là bản biên soạn học tập, không phải lời giải chính thức của tác giả tài liệu nguồn.

## Cách đọc

- Mở [mục lục](MUC_LUC_PDE.md), rồi chọn file Markdown của bài.
- Trong VS Code, dùng **Ctrl+Shift+V** để xem công thức và ảnh.
- Bản PDF của từng bài giữ phần scan gốc ở đầu và lời giải bổ sung ở sau.
- Nguồn LaTeX nằm trong [Nguon_loi_giai](PDE_Tach_bai_va_loi_giai/Nguon_loi_giai); mã vẽ nằm trong [Ma_ve_do_thi](PDE_Tach_bai_va_loi_giai/Ma_ve_do_thi).

## Tải đủ tài liệu

PDF nguồn `pde bài tập.pdf` được lưu bằng **Git LFS**. Cài Git LFS trước khi clone; sau khi clone, chạy:

```powershell
git lfs install
git lfs pull
```

Các PDF bài riêng, ảnh đề, đồ thị và bản tổng hợp được lưu trực tiếp trong repository.

## Nguồn xử lý và kiểm tra

Thư mục `_xu_ly` chứa các nguồn lời giải, bộ hướng dẫn theo chương, mã xuất Markdown/PDF và kiểm tra độc lập. Các file scan trung gian, bộ nhớ đệm, bản sao dự phòng và log biên dịch được bỏ khỏi Git.

Python cần `numpy`, `scipy`, `matplotlib`, `Pillow` và `PyMuPDF`. PDF LaTeX dùng **XeLaTeX** với font Times New Roman. Khi biên dịch một bài riêng, chạy từ thư mục `PDE_Tach_bai_va_loi_giai` để các đường dẫn đồ thị hợp lệ.

Chương 4 có 394 phép kiểm tra số về hệ số Fourier, biên và chuẩn Robin, tích phân thời gian, Gauss/erfc, phương trình và nhân Green. Các kiểm tra bản xuất đối chiếu đầy đủ nội dung Markdown, LaTeX và PDF, đường dẫn ảnh và số trang.
