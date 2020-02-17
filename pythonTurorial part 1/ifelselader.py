num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
num3 = int(input("Enter the number:"))
if num1 == 10:
    print("The number is 10")
    if num2 >5:
        print("Number 2 is > than 5")
    elif num2 <5:
        print("Number 2 is < than 5")
        if num3 >10:
            print("Number 3 is > than 10")
        elif num3 < 10:
            print("Number 3 is < than 10")
elif  num1 == 5:
    print("The number is 5")
else:
    print('wrong')