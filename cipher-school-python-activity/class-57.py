num=input("Enter a number countaining more than one digit: ")
total=0
i=0
while i<len(num):
    total+=int(num[i])
    i+=1
print(total)