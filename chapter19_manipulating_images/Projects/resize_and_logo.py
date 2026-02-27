# Lautarocuello98 - resize_and_logo.py
# Batch image resizing + conditional logo watermarking

from pathlib import Path
from PIL import Image

# ===== Configuration =====
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "catlogo.png"
OUTPUT_DIR_NAME = "with_logo"
SUPPORTED_FORMATS = (".png", ".jpg", ".jpeg", ".gif", ".bmp")


def resize_image(image: Image.Image, max_size: int) -> Image.Image:
    """Resize image proportionally to fit within max_size x max_size."""
    image.thumbnail((max_size, max_size))
    return image


def apply_logo(image: Image.Image, logo: Image.Image) -> Image.Image:
    """Apply logo to bottom-right corner if image is large enough."""
    width, height = image.size
    logo_width, logo_height = logo.size

    if width < logo_width * 2 or height < logo_height * 2:
        print("Skipping logo (image too small).")
        return image

    image.paste(
        logo,
        (width - logo_width, height - logo_height),
        logo
    )
    return image


def process_images():
    base_dir = Path(".")
    output_dir = base_dir / OUTPUT_DIR_NAME
    output_dir.mkdir(exist_ok=True)

    try:
        logo = Image.open(LOGO_FILENAME).convert("RGBA")
    except Exception as e:
        print(f"Error loading logo: {e}")
        return

    for image_path in base_dir.iterdir():

        if (
            not image_path.suffix.lower() in SUPPORTED_FORMATS
            or image_path.name == LOGO_FILENAME
        ):
            continue

        try:
            print(f"Processing {image_path.name}...")
            image = Image.open(image_path).convert("RGBA")

            image = resize_image(image, SQUARE_FIT_SIZE)
            image = apply_logo(image, logo)

            output_path = output_dir / image_path.name
            image.save(output_path)

        except Exception as e:
            print(f"Skipping {image_path.name}: {e}")


if __name__ == "__main__":
    process_images()