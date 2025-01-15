class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #  A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            props_string = " ".join(f'{key}="{value}"' for key, value in self.props.items())
            return f" {props_string}"
        return ""
        
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )
            
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if not self.tag:
            return self.value  # If no tag, return just the value as plain text
        
        props_string = self.props_to_html()
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("The 'tag' argument is required.")
        if not isinstance(children, list) or not children:
            raise ValueError("The 'children' argument must be a non-empty list.")
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self):
        # Check if the tag is missing
        if not self.tag:
            raise ValueError("The 'tag' attribute is missing.")
        # Check if children are missing
        if not self.children:
            raise ValueError("The 'children' attribute is missing.")
        
        # Convert properties to HTML if present
        props_string = self.props_to_html()
        
        opening_tag = f"<{self.tag}{props_string}>"
        children_html = "".join(child.to_html() for child in self.children)
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{children_html}{closing_tag}"