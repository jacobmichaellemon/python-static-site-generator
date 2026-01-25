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