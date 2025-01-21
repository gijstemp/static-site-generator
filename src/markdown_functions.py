import re
from htmlnode import *
from textnode import *
from text_to_textnode import *

def markdown_to_blocks(markdown):
    blocks = [block.strip() for block in markdown.split("\n\n") if block.strip()]
   
    return blocks

def block_to_block_type(markdown_block):
    if markdown_block.startswith("#"):
        return "heading"
    elif markdown_block.startswith("```") and markdown_block.endswith("```"):
        return "code"
    elif all(line.startswith(">") for line in markdown_block.splitlines()):
        return "quote"
    elif all(line.startswith(("* ", "- ")) for line in markdown_block.splitlines()):
        return "unordered_list"
    elif all(re.match(r"^\d+\. ", line) for line in markdown_block.splitlines()):
        return "ordered_list"
    else:
        return "paragraph"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == "unordered_list":
            list_items = [
                ParentNode(
                    "li",
                    [text_node_to_html_node(node) for node in text_to_textnodes(line.lstrip("-*").strip())]
                )
                for line in block.splitlines()
            ]
            child_nodes.append(ParentNode("ul", list_items))

        elif block_type == "ordered_list":
            list_items = [
                ParentNode(
                    "li",
                    [text_node_to_html_node(node) for node in text_to_textnodes(re.sub(r"^\d+\. ", "", line).strip())]
                )
                for line in block.splitlines()
            ]
            child_nodes.append(ParentNode("ol", list_items))

        elif block_type == "quote":
            quote_content = "\n".join(line.lstrip("> ") for line in block.splitlines())
            inline_nodes = [text_node_to_html_node(node) for node in text_to_textnodes(quote_content)]
            child_nodes.append(ParentNode("blockquote", inline_nodes))

        elif block_type == "code":
            code_content = block.strip("```").strip()
            child_nodes.append(ParentNode("pre", [LeafNode("code", code_content)]))

        elif block_type == "heading":
            level = block.split(" ")[0].count("#")
            tag = f"h{level}"
            content = block[level:].strip()
            inline_nodes = [text_node_to_html_node(node) for node in text_to_textnodes(content)]
            child_nodes.append(ParentNode(tag, inline_nodes))

        else:  # Paragraph or other generic blocks
            inline_nodes = [text_node_to_html_node(node) for node in text_to_textnodes(block.strip())]
            child_nodes.append(ParentNode("p", inline_nodes))

    return ParentNode("div", child_nodes)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block.strip("#").lstrip()
        else:
            raise Exception("No h1 found")
        
