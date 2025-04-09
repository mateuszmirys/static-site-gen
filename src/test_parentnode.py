import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_children(self):
        first_child = LeafNode("span", "first child")
        second_child = LeafNode("b", "second child")
        parent_node = ParentNode("div", [first_child, second_child])
        target_output = "<div><span>first child</span><b>second child</b></div>"
        self.assertEqual(parent_node.to_html(), target_output)

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children_many_grandchildren(self):
        grandchild_node_one = LeafNode("b", "grandchild")
        grandchild_node_two = LeafNode("a", "second grandchild")
        grandchild_node_three = LeafNode("span", "third grandchild")
        child_node_one = ParentNode("h1", [grandchild_node_one, grandchild_node_two])
        child_node_two = ParentNode("p", [grandchild_node_three])
        parent_node = ParentNode("div", [child_node_one, child_node_two])
        self.assertEqual(
            parent_node.to_html(),
            "<div><h1><b>grandchild</b><a>second grandchild</a></h1><p><span>third grandchild</span></p></div>",
        )

    def test_to_html_parent_with_props(self):
        first_child = LeafNode("span", "first child")
        second_child = LeafNode("b", "second child")
        parent_node = ParentNode("div", [first_child, second_child], {"style": "display: block;"})
        target_output = '<div style="display: block;"><span>first child</span><b>second child</b></div>'
        self.assertEqual(parent_node.to_html(), target_output)        