def GetKey():
    import tty, termios, sys
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    if ch == "\x04":
        raise Exception("User hit Control+D. Ending program as result.")

    if ch == "\x1b":
        ch += GetKey()
        ch += GetKey()

    return ch

def IndexOf(_list, _item):
    for i in range(len(_list)):
        if _item == _list[i]: return i
    return -1

def ExtendText(text, length):
    text = str(text)
    diff = length - len(text)
    if diff < 0:
        return text[0:diff]
    
    txt=text
    txt+=" "*diff

    return txt

def MoveCursor(x, y):
    print("\033[%d;%dH" % (y, x), end="")
