# pdf_paranoia_decrypt.py
# Finds encrypted PDFs (_encrypted.pdf), attempts to decrypt them and creates a decrypted copy with suffix _decrypted.pdf.
# Usage: python pdf_paranoia_decrypt.py "FOLDER" "PASSWORD'


import os
import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def decrypt_pdf(pdf_path: Path, password: str) -> bool:
    """Decrypt a PDF and create <name>_decrypted.pdf. Returns True if successful."""

    # Remove only the suffix "_encrypted" before adding "_decrypted"
    base_name = pdf_path.stem.removesuffix("_encrypted")
    out_path = pdf_path.with_name(base_name + "_decrypted.pdf")

    # Skip if decrypted file already exists
    if out_path.exists():
        print(f"[SKIP] Already exists: {out_path}")
        return False

    # Try to open the PDF
    try:
        reader = PdfReader(str(pdf_path))
    except Exception as e:
        print(f"[ERROR] Could not read {pdf_path}: {e}")
        return False

    # Skip if file is not encrypted
    if not reader.is_encrypted:
        print(f"[SKIP] Not encrypted: {pdf_path}")
        return False

    # Attempt to decrypt using the provided password
    try:
        success = (reader.decrypt(password) != 0)
        if not success:
            print(f"[BAD PASS] {pdf_path.name} (incorrect password)")
            return False
    except Exception as e:
        print(f"[ERROR] Decrypt failed for {pdf_path}: {e}")
        return False

    writer = PdfWriter()

    # Copy all pages into a new writer object
    try:
        for page in reader.pages:
            writer.add_page(page)
    except Exception as e:
        print(f"[ERROR] Failed copying pages from {pdf_path}: {e}")
        return False

    # Save decrypted file
    try:
        with open(out_path, "wb") as f:
            writer.write(f)
    except Exception as e:
        print(f"[ERROR] Could not write {out_path}: {e}")
        return False

    print(f"[OK] Decrypted: {pdf_path.name} -> {out_path.name}")
    return True


def main():
    # Expect folder and password as command-line arguments
    if len(sys.argv) != 3:
        print('Usage: python pdf_paranoia_decrypt.py "FOLDER" "PASSWORD"')
        sys.exit(1)

    root = Path(sys.argv[1]).expanduser().resolve()
    password = sys.argv[2]

    # Validate folder path
    if not root.exists() or not root.is_dir():
        print(f"[ERROR] Invalid folder: {root}")
        sys.exit(1)

    count = 0

    # Walk through all folders and subfolders
    for foldername, subfolders, filenames in os.walk(root):
        for filename in filenames:
            # Only process encrypted PDFs
            if not filename.lower().endswith("_encrypted.pdf"):
                continue

            pdf_path = Path(foldername) / filename

            if decrypt_pdf(pdf_path, password):
                count += 1

    print(f"\nDone. PDFs decrypted: {count}")


if __name__ == "__main__":
    main()
