import unittest
from extract_functions import *
from split_nodes_functions import *
from textnode import TextType, TextNode
from text_to_textnode import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_plain_text(self):
        text = "This is plain text."
        result = text_to_textnodes(text)
        expected = [TextNode("This is plain text.", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_bold_text(self):
        text = "This is **bold** text."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_italic_text(self):
        text = "This is *italic* text."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_code_text(self):
        text = "This is `code` text."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_mixed_styles(self):
        text = "This is *italic*, **bold**, and `code`."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_image_node(self):
        text = "This is an image: ![alt text](url)"
        result = text_to_textnodes(text)
        # Assuming split_nodes_image creates an Image TextNode for the image part
        expected = [
            TextNode("This is an image: ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "url"),
        ]
        self.assertEqual(result, expected)

    def test_link_node(self):
        text = "This is a link: [link text](url)"
        result = text_to_textnodes(text)
        # Assuming split_nodes_link creates a Link TextNode for the link part
        expected = [
            TextNode("This is a link: ", TextType.TEXT),
            TextNode("link text", TextType.LINK, "url"),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
