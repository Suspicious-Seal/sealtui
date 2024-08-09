import styles, errors

def ParseString(string):
    # The job of this function is ONLY to parse the strings into their styles (in string form) 
    # for the styler to then process.
    
    splstr = string.split("[")

    CurrentStyles = []

    Text = [] # List of tuples (but len of 2)
    # FORMAT: ( TEXT: str, STYLE: list(str) )

    for _str in splstr:
        if len(_str) == 0: continue # Handle any blank strings ( "" )

        if _str[0] == "/":
            # Handle the style part of the text
            stylestr = _str.split("]")[0]
            stlend = stylestr[1:]
            if len(stlend) < 1: 
                CurrentStyles = []

            # Handle the normal text part (If it exists)
            textstr = _str.split("]")[1]
            if len(textstr) == 0: continue
            Text.append( (textstr, []) ) # No style, so add it to the list w/o style

        else:
            stylestr = _str.split("]")[0]
            textstr = _str.split("]")[1]

            for stl in stylestr.split(" "):
                if len(stl) == 0: continue # Ensure no blank styles enter the list
                else: CurrentStyles.append(stl)

            Text.append( (textstr, CurrentStyles) )

    return Text

def GetStyle(Style, text, args):
    STYLES = {
        "bold": styles.Bold,
        "underline": styles.Underline,
    }

    return STYLES[Style](text, args)

def StyleString(string):
    parsedstr = ParseString(string)

    TEXT = []
    for item in parsedstr:
        curtext = item[0]

        STYLES = []
        styles = item[1]
        for stl in styles: STYLES.append(GetStyle( stl, curtext, curtext.split(":")[1:] ))

        for STL in STYLES:
            curtext = STL()

        TEXT.append(curtext)

    ENDSTR = ""
    for txt in TEXT:
        ENDSTR += txt

    return ENDSTR
