
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
            stripped_word = word.rstrip('!.,?')
            punctuation = word[len(stripped_word):]

            # Handling for words that begin with a vowel
            if stripped_word[0].lower() in "aeiou":
                if stripped_word[-1].lower() in "aeiou":
                    translated_words.append(stripped_word + "yay" + punctuation)
                elif stripped_word[-1] == 'y':
                    translated_words.append(stripped_word + "nay" + punctuation)
                else:
                    translated_words.append(stripped_word + "ay" + punctuation)

            # Handling for words that begin with consonants
            else:
                consonants = ""
                i = 0
                for i, letter in enumerate(stripped_word):
                    if letter.lower() in "aeiou":
                        break
                    consonants += letter

                translated_words.append(stripped_word[i:] + consonants + "ay" + punctuation)

        return self.__delimiter.join(translated_words)

