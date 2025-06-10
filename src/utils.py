from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type: TextType):

    def delimiter_to_text_type():
        match delimiter:
            case "`":
                return TextType.CODE
            case "**":
                return TextType.BOLD
            case "__":
                return TextType.ITALIC

    def split_by_delimeter(node: TextNode):
        r_list = []
        if node.text_type != TextType.TEXT:
            r_list.append(node)
        else:
            a = node.text.split(delimiter, maxsplit=1)
            r_list.append(TextNode(text=a[0], text_type=TextType.TEXT))
            b = a[1].split(delimiter, maxsplit=1)
            r_list.append(TextNode(text=b[0], text_type=delimiter_to_text_type()))
            r_list.append(TextNode(text=b[1], text_type=TextType.TEXT))
        return r_list

    return list(map(split_by_delimeter, old_nodes))[0]
