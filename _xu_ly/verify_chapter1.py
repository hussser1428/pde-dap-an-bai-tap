"""Kiểm tra độc lập các nghiệm và bước tương tác được bổ sung ở Chương 1."""
from pathlib import Path
import json
import re
import numpy as np
import fitz

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT/'PDE_Tach_bai_va_loi_giai'
H = 1e-20

def first_derivatives(fn,x,y):
    return fn(x,y), np.imag(fn(x+1j*H,y))/H, np.imag(fn(x,y+1j*H))/H

def transport(a,b,c,source):
    return lambda x,y,u,p,q:a(x,y)*p+b(x,y)*q+c(x,y)*u-source(x,y)

one=lambda x,y:1
zero=lambda x,y:0
exp=np.exp
cases={
    'VD_1_2_2_2_05':(lambda x,y:2*y+exp(-x*x)*np.sin(y),transport(one,zero,lambda x,y:2*x,lambda x,y:4*x*y)),
    'VD_1_3_1_2_04':(lambda x,y:(y-2*x)**2*exp(-y/2)/4,transport(one,lambda x,y:2,one,zero)),
    'VD_1_3_1_2_06':(lambda x,y:exp(2*y)*np.sin((y-2*x)**2/4)+exp(x+1.5*y)-exp(x+y),transport(one,lambda x,y:2,lambda x,y:-4,lambda x,y:exp(x+y))),
    'BT_1_3_1_3_03_b':(lambda x,y:.5+exp(-y)*(2*(x-y/2)**2+3*(x-y/2)-.5),transport(one,lambda x,y:2,lambda x,y:2,one)),
    'BT_1_3_1_3_03_c':(lambda x,y:x*x/6+exp(x)/3+2*(x+3*y/4)**2+3*(x+3*y/4)-(x+3*y/4)**2/6-exp(x+3*y/4)/3,transport(lambda x,y:3,lambda x,y:-4,zero,lambda x,y:x+exp(x))),
    'BT_1_3_1_3_03_d':(lambda x,y:y**3+2*(x-y/3)**2+3*(x-y/3),transport(one,lambda x,y:3,zero,lambda x,y:9*y*y)),
    'BT_1_3_1_3_04_b':(lambda x,y:-exp(x+y)+exp(4*x)*(1-(y-2*x)/3)*exp(4*(y-2*x)/3),transport(one,lambda x,y:2,lambda x,y:-4,lambda x,y:exp(x+y))),
    'BT_1_3_1_3_10':(lambda x,y:x-3+3*exp((y-x)/5),transport(lambda x,y:3,lambda x,y:-2,one,lambda x,y:x)),
    'BT_1_3_2_3_04':(lambda x,y:exp(y)*np.sin(x*y),transport(lambda x,y:x,lambda x,y:-y,lambda x,y:y,zero)),
    'BT_1_3_2_3_05':(lambda x,y:y+1+exp(y)*np.sin(x*y),transport(lambda x,y:x,lambda x,y:-y,lambda x,y:y,lambda x,y:y*y)),
    'BT_1_3_2_3_06_b_hom':(lambda x,y:x*x*y*y*exp(y-x*y),transport(lambda x,y:x,lambda x,y:-y,lambda x,y:y,zero)),
    'BT_1_3_2_3_06_b_source':(lambda x,y:y+1+exp(y-x*y)*(x*x*y*y-x*y-1),transport(lambda x,y:x,lambda x,y:-y,lambda x,y:y,lambda x,y:y*y)),
    'BT_1_3_2_3_08_b':(lambda x,y:np.sin(x*exp(-y*y/2)),transport(lambda x,y:x*y,one,zero,zero)),
    'BT_1_3_2_3_08_c':(lambda x,y:(x+y*y)**3/x,transport(lambda x,y:-2*x*y,lambda x,y:x,lambda x,y:-2*y,zero)),
    'VD_1_4_2_02_d':(lambda x,y:(x-5*y**4/4)/(1+y**3/3)+5*y,lambda x,y,u,p,q:q+y*y*u*p-5),
    'BT_1_5_3_01_a':(lambda x,y:(x/2+2*y)**2,lambda x,y,u,p,q:p*p+p*q-5*u),
    'BT_1_5_3_01_b':(lambda x,y:(2.5*x-2*y)**2,lambda x,y,u,p,q:p*p+p*q-5*u),
    'BT_1_5_3_02_a':(lambda x,y:((7*x-3*y)/4)**2,lambda x,y,u,p,q:p*p-5*q*q-u),
    'BT_1_5_3_02_b':(lambda x,y:((3*x+y)/4)**2,lambda x,y,u,p,q:p*p-5*q*q-u),
    'BT_1_5_3_04_a':(lambda x,y:(1-x*x)/2+y,lambda x,y,u,p,q:p*p+q*q+2*x*p+2*y*q-2*u),
    'BT_1_5_3_04_b':(lambda x,y:(1-x*x)/2-y,lambda x,y,u,p,q:p*p+q*q+2*x*p+2*y*q-2*u),
    'BT_1_5_3_05_b':(lambda x,y:(x*x+y*y)/2-2*x*y,lambda x,y,u,p,q:p*p+q*q+2*y*p+2*x*q-2*u),
    'BT_1_5_3_06_a':(lambda x,y:2*y*y,lambda x,y,u,p,q:4*p*p+q*q+4*(p-x)*(q-4*y)-8*u),
    'BT_1_5_3_06_b':(lambda x,y:4*x*y-6*y*y,lambda x,y,u,p,q:4*p*p+q*q+4*(p-x)*(q-4*y)-8*u),
    'BT_1_5_3_08':(lambda x,y:x*y,lambda x,y,u,p,q:p*q-u),
    'BT_1_5_3_11':(lambda x,y:x+y*y/(1+2*x),lambda x,y,u,p,q:p+q*q/2-1),
    'BT_1_5_3_12':(lambda x,y:x/2,lambda x,y,u,p,q:2*x*p*p+y*q-u),
    'BT_1_5_3_14_a':(lambda x,y:exp(y),lambda x,y,u,p,q:p*p+q*q-u*u),
    'BT_1_5_3_14_b':(lambda x,y:exp(-y),lambda x,y,u,p,q:p*p+q*q-u*u),
    'BT_1_5_3_15_a':(lambda x,y:exp(np.sqrt(x*x+y*y)-1),lambda x,y,u,p,q:p*p+q*q-u*u),
    'BT_1_5_3_15_b':(lambda x,y:exp(1-np.sqrt(x*x+y*y)),lambda x,y,u,p,q:p*p+q*q-u*u),
    'BT_1_5_3_16_a':(lambda x,y:(np.sqrt(x*x+y*y)+1)**2/4,lambda x,y,u,p,q:p*p+q*q-u),
    'BT_1_5_3_16_b':(lambda x,y:(3-np.sqrt(x*x+y*y))**2/4,lambda x,y,u,p,q:p*p+q*q-u),
    'BT_1_5_3_18_a':(lambda x,y:(x+y/2)**2,lambda x,y,u,p,q:p*p-3*q*q-u),
    'BT_1_5_3_18_b':(lambda x,y:(x-y/2)**2,lambda x,y,u,p,q:p*p-3*q*q-u),
}
residuals={}
for ident,(fn,op) in cases.items():
    error=max(abs(op(x,y,*first_derivatives(fn,x,y))) for x,y in [(0.2,0.4),(0.7,0.8),(1.3,-.15)])
    assert error<1e-9,(ident,error)
    residuals[ident]=float(error)
for y in [-.7,0,.8]:
    assert abs(cases['BT_1_3_1_3_04_b'][0](y,-y)-y)<1e-10
    for ident in ['BT_1_3_2_3_06_b_hom','BT_1_3_2_3_06_b_source']:
        assert abs(cases[ident][0](1,y)-y*y)<1e-10
for x in [.2,.6,1.2]:
    for ident in ['BT_1_3_1_3_03_b','BT_1_3_1_3_03_c','BT_1_3_1_3_03_d']:
        assert abs(cases[ident][0](x,0)-(2*x*x+3*x))<1e-10
    assert abs(cases['BT_1_3_2_3_08_c'][0](x,0)-x*x)<1e-10

def param3(s,t,sign):
    disc=64*s**3*(s+1)
    Q=(4*s-8*s*s+sign*np.sqrt(disc))/(2*(1-8*s))
    p0=2*s-Q
    E=exp(-8*Q*t)
    X=s+p0*(1-E)/(4*Q)
    Y=s*E*E+s*s*(E-E*E)/Q
    U=s*s*E
    return np.array([X,Y,U,p0*E,Q])

def param5(s,t,branch):
    q0=0 if branch==1 else -2*s
    R=s+q0
    D0=s-q0
    D=D0*exp(4*t)
    S=(s+R)*exp(2*t)-R
    T=(s-D0/3)*exp(-2*t)+D0*exp(4*t)/3
    X,Y=(S+T)/2,(S-T)/2
    p,q=(R+D)/2,(R-D)/2
    U=(p*p+q*q+2*Y*p+2*X*q)/2
    return np.array([X,Y,U,p,q])

parameter_errors={}
for name,fn,ss,branches,op in [
    ('BT_1_5_3_03',param3,[.2,.7,1.5,-1.5],[-1,1],lambda x,y,u,p,q:p*p+8*q*u-8*y*q*q),
    ('BT_1_5_3_05',param5,[.4,1.2,-.8],[1,2],lambda x,y,u,p,q:p*p+q*q+2*y*p+2*x*q-2*u),
]:
    error=0
    for s in ss:
        for branch in branches:
            for t in [-.025,0,.035]:
                v=fn(s,t,branch)
                error=max(error,abs(op(*v)))
                for axis in ['s','t']:
                    d=np.imag(fn(s+1j*H if axis=='s' else s,t+1j*H if axis=='t' else t,branch))/H
                    error=max(error,abs(d[2]-v[3]*d[0]-v[4]*d[1]))
    assert error<1e-8,(name,error)
    parameter_errors[name]=float(error)

# Independently check shock speed in the changing states after interactions.
shock_specs=[
    ('VD_1_6_2_03',lambda t:np.sqrt(2*t),3,lambda t,s:s/t,lambda t,s:0,lambda u:u*u/2),
    ('BT_1_6_3_10',lambda t:3**(2/3)*t**(1/3)-1,5,lambda t,s:np.sqrt((s+1)/t),lambda t,s:0,lambda u:u**3/3),
    ('BT_1_6_3_11',lambda t:1-np.sqrt(2*t),4,lambda t,s:1,lambda t,s:1+(1-s)/t,lambda u:u-u*u/2),
    ('BT_1_6_3_12_middle',lambda t:2*np.sqrt(t),2,lambda t,s:s/t,lambda t,s:0,lambda u:u*u/2),
    ('NC_1_7_03',lambda t:np.sqrt(2*(t+1))-1,3,lambda t,s:(s+1)/(t+1),lambda t,s:0,lambda u:u*u/2),
    ('NC_1_7_04_middle',lambda t:3*np.sqrt(2*t)-1,4,lambda t,s:(s+1)/t,lambda t,s:0,lambda u:u*u/2),
    ('NC_1_7_04_final',lambda t:np.sqrt(20*t)-2,24,lambda t,s:(s+2)/t,lambda t,s:0,lambda u:u*u/2),
]
for name,fn,t,left,right,flux in shock_specs:
    s=fn(t); speed=np.imag(fn(t+1j*H))/H
    ul,ur=left(t,s),right(t,s)
    assert abs(speed-(flux(ul)-flux(ur))/(ul-ur))<1e-10,name
for xi in [-.9,-.5,-.1]:
    def time(z):return 2*(2-z)/(3*(1-z)**2)
    def pos(z):return z+z*z*time(z)
    ratio=(np.imag(pos(xi+1j*H))/H)/(np.imag(time(xi+1j*H))/H)
    assert abs(ratio-(1+xi*xi)/2)<1e-10,('NC_1_7_02',xi)
joins=[
    (2,1+2/2,np.sqrt(4)),
    (3,1+3/3,3**(2/3)*3**(1/3)-1),
    (2,-2/2,1-np.sqrt(4)),
    (1,1+1,2*np.sqrt(1)),(4,2*np.sqrt(4),4/2+2),
    (.5,1+2.5*.5,2*.5+1.25),
    (9/8,2*(9/8)+1.25,3*np.sqrt(2*(9/8))-1),
    (18,3*np.sqrt(36)-1,18/2+8),
    (20,20/2+8,np.sqrt(400)-2),
]
assert all(abs(a-b)<1e-10 for t,a,b in joins)

rows=json.loads((OUT/'manifest.json').read_text(encoding='utf-8'))
chapter=[row for row in rows if row['section'].startswith('1.')]
assert len(chapter)==93
for row in chapter:
    md=OUT/Path(row['file']).with_suffix('.md')
    value=md.read_text(encoding='utf-8')
    assert '## Kiến thức và trình tự giải' in value
    assert '## Lời giải áp dụng cho bài' in value
    assert value.count('$$')%2==0,md
    for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',value):
        assert (md.parent/link).resolve().exists(),(md,link)
    with fitz.open(OUT/row['file']) as doc:
        assert len(doc)==row['original_pages']+row['solution_pages'],row['id']
        solution=re.sub(r'\s+','',''.join(p.get_text() for p in list(doc)[row['original_pages']:]))
        assert 'Kiếnthứcvàtrìnhtựgiải' in solution,row['id']
        assert 'Lờigiảiápdụngchobài' in solution,row['id']
    editable=(OUT/'Nguon_loi_giai'/(row['id']+'.tex')).read_text(encoding='utf-8')
    assert 'Kiến thức và trình tự giải' in editable,row['id']
report={'chapter1_items':93,'explicit_pde_checks':len(cases),'residuals':residuals,
        'parametric_pde_and_gradient_checks':parameter_errors,
        'shock_speed_checks':len(shock_specs)+3,'interaction_joins':len(joins),
        'markdown_pdf_and_editable_sources':'passed'}
(ROOT/'_xu_ly'/'verification_chapter1.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
