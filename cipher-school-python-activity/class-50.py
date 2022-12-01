age=int(input("Enter your age : "))
if age>0:
    if 0<age<=3:
        print("Ticket price : Free")
    elif 3<age<=10:    
        print("Ticket price : 150")
    elif 10<age<=60:
        print("Ticket price : 250")
    else:    
        print("Ticket price : 200")
else:
    print("Enter valid age ")