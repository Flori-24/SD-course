#fp = open(r'C:\Users\Alin\Desktop\SD course\sample\data.txt', 'r')
#print(fp.read())
#fp.close()


#fp = open ('sample\\data.txt', 'r')
#print(fp.read())
#fp.close()

          

#fp = open(r'sample\file1.txt', 'w')
#fp.write('first line ')
#fp.close()



#Open an existing file and add a new line at the end of the file in python
#with  open(r'sample\file1.txt', 'a') as fp:
 # fp.write("This will go last")
  


#Write a Python code to read first 2 lines of a file  
#N=2
#with open(r'sample\data.txt', 'r') as fp:
  #for i in range(N):     # we can use range or enumerate
  #  line = next(fp).strip()  #next is a pointer to the first line of fp file
   # print(line)



                                                #Read lines
#import linecache
#line = linecache.getline(r"C:\Users\Alin\Desktop\SD course\sample\data.txt", 3)  #single line
#print(line)



#with open(r"C:\Users\Alin\Desktop\SD course\sample\data.txt", 'r') as fp:
   # x = fp.readlines()[0:2]   # excluding 0: starts from 1 to 2 - multiples lines
   # print(x)



                              #Creating a new file and writing a text
#text = "This is new content for the new file2"
#fp = open("sample\\file2.txt", 'w')
#fp.write(text)
#print('Done printing')
#fp.close()


                      #Move File Pointer
#f = open('sample\\data.txt', 'r')  #the pointer stars ussually from the first position(index=0, just like the string index)
#f.seek(5)  # reading from the 5th character 
#print(f.read())


                #Return the current position of the file pointer from the begginning of the file
#f = open('sample\\data.txt', 'r')
#f.readline() #read first line
#print(f.tell()) #method -tell()- get current position of file handle (the pointer)


#with open(r'sample\data.txt', 'r') as fp:
    #lines = fp.readlines()
   # print(lines)   #'\n'- empty line



#Write a Python program to write a list content to a file
#list = ['Red', 'Green', 'Yellow']
#with open(r'sample\dummy.txt', 'w') as fp:  #opened a new file dummy.txt
 #   for item in list:
 #       fp.write(item + '\n')               # new line after each item        
#print('File written successfully') 
                                   #OR using "%s"

#list = ['Red', 'Green', 'Yellow']
#with open(r'sample\dummy1.txt', 'w') as fp: 
  #  for item in list:
  #      fp.write("%s\n" % item)    #-%s-will write the entire string  fp=%                
#print('File written successfully') 





 #Write a python program to combine each line from first file with the 
 # corresponding line in second file
#with open(r'sample\data.txt') as file1, open(r'sample\dummy.txt') as file2:
    #for line1, line2 in zip(file1, file2):
      #  print(line1+ ''+ line2)



                  #Copy Files  -shutil.copy()- used to copy the source file's content to the destination file(from one place to the other)
#import shutil
#src_path = r"C:\Users\Alin\Desktop\SD course\sample\file1.txt"
#dst_path = r"C:\Users\Alin\Desktop\SD course\sample\copiedfile1.txt"
#shutil.copy(src_path,dst_path)
#print('Copied')

                         #Rename Files -os.rename- os mudule provides functions for fiel processing: renameing, deleting.
#import os
#old_name = r"E:\Users\Alin\Desktop\SD course\sample\copiedfile1.txt"
#new_name = r"E:\Users\Alin\Desktop\SD course\sample\copiedfile1.txt"
#os.rename(old_name, new_name)


                          #Delete Files -os.delete-
#import os
#os.remove(r"E:\Users\Alin\Desktop\SD course\sample\copiedfile1.txt")




