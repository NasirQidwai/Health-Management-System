""" Health Management System"""
    # Make list of clients so that the files of foods and exercise will be automaatically prepared.
    # Make six files three for food and three for exercise.\
    # Write a function, when its executed, it will take client name as input
    # write one more function to retrieve exersice or food for any client.


def getdate():
    import datetime
    return datetime.datetime.now()

dicc = {1:"Foods", 2:"Excercise"}
ca__Name = ["Tasneem", "Sabiha", "Azeem", "Huma","Saad",
            "Nasir", "Uzair", "Urooba", "Ayesha", "Sameer", "Huzaifa", "Laiba", "Areeb"]
i = 1
j = str(i)


def mdd():
    replay = "iieiei"
    while replay != "No":
        c__Name = input("Enter Client Name: ")
        c__Name = c__Name.capitalize()
        # ca__Name.append(c__Name) #for add Name in list but after end the name will be vanished. find solution.
        # print(ca__Name)
        # replay = "iieiei"

    # while replay != "No":

        if c__Name in ca__Name:

            fftt = "rrr"

            while fftt != 1 and fftt != 2:
                if fftt != 1 and fftt != 2 and fftt != "rrr":
                    print("we have only two options kindly select 1 or 2")

                print("-----|enter 1 for Foods and 2 for Exercise|-----")
                fftt = int(input("select for Food or exercise: "))

            ffname = c__Name+" "+dicc[fftt]+".txt"
            f = open(ffname, "a")

            print("-----|Enter 1 for add or 2 for retrieve|-----")
            add_ret = int(input("Select add or retrieve: "))

            if add_ret == 1:
                fr2 = input("enter the "+dicc[fftt]+" you have consumed: ")
                f.write("\n" + getdate().strftime("(%H:%M), %d.%m.%y")+" | "+fr2)
                f.close()
            elif add_ret == 2:
                # fr2 = input("enter the "+dicc[fftt]+" you have done: ")
                with  open(ffname) as fff:
                    print("\n\t\t\t\tLog sheet\t\t\t\t")
                    for i in fff:
                        print(i, end="")

            replay = input("\n\n\nDo you want to enter data again, Yes or No: ")
            replay = replay.capitalize()

        else:
            print("Client Name is not in our database")
            replay = input("Do you want to enter data again, Yes or No: ")
            replay = replay.capitalize()
            # break

mdd()
