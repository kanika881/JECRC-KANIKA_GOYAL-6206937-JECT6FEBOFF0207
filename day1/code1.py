FirstA=10
# see the type of variable
type(FirstA)

FirstA=input()
SecondB=input()
c=FirstA+SecondB
print(c)
type(c)

FirstA=20
id(FirstA)

class Temp:
  pass

obj=Temp()
obj

FirstA=30
SecondB=FirstA
FirstA=FirstA+SecondB
print(FirstA,SecondB)
print(id(FirstA))
print(id(SecondB))
print(id(30))
#id of SecondB and 60 is same
print(id(60))

n1=int(input())
n2=int(input())
class Add:
  @staticmethod
  def result(n1,n2):
    return (n1+n2)

print(Add.result(n1,n2))

#mvc - multiple variable creation , reduce time, creating multiple variables in FirstA single line
#var1,var2,...,varn=val1,val2,...,val3
#the number of variables and values should be same

FirstA,SecondB,c=10,20,30
print(FirstA,SecondB,c)
result=FirstA,SecondB,c
type(result)

# x,y,z=10,20
# #number of variable greater than number of values

#number of variable less than number of values
x,y,z=1,2,3,4


num=20
#num is FirstA name given to FirstA variable
_n=2

#23 Feb

#checking if operators are function
# help('+')

dir(int)


help('keywords')

import keyword
keyword.kwlist

len(keyword.kwlist)

type(None)

FirstA=None
#initialize empty variable

print(type(None))
print(type([1,2,3]))

var=1000 #single value
var2='HELLO' #collection of multiple characters- multivalue data type

#int
type(888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888)

type(65656616.0000646)

print(type(20+9j))
print(type(-1.1 -7878j))
num=45j+7
print(type(num))

type(7+8J)


FirstA=6.7
SecondB=23+67676j
print(FirstA+SecondB)

print(id(True))
print(id(False))


print(True+True+False)
print(20*False)
print(20*True)
print(20*1)
print(20*0)

print('HELLO')
print("HELLO")
print('''HELLO''')

name="kanika"
print(id(name))
print(id(name[0:1]))
print(id(name[1:2]))

paragraph="""
hrkhhafk
jjgjgjfg
lhlafafblb
"""

print(paragraph)

name="HelloPython"
print(name[-6]+name[-4]+name[-1])
print(name[-len(name)+1])

print(int())
print(float())
print(bool())
print(str())
print(complex())
print(list())
print(tuple())
print(set())
print(dict())

bool('')