#!/usr/bin/python3
"""Function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Print a text
    Raises:
        TypeError: if one text argument is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    
    characters = ['.', '?', ':']
    i = 0
    while(i < len(text) - 1):
        c = 0
        if text[i] in characters:
            print(text[i], end='\n\n')
            if i < (len(text) - 1):
                i = i + 1
                while(text[i] == ' '):
                    c += 1
                    i+=1
                continue
        else:
            print(text[i], end='')
        
        i = i + c + 1
