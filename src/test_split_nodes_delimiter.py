import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import *
from text_to_textnodes import *
from block import markdown_to_blocks

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

class TestSplitNodes(unittest.TestCase):
    def test_images(self):
        test_node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
            )
        
        new_node = split_nodes_images([test_node])
        goal_output = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMG, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMG, "https://i.imgur.com/3elNhQu.png"),
            ]
        self.assertEqual(new_node, goal_output)

    def test_links(self):
        test_node = TextNode(
            "This is text with an [link](https://mirys.pl/) and [another link](https://google.com/)",
            TextType.TEXT,
            )
        
        new_node = split_nodes_links([test_node])
        goal_output = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("link", TextType.URL, "https://mirys.pl/"),
            TextNode(" and ", TextType.TEXT),
            TextNode("another link", TextType.URL, "https://google.com/")
        ]
        self.assertEqual(new_node, goal_output)
    
class TestTextToNodes(unittest.TestCase):
    def test_text_simple(self):
        test_text = "An example of **bold** Markdown"
        planned_output = [
            TextNode("An example of ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" Markdown", TextType. TEXT)
            ]
        
        self.assertEqual(text_to_textnodes(test_text), planned_output)
    
    def test_text_italic_links(self):
        test_text = "A italic _Markdown_ with [link](https://boot.dev)"
        planned_output = [
            TextNode("A italic ", TextType.TEXT),
            TextNode("Markdown", TextType.ITALIC),
            TextNode(" with ", TextType.TEXT),
            TextNode("link", TextType.URL, "https://boot.dev")
        ]

        self.assertEqual(text_to_textnodes(test_text), planned_output)