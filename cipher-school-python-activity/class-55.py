n=int(input("Enter a number : "))
sum=0
i=1
if n>=1:
    while i<=n:
        sum+=i
        i+=1
    print("Sum of n natural numbers is : ",sum)
else:
    print("Enter a valid number")