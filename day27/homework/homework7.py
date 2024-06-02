def odds(numbers):
    odd = []
    for i in numbers:
        if i % 2 != 0:
            odd.append(i)
    return odd
print(odds([1,2,3,4,5,6,7,8,9]))