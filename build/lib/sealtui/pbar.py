from sealtui import helpers, errors, core
from math import ceil, floor

class Bar:
    def __init__(self, size, lchar, uchar):
        self.size = size
        self.lchar = str(lchar)
        self.uchar = str(uchar)

    def start(self, start, end):
        self.end = end
        self.start = start
        self.current = start

        self.update(0)

class ProgressBar(Bar):
    def update(self, current=None):
        if current != None: self.current = current
        else: self.current += 1

        print("\r[", end="")
        loaded = self.current
        unloaded = self.end - loaded
        
        # Convert the values into percentage
        loaded_percent = floor(loaded / self.end * 100)
        unloaded_percent = ceil(unloaded / self.end * 100)

        # Convert the percentage into the characters
        loaded = floor(loaded_percent / self.size)
        unloaded = ceil(unloaded_percent / self.size)

        CURRENT_END = f"{self.current}/{self.end}"
        
        if loaded_percent < 33: COLOR = "red"
        elif loaded_percent > 32 and loaded_percent < 70: COLOR = "yellow"
        else: COLOR = "green"

        PERCENT = core.styled(f"[color:{COLOR}]{loaded_percent}[/]")

        core.sealprint(f"{self.lchar * loaded}{self.uchar * unloaded}", end="")
        print(f"] [{CURRENT_END}] [{PERCENT}%]",end="")

    def stop(self):
        print()
