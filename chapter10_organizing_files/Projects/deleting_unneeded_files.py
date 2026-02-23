# Lautarocuello98

import os
from pathlib import Path
import send2trash

# Base directory (user's home folder)
base = Path.home()

# Ask user which subfolder inside home should be scanned
source_folder = input("Which folder do you want to clean up?: ").strip()
source_path = (base / source_folder).resolve()

# Validate path existence
if not source_path.exists():
    print("Source folder does not exist.")
    raise SystemExit(1)

# Safety confirmation before modifying files
confirm = input("This will move all empty (0-byte) files to the trash. Continue? (y/n): ")
if confirm.lower() != "y":
    print("Operation cancelled.")
    raise SystemExit(0)

# Walk recursively through directory tree
for root, _, files in os.walk(source_path):
    for name in files:
        file_path = Path(root) / name
        try:
            # Identify empty files (0 bytes)
            if file_path.stat().st_size == 0:
                send2trash.send2trash(str(file_path))
                print(f"Moved to trash: {file_path}")
        except Exception as e:
            # Catch and report unexpected filesystem errors
            print(f"Error processing {file_path}: {e}")

print("Cleanup complete.")