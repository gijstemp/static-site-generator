import re
from htmlnode import *

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
    # Shared helper function for text to child nodes
    def text_to_children(text):
        return [LeafNode("span", text)]  # Placeholder; replace with actual inline markdown parsing
    
    # Split the markdown into blocks
    blocks = markdown_to_blocks(markdown)

    # Initialize an empty list to store child nodes
    child_nodes = []
    
    # Loop over each block
    for block in blocks:
        block_type = block_to_block_type(block)
        
        # Create new HTMLNode based on block type
        if block_type == "heading":
            level = block.split(" ")[0].count('#')
            tag = f"h{level}"
            value = block[level:].strip()
            child_nodes.append(ParentNode(tag, text_to_children(value)))
            
        elif block_type == "code":
            code_content = block.strip("```")
            code_content = code_content.strip()
            child_nodes.append(ParentNode("pre", [LeafNode("code", code_content)]))
            
        elif block_type == "quote":
            quote_content = "\n".join(line.lstrip("> ") for line in block.splitlines())
            child_nodes.append(ParentNode("blockquote", text_to_children(quote_content)))
            
        elif block_type == "unordered_list":
            list_items = [LeafNode("li", line.lstrip("*- ").strip()) for line in block.splitlines()] 
            child_nodes.append(ParentNode("ul", list_items))
        
        elif block_type == "ordered_list":
            list_items = [LeafNode("li", re.sub(r"^\d+\. ", "", line).strip()) for line in block.splitlines()]
            child_nodes.append(ParentNode("ol", list_items))
            
        else:
            child_nodes.append(ParentNode("p", text_to_children(block)))
            
    
    parent_node = ParentNode("div", child_nodes)
    return parent_node


markdown_text = """- Item 1
- Item 2
- Item 3"""

html_tree = markdown_to_html_node(markdown_text)
print(html_tree.to_html())