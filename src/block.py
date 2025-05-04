from enum import Enum
import re
from htmlnode import *
from text_to_textnodes import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"

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

def block_to_block_type(markdown):
    headings = re.findall(r"#{1,6}\s.*", markdown)
    code_block = re.findall(r"`{3}.*(\n.*)|`{3}", markdown)
    quote = re.findall(r">.*", markdown)
    unordered_list = re.findall(r"-.*", markdown)
    
    # Ordered list 
    separated_lines = markdown.split("\n")
    if markdown.startswith("1. "):
        i = 1
        for line in separated_lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OL

    # Condition Check
    if headings != []:
        return BlockType.HEADING
    
    if code_block != []:
        return BlockType.CODE
    
    if quote != []:
        return BlockType.QUOTE
    
    if unordered_list != []:
        return BlockType.UL
    
    return BlockType.PARAGRAPH
    
def blocktype_to_html(block):
    block_type = block_to_block_type(block)

    # Check if it is heading, if so then check which
    if block_type == BlockType.HEADING:
        if block.startswith("# "):
            block_text_nodes = text_to_textnodes(block[2:])
            new_node = HTMLNode("h1", block[2:], block_text_nodes)
            return new_node
        
        if block.startswith("## "):
            block_text_nodes = text_to_textnodes(block[3:])
            new_node = HTMLNode("h2", block[3:], block_text_nodes)
            return new_node
        
        if block.startswith("### "):
            block_text_nodes = text_to_textnodes(block[4:])
            new_node = HTMLNode("h3", block[4:], block_text_nodes)
            return new_node
        
        if block.startswith("#### "):
            block_text_nodes = text_to_textnodes(block[5:])
            new_node = HTMLNode("h4", block[5:], block_text_nodes)
            return new_node

        if block.startswith("##### "):
            block_text_nodes = text_to_textnodes(block[6:])
            new_node = HTMLNode("h5", block[6:], block_text_nodes)
            return new_node
        
        if block.startswith("###### "):
            block_text_nodes = text_to_textnodes(block[7:])
            new_node = HTMLNode("h6", block[7:], block_text_nodes)
            return new_node
    
    if block_type == BlockType.CODE:
        new_node = HTMLNode("code", block)
        return new_node
    
    if block_type == BlockType.QUOTE:
        new_node = HTMLNode("blockquote", block)
        return new_node
    
    if block_type == BlockType.UL:
        new_node = HTMLNode("ul", block)
        return new_node
    
    if block_type == BlockType.OL:
        new_node = HTMLNode("ol", block)
        return new_node
    
    new_node = HTMLNode("p", children=block_text_nodes)
    print(f"TEST4 {new_node}")
    return new_node

testblock = "## Heading"
multiple_test_block = "This is a paragraph with **bold text** and _italic_ text"
blocktype_to_html(testblock)
#blocktype_to_html(multiple_test_block)
