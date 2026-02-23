# pdf_paranoia_encrypt.py
# Recursively encrypts PDFs in a folder, verifies the encrypted copy and removes the original only if verification succeeds.
# Usage: python pdf_paranoia_encrypt.py "FOLDER" "PASSWORD"

import os
import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def encrypt_pdf(pdf_path: Path, password: str) -> bool:
    """Encrypt a PDF and create <name>_encrypted.pdf. Returns True if successful."""
    out_path = pdf_path.with_name(pdf_path.stem + "_encrypted.pdf")

    # Avoid overwriting existing encrypted files
    if out_path.exists():
        print(f"[SKIP] Already exists: {out_path}")
        return False

    # Load original PDF
    try:
        reader = PdfReader(str(pdf_path))
    except Exception as e:
        print(f"[ERROR] Could not read {pdf_path}: {e}")
        return False

    writer = PdfWriter()

    # Copy all pages to new writer
    try:
        for page in reader.pages:
            writer.add_page(page)
    except Exception as e:
        print(f"[ERROR] Failed copying pages in {pdf_path}: {e}")
        return False

    # Apply password protection
    try:
        writer.encrypt(password)
    except Exception as e:
        print(f"[ERROR] Could not encrypt {pdf_path}: {e}")
        return False

    # Write encrypted file
    try:
        with open(out_path, "wb") as f:
            writer.write(f)
    except Exception as e:
        print(f"[ERROR] Could not write {out_path}: {e}")
        return False

    # Verify encryption before deleting original
    try:
        test_reader = PdfReader(str(out_path))
        if not test_reader.is_encrypted:
            print(f"[ERROR] File is not encrypted: {out_path}")
            return False

        success = test_reader.decrypt(password) != 0
        if not success:
            print(f"[ERROR] Verification failed for: {out_path}")
            return False

    except Exception as e:
        print(f"[ERROR] Verification failed reading {out_path}: {e}")
        return False

    # Remove original only after successful verification
    try:
        pdf_path.unlink()
        print(f"[OK] Encrypted and removed original: {pdf_path.name}")
        return True
    except Exception as e:
        print(f"[WARN] Encrypted but could not delete original: {e}")
        return True


def main():
    # Expect folder and password as CLI arguments
    if len(sys.argv) != 3:
        print('Usage: python pdf_paranoia_encrypt.py "FOLDER" "PASSWORD"')
        sys.exit(1)

    root = Path(sys.argv[1]).expanduser().resolve()
    password = sys.argv[2]

    if not root.exists() or not root.is_dir():
        print(f"[ERROR] Invalid folder: {root}")
        sys.exit(1)

    count = 0

    # Traverse directory tree and process PDFs
    for foldername, _, filenames in os.walk(root):
        for filename in filenames:
            if not filename.lower().endswith(".pdf"):
                continue
            if filename.lower().endswith("_encrypted.pdf"):
                continue

            pdf_path = Path(foldername) / filename

            if encrypt_pdf(pdf_path, password):
                count += 1

    print(f"\nDone. PDFs encrypted: {count}")


if __name__ == "__main__":
    main()