#!/usr/bin/python3
"""
This is a module for matrix operations.
It contains a function to divide all elements of a matrix.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    
    Args:
        text (str): The text to process
        
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    result = ""
    i = 0
    while i < len(text):
        char = text[i]
        result += char
        if char in ".?:":
            result += "\n\n"
        i += 1

    # Remove leading and trailing whitespaces on each line
    result = "\n".join(line.strip() for line in result.splitlines())

    print(result)
