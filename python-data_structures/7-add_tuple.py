#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Assurer que tuple_a a au moins deux éléments
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    else:
        tuple_a = tuple_a[:2]

    # Assurer que tuple_b a au moins deux éléments
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    else:
        tuple_b = tuple_b[:2]

    # Additionner les éléments correspondants
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])