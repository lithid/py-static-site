from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType


def main():
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())


if __name__ == "__main__":
    main()
