# Faulty Calculator: 45 * 9 = 34 and 92, 89 + 4 = 45, 56-2 = 12, 67/2 = 78
# # Design A calculator which will correctly calculate all the calculations except the above ones.
# """Your program should take the operator and the two numbers from the user and then
# return the result."""

X = input("what operation you want perform(+,-,*,/): ")
Y = int(input("Enter first Number: "))
Z = int(input("Enter Second Number: "))


if X=="*" and ( ((Y==45) and (Z==3)) or ((Y==3) and (Z==45)) ):
    print(555)
elif X=="+" and ((Y ==56 and Z== 9) or (Y ==9 and Z== 56)):
    print(77)
elif X=="/" and Y==56 and Z==6:
    print(4)
elif X == "+":
    print(Y+Z)
elif X == "*":
    print(Y*Z)
elif X == "-":
    print(Y-Z)
elif X == "/":
    print(float(Y/Z))
else:
    print("\nPlease enter valid operation sign.")