import unittest

from markdown_functions import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_empty_input(self):
        """Test with an empty string."""
        self.assertEqual(markdown_to_blocks(""), [])

    def test_single_block(self):
        """Test with a single block of text."""
        markdown = "This is a single block."
        expected = ["This is a single block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_blocks(self):
        """Test with multiple blocks separated by double newlines."""
        markdown = "Block one.\n\nBlock two.\n\nBlock three."
        expected = ["Block one.", "Block two.", "Block three."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_trailing_and_leading_whitespace(self):
        """Test input with leading and trailing whitespace."""
        markdown = "   Block one.   \n\n   Block two.\n\n   Block three.   "
        expected = ["Block one.", "Block two.", "Block three."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_lines(self):
        """Test input with extra empty lines."""
        markdown = "Block one.\n\n\n\nBlock two.\n\n\nBlock three."
        expected = ["Block one.", "Block two.", "Block three."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_only_whitespace(self):
        """Test input with only whitespace."""
        markdown = "   \n   \n"
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_mixed_content(self):
        """Test input with a mix of blocks and whitespace-only sections."""
        markdown = "Block one.\n\n\n   \nBlock two.\n\n   \n   Block three."
        expected = ["Block one.", "Block two.", "Block three."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

if __name__ == "__main__":
    unittest.main()