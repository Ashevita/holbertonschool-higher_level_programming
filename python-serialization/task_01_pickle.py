#!/usr/bin/python3
"""Module for CustomObject using pickle
for serialization and deserialization."""


import pickle


class CustomObject:
    """A custom class to represent an object with name,
    age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initializes the CustomObject instance with
        name, age, and is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the object and saves it to the specified filename.

        Args:
            filename (str): The file where the object will be saved.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Failed to serialize object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from the specified filename.

        Args:
            filename (str): The file to load the object from.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Failed to deserialize object: {e}")
            return None
