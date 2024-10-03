#!/usr/bin/python3
"""Module to create class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.
        If attrs is a list of strings, only those attributes are returned.
        Otherwise, all attributes are returned with 'age' first.
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
            # Return all attributes, ensuring 'age' is first
            result = {}
            result['age'] = self.age
            result['last_name'] = self.last_name
            result['first_name'] = self.first_name
            return result
