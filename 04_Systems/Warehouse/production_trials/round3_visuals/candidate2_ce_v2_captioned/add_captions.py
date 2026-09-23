from pathlib import Path
from shutil import copyfile

from PIL import Image, ImageDraw, ImageFont


SOURCE_DIR = Path(
    r"C:\Users\user\Desktop\MyProjects01\AIOS\04_Systems\Warehouse\production_trials\round3_visuals\candidate2_ce_v2"
)
OUTPUT_DIR = Path(__file__).resolve().parent
FONT_PATH = Path(r"C:\Windows\Fonts\msjh.ttc")

PANELS = [
    ("panel_1.png", "panel_1_captioned.png", ""),
    ("panel_2.png", "panel_2_captioned.png", "你有完沒完？"),
    ("panel_3.png", "panel_3_captioned.png", "還不走？"),
    ("panel_4.png", "panel_4_captioned.png", ""),
]


def load_font(image_height: int, text: str, max_width: int) -> ImageFont.ImageFont:
    size = max(24, int(image_height * 0.047))
    font_file = str(FONT_PATH) if FONT_PATH.exists() else None

    while size >= 14:
        try:
            font = ImageFont.truetype(font_file, size) if font_file else ImageFont.load_default(size=size)
        except TypeError:
            font = ImageFont.load_default()

        bbox = ImageDraw.Draw(Image.new("RGB", (1, 1))).textbbox((0, 0), text, font=font, stroke_width=2)
        if bbox[2] - bbox[0] <= max_width:
            return font
        size -= 2

    return font


def add_caption(src: Path, dst: Path, caption: str) -> None:
    with Image.open(src) as image:
        base = image.convert("RGBA")
        width, height = base.size
        margin = int(height * 0.05)

        font = load_font(height, caption, int(width * 0.9))
        draw_probe = ImageDraw.Draw(base)
        stroke = max(2, int(height * 0.004))
        text_bbox = draw_probe.textbbox((0, 0), caption, font=font, stroke_width=stroke)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        pad_x = int(width * 0.04)
        pad_y = int(height * 0.018)
        band_height = text_height + pad_y * 2
        band_top = height - margin - band_height
        band_bottom = height - margin

        overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.rectangle((0, band_top, width, band_bottom), fill=(0, 0, 0, 150))

        x = (width - text_width) / 2 - text_bbox[0]
        y = band_top + (band_height - text_height) / 2 - text_bbox[1]
        overlay_draw.text(
            (x, y),
            caption,
            font=font,
            fill=(255, 255, 255, 255),
            stroke_width=stroke,
            stroke_fill=(0, 0, 0, 255),
        )

        result = Image.alpha_composite(base, overlay)
        result.convert(image.mode if image.mode in ("RGB", "RGBA") else "RGB").save(dst)


def main() -> None:
    outputs = []
    for source_name, output_name, caption in PANELS:
        src = SOURCE_DIR / source_name
        dst = OUTPUT_DIR / output_name
        if not src.exists():
            raise FileNotFoundError(src)

        if caption:
            add_caption(src, dst, caption)
        else:
            copyfile(src, dst)

        outputs.append(dst)

    print("Generated files:")
    for path in outputs:
        with Image.open(path) as image:
            print(f"- {path.name}: {image.size[0]}x{image.size[1]}")


if __name__ == "__main__":
    main()
