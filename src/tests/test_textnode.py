import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_functions.htmlnode import *
from core_functions.textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD, "www.something.com")
        self.assertEqual(node, node2, node3)
        
    def test_text_node(self):
        text_node = TextNode("Plain text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Plain text")

    def test_bold_node(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_italic_node(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_code_node(self):
        text_node = TextNode("Code snippet", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code snippet</code>")

    def test_link_node(self):
        text_node = TextNode("Click here", TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://example.com">Click here</a>')

    def test_image_node(self):
        text_node = TextNode("Alt text", TextType.IMAGE, url="https://example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://example.com/image.png" alt="Alt text"></img>')

    def test_unknown_type(self):
        text_node = TextNode("Unknown text", "UNKNOWN")
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()
