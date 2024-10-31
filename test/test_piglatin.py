import unittest
from idlelib.pyparse import trans

from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        """
        to test if the phrase given as input is returned as is
        """

        translator = PigLatin("hello world")
        self.assertEqual("hello world", translator.get_phrase())

    def test_translate_empty_string(self):
        """
        test if an empty word returns `nil` as string
        """

        translator = PigLatin("")
        self.assertEqual("nil", translator.translate())

    def test_translate_word_ends_with_y(self):
        """
        test if a word ending with `y` is appended with `nay` when translated
        """

        translator = PigLatin("any")
        self.assertEqual("anynay", translator.translate())

    def test_translate_word_ends_with_vowel(self):
        """
        test if a word ending with a vowel is appended with `yay` when translated
        """

        translator = PigLatin("apple")
        self.assertEqual("appleyay", translator.translate())

    def test_translate_word_ends_with_consonant(self):
        """
        test if a word ending with a consonant is appended with `ay` when translated
        """

        translator = PigLatin("ask")
        self.assertEqual("askay", translator.translate())

    def test_translate_word_starts_with_consonant(self):
        """
        if a word starts with a consonant, the translation should have the consonant removed
        from the beginning and appended to the end along with `ay`. This rule has priority over others
        """

        translator = PigLatin("hello")
        self.assertEqual("ellohay", translator.translate())

    def test_translate_word_with_consonant_in_beginning(self):
        """
        If the word has consonants in the beginning, the translation should have the consonant removed
        from the beginning and appended to the end along with `ay`. The trasnlator should keep removing the
        consonants till it reaches a vowel. This rule has priority over others
        """

        translator = PigLatin("known")
        self.assertEqual("ownknay", translator.translate())

    def test_translate_words_seperated_by_whitespaces(self):
        """
        If the words have whitespaces, the translator will apply the translation rules to the individual words.
        """

        translator = PigLatin("hello world")
        self.assertEqual("ellohay orldway", translator.translate())

    def test_translate_words_seperated_by_hyphen(self):
        """
        If the words are seperated by hyphens, they are treated as individual words in the translation.
        The hyphen stays in the translation
        """

        translator = PigLatin("well-being")
        self.assertEqual("ellway-eingbay", translator.translate())

    def test_translate_words_containing_valid_punctuations(self):
        """
        test if the word containing a valid punctuation is translated with the punctuations still intact in the
        translation.
        """

        translator = PigLatin("hello world!")
        self.assertEqual("ellohay orldway!", translator.translate())

    def test_translate_words_containing_invalid_punctuation(self):
        """If the words contain invalid puncutations, the translator should raise a
        `PigLatinError`.
        """
        translator = PigLatin("hello world[")

        self.assertRaises(PigLatinError, translator.translate)

    def test_translate_words_title_case(self):
        """if words have titlecases, their translation should also be upper case"""

        translator = PigLatin("APPLE")
        self.assertEqual("APPLEYAY", translator.translate())

