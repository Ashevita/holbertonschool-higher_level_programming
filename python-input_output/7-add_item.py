#!/usr/bin/python3
"""Script to add all command-line arguments
to a Python list and save them to a JSON file."""

import sys
from os.path import exists


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Nom du fichier où on stockera la liste d'éléments en JSON
filename = "add_item.json"

if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Ajouter tous les arguments de la ligne de commande à la liste
items.extend(sys.argv[1:])

# Sauvegarder la liste mise à jour dans le fichier JSON
save_to_json_file(items, filename)
