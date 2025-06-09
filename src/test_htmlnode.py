import sys
import unittest
import logging

from htmlnode import HTMLNode

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestHTMLNode(unittest.TestCase):
    def test_html_to_props(self):
        props = {}
        props["href"] = "https://www.google.com"
        props["target"] = "_blank"
        node = HTMLNode(props=props)
        s = node.props_to_html()
        self.assertEqual(s, 'href="https://www.google.com" target="_blank"')

    def test_html_equal(self):
        props = {}
        props["href"] = "https://www.google.com"
        props["target"] = "_blank"
        node = HTMLNode(props=props)
        node2 = HTMLNode(props=props)
        self.assertEqual(node, node2)

    def test_html_not_equal(self):
        props = {}
        props["href"] = "https://www.google.com"
        props["target"] = "_blank"
        node = HTMLNode(props=props)

        props2 = {}
        props2["href"] = "https://www.google2.com"
        props2["target"] = "_blank"
        node2 = HTMLNode(props=props2)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
