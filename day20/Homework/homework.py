def calculate_average(list):
    total = sum(list)
    average = total // len(list)
    return average
numbers = [2, 3, 7, 16, 26, 30]
average = calculate_average(numbers)
print("საშულო არითმეტიკული:", average)