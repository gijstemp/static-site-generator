from extract_functions import *
from split_nodes_functions import *
from textnode import TextType, TextNode
import re

def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    new_node = split_nodes_image(node)
    new_node = split_nodes_link(new_node)
    new_node = split_nodes_delimiter(new_node, "**", TextType.BOLD)
    new_node = split_nodes_delimiter(new_node, "*", TextType.ITALIC)
    new_node = split_nodes_delimiter(new_node, "`", TextType.CODE)
    return new_node
