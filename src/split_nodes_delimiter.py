from textnode import TextNode, TextType
from extract_markdown import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
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

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        node_text = node.text
        extracted = extract_markdown_images(node_text)
        
        if len(extracted) == 0:
            new_nodes.append(node)
            continue
        
        for e in extracted:
            image_alt = e[0]
            image_src = e[1]
            split_node = node_text.split(f"![{image_alt}]({image_src})", 1)
            if len(split_node) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image_alt,
                    TextType.IMG,
                    image_src,
                )
            )
            node_text = split_node[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    #print(f"TEST {new_nodes}")
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.URL, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    final_blocks = []
    for block in blocks:
        if block == "":
            continue
        new_block = block.strip()
        final_blocks.append(new_block)
    #print(f"TEST How md looks like: {final_blocks}")
    return final_blocks
