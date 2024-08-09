from sealtui import styler, errors, helpers

class Prompt:
    ENTER = "\r"
    BACKSPACE = "\x7f"

    def baseprompt(self):
        key = helpers.GetKey()

        if key == self.BACKSPACE: 
            self.text = self.text[0:-1]
        elif key == self.ENTER: 
            return True
        elif key[0] == "\x1b":
            pass
        else:
            if self.maxlen<0: self.text += key
            elif len(self.text)<self.maxlen: self.text += key

        return False

    def __init__(self, _input, maxlen, args=None):
        self.input = _input
        self.maxlen = maxlen
        self.args = args

    def __call__(self):
        self.promptinit()
        self.text = ""
        
        self.prompt()
        print("\033c",end="")
        return self.text

class ClassicPrompt(Prompt):
    def promptinit(self):
        print("\033c",end="")
        print(f"+{'-'*(self.maxlen)}+")
        print()
        print(f"+{'-'*(self.maxlen)}+")

    def prompt(self):
        finished = False
        while finished != True:
            finished = self.baseprompt() 
            text = helpers.ExtendText(self.text, self.maxlen)
            
            helpers.MoveCursor(0,2)
            print(f"|{text}|")

        return

class SearchPrompt(Prompt):
    def promptinit(self):
        print("\033c",end="")
        print(f"+{'-'*(self.maxlen)}+")
        print()
        print(f"+{'-'*(self.maxlen)}+")
        print()

    def prompt(self):
        searchitems = self.args
        
        if type(searchitems) != list:
            raise errors.SealStyleArgumentsInvalidError(f"Expected list as arguments for SearchPrompt. Got '{type(self.args)}' instead.")

        finished=False
        while finished != True:
            finished=self.baseprompt()
            text = helpers.ExtendText(self.text, self.maxlen)

            helpers.MoveCursor(0,2)
            print(f"|{text}|")

            helpers.MoveCursor(0,4)

            count=0
            for item in searchitems:
                if not self.text in item: continue
                print(f"|{helpers.ExtendText(item, self.maxlen)}|")
                count += 1

            if count == 0:
                print(f"|{helpers.ExtendText('No results', self.maxlen)}|")
            print(f"+{'-'*(self.maxlen)}+")

            for i in range(len(searchitems)-count):
                print(f" {' '*self.maxlen} ")
