from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            # Split the text by the delimiter while keeping the delimiter segments
            parts = node.text.split(delimiter)

            # Check for unmatched delimiters
            if len(parts) % 2 == 0:
                raise ValueError(f"Unmatched delimiter '{delimiter}' found in text: {node.text}")

            for i, part in enumerate(parts):
                if i % 2 == 0:
                    # Even indices are regular text
                    if part:
                        new_nodes.append(TextNode(TextType.TEXT, part))
                else:
                    # Odd indices are within the delimiters
                    if part:
                        new_nodes.append(TextNode(text_type, part))
        else:
            # Add non-text nodes as they are
            new_nodes.append(node)

    return new_nodes