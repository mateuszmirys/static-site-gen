from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        
        temp_nodes = []
        split_nodes = node.text.split(delimiter)

        if len(split_nodes) % 2 == 0:
            raise Exception("invalid Markdown format")
        for n in range(len(split_nodes)):
            if split_nodes[n] == "":
                continue
            if n % 2 == 0:
                temp_nodes.append(TextNode(split_nodes[n], TextType.TEXT))
            else:
                temp_nodes.append(TextNode(split_nodes[n], text_type))
        new_nodes.extend(temp_nodes)
  
    return new_nodes
