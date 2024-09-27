#Write a python program to turn every intem in a list its square
#eg: [2,4,6,3] Output: [4,16,36,9]

eg =[2,4,6,3]
def square(number) :
    return number**2
result= list(map(square,eg))
print(result)