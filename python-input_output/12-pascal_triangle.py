#!/usr/bin/python3
"""Module to create class
"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]  # Le premier niveau du triangle est toujours [1]

    for i in range(1, n):
        prev_row = triangle[-1]  # La ligne précédente
        # On génère la nouvelle ligne en ajoutant les éléments adjacents
        new_row = [1]  # Chaque ligne commence par 1
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)  # Chaque ligne se termine par 1
        triangle.append(new_row)

    return triangle
