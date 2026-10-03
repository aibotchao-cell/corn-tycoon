# -*- coding: utf-8 -*-
"""產生《玉米罐頭大亨》PWA 圖示：綠底 + 玉米罐頭"""
from PIL import Image, ImageDraw

S = 1024

def draw_icon(size):
    img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # 背景：綠色漸層
    for y in range(S):
        t = y / S
        r = int(0x74 + (0x46 - 0x74) * t)
        g = int(0xc8 + (0x8f - 0xc8) * t)
        b = int(0x5e + (0x36 - 0x5e) * t)
        d.line([(0, y), (S, y)], fill=(r, g, b, 255))
    # 草地：底部深綠丘陵（用實色疊，不用 alpha，否則 PIL 會直接覆蓋成半透明）
    d.ellipse([-S * 0.35, S * 0.62, S * 1.35, S * 1.35], fill=(0x4e, 0x94, 0x3e, 255))
    d.ellipse([-S * 0.20, S * 0.74, S * 1.20, S * 1.45], fill=(0x45, 0x86, 0x36, 255))

    # 罐頭（置中）
    cw, ch = int(S * 0.46), int(S * 0.60)
    cx, cy = (S - cw) // 2, (S - ch) // 2 + int(S * 0.02)
    # 陰影
    d.ellipse([cx - 30, cy + ch - 40, cx + cw + 30, cy + ch + 60], fill=(20, 50, 16, 90))
    # 罐身
    d.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=int(cw * 0.16), fill=(0xd9, 0xdf, 0xe7, 255))
    # 上下金屬邊
    rim = int(ch * 0.13)
    d.rounded_rectangle([cx, cy, cx + cw, cy + rim], radius=int(cw * 0.10), fill=(0xb2, 0xbc, 0xc7, 255))
    d.rounded_rectangle([cx, cy + ch - rim, cx + cw, cy + ch], radius=int(cw * 0.10), fill=(0xb2, 0xbc, 0xc7, 255))
    # 標籤（黃）
    ly0, ly1 = cy + int(ch * 0.24), cy + int(ch * 0.76)
    d.rectangle([cx, ly0, cx + cw, ly1], fill=(0xf2, 0xc3, 0x3d, 255))
    d.rectangle([cx, ly0, cx + cw, ly0 + int(ch * 0.02)], fill=(0xc9, 0x94, 0x1c, 255))
    d.rectangle([cx, ly1 - int(ch * 0.02), cx + cw, ly1], fill=(0xc9, 0x94, 0x1c, 255))

    # 標籤上的玉米
    bx, by = cx + cw // 2, (ly0 + ly1) // 2
    bw, bh = int(cw * 0.30), int((ly1 - ly0) * 0.78)
    # 玉米葉
    d.ellipse([bx - bw * 0.95, by - bh * 0.05, bx - bw * 0.05, by + bh * 0.85], fill=(0x4f, 0x9a, 0x2f, 255))
    d.ellipse([bx + bw * 0.05, by - bh * 0.05, bx + bw * 0.95, by + bh * 0.85], fill=(0x63, 0xbd, 0x3e, 255))
    # 玉米穗
    d.rounded_rectangle([bx - bw / 2, by - bh / 2, bx + bw / 2, by + bh / 2],
                        radius=int(bw * 0.5), fill=(0xe8, 0xb5, 0x2a, 255))
    # 玉米粒
    for r in range(5):
        for c in range(3):
            px = bx - bw * 0.30 + c * bw * 0.30
            py = by - bh * 0.32 + r * bh * 0.16
            d.ellipse([px - bw * 0.07, py - bw * 0.07, px + bw * 0.07, py + bw * 0.07],
                      fill=(0xff, 0xd9, 0x5e, 255))

    # 反光
    d.rounded_rectangle([cx + int(cw * 0.10), cy + rim + 8, cx + int(cw * 0.22), cy + ch - rim - 8],
                        radius=int(cw * 0.06), fill=(255, 255, 255, 90))
    # 邊框
    d.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=int(cw * 0.16), outline=(0x8f, 0x9a, 0xa6, 255), width=6)

    return img.resize((size, size), Image.LANCZOS)

for sz in (512, 192, 180):
    draw_icon(sz).save('corn-icon-%d.png' % sz)
    print('wrote corn-icon-%d.png' % sz)
