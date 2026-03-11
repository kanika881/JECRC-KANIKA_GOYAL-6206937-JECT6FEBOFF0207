'''
for write operation,
	1.write(str_data):single line of data
	2.writelines([line1,line2.....linen]):Multiple line of data

In this ,if the file is not present , it will create one then perform write operation
If the file is already present , them it will override the prev data with new one
'''

file = open("D:/capgemini/day10(10.03.2026)/temp.txt","w+")
# file.write("i am the first line")
file.writelines([
    'first line\n',
    'secod line\n',
    'third line\n',
    'fourth line\n',
    'fifth line\n',
    'sixth line\n',

])
# To make the python interpretor to point at a specific index, we use seek(index)
file.seek(0)
print(file.read())
file.close()


# file = open("temp2.txt","w")
# file.write("i am the first line")

# file.close()