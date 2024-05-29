def whole(number):
    result = []
    for i in number:
        if number == list(number):
            result.append(number * 2)
        else:
            result.append(number * 4)
    return result

result1 = whole([10,5.5,20,30])
print(result1)