file=open("D:/capgemini/day10(10.03.2026)/temp.txt","r")

print(file.read())
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.seek(0)
print(file.readlines())  #empty list 

file.close()
'''
read()-->display a file content as it is
readline()-->display single line of data at a time 
readlines()-->it will display backward slash also 

'''
# FileNotFoundError: [Errno 2] No such file or directory: 'notes.txt'
# file=open("notes.txt","r")
# print(file.read())
# file.close()
