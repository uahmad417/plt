
class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"

        # if the phrase starts with a consonant
        if self.phrase[0] not in "aeiouAEIOU":
            return self.phrase[1:] + self.phrase[0] + "ay"

        # if the phrase ends with a vowel
        if self.phrase[-1] in "aeiouAEIOU":
            return self.phrase + "yay"

        # if the phrase ends with `y`
        elif self.phrase[-1] == "y":
            return self.phrase + "nay"

        # if the phrase ends with a consonant
        else:
            return self.phrase + "ay"

