#!/usr/bin/python3
"""Module for serializing and deserializing a dictionary to/from XML."""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML and save it to a file."""
    root = ET.Element("data")  # Créer l'élément racine

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Créer l'arbre XML et l'écrire dans le fichier
    tree = ET.ElementTree(root)
    with open(filename, 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file to a dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary


# Exemple d'utilisation dans un script main.py
if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    # Fichier XML dans lequel on sérialise le dictionnaire
    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    # Désérialisation du fichier XML en dictionnaire
    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
