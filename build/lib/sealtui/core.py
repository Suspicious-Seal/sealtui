from sealtui import styler, styles, errors

def sealprint(*args, end="\n", flush=True):
    for txt in args:
        styled_text = styler.StyleString(txt)
        print(styled_text, end=end, flush=flush)

def styled(arg):
    return styler.StyleString(arg)
