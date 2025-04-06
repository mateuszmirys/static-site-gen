from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):

        # Checks if tag or children are empty
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError("object must have children")
        
        # Make opening parent tag
        props_to_html = ''
        if self.props != None:
            props_to_html = super().props_to_html()
        opening_tag = f"<{self.tag}{props_to_html}>"
        closing_tag = f"</{self.tag}>"

        #Prepare full HTML string, get child node
        html_string = f"{opening_tag}{closing_tag}"
        children = self.children
        child_strings = ''

        #Recursion
        def children_to_html(children, child_strings):
            child = children[0]
            #Base case for recursion
            if len(children) == 1:
                child_string = f"<{child.tag}>{child.value}</{child.tag}>"
                child_strings = child_strings + child_string
                #print(f"TEST! {opening_tag}{child_strings}{closing_tag}")
                return f"{child_strings}"
            
            #ParentNode case
            if child == ParentNode:
                print(f"TEST of ParentNode case")
                children_to_html(child, child_strings)

            #LeafNode case
            child_string = f"<{child.tag}>{child.value}</{child.tag}>"
            #print(f"TEST recursion: {child_string}")
            child_strings = child_strings + child_string
            #print(f"Test of child strings together: {child_strings}")
            return children_to_html(children[1:], child_strings)
        
        #Return final HTML string
        #print(f"Test of child strings together: {child_strings}")
        return opening_tag + children_to_html(children, child_strings) + closing_tag
        
        
        
       