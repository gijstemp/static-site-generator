import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("p", "This is a paragraph of text.")
        node3 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node, node2)
        self.assertEqual(node2, node3)

    def test_not_eq(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("p", "This is a different paragraph of text.")
        self.assertNotEqual(node1, node2)

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is plain text.")
        self.assertEqual(node.to_html(), "This is plain text.")

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click here", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" target="_blank">Click here</a>')

if __name__ == "__main__":
    unittest.main()