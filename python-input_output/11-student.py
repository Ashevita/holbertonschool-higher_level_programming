#!/usr/bin/python3
"""Module to create class
"""


class Student:

    """Class that defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance
        with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.
        If attrs is a list of strings, only those attributes are returned.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                # Filter the attributes based on the given list
                result = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        result[attr] = getattr(self, attr)
                return result
        else:
            # Return all attributes if no filter is applied
            return self.__dict__


def reload_from_json(self, json):

    """Replaces all attributes of the Student
        instance using the given json dictionary.
        You can assume json will always be a
        dictionary with keys matching attribute names.
        """
    for key, value in json.items():
        # Replace or add the attributes from the json dictionary
        setattr(self, key, value)
