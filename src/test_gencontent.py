import unittest

from gencontent import extract_title

class Testgencontent(unittest.TestCase):

    def test_extract_title(self):
        markdown = """
# this is the title   
this is not the title
**bold** and _italic_
"""
        self.assertEqual(extract_title(markdown), "this is the title")

    def test_extract_title_no_heading(self):
        markdown = "this string has no heading"
        with self.assertRaises(Exception):
            extract_title(markdown)