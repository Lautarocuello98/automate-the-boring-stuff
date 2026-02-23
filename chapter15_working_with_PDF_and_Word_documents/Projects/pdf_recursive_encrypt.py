# Lautarocuello98
# pdf_recursive_encrypt.py
# Recursively encrypts PDFs, verifies the result, then removes the original.
# Usage: python pdf_recursive_encrypt.py "FOLDER" "PASSWORD"

import os
import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def encrypt_pdf(pdf_path: Path, password: str) -> bool:
    out_path = pdf_path.with_name(pdf_path.stem + "_encrypted.pdf")

    if out_path.exists():
        print(f"[SKIP] {out_path.name} already exists")
        return False

    try:
        reader = PdfReader(str(pdf_path))

        # Skip already encrypted PDFs
        if reader.is_encrypted:
            print(f"[SKIP] Already encrypted: {pdf_path.name}")
            return False

    except Exception as e:
        print(f"[ERROR] Cannot read {pdf_path.name}: {e}")
        return False

    writer = PdfWriter()

    try:
        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        with open(out_path, "wb") as f:
            writer.write(f)

    except Exception as e:
        print(f"[ERROR] Failed processing {pdf_path}: {e}")
        return False

    # Verify encryption before deleting original
    try:
        test_reader = PdfReader(str(out_path))

        if not test_reader.is_encrypted:
            print(f"[ERROR] File not encrypted: {out_path.name}")
            return False

        if test_reader.decrypt(password) == 0:
            print(f"[ERROR] Verification failed for {out_path.name}")
            return False

    except Exception as e:
        print(f"[ERROR] Verification failed: {e}")
        return False

    try:
        pdf_path.unlink()
        print(f"[OK] {pdf_path.name} -> {out_path.name}")
        return True
    except Exception as e:
        print(f"[WARN] Encrypted but could not delete original: {e}")
        return True


def main():
    if len(sys.argv) != 3:
        print('Usage: python pdf_recursive_encrypt.py "FOLDER" "PASSWORD"')
        raise SystemExit(1)

    root = Path(sys.argv[1]).expanduser().resolve()
    password = sys.argv[2]

    if not root.is_dir():
        print(f"[ERROR] Invalid folder: {root}")
        raise SystemExit(1)

    count = 0

    for foldername, _, filenames in os.walk(root):
        for filename in filenames:
            name = filename.lower()
            if name.endswith(".pdf") and not name.endswith("_encrypted.pdf"):
                if encrypt_pdf(Path(foldername) / filename, password):
                    count += 1

    print(f"\nDone. PDFs encrypted: {count}")


if __name__ == "__main__":
    main()