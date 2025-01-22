import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_functions.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a text node")
        node2 = HTMLNode("p", "This is a text node")
        node3 = HTMLNode("p", "This is a text node")
        self.assertEqual(node, node2)
        self.assertEqual(node2, node3)

    def test_not_eq(self):
        node1 = HTMLNode("p", "This is a text node")
        node2 = HTMLNode("p", "This is a different text node")
        self.assertNotEqual(node1, node2)

    def test_props_to_html(self):
        node = HTMLNode("a", None, None, props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode("a")
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()