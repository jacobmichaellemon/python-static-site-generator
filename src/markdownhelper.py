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
