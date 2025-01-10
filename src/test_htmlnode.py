import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a text node")
        node2 = HTMLNode("p", "This is a text node")
        node3 = HTMLNode("p", "This is a text node")
        self.assertEqual(node, node2)
        self.assertEqual(node2, node3)


if __name__ == "__main__":
    unittest.main()
    
