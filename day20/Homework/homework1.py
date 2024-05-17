
def filter_positive_negative(numbers):
    positive_numbers = [num for num in numbers if num >= 0]
    negative_numbers = [num for num in numbers if num < 0]
    return positive_numbers, negative_numbers
numbers = [1,2,6,7,-1,-5,-2,5]
positive, negative = filter_positive_negative(numbers)
print("დადებითი რიცხვები:", positive)
print("უარყოფითი რიცხვები:", negative)