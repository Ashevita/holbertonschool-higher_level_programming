import os

def generate_invitations(template, attendees):
    # Vérification du type de template
    if not isinstance(template, str):
        print("Erreur : Le template doit être une chaîne de caractères.")
        return

    # Vérification du type d'attendees
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Erreur : Les invités doivent être une liste de dictionnaires.")
        return

    # Vérification si le template est vide
    if template.strip() == "":
        print("Erreur : Le template est vide, aucun fichier de sortie généré.")
        return

    # Vérification si la liste des invités est vide
    if len(attendees) == 0:
        print("Aucun invité fourni, aucun fichier de sortie généré.")
        return

    # Traitement de chaque invité
    for i, attendee in enumerate(attendees, start=1):
        # Création du contenu de l'invitation en remplaçant les valeurs manquantes par "N/A"
        invitation_content = template
        invitation_content = invitation_content.replace("{name}", attendee.get("name", "N/A"))
        invitation_content = invitation_content.replace("{event_title}", attendee.get("event_title", "N/A"))
        invitation_content = invitation_content.replace("{event_date}", attendee.get("event_date", "N/A"))
        invitation_content = invitation_content.replace("{event_location}", attendee.get("event_location", "N/A"))

        # Création du fichier de sortie avec un nom unique
        filename = f"output_{i}.txt"
        with open(filename, 'w') as file:
            file.write(invitation_content)
        print(f"Fichier généré : {filename}")

# Exemple d'utilisation dans le fichier principal
if __name__ == "__main__":
    # Lecture du template
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # Liste des invités
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Appel de la fonction avec le template et la liste des invités
    generate_invitations(template_content, attendees)
