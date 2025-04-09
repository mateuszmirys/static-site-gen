import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("Some text in bold", TextType.BOLD)
        node2 = TextNode("Some text in italic", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_all(self):
        node = TextNode("This is an url", TextType.URL, "https://mirys.pl")
        node2 = TextNode("This is an url", TextType.URL, "https://mirys.pl")
        self.assertEqual(node, node2)
    
    def test_not_eq_all(self):
        node = TextNode("Some text in bold", TextType.BOLD)
        node2 = TextNode("This is an url", TextType.URL, "https://mirys.pl")
        self.assertNotEqual(node, node2)

    def test_not_eq_url_none(self):
        node = TextNode("This is an url", TextType.URL, None)
        node2 = TextNode("This is an url", TextType.URL, "https://mirys.pl")
        self.assertNotEqual(node, node2)

    def test_not_eq_missing_props(self):
        node = TextNode(TextType.URL, "https://mirys.pl")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold_with_tag(self):
        node = TextNode("This is a text node in bold", TextType.BOLD)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node in bold")

    def test_text_img_props(self):
        node = TextNode("Alt text of img LeafNode", TextType.IMG, "https://mirys.pl/")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")             
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {'src': 'https://mirys.pl/', 'alt': 'Alt text of img LeafNode'})


if __name__ == "__main__":
    unittest.main()