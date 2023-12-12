import random
value = random.randrange(20,30)
print("Starting Number: ", value)
if(20<=value<30):
    while(value>0):
        userInput = int(input("How many do you want to remove in the range of 1 to 3?"))
        if(0<userInput<4):
            value = value-userInput
            print(value,"Left")
            if(value>0):
                value1 = random.randrange(1,4)
                print("Computer Turn:", value1)
                value = value - value1
                if(value>0):
                    print(value,"Left")
                elif(value<=0):
                    print("Computer is the loser")
            elif(value<=0):
                print("You are the loser")
        else:
            print()
            print("Enter a number between 1 and 3")
            pass



