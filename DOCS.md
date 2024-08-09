# SealTUI Documentation

## Styling
All text can be styled. Text in SealTUI is styled using a tag like system, called SealStyle.
 - EXAMPLE: [bold]text[/]

Text inside brackets [ ] will be counted as style.

If the first character inside the brackets is a /, all styles inside will be removed from the following text.
 - If no styles are specified after the /, it removes all styles from the following text.

**Arguments**

Some styles need arguments, like color.
Arguments are specified with the colon :
 - All arguments come AFTER the style name.
   - EXAMPLE: [color:red bold]text[/]
 - If arguments are not supplied to a style that requries arguments, an exception is thrown.

**Styles**

bold
 Self explanitory.
 - Arguments: None

underline
 Self explanitory.
 - Arguments: None

color
 Applies color to the text.
 - Arguments (1): Color Name - NOT CASE SENSITIVE

**Colors**

Red
Yellow
Green
Blue
Cyan
DarkCyan
Purple

## Prompts
All prompts follow a basic format: The class is initialized, the class is called, the class returns a string.
During class initialization, you can specify that you want to sanitize inputs. This is done using: sanitize=True.

Prompt template:
 - Prompt(Input Field, Max Length, Arguments=None, sanitize=False)

To initiate a prompt:
 - print(MyPrompt())
 - Simply call the class, as it triggers the \_\_call\_\_ method of the class.

**Prompt Types**

ClassicPrompt
 A classic prompt. Simply shows a box for input, and returns it when the user presses enter.
 - Arguments: None

SearchPrompt
 A version of the ClassicPrompt. Has a box for input, but as the user types, it filters
  through all the different items provided.
 - Arguments: Items to filter (list)
