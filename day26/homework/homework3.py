def find_(collection, value_to_find):
    for index in range(len(collection)):
        if collection[index] == value_to_find:
            return index

print(find_(["luka", "zuka", "mari"], "zuka"))