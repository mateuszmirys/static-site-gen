class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_string = ''
        props = self.props
        if props == None:
            return html_string
        for item in props:
            item_value = props.get(item)
            html_string = html_string + f' {item}' + f'="{item_value}"'
        return html_string

    def __repr__(self):
        return f"HTMLNode({self.tag} {self.value} {self.children} {self.props})"
