# Lautarocuello98
# pdf_recursive_decrypt.py
# Recursively decrypts _encrypted.pdf files and creates _decrypted.pdf copies.
# Usage: python pdf_recursive_decrypt.py "FOLDER" "PASSWORD"

import os
import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def decrypt_pdf(pdf_path: Path, password: str) -> bool:
    out_path = pdf_path.with_name(
        pdf_path.stem.removesuffix("_encrypted") + "_decrypted.pdf"
    )

    if out_path.exists():
        print(f"[SKIP] {out_path.name} already exists")
        return False

    try:
        reader = PdfReader(str(pdf_path))
    except Exception as e:
        print(f"[ERROR] Cannot read {pdf_path.name}: {e}")
        return False

    if not reader.is_encrypted:
        print(f"[SKIP] Not encrypted: {pdf_path.name}")
        return False

    try:
        if reader.decrypt(password) == 0:
            print(f"[BAD PASS] Incorrect password for {pdf_path.name}")
            return False
    except Exception as e:
        print(f"[ERROR] Decrypt failed for {pdf_path.name}: {e}")
        return False

    writer = PdfWriter()

    try:
        for page in reader.pages:
            writer.add_page(page)

        with open(out_path, "wb") as f:
            writer.write(f)

    except Exception as e:
        print(f"[ERROR] Failed writing {out_path.name}: {e}")
        return False

    print(f"[OK] {pdf_path.name} -> {out_path.name}")
    return True


def main():
    if len(sys.argv) != 3:
        print('Usage: python pdf_recursive_decrypt.py "FOLDER" "PASSWORD"')
        raise SystemExit(1)

    root = Path(sys.argv[1]).expanduser().resolve()
    password = sys.argv[2]

    if not root.is_dir():
        print(f"[ERROR] Invalid folder: {root}")
        raise SystemExit(1)

    count = 0

    for foldername, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.lower().endswith("_encrypted.pdf"):
                if decrypt_pdf(Path(foldername) / filename, password):
                    count += 1

    print(f"\nDone. PDFs decrypted: {count}")


if __name__ == "__main__":
    main()