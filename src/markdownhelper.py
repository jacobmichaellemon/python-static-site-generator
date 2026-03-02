from enum import Enum
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
