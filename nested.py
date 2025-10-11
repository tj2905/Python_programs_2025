num=int(input("enter a number: "))
if(num<=0):
    print(f"{num} is not a positive number")
elif(num>0):
    if(num<10):
        print(f"{num} lies between 1 and 10")
    elif(num>=10 and num<20):
        print(f"{num} lies between 10 and 20")
    else:
        print("number is greater than 20")

else:
    print("number is zero")
    