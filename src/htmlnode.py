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
            props_string = ""
            for key, value in self.props.items():
                props_string += f'{key}="{value}" '
            return props_string.rstrip()
        
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
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        if self.tag == "p":
            p_string = f"<{self.tag}>{self.value}</{self.tag}>"
            p_string.replace('""', "")
            return p_string
        if self.tag == "a":
            if self.props:
                props_string = ""
                for key, value in self.props.items():
                    props_string += f'{key}="{value}" '
                    props_string = props_string.rstrip()
            a_string = f"<{self.tag}> {props_string}>{self.value}</{self.tag}>"
            a_string.replace('""', "")
            return a_string
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError
        if not self.children:
            raise ValueError("Children arg is missing")
        