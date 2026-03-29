from enum import Enum
from textnode import text_node_to_html_node
from nodehelper import text_to_textnodes
from htmlnode import ParentNode
import re

class BlockType(Enum):
    paragraph = 1
    heading = 2
    code = 3
    quote = 4
    unordered_list = 5
    ordered_list = 6

def block_to_block_type(markdown):
    heading = re.findall(r"(#{1,6} (.*))\w+", markdown)
    code = re.findall(r"(`{3}\n(.*)\n`{3})+", markdown)
    quote = re.findall(r"(> ?(.*))\w+", markdown)
    ulist = re.findall(r"(- (.*))\w+", markdown)
    olist = re.findall(r"1.(.*)", markdown)

    if heading:
        return BlockType.heading
    if code:
        return BlockType.code
    if quote:
        return BlockType.quote
    if ulist:
        return BlockType.unordered_list
    if olist:
        return BlockType.ordered_list
    
    return BlockType.paragraph

def markdown_to_blocks(markdown):
    block_to_return = []
    md = markdown.split("\n\n")
    for block in md:
        block = block.strip()
        if not block:
            continue
        else:
            block_to_return.append(block)
    return block_to_return

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def markdown_to_html_node(markdown):
    htmlnodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match(block_type):
            case BlockType.paragraph:
                lines = block.split("\n")
                paragraph = " ".join(lines)
                children = text_to_children(paragraph)
                node = ParentNode("p", children)
                htmlnodes.append(node)
            case _:
                return f"Issue creating html with {block}"
    return ParentNode("div", htmlnodes)