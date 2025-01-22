import os
from core_functions.copy_directory import *
from core_functions.generate_page import *

def main():
    """
    Main function to generate a static site.
    """
    content_dir = "content"  # Directory containing markdown files
    public_dir = "public"    # Directory to output the generated HTML files
    static_dir = "static"    # Directory containing static files to be copied
    template_file = "template.html"  # HTML template file
    
    # Step 1: Clean and prepare the public directory
    if os.path.exists(public_dir):
        os.makedirs(public_dir, exist_ok=True)
    
    # Step 2: Copy static files to the public directory
    copy_directory_recursive(static_dir, public_dir)
    
    # Step 3: Generate pages for all markdown files
    generate_pages_recursive(content_dir, template_file, public_dir)
    
if __name__ == "__main__":
    main()