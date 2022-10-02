""" Pattern Printing"""
    # there are two task:
    # 1- take input and print stars
    # 2- take boolean true or falls and print above if true and revers if false.

# 1- take input and print stars:
# print("How many number of rows (n) you want?")
# n = int(input("enter n: "))


""" By simple method"""
# n = int(input("rows: "))
# def py(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("*", end=" ")
#         print("\n")
# py(n)


""" Using List"""
# n = int(input("Enter: "))
#
# def py(n):
#     mylist = []
#     for i in range(1,n+1):
#         mylist.append("*" *i)
#     print("\n".join(mylist))
# py(n)



# n = int(input("Enter: "))
#
# def tti(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("*",end="")
#         print("\n",end="")
# tti(n)


# n = int(input("Enter: "))
# print("for pramid enter 1, and its revers enter 0")
# b = bool(int(input("Give input: ")))
# # print(b)
#
# def test(n,b):
#     if b:
#         for i in range(0,n):
#             for j in range(0,i+1):
#                 print("*",end=" ")
#             print("\n",end="")
#     else:
#         for i in range(0,n):
#             for j in range(n-i,0,-1):
#                 print("*",end=" ")
#             print("\n",end="")
# test(n,b)

n= int(input("Enter How many rows you want to print: "))
# def t1(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("*",end="")
#         print("\n",end="")
# t1(n)


print("\nEnter any number for pyramid, and for it upside down enter 0")
b = bool(int(input("                Enter: ")))

def l1(n):
    if b:
        for i in range(0,n):
            for j in range(0,i+1):
                print("*",end=" ")
            print("\n",end="")
    else:
        for i in range(0,n):
            for j in range(n-i,0,-1):
                print("*",end="")
            print("\n",end="")
l1(n)


