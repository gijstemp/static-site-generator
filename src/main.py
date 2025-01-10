from textnode import *
from htmlnode import *

# For text
TEXT = "This is a text node"
URL = "www.something.com"

# for HTML
TAG = "p"
VALUE = "This is a test text"
CHILDREN = None
PROPS = {"href": "https://www.google.com", "target": "_blank",}

def main():
    textnode = TextNode(TEXT, TextType.BOLD, URL)
    htmlnode = HTMLNode(TAG, VALUE, CHILDREN, PROPS)
    leafnode1 = LeafNode("p", "This is a paragraph of text.")
    leafnode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leafnode1.to_html())
    print(leafnode2.to_html())

if __name__ == "__main__":
    main()