import unittest

from src.utils import extract_title


class TestUtils(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello World"), "Hello World")

    def test_extract_title_no_header(self):
        with self.assertRaises(Exception):
            extract_title("Hello World")
