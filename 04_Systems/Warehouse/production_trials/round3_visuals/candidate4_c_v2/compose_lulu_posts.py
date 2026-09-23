from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parent
GEN_DIR = Path(r"C:\Users\user\.codex\generated_images\01a0cc57-59f0-76b0-8ac1-d46176641da3")
FACE_REF = Path(r"C:\Users\user\Desktop\有的沒的小舖\魯魯\寫實生圖規格包\00_official_refs\lulu_ref_face.jpg")
PHOTO_A = GEN_DIR / "call_OYGUIzPzherAPYx7C9vJzhnA.png"
PHOTO_B = GEN_DIR / "call_LcI04nFZ2mnnX1nJMd5bdsyb.png"

FONT_REG = r"C:\Windows\Fonts\NotoSansTC-VF.ttf"
FONT_BOLD = r"C:\Windows\Fonts\Noto Sans SC Bold (TrueType).otf"
FONT_EMOJI = r"C:\Windows\Fonts\seguiemj.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size=size)


def fit_cover(img, size):
    img = img.convert("RGB")
    w, h = img.size
    tw, th = size
    scale = max(tw / w, th / h)
    nw, nh = int(w * scale), int(h * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - tw) // 2
    top = (nh - th) // 2
    return img.crop((left, top, left + tw, top + th))


def rounded_mask(size, radius):
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    return mask


def paste_round(base, img, xy, radius):
    mask = rounded_mask(img.size, radius)
    base.paste(img, xy, mask)


def circle_crop(img, size):
    img = fit_cover(img, (size, size))
    mask = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse((0, 0, size - 1, size - 1), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img.convert("RGBA"), (0, 0), mask)
    return out


def text_w(draw, text, fnt):
    if not text:
        return 0
    return draw.textbbox((0, 0), text, font=fnt)[2]


def draw_mixed_text(draw, xy, text, fnt, fill):
    x, y = xy
    emoji_font = ImageFont.truetype(FONT_EMOJI, size=fnt.size)
    for ch in text:
        use_font = emoji_font if ch == "😂" else fnt
        draw.text((x, y), ch, font=use_font, fill=fill)
        x += text_w(draw, ch, use_font)


def wrap_text(draw, text, fnt, max_width):
    lines = []
    current = ""
    for ch in text:
        if ch == "\n":
            lines.append(current)
            current = ""
            continue
        trial = current + ch
        if text_w(draw, trial, fnt) <= max_width or not current:
            current = trial
        else:
            lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, xy, text, fnt, fill, max_width, line_gap=8):
    x, y = xy
    for line in wrap_text(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        bbox = draw.textbbox((x, y), line or "口", font=fnt)
        y = bbox[3] + line_gap
    return y


def bubble(draw, xy, name, text, color, max_width):
    x, y = xy
    name_font = font(28, True)
    body_font = font(30)
    name_w = text_w(draw, name, name_font)
    body_lines = wrap_text(draw, text, body_font, max_width - 44)
    body_w = max([text_w(draw, line, body_font) for line in body_lines] + [0])
    bw = max(name_w + 44, body_w + 44, 180)
    line_h = 39
    bh = 28 + len(body_lines) * line_h + 26
    draw.rounded_rectangle((x, y, x + bw, y + bh), radius=26, fill=color)
    draw.text((x + 22, y + 14), name, font=name_font, fill=(44, 49, 57))
    ty = y + 51
    for line in body_lines:
        draw_mixed_text(draw, (x + 22, ty), line, body_font, (30, 35, 42))
        ty += line_h
    return y + bh


def add_comment(draw, x, y, avatar_color, name, text, max_width):
    draw.ellipse((x, y + 5, x + 48, y + 53), fill=avatar_color)
    return bubble(draw, (x + 66, y), name, text, (242, 243, 245), max_width) + 16


def compose(photo_path, out_path, caption, comments, timestamp):
    W, H = 1080, 1350
    base = Image.new("RGB", (W, H), (247, 248, 250))
    draw = ImageDraw.Draw(base)

    card_x, card_y = 50, 44
    card_w, card_h = 980, 1260
    shadow = Image.new("RGBA", (card_w + 36, card_h + 36), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((18, 18, card_w + 18, card_h + 18), radius=38, fill=(0, 0, 0, 55))
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    base.paste(shadow, (card_x - 18, card_y - 14), shadow)
    draw.rounded_rectangle((card_x, card_y, card_x + card_w, card_y + card_h), radius=36, fill=(255, 255, 255))

    pad = 34
    header_y = card_y + 30
    avatar = circle_crop(Image.open(FACE_REF), 68)
    base.paste(avatar, (card_x + pad, header_y), avatar)
    draw.text((card_x + pad + 86, header_y + 2), "有的沒的小舖", font=font(32, True), fill=(23, 26, 31))
    draw.text((card_x + pad + 86, header_y + 42), timestamp, font=font(22), fill=(122, 129, 139))
    draw.text((card_x + card_w - pad - 40, header_y + 15), "•••", font=font(36, True), fill=(98, 105, 115))

    photo_size = 760
    photo_x = card_x + pad
    photo_y = header_y + 94
    photo = fit_cover(Image.open(photo_path), (photo_size, photo_size))
    paste_round(base, photo, (photo_x, photo_y), 22)

    icon_y = photo_y + photo_size + 22
    icon_font = font(34, True)
    for i, glyph in enumerate(["♡", "◌", "↗"]):
        draw.text((photo_x + i * 58, icon_y), glyph, font=icon_font, fill=(34, 38, 45))
    draw.text((photo_x + photo_size - 34, icon_y), "▱", font=icon_font, fill=(34, 38, 45))

    cap_y = icon_y + 56
    cap_font = font(31)
    draw.text((photo_x, cap_y), "有的沒的小舖", font=font(31, True), fill=(20, 23, 28))
    name_width = text_w(draw, "有的沒的小舖  ", font(31, True))
    cap_y = draw_wrapped(draw, (photo_x + name_width, cap_y), caption, cap_font, (20, 23, 28), photo_size - name_width, 5)

    sep_y = cap_y + 13
    draw.line((photo_x, sep_y, photo_x + photo_size, sep_y), fill=(233, 236, 240), width=2)

    y = sep_y + 22
    for avatar_color, name, text in comments:
        y = add_comment(draw, photo_x, y, avatar_color, name, text, photo_size - 66)

    base.save(ROOT / out_path, quality=95)


compose(
    PHOTO_A,
    "post_A.png",
    "魯魯今天的表情包 #日常",
    [
        ((206, 221, 246), "小港仔", "這個叫無辜攻擊吧😂"),
        ((234, 216, 229), "路過的書友", "截圖存起來，這張太可以。"),
    ],
    "今天 14:08",
)

compose(
    PHOTO_B,
    "post_B.png",
    "上次你們自己取的名字：無辜攻擊。是你們取的，我沒說過。以後你們在這裡取的每一個名字，我都可能之後拿來用。",
    [
        ((206, 221, 246), "小港仔", "等等這隻貓認真的？？"),
    ],
    "兩週後 19:32",
)
