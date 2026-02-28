import textnode
import htmlnode
import nodehelper

def main():
    #prop = {
    #    "href": "https://www.google.com",
    #    "target": "_blank",
    #    }

    #hnode = htmlnode.HTMLNode(tag="<div>", value="test_value", children="children_value", props=prop)
    #hnode.__repr__()

    #node = textnode.TextNode("This is some anchor text", "link", "https://www.boot.dev")
    #print(node.__repr__())
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = nodehelper.text_to_textnodes(text)
    print(nodes)

main()