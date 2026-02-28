import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
import nodehelper


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAINTEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, None)

    def test_b_text(self):
        node = TextNode("Swiggity swooty", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Swiggity swooty")
        self.assertEqual(html_node.props, None)

    def test_i_text(self):
        node = TextNode("Badda bing", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Badda bing")
        self.assertEqual(html_node.props, None)
    
    def test_code_text(self):
        node = TextNode("Beeep boop, this is some code for an alien language", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Beeep boop, this is some code for an alien language")
        self.assertEqual(html_node.props, None)
    
    def test_link_text(self):
        node = TextNode("~yarrghhh, anchor text~", TextType.LINK, url="https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "~yarrghhh, anchor text~")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_image_text(self):
        node = TextNode("ALTERNATIVE text", TextType.IMAGE, url="https://img.url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props,{"src": "https://img.url", "alt": "ALTERNATIVE text"})

    def test_split_nodes_plain(self):
        node = TextNode("This is some text", TextType.PLAINTEXT, url=None)
        new_nodes = nodehelper.split_nodes_delimiter([node], "", TextType.PLAINTEXT)
        self.assertEqual(new_nodes, [node])

    def test_split_nodes_bold(self):
        node = TextNode("This is text with a **BOLDED WORDS** word", TextType.PLAINTEXT)
        new_nodes = nodehelper.split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.PLAINTEXT, None),
                                    TextNode("BOLDED WORDS", TextType.BOLD, None),
                                    TextNode(" word", TextType.PLAINTEXT, None)])
        
    def test_split_nodes_italics(self):
        node = TextNode("This is text with a _italic words_ word", TextType.PLAINTEXT)
        new_nodes = nodehelper.split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.PLAINTEXT, None),
                                    TextNode("italic words", TextType.ITALIC, None),
                                    TextNode(" word", TextType.PLAINTEXT, None)])
    def test_split_nodes_code(self):
        node = TextNode("This is text with a `important code business` word", TextType.PLAINTEXT)
        new_nodes = nodehelper.split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.PLAINTEXT, None),
                                    TextNode("important code business", TextType.CODE, None),
                                    TextNode(" word", TextType.PLAINTEXT, None)])
        
    def test_extract_markdown_images(self):
        matches = nodehelper.extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_markdown_images(self):
        matches = nodehelper.extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) Monkey Business--> ![ooooh banana](https://i.imgur.com/dkbananahorde.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("ooooh banana", "https://i.imgur.com/dkbananahorde.png")], matches)

    def test_extract_link_ref(self):
        matches = nodehelper.extract_markdown_links(
        "This is text with a link [googlin](https://www.google.com)"
        )
        self.assertListEqual([("googlin", "https://www.google.com")], matches)

    def test_extract_multiple_link_refs(self):
        matches = nodehelper.extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_images(self):
        node = TextNode(
                        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                        TextType.PLAINTEXT,
                        )
        new_nodes = nodehelper.split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAINTEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAINTEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
            )
        
    def test_split_links(self):
            node = TextNode(
                            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                            TextType.PLAINTEXT,
                            )
            new_nodes = nodehelper.split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This is text with a link ", TextType.PLAINTEXT),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode(" and ", TextType.PLAINTEXT),
                    TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                ],
                new_nodes,
                )
    
    def test_text_to_nodes_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = nodehelper.text_to_textnodes(text)
        self.assertListEqual(
                [
                    TextNode("This is ", TextType.PLAINTEXT, None),
                    TextNode("text", TextType.BOLD, None), 
                    TextNode(" with an ", TextType.PLAINTEXT, None), 
                    TextNode("italic", TextType.ITALIC, None), 
                    TextNode(" word and a ", TextType.PLAINTEXT, None), 
                    TextNode("code block", TextType.CODE, None), 
                    TextNode(" and an ", TextType.PLAINTEXT, None), 
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), 
                    TextNode(" and a ", TextType.PLAINTEXT, None), 
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                ],
                nodes,
                )

    

if __name__ == "__main__":
    unittest.main()
