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

    # Initialize a variable to accumulate the result
    result = []
    i = 0
    length = len(text)

    while i < length:
        char = text[i]

        # Append the current character to the result
        result.append(char)

        # Check if the character is one of the specified punctuation marks
        if char in ".?:":
            # Add two new lines
            result.append("\n\n")
            # Skip any additional spaces or newlines
            while i + 1 < length and text[i + 1] in " \n":
                i += 1
                if text[i] == "\n":
                    result.append("\n")

        i += 1

    result_text = ''.join(result).strip()
    cleaned_text = "\n".join(
        line.strip()
        for line in result_text.splitlines()
        if line.strip()
    )
    # Print the cleaned text without adding an extra newline at the end
    print(cleaned_text, end="")
