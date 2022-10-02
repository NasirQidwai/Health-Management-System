""" make the guess of the hidden number"""
# Rules
    # Number of guesses are 9
    #print Number of guesses left
    # print game over it the user will not able to guesse.


n = 13
print("\n---> A Guessing game, check your IQ level. <---")

print("\n--> Guess the hidden number, which is between 0 to 20. <--")

i = 0
a = 2

while (True):

    inpt = int(input("\nEnter your guess: "))

    if inpt == n:
        print("Yes..! You have guessed it correct. Your IQ is above average IQ level.\n You have tooken:",i," turn to guess")
        break
    elif (inpt-n<=5) and (inpt-n>0):
        print("oh You're very close to the number, some decrease required")
    elif ((inpt-n>5)and (inpt-n<10)):
        print("You are getting away.. Make it small.")
    elif ((inpt-n>17) and (inpt-n<20)):
        print("Bro..! You have got too far, keep the guess in lower side.")
    elif (inpt-n>=20):
        print("the Difference is too high.")
    elif (inpt-n>=-5) and (inpt-n>-1):
        print("Keep the side at high side, You are very close.")
    elif (inpt-n<=-10):
        print("KEEP THE GUESS AT HIGH SIDE, keep it hight......")
    else:
        print("Your IQ level Below the average.")
    if i==a:
        print("\n\tYou have reached the guessing limit. \n\t\t\tGame Over")
        break
    i +=1
    print("\n\tYou have only",a-i, "guess left.")


