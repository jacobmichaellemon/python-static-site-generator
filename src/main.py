#import textnode
import htmlnode

def main():
    prop = {
        "href": "https://www.google.com",
        "target": "_blank",
        }

    hnode = htmlnode.HTMLNode(tag="<div>", value="test_value", children="children_value", props=prop)
    hnode.__repr__()

    #node = textnode.TextNode("This is some anchor text", "link", "https://www.boot.dev")
    #print(node.__repr__())

main()