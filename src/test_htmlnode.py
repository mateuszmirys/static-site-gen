import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_is_eq_to_prop(self):
        test_prop = {"href": "https://mirys.pl", "target": "_blank"}
        test_output = ' href="https://mirys.pl" target="_blank"'
        input = HTMLNode(None, None, None, test_prop)
        output = input.props_to_html()
        self.assertEqual(output, test_output)

    def test_prop_none(self):
        test_prop = {"href": "https://mirys.pl", "target": "_blank"}
        test_output = ' href="https://mirys.pl" target="_blank"'
        input = HTMLNode(None, None, None, None)
        output = input.props_to_html()
        self.assertNotEqual(output, test_output)
    
    def test_with_values(self):
        test_prop = {"href": "https://mirys.pl", "target": "_blank"}
        test_output = ' href="https://mirys.pl" target="_blank"'
        input = HTMLNode("<a>", None, None, test_prop)
        output = input.props_to_html()
        self.assertEqual(output, test_output)

if __name__ == "__main__":
    unittest.main()