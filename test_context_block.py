import unittest
from context_block import format_context_block, extract_context

class TestContextBlock(unittest.TestCase):
    def test_format_empty(self):
        self.assertEqual(format_context_block(""), "")

    def test_format_single(self):
        result = format_context_block("User asked about pyglet.")
        self.assertIn("User asked about pyglet.", result)
        self.assertIn("<memory>", result)
        self.assertIn("</memory>", result)

    def test_format_multiple(self):
        result = format_context_block("Fact 1.\n\nFact 2.")
        self.assertIn("Fact 1.", result)
        self.assertIn("Fact 2.", result)
        self.assertIn("<memory>", result)

    def test_extract_roundtrip(self):
        original = "Some context."
        block = format_context_block(original)
        extracted = extract_context(block)
        self.assertEqual(original, extracted)

    def test_extract_empty_block(self):
        self.assertEqual(extract_context(""), "")

    def test_extract_wrong_tags(self):
        self.assertEqual(extract_context("<context>foo</context>"), "")

if __name__ == "__main__":
    unittest.main()
