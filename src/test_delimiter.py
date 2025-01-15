import unittest
from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_delimiter(self):
        node = TextNode(TextType.TEXT, "This is *italic* text")
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode(TextType.TEXT, "This is "),
            TextNode(TextType.ITALIC, "italic"),
            TextNode(TextType.TEXT, " text"),
        ]
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):
        node = TextNode(TextType.TEXT, "This is **bold** and *italic* text")
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = split_nodes_delimiter(result, "*", TextType.ITALIC)
        expected = [
            TextNode(TextType.TEXT, "This is "),
            TextNode(TextType.BOLD, "bold"),
            TextNode(TextType.TEXT, " and "),
            TextNode(TextType.ITALIC, "italic"),
            TextNode(TextType.TEXT, " text"),
        ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        node = TextNode(TextType.TEXT, "This is *italic text")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", TextType.ITALIC)
            
    def test_no_delimiters(self):
        node = TextNode(TextType.TEXT, "This is plain text")
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [TextNode(TextType.TEXT, "This is plain text")]
        self.assertEqual(result, expected)    

    def test_mixed_nodes(self):
        nodes = [
            TextNode(TextType.TEXT, "Plain text "),
            TextNode(TextType.TEXT, "with *italic* and "),
            TextNode(TextType.TEXT, "bold **text**"),
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        result = split_nodes_delimiter(result, "*", TextType.ITALIC)
        expected = [
            TextNode(TextType.TEXT, "Plain text "),
            TextNode(TextType.TEXT, "with "),
            TextNode(TextType.ITALIC, "italic"),
            TextNode(TextType.TEXT, " and "),
            TextNode(TextType.TEXT, "bold "),
            TextNode(TextType.BOLD, "text"),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
