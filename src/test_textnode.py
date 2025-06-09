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


if __name__ == "__main__":
    unittest.main()
