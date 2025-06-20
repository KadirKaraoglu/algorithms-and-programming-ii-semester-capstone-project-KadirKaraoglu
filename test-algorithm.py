import unittest
from algorithm import boyer_moore_search

class TestBoyerMooreSearch(unittest.TestCase):
    """
    Test scenarios for the Boyer-Moore Search Algorithm.
    """

    def test_basic_search(self):
        text = "ABAAABCD"
        pattern = "ABC"
        expected_indices = [4]
        self.assertEqual(boyer_moore_search(text, pattern), expected_indices)

        text = "THIS IS A TEST TEXT"
        pattern = "TEST"
        expected_indices = [10]
        self.assertEqual(boyer_moore_search(text, pattern), expected_indices)

    def test_multiple_occurrences(self):
        """
        Tests cases where the pattern appears multiple times in the text.
        """
        text = "DAVULCU VUR DAVULAAAA VUR VUR DURMA"
        pattern = "VUR"
        expected_indices = [8, 22, 26]
        self.assertEqual(boyer_moore_search(text, pattern), expected_indices)

        text = "AAAAA"
        pattern = "AA"
        expected_indices = [0, 1, 2, 3]
        self.assertEqual(boyer_moore_search(text, pattern), expected_indices)

    def test_no_occurrence(self):
        """
        Tests cases where the pattern is not found in the text.
        """
        text = "Hello World"
        pattern = "KADIR"
        expected_indices = []
        self.assertEqual(boyer_moore_search(text, pattern), expected_indices)

    def test_empty_pattern(self):
        """
        Tests the case where an empty pattern is searched.
        An empty pattern is generally considered to be found at every possible starting position
        in the text (length of text + 1).
        """
        text = "abc"
        pattern = ""
        expected_indices = [0, 1, 2, 3]
        self.assertEqual(boyer_moore_search(text, pattern), expected_indices)

        text = ""
        pattern = ""
        expected_indices = [0]
        self.assertEqual(boyer_moore_search(text, pattern), expected_indices)

    def test_empty_text(self):
        """
        Tests searching for a pattern within an empty text.
        """
        text = ""
        pattern = "abc"
        expected_indices = []
        self.assertEqual(boyer_moore_search(text, pattern), expected_indices)

    def test_pattern_longer_than_text(self):
        """
        Tests cases where the pattern is longer than the text.
        """
        text = "short"
        pattern = "longer pattern than text"
        expected_indices = []
        self.assertEqual(boyer_moore_search(text, pattern), expected_indices)

    def test_single_character_pattern(self):
        """
        Tests single-character patterns.
        """
        text = "KADIR KARAOGLU"
        pattern = "A"
        expected_indices = [1, 7, 9]
        self.assertEqual(boyer_moore_search(text, pattern), expected_indices)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
