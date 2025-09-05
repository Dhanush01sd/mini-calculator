a="""
calculator!
1.addition
2.subtraction
3.multiplication
4.division
5.square value
6.cube value
7.factorial value
8.square root value
9.cos value
10.sin value
11.tan value
12.mode off
"""
print(a)
while True:
 import math 
 a=int(input())
 if(a==1):
    print("addition")
    a1=int(input("a:"))
    a2=int(input("b:"))
    c=a1+a2
    print(c)
 elif(a==2):
       print("subtraction")
       a1=int(input("a:"))
       a2=int(input("b:"))
       c=a1-a2
       print(c)
 elif(a==3):
     print("multiplication")
     a1=int(input("a:"))
     a2=int(input("b:"))
     c=a1*a2
     print(c)
 elif(a==4):
     print("division")
     a1=int(input("a:"))
     a2=int(input("b:"))
     c=a1/a2
     print(c)
 elif(a==5):
     print("sqrt value")
     a1=int(input())
     print(math.pow(a1,2))
 elif(a==6):
     print("cube value")
     a1=int(input())
     print(math.pow(a1,3))
 elif(a==7):
     print("factorial")
     a1=int(input("fact no:"))
     print(math.factorial(a1))
 elif(a==8):
     print("square root value:")
     a1=int(input())
     print(math.sqrt(a1))
 elif(a==9):
     print("cos value")
     a1=int(input())
     print(math.cos(a1))
 elif(a==10):
     print("sin value")
     a1=int(input())
     print(math.sin(a1))
 elif(a==11):
     print("tan value")
     a1=int(input())
     print(math.tan(a1))
 else:
    print("mode off")
