from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):

        #Set self.children as children, set child_strings
        children = self.children

        # Checks if tag or children are empty
        if self.tag == None:
            raise ValueError
        if children == None:
            raise ValueError("object must have children")
        
        # Make props, open and close tags
        html_string = f"<{self.tag}{self.props_to_html()}>"
        close_tag = f"</{self.tag}>"

        #Recursion
        for child in children:
            html_string += child.to_html()
        
        html_string += close_tag
        return html_string
    
#        #Checks if child is of LeafNode class
#        if isinstance(self, LeafNode):
#            child_node_string = self.to_html()
#            return child_node_string
#
#        #Checks if child is of ParentNode class
#        if isinstance(self, ParentNode) and len(children) > 1:
#            print(f"TEST if of instance ParentNode")
#            return children[0 + 1].to_html()
#        
#        print(f"TEST of first pass")

    def __repr__(self):
        return f"ParentNode({self.tag} {self.children} {self.props})"
        
        
        
       