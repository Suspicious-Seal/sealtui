from sealtui import errors

class Style:
    def __init__(self, text, args):
        self.text = str(text)
        self.end = "\033[0m"
        self.args = args

    def __call__(self):
        return self.style()

class Bold(Style):
    def style(self):
        return "\033[1m" + self.text

class Underline(Style):
    def style(self):
        return "\033[4m" + self.text

class Color(Style):
    COLORS = {
        "red": "\033[91m",
        "yellow": "\033[93m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "cyan": "\033[96m",
        "darkcyan": "\033[36m",
        "purple": "\033[95m",
    }

    def style(self):
        try:
            clr = self.COLORS[self.args[0]]
            return clr + self.text 
        except KeyError:
            raise errors.SealStyleInvalid(f"Invalid Color: {self.args[0]}")
