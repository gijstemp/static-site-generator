import unittest
from htmlnode import *
from markdown_functions import *

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_heading(self):
        markdown = "# Heading 1"
        html_node = markdown_to_html_node(markdown)
        expected_html = "<div><h1><span>Heading 1</span></h1></div>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_paragraph(self):
        markdown = "This is a paragraph."
        html_node = markdown_to_html_node(markdown)
        expected_html = "<div><p><span>This is a paragraph.</span></p></div>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_unordered_list(self):
        markdown = """- Item 1
- Item 2
- Item 3"""
        html_node = markdown_to_html_node(markdown)
        expected_html = "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_ordered_list(self):
        markdown = """1. First
2. Second
3. Third"""
        html_node = markdown_to_html_node(markdown)
        expected_html = "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_quote(self):
        markdown = "> This is a quote."
        html_node = markdown_to_html_node(markdown)
        expected_html = "<div><blockquote><span>This is a quote.</span></blockquote></div>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_code_block(self):
        markdown = """```
Code block
```"""
        html_node = markdown_to_html_node(markdown)
        expected_html = "<div><pre><code>Code block</code></pre></div>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_combined_blocks(self):
        markdown = """# Heading 1

This is a paragraph.

- Item 1
- Item 2
- Item 3

> This is a quote.

```
Code block
```

## Heading 2"""
        html_node = markdown_to_html_node(markdown)
        expected_html = ("<div><h1><span>Heading 1</span></h1><p><span>This is a paragraph.</span></p><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><blockquote><span>This is a quote.</span></blockquote><pre><code>Code block</code></pre><h2><span>Heading 2</span></h2></div>")
        self.assertEqual(html_node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()