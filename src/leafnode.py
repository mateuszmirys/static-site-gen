from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
    
    def to_html(self):
        print(f"What are the props? Props: {self.props}")
        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return self.value
        
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        current_props = super().props_to_html(self)
        return f"<{self.tag}{current_props}>{self.value}</{self.tag}>"
        

