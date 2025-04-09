import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        test_nodes = [TextNode("This is a test of **bold case style** text", TextType.TEXT)]
        new_target_nodes = [
            TextNode("This is a test of ", TextType.TEXT),
            TextNode("bold case style", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
            ]
        
        nodes = split_nodes_delimiter(test_nodes, "**", TextType.BOLD)

        self.assertEqual(nodes, new_target_nodes)

    def test_bold_double(self):
        test_nodes = [TextNode("This is a **second test** of **bold case style** text", TextType.TEXT)]
        new_target_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("second test", TextType.BOLD),
            TextNode(" of ", TextType.TEXT),            
            TextNode("bold case style", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
            ]
        
        nodes = split_nodes_delimiter(test_nodes, "**", TextType.BOLD)

        self.assertEqual(nodes, new_target_nodes)

    def test_italic(self):
        test_nodes = [TextNode("This is a test of _italic case style_ text", TextType.TEXT)]
        new_target_nodes = [
            TextNode("This is a test of ", TextType.TEXT),
            TextNode("italic case style", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
            ]
        
        nodes = split_nodes_delimiter(test_nodes, "_", TextType.ITALIC)

        self.assertEqual(nodes, new_target_nodes)
