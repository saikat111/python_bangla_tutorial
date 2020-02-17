n = int(input("enter the number:"))
n2 = int(input("enter the number 2:"))
try :
    d = n / n2
    print(d)
except  ZeroDivisionError as e:
    print(e)
print(sum)