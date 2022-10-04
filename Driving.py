"""Driving Age"""

print("Enter your age to Know you are eligible to drive\n")
AGE = int(input("Enter Your Age: "))

if 9>AGE:
   print("ohh",AGE,"Years!!!","You are too young for driving.")
elif 101<AGE:
    print("Dear sir kindly get rest as your age",AGE,"years","its too dangerous for others.")
elif AGE<18:
    print("You are under age. Please wait until your turns 18")
elif AGE==18:
    print("you are eligible, please come, clear test and get your licence")
else:
    print("yes come on, your age is perfect for driving.")



""" Call number from list."""
# House = [2, 6, 8, 34, 98, 4254, 234, 34, 43, 253, 245, 24]
# House.sort()
# Ho = int(input("Search for your house: "))
# # try:
# if Ho in House:
#         print("You'r house Number is: ", Ho)
#         print("You'r street number is: ", House.index(Ho))
# else:
#     print("Your house is not in this area.")
#
# # except ValueError:
# #     print("You house is not in the area")

