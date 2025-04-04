import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
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


if __name__ == "__main__":
    unittest.main()