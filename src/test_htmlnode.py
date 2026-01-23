import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_not_eq(self):
        prop1 = {
        "href": "https://www.google.com",
        "target": "_blank",
        "tooty" : "fruity",
        }
        prop2 = {
        "href": "https://www.boot.dev",
        "target": "_blank",
        }

        hnode1 = HTMLNode(tag="<div>", value="test_value", children="children_value", props=prop1)
        hnode2 = HTMLNode(tag="<p>", value="test_value", children="children_value", props=prop2)


        self.assertNotEqual(hnode1.props_to_html(), hnode2.props_to_html())

    def test_props_format(self):
        prop = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        hnode = HTMLNode(tag="<div>", value="test_value", children="children_value", props=prop)
        expected_outcome = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(hnode.props_to_html(), expected_outcome)

    def test_none_init(self):
        hnode = HTMLNode()
        expected_outcome = None
        self.assertEqual(hnode.tag, expected_outcome)
        self.assertEqual(hnode.value, expected_outcome)
        self.assertEqual(hnode.children, expected_outcome)
        self.assertEqual(hnode.props, expected_outcome)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_link_with_props(self):
        prop = { "href": "https://www.google.com" }
        node = LeafNode("a", "Click me!", prop)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_invalid_link(self):
        prop = { "href": "https://www.google.com" }
        node = LeafNode("a", "Click me!", prop)
        self.assertNotEqual(node.to_html(), '$$$   <a href="https://www.google.com">Click me!</a>')

    def test_to_html_blank_children(self):
        child_node = LeafNode("", "")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><></></div>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        child1_node = LeafNode("b", "WOW")
        child2_node = LeafNode("p", "holy moly")
        parent_node = ParentNode("div", [child1_node, child2_node])
        self.assertEqual(parent_node.to_html(), "<div><b>WOW</b><p>holy moly</p></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
