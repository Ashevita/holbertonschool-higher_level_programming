#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Tenter d'accéder à l'élément et de l'imprimer
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Ignorer silencieusement les types qui ne sont pas des entiers
            continue
        except IndexError as e:
            # Afficher l'erreur IndexError si l'indice est hors limite
            print("\nIndexError:", e)
            break
    print()  # Pour ajouter une nouvelle ligne après l'impression
    return count
