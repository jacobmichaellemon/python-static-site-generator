import unittest

import markdownhelper
from markdownhelper import BlockType

class TestHTMLNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdownhelper.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blocktype_ulist(self):
        md = """
- This is a list
- with items
"""
        block_type = markdownhelper.block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.unordered_list
        )
    def test_block_to_blocktype_olist(self):
        md = """
1. This is a list
2. with items
"""
        block_type = markdownhelper.block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.ordered_list
        )
    def test_block_to_blocktype_ulist(self):
        md = """
```
This is code
```
"""
        block_type = markdownhelper.block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.code
        )

    def test_block_to_blocktype_quote(self):
        md = """
> quote about really cool things
"""
        block_type = markdownhelper.block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.quote
        )

    def test_block_to_blocktype_paragraph(self):
        md = """
ZZZZZZZZzzzzzzzZZZZZzZzzzzzzzzz
zzzzz
zzzz
zz
z
"""
        block_type = markdownhelper.block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.paragraph
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdownhelper.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

