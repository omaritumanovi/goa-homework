def convert(names):
    converted = []

    for i in range(len(names)):
        if i % 2 == 0:
            converted.append(names[i].upper())
        else:
            converted.append(names[i].lower())
            return converted
name = ["zuka","bob","gemalala","guram"]

converted = convert(name)

print(converted)