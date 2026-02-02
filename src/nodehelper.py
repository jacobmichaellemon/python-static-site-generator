import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        match(text_type):
            case TextType.PLAINTEXT:
                new_nodes.append(TextNode(node.text, TextType.PLAINTEXT))
                break
            case TextType.BOLD:
                temp = node.text.split(delimiter)
                temp_list = []
                temp_list.append(TextNode(temp[0], TextType.PLAINTEXT))
                temp_list.append(TextNode(temp[1], TextType.BOLD))
                temp_list.append(TextNode(temp[2], TextType.PLAINTEXT))
                new_nodes.extend(temp_list)
                break
            case TextType.ITALIC:
                temp = node.text.split(delimiter)
                temp_list = []
                temp_list.append(TextNode(temp[0], TextType.PLAINTEXT))
                temp_list.append(TextNode(temp[1], TextType.ITALIC))
                temp_list.append(TextNode(temp[2], TextType.PLAINTEXT))
                new_nodes.extend(temp_list)
                break
            case TextType.CODE:
                temp = node.text.split(delimiter)
                temp_list = []
                temp_list.append(TextNode(temp[0], TextType.PLAINTEXT))
                temp_list.append(TextNode(temp[1], TextType.CODE))
                temp_list.append(TextNode(temp[2], TextType.PLAINTEXT))
                new_nodes.extend(temp_list)
                break

            case _:
                raise("Found no matching cases to delimit!!")
    return new_nodes

def extract_markdown_images(text):
    images_found = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images_found

def extract_markdown_links(text):
    links_found = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links_found

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAINTEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAINTEXT))
            new_nodes.append(
                TextNode(image[0], TextType.IMAGE, image[1])
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAINTEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAINTEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAINTEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAINTEXT))
    return new_nodes