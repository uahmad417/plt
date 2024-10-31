
class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        if self.phrase.endswith("y"):
            return self.phrase + "nay"
        if self.phrase[-1] in "aeiou":
            return self.phrase + "yay"

