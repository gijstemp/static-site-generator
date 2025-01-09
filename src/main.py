from textnode import *

TEXT = "This is a text node"
URL = "www.something.com"

def main():
    textnode = TextNode(TEXT, TextType.BOLD, URL)
    print(textnode)


if __name__ == "__main__":
    main()