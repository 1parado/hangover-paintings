"""批量压缩画廊图片：最长边 1400px，JPEG q82，转存 site/img_opt"""
from pathlib import Path
from PIL import Image

src = Path(r'E:\draw\site\img')
dst = Path(r'E:\draw\site\img_opt')
dst.mkdir(exist_ok=True)

total_in = total_out = 0
for f in sorted(src.iterdir()):
    im = Image.open(f)
    im = im.convert('RGB') if im.mode != 'RGB' else im
    w, h = im.size
    scale = 1400 / max(w, h)
    if scale < 1:
        im = im.resize((round(w*scale), round(h*scale)), Image.LANCZOS)
    out = dst / (f.stem + '.jpg')
    im.save(out, 'JPEG', quality=82, optimize=True, progressive=True)
    total_in += f.stat().st_size
    total_out += out.stat().st_size
    print(f'{f.name} {f.stat().st_size//1024}KB -> {out.name} {out.stat().st_size//1024}KB')

print(f'TOTAL {total_in//1024}KB -> {total_out//1024}KB')
