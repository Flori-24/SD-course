#3. Write a python program to sum three given integers. However, if two values are equal then the sum will be zero.
num1= int(input("Enter first integer: "))
num2= int(input("Enter second integer: "))
num3= int(input("Enter third integer: "))

def sum_integers(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a+b+c
result= sum_integers(num1, num2 ,num3)
print(result)
        