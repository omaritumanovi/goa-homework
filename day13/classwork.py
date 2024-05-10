person_info = []

name = input("Please enter your name: ")
lastname = input("Please enter your lastname: ")
age = int(input("Please enter your age: "))
address = input("Please enter your addres: ")

person_info.append(name)
person_info.append(lastname)
person_info.append(age)
person_info.append(address)

print(person_info)
print(person_info[0:2])
print(person_info[1:3])
print(person_info[0:3])
print(person_info[1:])

fullname = "omari tumanovi"

print(fullname[:4])
print(fullname[5:])