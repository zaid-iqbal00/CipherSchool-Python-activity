name,age=input("Enter your name and age").split(",")
age=int(age)
if (name[0] == 'a' or 'A') and age>10:
    print("You can wath coco movie")
else:
    print("sorry,you cannot watch coco movie")