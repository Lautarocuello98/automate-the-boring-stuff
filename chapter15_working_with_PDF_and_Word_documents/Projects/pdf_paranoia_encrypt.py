# pdf_paranoia_encrypt.py
# Walks through a folder (and subfolders), encrypts all PDFs and saves a copy with the suffix _encrypted.pdf.
# Before deleting the original file, it verifies that the encrypted file can be opened and decrypted correctly.
# Usage: python pdf_paranoia_encrypt.py "FOLDER" "PASSWORD

import os
import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter

def encrypt_pdf(pdf_path: Path, password: str) -> bool:
    # Encrypt a PDF and create <name>_encrypted.pdf. Returns True if successful.
    out_path = pdf_path.with_name(pdf_path.stem + '_encrypted.pdf')

    # Skip if encrypted file already exists to avoid overwriting
    if out_path.exists():
        print(f"[SKIP] Already exists: {out_path}")
        return False
    
    # Try to read the original PDF
    try:
        reader = PdfReader(str(pdf_path))
    except Exception as e:
        print(f"[ERROR] Could not read {pdf_path}: {e}")
        return False
    
    writer = PdfWriter()

    # Copy all pages into the writer object
    try:
        for page in reader.pages:
            writer.add_page(page)
    except Exception as e:
        print(f"[ERROR] Failed copying pages in {pdf_path}: {e}")
        return False
    
    # Encrypt using the provided password
    try:
        writer.encrypt(password)
    except Exception as e:
        print(f"[ERROR] Could not encrypt {pdf_path}: {e}")
        return False
    
    # Save the encrypted file
    try:
        with open(out_path, 'wb') as f:
            writer.write(f)
    except Exception as e:
        print(f"[ERROR] Could not write {out_path}: {e}")
        return False
    
    # Verification step: attemp to open and decrypt the new file
    try:
        test_reader = PdfReader(str(out_path))
        if test_reader.is_encrypted:
            succes = (test_reader.decrypt(password) != 0)
            if not succes:
                print(f"[ERROR] Verification failed (wrong password) for: {out_path}")
                return False
        else:
            print(f"[ERROR] File is not encrypted: {out_path}")
            return False
    except Exception as e:
        print(f"[ERROR] Verification failed reading {out_path}: {e}")
        return False
    
    # If verification succeeded, delete original file
    try: 
        pdf_path.unlink()
        print(f"[OK] Encrypted and removed original: {pdf_path.name}")
        return True
    except Exception as e:
        print(f"[WARN] Encrypted {pdf_path} but could not delete original: {e}")
        return True


def main():
    # Except folder and password as command-line arguments
    if len(sys.argv) != 3:
        print('Usage: python pdf_paranoia_encrypt.py "FOLDER" "PASSWORD"')
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
            # Process only PDF files
            if not filename.lower().endswith(".pdf"):
                continue

            # Avoid re-encrypting already encrypted files
            if filename.lower().endswith("_encrypted.pdf"):
                continue

            pdf_path = Path(foldername) / filename

            if encrypt_pdf(pdf_path, password):
                count += 1

    print(f"\nDone. PDFs processed: {count}")


if __name__ == "__main__":
    main()