#-Write a python program to turn every intem in a list its square
#eg: [2,4,6,3] Output: [4,16,36,9]


from Factors import print_factors
#eg =[2,4,6,3]
#def square(number) :
   # return number**2
#result= list(map(square,eg))
#print(result)




#-Concatenate two lists in the following order: LIST COMPREHENSION
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected Output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']


#list1= ["Hello", "take"]
#list2= ["Dear", "Sir"]
#result = []
#for txt1 in list1:
 #   for txt2 in list2:
  #      result.append(txt1+txt2)
#print(result)  #nested for loop   OR

#numbers= [1,2,3,4,5 ]    

#odd_nums =[]
#for num in numbers:
 #   if num % 2 !=0:
 #     odd_nums.append(num)
#print(odd_nums)    OR

#odd_numbers = [num for num in numbers if num % 2 !=0]
#print(odd_numbers)          OR

#list1= ["Hello", "take"]
#list2= ["Dear", "Sir"]
#result= [txt1 + " " +txt2 for txt1 in list1 for txt2 in list2]
#print(result)



#- Write a program to find value 20 in the list,
# and if it is present, replace it with 200.
# Only update the first occurrence of an item.
# Input: list1 = [5, 10, 15, 20, 25, 50, 20]
# Output: [5, 10, 15, 200, 25, 50, 20]


#list1 = [5, 10, 15, 20, 25, 50, 20]
#list1[i] = 200
#print(list1)

#-Remove all the occurences of 20
#list_1 = [5, 10, 15, 20, 25, 50, 20]
#result = [num for num in list_1 if num !=20]
#print(result)

#-Reverse the given tuple
# tuple1 = (10, 20, 30, 40, 50)
# Output: (50, 40, 30, 20, 10)
#tuple1= (10, 20, 30, 40, 50)   
#result= tuple1[::-1]
#print(result)               OR

#start
#stop
#step
#number_list = [2,4,6,8,10,12]
#print(number_list[2:])     #we can apply for list or tuple
#print(number_list[:2])
#print(number_list[::-1])

# -Unpack the tuple items
# Input: tuple1 = (10, 20, 30, 40)
# Output:
# print(a) = 10
# print(b) = 20
# print(c) = 30
# print(d) = 40

#tuple1 = (10, 20, 30, 40)
#a, b, c, d= tuple1
#print("a=", a)
#print("b=", b)
#print("c=", c)
#print("d=", d)


# -Convert two lists into a dictionary
# Input:
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
 

#keys = ['Ten', 'Twenty', 'Thirty'] 
#values = [10, 20, 30]
#result=dict(zip(keys, values))  
#result=tuple(zip(keys, values))
#print(result)




#-Write a Python program to check if value 200 exists in the following dictionary.
#Input:
#    sample_dict = {'a': 100, 'b': 200, 'c': 300}
#Output:
#   200 present in a dict

#sample_dict = {'a': 100, 'b': 200, 'c': 300}
#value= 200
#if value in sample_dict.values():           
 #        result= ("200 present")
#print(result)   OR

#sample_dict = {'a': 100, 'b': 200, 'c': 300}
#print(tuple(sample_dict.keys()))     


#-Get the key of a minimum value from the following dictionary
#sample_dict = {
 # 'Physics': 82,
 # 'Math': 65,
  #'history': 75
#}
#Output:
   # Math

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
#print(min(sample_dict, key=sample_dict.get))


#-Enumerate
#list1 = ["eat", "drink", "sleep"]
#print(list(enumerate(list1,5)))
    


                            #PYTHON MODULES

#-Create a python module that gives factors of a number



#print_factors(56)

#-create a list and shuffle its elements using random module
#import random
#list_1 = [1, 2, 3, 4, 5]
#print("Original list:", list_1)
#random.shuffle(list_1)
#print("Shuffled list:", list_1)





           


