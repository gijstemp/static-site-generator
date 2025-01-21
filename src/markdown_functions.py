import re

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