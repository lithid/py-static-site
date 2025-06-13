from utils import copy_files_recursive, generate_page, generate_pages_recursive
from textnode import TextNode, TextType


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


if __name__ == "__main__":
    copy_files_recursive("static", "public", True)
    generate_pages_recursive("content", "template.html", "public")
