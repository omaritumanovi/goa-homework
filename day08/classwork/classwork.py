# # name = input("Please enter your name: ")
# # password = input("Please enter your password: ")
# # repeat_password = input("Please enter your password again: ")

# # if password == repeat_password:
# #     print(name, "registered succsesfully!")
# # else:
# #     # print("Invalid Passwords!")

# # Logical OR operator
# print(True or False)    # Result: True
# print(False or True)    # Result: True
# print(True or True)     # Result: True
# print(False or False)   # Result: False


# num = int(input("please enter you're number: "))
# if (num > 0 and 11 > num):
#     print("you're number is correct from 1-10")
# else:
#     print("you're number is not between 1-10")


# num = int(input("please enter number: "))
# print(num % 5 == 0 and num % 10==0)

# """მომხმარებელს შემოატანინეთ 1 რიცხვი და შეამოწმეთ იყოფა თუ არა ეგ რიცხვი 5ზე და 10ზე

# 1) როგორ შემოვატანინო მომხმარებელს მონაცემი პროგრამაში
#     ა) გამოვიყენოთ input() ფუნქცია, და შევინახოთ ის ცვლადში

# 2) როგორ შევამოწმოთ იყოფა თუ არა ერთი რიცხვი მეორეზე?

#     მათემათიკური ახსნა: რომ გავიგოთ იყოფა თუ არა ერთი რიცხვი მეორეზე, უნდა დავაკვირდეთ ნაშთს
#     თუ ნაშთი ნულია მაშინ ერთი რიცხვი ზუსტად იყოფა მეორეზე (მაგ: 5 : 5 = 1 ნაშთი(0))

#     ა) სანამ მე რაიმეს გავაკეთებ კონკრეტულ მონაცემებზე იქამდე ის უნდა გარდავქმნა
#     მათემათიკურ რიცხვად, იმიტომ რომ ინფუთ ფუნქცია გვიბრუნებს ჩვენ ყოველთვის სტრინგს 
#     გამოვიყენოთ, int() ფუნქცია მაგ: int("5") შედეგი კი იქნება 5 ბრჭყალების გარეშე შედეგად
    
#     ბ) რომ შევამოწმოთ ნაშთი არის თუ არა ნულის ტოლი გამოვიყენოთ % გაყოფა 
#     (ანუ ეს გაყოფა % დაგვიბრუნებს ნაშთს მაგ: 7 % 5 = 2 - ეს არის მორჩენილი ნაწილი ანუ ნაშთი)
#     შემდეგ ეგ ნაშთი შევამოწმოთ უდრის თუ არა 0, გამოვიყენოთ შედარების ოპერატორი რომელიც არის
#     == ორი ტოლობა პითონში, მაგალითად  5 == 5 შედეგი იქნება True

# 3) როგორ დავაკავშირო ორი შედარება ერთმანეტთან, მიზეზი დაკავშირების არი ის რომ პირობაში ეწერა
# და კავშრილი, ანალოგიურად მეც მჭირდება და კავშირი

#     ა) გამოვიყენოთ and ოპერატორი
# """

# num = int(input("Please enter number: "))

# print(num % 5 == 0 and num % 10 == 0)
