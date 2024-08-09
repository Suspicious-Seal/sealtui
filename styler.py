import styles, errors, helpers

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
            else:
                _stlends = stlend.split(" ")
                for _stlend in _stlends:
                    indx = helpers.IndexOf(CurrentStyles, _stlend)
                    if indx < 0:
                        raise errors.SealStyleSyntaxError(f"""No style
                            to close. Style: {_stlend} at {_str} in
                            {string}""")
                    del CurrentStyles[indx]

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

def GetStyle(Style, args, text):
    STYLES = {
        "bold": styles.Bold,
        "underline": styles.Underline,
        "color": styles.Color,
    }

    try:
        return STYLES[Style](text, args)
    except KeyError:
        raise errors.SealStyleNotFoundError(f"""Could not find style {Style}.
        Style had arguments {args} and text {text}. 
        Make sure arguments are seperated from the style name using an colon (:)!""")

def StyleString(string):
    parsedstr = ParseString(string)

    TEXT = []
    for item in parsedstr:
        curtext = item[0]

        styles = item[1]
        
        for stl in styles:
            style = stl.split(":")[0]
            arguments = stl.split(":")[1:]

            _Style = GetStyle(style, arguments, curtext)
            curtext = _Style()

        TEXT.append(curtext + "\033[0m")

    ENDSTR = ""
    for txt in TEXT:
        ENDSTR += txt

    return ENDSTR
