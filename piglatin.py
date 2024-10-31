
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

        # Handling words starting with consonants and moving them to the end
        consonants = ""
        i = 0
        while i < len(self.phrase) and self.phrase[i] not in "aeiouAEIOU":
            consonants += self.phrase[i]
            i += 1

        if consonants:
            return self.phrase[i:] + consonants + "ay"

        # Handling words ending with 'y'
        if self.phrase[-1] == 'y':
            return self.phrase + "nay"

        # Handling words ending with a vowel
        if self.phrase[-1] in "aeiouAEIOU":
            return self.phrase + "yay"

        # Handling words that end with consonants
        else:
            return self.phrase + "ay"

