from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
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