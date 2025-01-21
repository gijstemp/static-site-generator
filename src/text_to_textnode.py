from extract_functions import *
from split_nodes_functions import *
from textnode import TextType, TextNode
import re

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    # Process inline formatting in the correct order
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)   # Bold
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)  # Italic
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)    # Code
    nodes = split_nodes_link(nodes)                             # Links
    nodes = split_nodes_image(nodes)                            # Images
    return nodes
