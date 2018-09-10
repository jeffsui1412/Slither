keys = [119, 115, 97, 100]
with open("keys.txt", "w") as file:
    file.write(str(keys))
with open("keys.txt", "r") as file:
    keys = file.read()[1:-1]

    print(keys)
