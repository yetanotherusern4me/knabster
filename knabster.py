import os
import time
from humanize import naturalsize
from knabster.configs.extensions import file_extensions

def print_file_info(file_path, file_size, description):
    print(f"Path: {file_path}, Type: {description}, Size: {file_size}")

def walk_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file_path in (os.path.join(root, file) for file in files):
            ext = os.path.splitext(file_path)[1].lower()
            if ext in extensions.file_extensions:
                try:
                    file_size = naturalsize(os.path.getsize(file_path))
                    description = file_extensions.get(ext, "Unknown file type")
                    print_file_info(file_path, file_size, description)
                except OSError as e:
                    print(f"Error accessing file {file_path}: {e}")

def main():
    start_time = time.time()
    directory_to_scan = "."  # Change this to the directory you want to scan, assumes local
    walk_directory(directory_to_scan)
    print(f"\nTime elapsed: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
