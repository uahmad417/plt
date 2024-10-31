
import string
from error import PigLatinError

class PigLatin:
    """
    PigLatin class to translate English phrases to Pig Latin
    """

    def __init__(self, phrase: str):
        """
        Initialize the Pig Latin object

        :param phrase: the English phrase to be translated
        """
        self.phrase = phrase
        self.__delimiter = " "

    def get_phrase(self) -> str:
        """
        Returns the English phrase

        :return: the English phrase as a string
        """
        return self.phrase

    def translate(self) -> str:
        """
        Translates the phrase from English to Pig Latin

        :return: the Pig Latin translation as string
        """
        # Handling words that are empty strings
        if self.phrase == "":
            return "nil"

        # Splitting the phrase based on spaces and hyphens
        if '-' in self.phrase:
            words = self.phrase.split('-')
            self.__delimiter = "-"
        else:
            words = self.phrase.split()
            self.__delimiter = " "

        translated_words = []

        for word in words:
            # Strip punctuation from the end of the word
            stripped_word = word.rstrip("!.,?;:'()")
            punctuation = word[len(stripped_word):]

            # Check for invalid punctuation
            if any(char in stripped_word for char in string.punctuation):
                raise PigLatinError("Invalid punctuation found in the word.")

            # Handling for words that begin with a vowel
            if stripped_word[0].lower() in "aeiou":
                if stripped_word[-1].lower() in "aeiou":
                    translation = stripped_word + "yay" + punctuation
                elif stripped_word[-1] == 'y':
                    translation = stripped_word + "nay" + punctuation
                else:
                    translation = stripped_word + "ay" + punctuation

            # Handling for words that begin with consonants
            else:
                consonants = ""
                i = 0
                for i, letter in enumerate(stripped_word):
                    if letter.lower() in "aeiou":
                        break
                    consonants += letter

                translation = stripped_word[i:] + consonants + "ay" + punctuation

            # Maintain the case of the original word
            if word.isupper():
                translation = translation.upper()

            translated_words.append(translation)

        return self.__delimiter.join(translated_words)

