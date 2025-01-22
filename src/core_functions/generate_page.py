import os
from .markdown_functions import *

def generate_page(from_path, template_path, dest_path):
    """
    Generates an HTML page from a markdown file using a template.

    Args:
        from_path (str): Path to the source markdown file.
        template_path (str): Path to the HTML template file.
        dest_path (str): Path to the destination HTML file.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown file
    with open(from_path, 'r') as file:
        markdown_content = file.read()
        
    # Read the template file
    with open(template_path, 'r') as file:
        template_content = file.read()
        
    # Convert markdown to HTML using markdown_to_html_node
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract title from the markdown content
    title = extract_title(markdown_content)
    
    # Replace placeholders in the template with actual content
    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)
    
    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the full HTML page to the destination
    with open(dest_path, 'w') as file:
        file.write(full_html)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generates HTML pages from markdown files in a directory.

    Args:
        dir_path_content (str): Path to the directory containing markdown files.
        template_path (str): Path to the HTML template file.
        dest_dir_path (str): Path to the destination directory for HTML files.
    """
    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):  # Only process markdown files
                # Construct the full paths
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + ".html")
                
                # Generate the HTML page
                generate_page(from_path, template_path, dest_path)