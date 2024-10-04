fp = open(r'C:\Users\Alin\Desktop\SD course\sessions\python\sample\data.txt ', 'r')
print(fp.read())
fp.close()



fp = open('sample/file1.txt', 'x')
fp.write('firstline')
fp.close()




with  open(r'sample/data.txt, 'a') as fp:
  fp.write("This will go last")

