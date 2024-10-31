import unittest
from idlelib.pyparse import trans

from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        """to test if the phrase given as input is returned as is"""

        translator = PigLatin("hello world")
        self.assertEqual("hello world", translator.get_phrase())

    def test_translate_empty_string(self):
        """test if an empty word returns `nil` as string """

        translator = PigLatin("")
        self.assertEqual("nil", translator.translate())

    def test_translate_word_ends_with_y(self):
        """test if a word ending with `y` is appended with `nay` when translated"""

        translator = PigLatin("any")
        self.assertEqual("anynay", translator.translate())

    def test_translate_word_ends_with_vowel(self):
        """test if a word ending with a vowel is appended with `yay` when translated"""

        translator = PigLatin("apple")
        self.assertEqual("appleyay", translator.translate())

    def test_translate_word_ends_with_consonant(self):
        """test if a word ending with a consonant is appended with `ay` when translated"""

        translator = PigLatin("ask")
        self.assertEqual("askay", translator.translate())

    def test_translate_word_starts_with_consonant(self):
        """if a word starts with a consonant, the translation should have the consonant removed
        from the beginning and appended to the end along with `ay`
        """

        translator = PigLatin("hello")
        self.assertEqual("ellohay", translator.translate())