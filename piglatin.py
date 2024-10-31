
class PigLatin:
    """
    PigLatin class to translate english phrases to pig latin
    """

    def __init__(self, phrase: str):
        """
        initialize the pig latin object

        :param phrase: the english phrase to be translated
        """

        self.phrase = phrase

    def get_phrase(self) -> str:
        """
        Returns the english phrase

        :return: the english phrase as a string
        """

        return self.phrase

    def translate(self) -> str:
        """
        Translates the phrase from english to pig latin

        :return: the piglatin translation as string
        """

        # Handling words that are empty strings
        if self.phrase == "":
            return "nil"

        words = self.phrase.split()
        translated_words = []

        for word in words:

            # handling for words that begin with vowel
            if word[0] in "aeiouAEIOU":
                if word[-1] in "aeiouAEIOU":
                    translated_words.append(word + "yay")
                elif word[-1] == 'y':
                    translated_words.append(word + "nay")
                else:
                    translated_words.append(word + "ay")

            # handling for words that begin with consonants
            else:
                consonants = ""
                i = 0
                while i < len(word) and word[i] not in "aeiouAEIOU":
                    consonants += word[i]
                    i += 1
                translated_words.append(word[i:] + consonants + "ay")

        return " ".join(translated_words)

