import unittest
from textnode import TextType, TextNode
from split_nodes_functions import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_delimiter(self):
        node = TextNode("This is *italic* text", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):
        node = TextNode("This is **bold** and *italic* text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = split_nodes_delimiter(result, "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        node = TextNode("This is *italic text", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", TextType.ITALIC)
            
    def test_no_delimiters(self):
        node = TextNode("This is plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [TextNode("This is plain text", TextType.TEXT)]
        self.assertEqual(result, expected)    

    def test_mixed_nodes(self):
        nodes = [
            TextNode("Plain text ", TextType.TEXT),
            TextNode("with *italic* and ", TextType.TEXT),
            TextNode("bold **text**", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        result = split_nodes_delimiter(result, "*", TextType.ITALIC)
        expected = [
            TextNode("Plain text ", TextType.TEXT),
            TextNode("with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
