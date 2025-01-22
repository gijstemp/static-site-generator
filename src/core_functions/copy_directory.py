import os
import shutil

def copy_directory_recursive(source, destination):
    """
    Recursively copies all contents from the source directory to the destination directory.
    Clears the destination directory before copying.

    Args:
        source (str): Path to the source directory.
        destination (str): Path to the destination directory.
    """
    # Delete the destination directory if it exists
    if os.path.exists(destination):
        shutil.rmtree(destination)
        print(f"Deleted contents of directory: {destination}")
        
    # Recreate the destination directory
    os.mkdir(destination)
    print(f"Created directory: {destination}")
    
    # Copy contents from source to destination
    for item in os.listdir(source):
        source_item_path = os.path.join(source, item)
        destination_item_path = os.path.join(destination, item)

        if os.path.isfile(source_item_path):
            # If the item is a file, copy it to the destination
            shutil.copy(source_item_path, destination_item_path)
            print(f"Copied file: {source_item_path} -> {destination_item_path}")
        elif os.path.isdir(source_item_path):
            # If the item is a directory, recursively copy its contents
            copy_directory_recursive(source_item_path, destination_item_path)