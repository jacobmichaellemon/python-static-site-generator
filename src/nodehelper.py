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
    nodes = []
    for node in old_nodes:
        temp_nodes = []
        temp_text = []
        temp_images = []
        temp_text = re.sub(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", '-', node.text)
        temp_text = temp_text.split('-')
        temp_images = extract_markdown_images(node.text)
        for i in range(len(temp_text)-1):
            temp_nodes.append(TextNode(temp_text[i], TextType.PLAINTEXT))
            if i < len(temp_images):
                temp_nodes.append(TextNode(temp_images[i][0], TextType.IMAGE, temp_images[i][1]))
        nodes.extend(temp_nodes)
    return nodes

def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        temp_nodes = []
        temp_text = []
        temp_links = []
        temp_text = re.sub(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", '-', node.text)
        temp_text = temp_text.split('-')
        temp_links = extract_markdown_links(node.text)
        for i in range(len(temp_text)-1):
            temp_nodes.append(TextNode(temp_text[i], TextType.PLAINTEXT))
            if i < len(temp_links):
                temp_nodes.append(TextNode(temp_links[i][0], TextType.LINK, temp_links[i][1]))
        nodes.extend(temp_nodes)
    return nodes