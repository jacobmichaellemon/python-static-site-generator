from enum import Enum
from textnode import text_node_to_html_node, TextType
from nodehelper import text_to_textnodes, TextNode
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
    code = re.findall(r"`{3}", markdown) #finds all ``` patterns, 2 or more means we have an opening and closing pair
    quote = re.findall(r"(> ?(.*))\w+", markdown)
    ulist = re.findall(r"(- (.*))\w+", markdown)
    olist = re.findall(r"1.(.*)", markdown)

    if heading:
        return BlockType.heading
    if len(code) > 1:
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
            case BlockType.code:
                stripped = block[4:-3]
                textnode = TextNode(stripped, TextType.PLAINTEXT)
                child = text_node_to_html_node(textnode)
                node = ParentNode("code", [child])
                pre = ParentNode("pre", [node])
                htmlnodes.append(pre)
            case BlockType.heading:
                heading_size = 0
                for char in block:
                    if char == "#" and heading_size <= 6:
                        heading_size += 1
                    else:
                        break
                text = block[(heading_size + 1):]
                children = text_to_children(text)
                node = ParentNode(f"h{heading_size}", children)
                htmlnodes.append(node)
            case BlockType.quote:
                lines = block.split("\n")
                cleaned = []
                for line in lines:
                    cleaned.append(line.lstrip(">").strip())
                paragraph = " ".join(cleaned)
                children = text_to_children(paragraph)
                node = ParentNode("blockquote", children)
                htmlnodes.append(node)
            case BlockType.unordered_list:
                lines = block.split("\n")
                cleaned = []
                for line in lines:
                    text = line[2:]
                    children = text_to_children(text)
                    li_node = ParentNode("li", children)
                    cleaned.append(li_node)
                ul = ParentNode("ul", cleaned)
                htmlnodes.append(ul)
            case BlockType.ordered_list:
                lines = block.split("\n")
                cleaned = []
                for line in lines:
                    text = line.split(". ", 1)[1]
                    children = text_to_children(text)
                    li_node = ParentNode("li", children)
                    cleaned.append(li_node)
                ul = ParentNode("ol", cleaned)
                htmlnodes.append(ul)
            case _:
                return f"Issue creating html with {block}"
    return ParentNode("div", htmlnodes)

def extract_title(markdown):
    match = re.search(r'^#\s+(.+)$', markdown, re.MULTILINE) #^ checks line start, s\+ checks space, (.+) is generic capture group, $ marks end of line
    if not match:
        raise Exception("No title found in markdown file!!")
    # .group(1) gives you just the title text without the '#'
    return match.group(1) 