import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_texttype_eq(self):
        for tt in TextType:
            node = TextNode("This is a text node", tt)
            node2 = TextNode("This is a text node", tt)
            self.assertEqual(node, node2)

    def test_texttype_not_eq(self):
        for tt in TextType:
            for ttt in TextType:
                if tt != ttt:
                    node = TextNode("This is a text node", tt)
                    node2 = TextNode("This is a text node", ttt)
                    self.assertNotEqual(node, node2)

    def test_texttype_w_url_eq(self):
        url = "https://example.com"
        for tt in TextType:
            node = TextNode("This is a text node", tt, url=url)
            node2 = TextNode("This is a text node", tt, url=url)
            self.assertEqual(node, node2)

    def test_texttype_w_url_not_eq(self):
        url = "https://example.com"
        for tt in TextType:
            for ttt in TextType:
                if tt != ttt:
                    node = TextNode("This is a text node", tt, url=url)
                    node2 = TextNode("This is a text node", ttt, url=url)
                    self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node 1", TextType.BOLD)
        node2 = TextNode("This is a text node 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_default_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_text_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_to_html(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic_to_html(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code_to_html(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link_to_html(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_img_to_html(self):
        node = TextNode(
            "This is a text node", TextType.IMAGE, url="https://example.com/img.png"
        )
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(
            html_node.props,
            {"src": "https://example.com/img.png", "alt": "This is a text node"},
        )


if __name__ == "__main__":
    unittest.main()
