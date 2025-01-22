import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_functions.extract_functions import *

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images_basic(self):
        text = "![alt text](image1.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt text", "image1.png")])

    def test_extract_markdown_images_multiple(self):
        text = "![alt1](image1.png) ![alt2](image2.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt1", "image1.png"), ("alt2", "image2.jpg")])

    def test_extract_markdown_images_no_images(self):
        text = "This is a test without any images."
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_extract_markdown_images_edge_cases(self):
        text = "![](empty-alt.png) ![alt](no-closing-parenthesis.png ![alt](correct.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("", "empty-alt.png"), ("alt", "correct.png")])

    def test_extract_markdown_links_basic(self):
        text = "[link text](https://example.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link text", "https://example.com")])

    def test_extract_markdown_links_multiple(self):
        text = "[link1](url1) [link2](url2)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link1", "url1"), ("link2", "url2")])

    def test_extract_markdown_links_no_links(self):
        text = "This is a test without any links."
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_extract_markdown_links_with_images(self):
        text = "![image](image.png) [link](url.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link", "url.com")])

if __name__ == "__main__":
    unittest.main()