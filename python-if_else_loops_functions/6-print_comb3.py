for i in range(10):
    for j in range(i + 1, 10):
        if i < 8 or (i == 8 and j < 9):
            print("{:2d}{},".format(i, j), end="")
        else:
            print("{:2d}{}".format(i, j))
