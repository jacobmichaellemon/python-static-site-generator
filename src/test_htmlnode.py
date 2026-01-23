import unittest
from htmlnode import HTMLNode


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

    

if __name__ == "__main__":
    unittest.main()
