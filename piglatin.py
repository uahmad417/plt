
class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        if self.phrase[-1] in "aeiouAEIOU":
            return self.phrase + "yay"
        elif self.phrase[-1] == "y":
            return self.phrase + "nay"
        else:
            return self.phrase + "ay"

