import unittest
from htmlnode import *
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode(TextType.BOLD, "This is a text node")
        node2 = TextNode(TextType.BOLD, "This is a text node")
        node3 = TextNode(TextType.BOLD, "This is a text node", "www.something.com")
        self.assertEqual(node, node2, node3)
        
    def test_text_node(self):
        text_node = TextNode(TextType.TEXT, "Plain text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Plain text")

    def test_bold_node(self):
        text_node = TextNode(TextType.BOLD, "Bold text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_italic_node(self):
        text_node = TextNode(TextType.ITALIC, "Italic text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_code_node(self):
        text_node = TextNode(TextType.CODE, "Code snippet")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code snippet</code>")

    def test_link_node(self):
        text_node = TextNode(TextType.LINK, "Click here", url="https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://example.com">Click here</a>')

    def test_image_node(self):
        text_node = TextNode(TextType.IMAGE, "Alt text", url="https://example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://example.com/image.png" alt="Alt text"></img>')

    def test_unknown_type(self):
        text_node = TextNode("UNKNOWN", "Unknown text")
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)


if __name__ == "__main__":
    unittest.main()
    