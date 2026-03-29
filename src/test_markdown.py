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
    def test_block_to_blocktype_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
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

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdownhelper.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headingblock(self):
        md = """
## Hello World
"""

        node = markdownhelper.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Hello World</h2></div>",
        )

    def test_quoteblock(self):
        md = """
> This is a quote
> with multiple lines
"""
# expected: <div><blockquote>This is a quote with multiple lines</blockquote></div>

    def test_unorderedlistblock(self):
        md = """
- First item
- Second item
- Third item
"""
# expected: <div><ul><li>First item</li><li>Second item</li><li>Third item</li></ul></div>
    
    def test_orderedlistblock(self):
        md = """
1. First item
2. Second item
3. Third item
"""
# expected: <div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>
