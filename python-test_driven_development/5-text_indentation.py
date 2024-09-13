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
    
    result = []
    i = 0
    while i < len(text):
        char = text[i]
        result.append(char)
        if char in ".?:":
            # Add two new lines after the specified characters
            result.append("\n\n")
        i += 1

    # Join the list into a single string
    result_text = ''.join(result)
    # Remove extra spaces from each line and handle leading/trailing spaces
    cleaned_text = "\n".join(line.strip() for line in result_text.splitlines())
    
    # Print the cleaned text, ensuring no trailing newline
    print(cleaned_text, end="")
