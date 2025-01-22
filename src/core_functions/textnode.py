from enum import Enum
from .htmlnode import *

class TextType(Enum):
    """
    Enum representing different types of text formatting.
    """
    TEXT = "text"
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGE = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        """
        Initializes a TextNode.

        Args:
            text (str): The text content.
            text_type (TextType): The type of text formatting.
            url (str, optional): The URL for links or images.
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        Checks if this TextNode is equal to another TextNode.

        Args:
            other (TextNode): The other TextNode to compare with.
        Returns:
            bool: True if the nodes are equal, False otherwise.
        """
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        """
        Returns a string representation of the TextNode.

        Returns:
            str: A string representation of the TextNode.
        """
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    """
    Converts a TextNode to an HTMLNode.

    Args:
        text_node (TextNode): The TextNode to convert.
    Returns:
        HTMLNode: The corresponding HTMLNode.
    """
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("Unknown text type given")