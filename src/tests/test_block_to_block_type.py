import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from core_functions.markdown_functions import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_single_block(self):
        """Test with a single block of text."""
        markdown = "This is a single block."
        expected = "paragraph"
        self.assertEqual(block_to_block_type(markdown), expected)
        
if __name__ == "__main__":
    unittest.main()