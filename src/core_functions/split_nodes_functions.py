import re
from .textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits text nodes by a specified delimiter and assigns a new text type to the delimited text.

    Args:
        old_nodes (list): A list of TextNode objects to be split.
        delimiter (str): The delimiter to split the text by.
        text_type (TextType): The text type to assign to the delimited text.
    Returns:
        list: A list of new TextNode objects with the text split by the delimiter.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            # Split the text by the delimiter
            parts = node.text.split(delimiter)

            # Ensure that delimiters are properly matched
            if len(parts) % 2 == 0:
                raise ValueError(f"Unmatched delimiter '{delimiter}' found in text: {node.text}")

            for i, part in enumerate(parts):
                if i % 2 == 0:  # Plain text outside the delimiter
                    if part:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                else:  # Text inside the delimiter
                    if part:
                        new_nodes.append(TextNode(part, text_type))
        else:
            # Non-text nodes are appended as-is
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes):
    """
    Splits text nodes by markdown image syntax and assigns the image text type to the image text.

    Args:
        old_nodes (list): A list of TextNode objects to be split.
    Returns:
        list: A list of new TextNode objects with the text split by markdown image syntax.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = re.split(r"(!\[[^\[\]]*\]\([^\(\)]*\))", node.text)
            for part in parts:
                if part:
                    match = re.match(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", part)
                    if match:
                        alt_text, url = match.groups()
                        new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                    else:
                        new_nodes.append(TextNode(part, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    """
    Splits text nodes by markdown link syntax and assigns the link text type to the link text.

    Args:
        old_nodes (list): A list of TextNode objects to be split.
    Returns:
        list: A list of new TextNode objects with the text split by markdown link syntax.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = re.split(r"(\[[^\[\]]*\]\([^\(\)]*\))", node.text)
            for part in parts:
                if part:
                    match = re.match(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", part)
                    if match:
                        link_text, url = match.groups()
                        new_nodes.append(TextNode(link_text, TextType.LINK, url))
                    else:
                        new_nodes.append(TextNode(part, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes