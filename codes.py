# a = 10
# b = float(a)
# print(b)
from itertools import product
from operator import truediv

# a = "12345"
# b=float(a)
# print(b)
# c = (a[::-1])
# print(c)
#
# vowles=['a','e','i','o','u']
# word = "programming"
# count= 0
# for character in word:
#     if character in vowles:
#         count +=1
#         print(count)
# # cou = 0
# # for character in word:
# #     if character not in vowles :
# #         cou +=1
# # print(cou)
# character ='g'
# count = 0
# for i in word:
#     if i== character:
#         count +=1
# print(count)
# #
# # l1 =[1,2,3]
# # l2=[4,5,6]
# # l3=l1+l2
# # print(l3)

#
numberlist=[2,24,6,4,33,22,3,11,223]
# # min=numberlist[0]
# # for nums in numberlist:
# #     if min>nums:
# #         min=nums
# # print(min)
#
# max = numberlist[0]
# for nums in numberlist:
#     if max<nums:
#         max=nums
# print(max)
# middle=int((len(numberlist)/2))
# print(numberlist[middle])

# list=['1','2','3','4']
# string = ''.join(list)
# print(string)

# a = "kayak"
# if a == a[::-1]:
#     print("true")
# else:
#     print("false")

# def pyramid(n):
#
#     for i in range(n):
#
#         print(" " * (n - i - 1), end="")
#
#
#         print("*" * (2 * i + 1))
# n = 5
# pyramid(n)
#
#
# from random2 import shuffle
#
# x = ['python','is','eaasy']
# shuffle(x)
# print(x)
#
# def prime(n):
#     for i in range (2,n):
#       if n%i == 0:
#         return "false"
#       else:
#         return "true"
#
# print(prime(4))

# n = 9
# for i in range(n):
#     for j in range(i,n):
#            print(" ",end=" ")
#     for j in range (i):
#         if j ==0 or i ==n-1 :
#             print("*",end=" ")
#         else :
#           print(" ",end=" ")
#     for j in range (i+1):
#         if i==j or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# def palindrome(n):
#     string = str(n)
#     string = string.lower()
#     if string == string[::-1]:
#         return "true"
#     else:
#         return "false"
# print(palindrome("nitin"))

# def duck(n):
#     for n in range (n,n+1):
#         if n%10 ==0:
#             return "true"
#         else:
#             return "false"
# print(duck(1))


# def duck(n):
#     string=str(n)
#     coun = string.count("0")
#     return coun
# print(duck(10001))


# n = int(input("enter n:"))
# sum=0
# for i in range (1,n+1):
#     sum = sum+i
#print(sum)

# n=int(input("enter n"))
# sum = 0
# a =9
# for i in range (1,n+1):
#     sum = sum+a
#     a+=4
#print(sum)
#
# n = int(input("enter n:"))
# x=int(input("enter x:"))
# sum=0
# a=2
# for i in range(1,n+1):
#     sum=sum+a**x
#     a+=2
# print(sum)
#
# n=int(input("enter n:"))
# x=int(input("emter x:"))
# sum=0
# a=1
# for i in range (1,n+1):
#     sum=sum+(a**3)/x
#     a+=2
# print(sum)

# n = int(input("enter n:"))
# sum=0
# a=2
# b=10
# for i in range (1,n+1):
#     sum=sum + a/b
#     a+=2;b-=1
# print(sum)

# n=int(input("enter n:"))
# x=int(input("enter x:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+x**i
# print(sum)

# import math as m
# n=int(input("enter n:"))
# x=int(input("enter x:"))
# sum=0
# a=9
# for i in range (1,n+1):
#     sum=sum+m.factorial(a)/x
#     a+=4
# print(sum)

# n=int(input("enter n:"))
# sum=0
# a=2
# for i in range(1,n+1):
#     sum=sum+a*2
#     a=a*2
# print(sum)


# n=int(input("enter n:"))
# sum=0
# a=2
# for i in range(1,n+1):
#     sum=sum+a
#     a=a*3
# print(sum)

# n=int(input("enter n:"))
# sum=0
# a=5
# for i in range (1,n+1):
#     sum=sum+a
#     a=a*3
# print(sum)


# n=int(input("enter n:"))
# x=int(input("enter x:"))
# sum=0
# a=2
# for i in range(1,n+1):
#     sum=sum+x/a
#     a=a*2
# print(sum)


# n=int(input("enter n:"))
# x=int(input("enter x:"))
# sum=0
# a=2
# b=10
# for i in range(1,n+1):
#     sum=sum+(x+a)/b
#     a+=2
#     b=b*3
# print(sum)


# import math as m
# n=int(input("enter n:"))
# x=int(input("enter x:"))
# sum=0;a=5;b=2
# for i in range (1,n+1):
#     sum =sum+(x*a**2)/(i+m.factorial(b))
#     a=a*5;b+=1
# print(sum)

# n= 132
# m=n
# sum=0
# prod = 1
# while m!=0:
#     d=m%10
#     m=m//10
#     sum=sum+d
#     prod=prod*d
# if sum==prod:
#     print("yes")
# else:
#     print("no")

# n=59
# m=n
# sum=0
# prod = 1
# while m!=0:
#     d=m%10
#     m=m//10
#     sum=sum+d
#     prod=prod*d
# if sum+prod==n:
#     print("yes")
# else:
#     print("no")

# n=156
# m=n
# sum=0
# prod=1
# while m!=0:
#     d=m%10
#     m=m//10
#     sum=sum+d
#     prod=prod*d
# if n%sum==0:
#     print("true")
# else:
#     print("false")


# n= 9
# flag=0
# m=n
# q=n*n
# while m!=0:
#     d=m%10;d1=q%10
#     if d!=d1:flag=1
#     m=m//10;q=q/10
# if flag ==0:
#     print("yes")
# else:
#     print("no")


# import math
# n=145
# m=nsum=0
# while m!=0:
#     d=m%10
#     sum=sum+math.factorial(d)
#     m=m//10
# if sum==n:
#     print("yes")
# else:
#     print("no")

# n=int(input("enter n:"))
# for i in range (1,n+1):
#     if n%i==0:
#         print(i,end=" ")

# n=int(input("enter n:"))
# sum=0
# for i in range (1,n-1):
#     if n%i==0:
#         sum=sum+i
# if n==sum:
#     print("yes")
# else:
#     print("no")

# n=int(input("enter n:"))
# count=0
# for i in range (1,n+1):
#     if n%i==0:count+=1
# if count>2:
#     print("yes")
# else:
#     print("no")


# n=int(input("enter n:"))
# sum=0
# for i in range (1,n):
#     if n%i==0:
#         sum=sum+i
# if sum>n:
#     print("abundant")
# else:
#     print("deficient")


# n=int(input("enter n:"))
# fact=0
# for i in range (1,n+1):
#     if(i*(i+1)==n):
#         print(f"{i} * {i+1}={n}")
#         fact=i
# if fact >0:
#     print("pronic")
# else:
#     print("not")


# n1=int(input("enter n1:"))
# n2=int(input("enter n2:"))
# def gcd(a,b):
#     if a==0 or a==b:
#         return b
#     elif b==0:
#         return a
#     elif a>b:
#         return gcd(a-b,b)
#     return gcd(a,b-a)
# print(gcd(n1,n2))

# l1=['abc',34.56,32,3+4j,'b',55,65.7,'90',180]
# print(l1)
# l2=[]
# for e in l1:
#     if type(e)==int:
#          l2.append(e)
# print(l2)


# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
# t1=test()
# print(t1.a,t1.b)
#
#
# i=1
# while i<=10:
#     print(i,end=" ")
#     if i==5:
#         break
#     i+=1
# else:
#     print("you are in else")


# f=lambda n: 1 if n==0 else n*f(n-1)
# print(f(5))

#
# f= lambda a,b:a+b
# r=f(3,7)
# print(r)

