from textnode import *
from htmlnode import *
from split_nodes_functions import split_nodes_delimiter

# For text
TEXT = "This is a text node"
URL = "www.something.com"

# for HTML
TAG = "p"
VALUE = "This is a test text"
CHILDREN = None
PROPS = {"href": "https://www.google.com", "target": "_blank",}

def main():
    textnode = TextNode("This is *italic* text", TextType.TEXT)
    htmlnode = HTMLNode(TAG, VALUE, CHILDREN, PROPS)
    leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    
    new_nodes = split_nodes_delimiter([textnode], "`", TextType.CODE)
    
    print(textnode)
    print(new_nodes)
    
if __name__ == "__main__":
    main()