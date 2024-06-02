def clones(collection):
    gregory = []
    for i in collection:
        if collection.count(i) == 1:
            gregory.append(i)
    return gregory
print(clones([1,1,2,2,3,3,4,4,5,6,6]))