import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_functions.htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_basic_structure(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "Paragraph 1"),
                LeafNode("p", "Paragraph 2"),
            ]
        )
        self.assertEqual(node.to_html(), "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>")

    def test_nested_structure(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        LeafNode("h1", "Header"),
                        LeafNode("p", "Paragraph inside section"),
                    ]
                ),
                LeafNode("footer", "Footer content"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><section><h1>Header</h1><p>Paragraph inside section</p></section><footer>Footer content</footer></div>"
        )

    def test_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "Content")])

    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_props_handling(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "Paragraph")],
            props={"class": "container", "id": "main-div"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container" id="main-div"><p>Paragraph</p></div>'
        )

    def test_recursive_children(self):
        node = ParentNode(
            "ul",
            [
                ParentNode(
                    "li",
                    [LeafNode("span", "Item 1")]
                ),
                ParentNode(
                    "li",
                    [LeafNode("span", "Item 2")]
                ),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<ul><li><span>Item 1</span></li><li><span>Item 2</span></li></ul>"
        )

if __name__ == "__main__":
    unittest.main()
