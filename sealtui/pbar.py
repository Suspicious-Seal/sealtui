from sealtui import helpers, errors, core
from math import ceil, floor

from time import sleep # REMOVE IN PRODUCTION

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

        print("\r|", end="")
        loaded = self.current
        unloaded = self.end - loaded
        
        # Convert the values into percentage
        loaded = floor(loaded / self.end * 100)
        unloaded = ceil(unloaded / self.end * 100)

        # Convert the percentage into the characters
        loaded = floor(loaded / self.size)
        unloaded = ceil(unloaded / self.size)

        core.sealprint(f"{self.lchar * loaded}{self.uchar * unloaded}", end="")
        print("|",end="")

    def stop(self):
        print()

mybar = ProgressBar(10, "[color:red]#[/]", "[color:red]-[/]")
mybar.start(0, 17)
mybar.update()
mybar.stop()
