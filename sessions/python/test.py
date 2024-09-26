#print("Hello from Python")  #displaying a variable
#value = input("Enter a value")  #take input from the user to be storred in a variable
#print(value)

#num1= int(input("Enter first number"))        #int() string converted  
#num2= int(input("Enter second number"))
#print(num1+num2)    


 

#  -print area of a triangle by tyaking length of 3 sides as input
# from the user
# to calculate area of triangle use 
# s = (a+b+c)/2
# area =  (s(s-a)(s-b(s-c)) **0.5

# a = int(input("Enter the length of first side"))
# b = int(input("Enter the length of second side"))
# c = int(input("Enter the length of third side"))
# s = (a+b+c)/2
# area = (s*(s-a)*(s-b)*(s-c)) **0.5
# print("Semiperimeter:", s)
# print("Area:", area)




# -Swap two numbers
#x=5
#y=10
               #temp = x  #temporary variable for swaping two numbers
                 #x = y
#x,y = y,x                 #y = temp 
#print(x,' ', y)




#  -input choice of basic calcualtor
# Get the input numbers from the user
# 1:Add
# 2:SUbtraction
# 3:Multiplication
# 4:Division
# Based on the choice, do the math and display the result

#num1= int(input("Enter first number"))
#num2= int(input("Enter second number"))
#operator= input("Enter an operator (+ - * /):")
#if operator == "+":
 #   result = num1 + num2
#elif operator == "-":
 #   result = num1 - num2
#elif operator == "*":
 #   result = num1 * num2
#elif operator == "/":
#   result = num1 / num2
#else:
 #    print("invalid input")
#print(result)     

# OR  

#def add(x, y):
 #   return x+y
#def subtract(x, y):
#    return x-y
#def multiply(x, y):
#    return x*y
#def divide(x, y):
#    return x/y
#print("Please select an operation to perfom.")
#print("1.Add")
#print("2.Subtract")
#print("3.Multiply")
#print("4.Divide")     

#while True:      #is the user wants to do infinite choices we are using loop: while -True value for infinite loop
 #   choice=input("Enter (1/2/3/4):")
  #  if choice in ('1','2','3','4'):  # in  compare multiply numbers
   #     try :                  # when the user wants to use a string for the calculator and is not possible                          
    #        num1 = float(input("Enter first number:"))
     #       num2 = float(input("Enter second number:"))
      #  except ValueError:
       #     print("Invalid input..Please enter a number")  # display the error and then continue the loop
        #    continue          
    #if choice == '1':
     #    print(num1, "+", num2, "=", add(num1,num2))
    #elif choice == '2':
#         print(num1, "-", num2, "=", subtract(num1,num2))
 #   elif choice == '3':
 #        print(num1, "*", num2, "=", multiply(num1,num2))
  #  elif choice == '4':
 #        print(num1, "/", num2, "=",  divide(num1,num2))
 #   more_calculation =input("Wanna do more calculations? (yes/no):")
 #   if more_calculation == 'no':
 #       break
  #  else:
 #       print("Invalid Input")

#str1 = "My name is {firstname}, I am{age}".format(firstname="Mahendra",age=36)
#str1 = "My name is {0}, I am {1}".format("Mahendra",36)
#str1 = "My name is {}, I am {}".format("Mahendra",36)
#print(str1)


#Important String function
#str2 = '349eeeer'
#print(str2.isdigit())    #true or false

text = 'pYThon is fun'
#print(text.casefold())
#print(text.split())  #array of strings


text1= 'Milk,Chicken,Bread'
#print(text1.split())
print(text1.rsplit(','))
print(text1.count('e'))
print(text1.find('Bread'))


#Write a python program to get a single string from two given strings
#separated by space and swap the string.
#Sample input: 'abc','xyz'
#Expected output: 'xyz , abc'

#string1= 'abc'
#string2= 'xyz'
def swap_and_combine_strings(str1,str2):
    combined_string = f"{str2} {str1}"
    return combined_string
#result = swap_and_combine_strings(string1, string2)
#print(result)


string1 = ['hello','world']
string1.reverse()
print(" ".join(string1))



#Write a python program that accepts a filename with extension from the user
#And prints the extension of the file: file.html
#filename= input("Enter filename with extension (file.html):")
#name,extension = filename.rsplit('.',1)
#print("The extension is:", extension)


file = 'file1.html'  #0 1 2       # -1 -2 -3
#print(file[1])   #index from b  
#print(file[-1])   #from the end
file= file.rsplit('.')
print(file[-1])
#print((file))




#Input an integer n and compute the value of n+nn+nnn
#example: 5 compute 5+55+555
n = 5
nn = int(str(n)*2)
nnn= int(str(n)*3)
result= n+nn+nnn
#print(result)


#Ask user to enter the list items
#Ask user to enter a particular number
#Count the number of occurrences of the given number in the list






#Web application architecture
#FRONT END: HTML, CSS, JS------->BACKEND: PYTHON------- > DATABASE

#Js: console.log
#Python: print function 



#Python- used for weeb applications, big data applications, testing, automation, data science, machine learning, and AI, desktop software, mobile apps.


#Def main():            to define a function-using def
 #   i= 1                      declaring the variable
 #  max = 10
 #  while (i<max):      loop
 #         print(i)
 #         i=i+1   
# main()                    call function


#Python data types:
#•	Numeric: interger, float, complex number.
#•	Dictionary
#•	Boolean
#•	Set: can’t have dupllicates
#•	Sequence type: strings (collection of characters), list(have duplicates), tuple(once a tuple is created, we can’t change the values)

# value = input('Enter a value:')   this input function returns a string
  # print(value)
# int() - convers string into int
# float(str) - convert a string to a floating-point number
# bool(val) - convert a value to a boolean value, either True or False
# str(val) - return the string representation of a value
#>>> type(100)
# <class 'int'>
#>>>type(2.0)
#<class 'float'>
#>>> type (True)
#<class 'bool'>

# The full syntax of the print() function is: print(object=separator=end=file=flush=)
         # object- values that will be printed
         # separator- to separate multiple objects inside print()
         # end- to add specific values like new line "\n", tab "\t"
         # file- where the values as printed
         # flush- boolean specifying if the output is flushed or buffered. the default is false