"""This is the game call, Snake Water and Gun"""
import random

"""Rules"""
    # Snake beats water, Water beats gun and gun beats snake.
    # computer take random choise but not print.
    # then give your input and compare them.
    # announce the winner.







def SnakeGame():
    restart_game = "Yes"
    while restart_game != "No":
        if restart_game == "Yes":
            print("\n-----||Welcome to the game||-----\n")
            print("---> This is best of 5 match series.\n")

            User_name = input("Enter your name: ")
            User_name = User_name.capitalize()
            print("\nGood Luck !", User_name, "\n")

            Counter_com = 0
            Counter_user = 0
            Counter_draw = 0

            i = 1
            while i < 6:

                print("\nNumber of game:", i,"out of 5\n")

                Game_list1 = ["Snake", "Water", "Gun"]
                Game_list2 = {"S":"Snake", "W":"Water", "G":"Gun"}

                computer_choice = random.choice(Game_list1)

                Your_Cho = input("S for Snake, W for Water and G for Gun\n"+"Please select: " )
                Your_Cho = Your_Cho.capitalize()
                Your_Choice = Game_list2[Your_Cho]

                print("computer has selected:", computer_choice)
                print("you have selected:", Your_Choice)

                if (computer_choice == "Snake" and Your_Choice == "Water"):
                    print("  * The computer is winner")
                    Counter_com += 1


                elif (computer_choice == "Water" and Your_Choice == "Gun"):
                    print("  * The computer is winner..!")
                    Counter_com += 1


                elif (computer_choice == "Gun" and Your_Choice == "Snake"):
                    print("  * The computer Wins..!")
                    Counter_com += 1


                elif (computer_choice == Your_Choice):
                    print("  * The Game Draw")
                    Counter_draw += 1


                else:
                    print("  * Congratulations..!", User_name, "You have Won the Game")
                    Counter_user += 1

                i+= 1

            print("\n---> series is over, Results:")
            print(" * No. of matches you have won =", Counter_user)
            print(" * No. of matches Computer has won =", Counter_com )
            print(" * No. of matches Draw =", Counter_draw)

            restart_game = input("\nDo You want to play series again,\n Yes or No: ")
            restart_game = restart_game.capitalize()

        else:
            print("\nYou have selected wrong opetion kindly Select it again.\n")
            restart_game = input("\nDo You want to play series again,\n Yes or No: ")
            restart_game = restart_game.capitalize()


SnakeGame()

print("\nThanks for playing this Game.")