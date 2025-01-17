import unittest
from textnode import TextType, TextNode
from split_nodes_functions import split_nodes_image, split_nodes_link

class TestSplitNodesFunctions(unittest.TestCase):

    def test_split_nodes_image_basic(self):
        old_nodes = [TextNode("Here is an image: ![Alt Text](http://example.com/image.png)", TextType.TEXT)]
        expected = [
            TextNode("Here is an image: ", TextType.TEXT),
            TextNode("Alt Text", TextType.IMAGE, "http://example.com/image.png")
        ]
        result = split_nodes_image(old_nodes)
        self.assertEqual(result, expected)

    def test_split_nodes_image_no_images(self):
        old_nodes = [TextNode("This is just plain text with no images.", TextType.TEXT)]
        result = split_nodes_image(old_nodes)
        self.assertEqual(result, old_nodes)

    def test_split_nodes_image_multiple_images(self):
        old_nodes = [TextNode("![Image1](http://example.com/img1.png) and ![Image2](http://example.com/img2.png)", TextType.TEXT)]
        expected = [
            TextNode("Image1", TextType.IMAGE, "http://example.com/img1.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Image2", TextType.IMAGE, "http://example.com/img2.png")
        ]
        result = split_nodes_image(old_nodes)
        self.assertEqual(result, expected)

    def test_split_nodes_image_non_text_nodes(self):
        old_nodes = [TextNode("![Alt Text](http://example.com/image.png)", TextType.IMAGE, "http://example.com/image.png")]
        result = split_nodes_image(old_nodes)
        self.assertEqual(result, old_nodes)

    def test_split_nodes_image_mixed_content(self):
        old_nodes = [TextNode("Text before ![Alt Text](http://example.com/image.png) and after", TextType.TEXT)]
        expected = [
            TextNode("Text before ", TextType.TEXT),
            TextNode("Alt Text", TextType.IMAGE, "http://example.com/image.png"),
            TextNode(" and after", TextType.TEXT)
        ]
        result = split_nodes_image(old_nodes)
        self.assertEqual(result, expected)

    def test_split_nodes_link_basic(self):
        old_nodes = [TextNode("Here is a link: [Link Text](http://example.com)", TextType.TEXT)]
        expected = [
            TextNode("Here is a link: ", TextType.TEXT),
            TextNode("Link Text", TextType.LINK, "http://example.com")
        ]
        result = split_nodes_link(old_nodes)
        self.assertEqual(result, expected)

    def test_split_nodes_link_no_links(self):
        old_nodes = [TextNode("This is just plain text with no links.", TextType.TEXT)]
        result = split_nodes_link(old_nodes)
        self.assertEqual(result, old_nodes)

    def test_split_nodes_link_multiple_links(self):
        old_nodes = [TextNode("[Link1](http://example.com/1) and [Link2](http://example.com/2)", TextType.TEXT)]
        expected = [
            TextNode("Link1", TextType.LINK, "http://example.com/1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Link2", TextType.LINK, "http://example.com/2")
        ]
        result = split_nodes_link(old_nodes)
        self.assertEqual(result, expected)

    def test_split_nodes_link_non_text_nodes(self):
        old_nodes = [TextNode("[Link Text](http://example.com)", TextType.LINK, "http://example.com")]
        result = split_nodes_link(old_nodes)
        self.assertEqual(result, old_nodes)

    def test_split_nodes_link_mixed_content(self):
        old_nodes = [TextNode("Text before [Link Text](http://example.com) and after", TextType.TEXT)]
        expected = [
            TextNode("Text before ", TextType.TEXT),
            TextNode("Link Text", TextType.LINK, "http://example.com"),
            TextNode(" and after", TextType.TEXT)
        ]
        result = split_nodes_link(old_nodes)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
