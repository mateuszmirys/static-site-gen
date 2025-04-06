from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return self.value
        
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        props_to_html = super().props_to_html()
        html_string = f"<{self.tag}{props_to_html}>{self.value}</{self.tag}>"
        #print(html_string)
        return html_string
    
    def __repr__(self):
        return f"LeafNode({self.tag} {self.value} {self.props})"
        

