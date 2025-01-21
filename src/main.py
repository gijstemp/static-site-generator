import os
from copy_directory import *
from generate_page import *

def main():  
    content_dir = "content"
    public_dir = "public"
    static_dir = "static"
    template_file = "template.html"
    
    # Step 1: Clean and prepare the public directory
    if os.path.exists(public_dir):
        os.makedirs(public_dir, exist_ok=True)
    
    # Step 2: Copy static files to the public directory
    copy_directory_recursive(static_dir, public_dir)
    
    # Step 3: Generate pages for all markdown files
    generate_pages_recursive(content_dir, template_file, public_dir)
    
if __name__ == "__main__":
    main()