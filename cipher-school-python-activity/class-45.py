winning_number=18
user_input=int(input("Enter a number from 1 to 50 : "))
if user_input == 18 :
    print("You Win")
else:
    if user_input > 18 :
        print("too high")
    else:
        print("too low")