import unittest

from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("p", "This is a paragraph of text.")
        node3 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node, node2)
        self.assertEqual(node2, node3)


if __name__ == "__main__":
    unittest.main()
    