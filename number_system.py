# a=0.4;b=0.2
# print(a+b)#0.6000000000000001
# c=a+b
# print('%f'%c)#0.600000
# print('%.1f'%c)#0.6
#
# from decimal import Decimal as d
# h=d(0.7+0.2)#0.899999999999999911182158029987476766109466552734375 (exact answer)
# h=d(0.7)+d(+0.2)#0.8999999999999999666933092612 (half answer)
# h=d('0.7')+d('0.2')
# print(h)#0.9

# print(7/0)#zerodivisionError:division by zero

from fractions import Fraction as f
# a=f(1,0)
# print(a) #ZeroDivisionError
# b=f(1,1)
# print(b)#1
# c=f(1,5)
# print(c)#1/5
# d=f(2)
# print(d)#2
# e=f(0,5)
# print(e)#0
# m=f(5,25)
# print(m)#1/5
# n=f(25,5)
# print(n)#5

# v=1_23
# print(v,type(v)) #123 int

# k=1_3.0
# print(k,type(k))#13.0 float

# d=1._03
# print(d)#SyntaxError: invalid decimal literal
# a=5;b=4.6
# print(a,type(a))#5 int
# print(b,type(b))#4.6 float
# print(isinstance(a,int))#True
# print(isinstance(b,int))#False
# print(isinstance(a,float))#False
# print(isinstance(b,float))#True

# c=4+5j
# print(c,type(c)) #(4+5j) complex
# d=3j
# print(d,type(d))#3j complex
# print(isinstance(d,complex))#True