import unittest
from extract_markdown import *

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_image(self):
        test_string = "Here's an image ![cute cat](https://mirys.pl/cat.png)"
        output = [("cute cat", "https://mirys.pl/cat.png")]
        self.assertEqual(extract_markdown_images(test_string), output)

    def test_extract_multiple_images(self):
        test_string = "Image One ![a crow](https://mirys.pl/crow.png) and Image Two ![a swallow](https://mirys.pl/swallow.png)"
        output = [("a crow", "https://mirys.pl/crow.png"), ("a swallow", "https://mirys.pl/swallow.png")]
        self.assertEqual(extract_markdown_images(test_string), output)

    def test_extract_links(self):
        test_string = "A link formatted in Markdown [mirys.pl](https://mirys.pl/)"
        output = [("mirys.pl", "https://mirys.pl/")]
        self.assertEqual(extract_markdown_links(test_string), output)