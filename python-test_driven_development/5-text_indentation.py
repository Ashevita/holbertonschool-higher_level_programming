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
    
    # Initialize the result variable
    result = ""
    
    # Traverse through each character in the text
    for char in text:
        # Add the character to the result
        result += char
        # Check if the character is one of the specified characters
        if char in ".?:":
            # Add two new lines after the character
            result += "\n\n"
    
    # Remove leading and trailing whitespaces on each line
    result = "\n".join(line.strip() for line in result.splitlines())
    
    # Print the final result
    print(result)
