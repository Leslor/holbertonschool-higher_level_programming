#!/usr/bin/python3
"""Function that prints a text with 2 new lines after each of
    these characters: ., ? and :"""


def text_indentation(text):
    """Print a text
    Raises:
        TypeError: if one text argument is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    characters, new_text = ['.', '?', ':', '\n'], ''
    size, starting = len(text), True
    idx = 0

    while idx < size:
        if text[idx] == ' ' and starting is True:
            idx += 1
            continue

        starting = False
        if text[idx] in characters:
            new_text += text[idx]
            if text[idx] != '\n':
                new_text += '\n\n'
            idx += 1
            while idx < size and text[idx] == ' ':
                idx += 1
                continue

        if idx < size:
            new_text += text[idx]
            idx += 1
    print(new_text, end='')
