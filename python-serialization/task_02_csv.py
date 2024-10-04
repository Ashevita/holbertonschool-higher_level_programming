#!/usr/bin/python3
"""Module to convert CSV to JSON."""


import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to JSON and writes it to data.json.

    Args:
        csv_filename (str): The name of the CSV file to convert.

    Returns:
    bool: True if the conversion was successful, False if an error occurred.
    """
    try:
        # Ouvrir le fichier CSV et lire les données en utilisant DictReader
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        # Retourner False si le fichier CSV n'est pas trouvé
        print(f"Error: File {csv_filename} not found.")
        return False

    except Exception as e:
        # Gérer toute autre exception
        print(f"An error occurred: {e}")
        return False
