import os
from copy_directory import *

def main():
    source_dir = "static"
    destination_dir = "public"

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist. Please create it and add content.")
    else:
        copy_directory_recursive(source_dir, destination_dir)
        print("All contents have been copied successfully.")
    
if __name__ == "__main__":
    main()