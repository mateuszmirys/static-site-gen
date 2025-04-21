from textnode import *
from split_nodes_delimiter import *
from extract_markdown import *

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    bold_nodes = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
    extract_images = split_nodes_images(code_nodes)
    extract_links = split_nodes_links(extract_images)
    final_nodes = extract_links
    return final_nodes