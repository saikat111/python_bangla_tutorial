num1  = [10,100,80,7]
#num1.sort()
#print(num1)
#num2 = num1.copy()
#print(num2)
#num1.reverse()
#print(num1)\
number_array = list()
number = input("Enter the number of elements you want:")
print ('Enter numbers in array: ')
for i in range(int(number)):
    n = input("number :")
    number_array.append(int(n))
print ('ARRAY: ',number_array)
