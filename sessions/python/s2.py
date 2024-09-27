#-Write a python program to turn every intem in a list its square
#eg: [2,4,6,3] Output: [4,16,36,9]

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
list_1 = [5, 10, 15, 20, 25, 50, 20]
#result = [num for num in list_1 if num !=20]
#print(result)

#-Reverse the given tuple
# tuple1 = (10, 20, 30, 40, 50)
# Output: (50, 40, 30, 20, 10)

tuple1= [10, 20, 30, 40, 50]
result= tuple1[::-1]
print(result)








           


