import re

def extract_markdown_images(text):
    """
    Extracts all image references from a markdown text.

    Args:
        text (str): The markdown text to search for image references.
    Returns:
        list of tuples: A list of tuples where each tuple contains the alt text and the URL of an image.
    """
    # Regular expression to find markdown image references
    extracted = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted

def extract_markdown_links(text):
    """
    Extracts all hyperlink references from a markdown text.

    Args:
        text (str): The markdown text to search for hyperlink references.
    Returns:
        list of tuples: A list of tuples where each tuple contains the link text and the URL.
    """
    # Regular expression to find markdown hyperlink references
    extracted = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted