# def new_func(str1):
#     print(str1.upper()*3)
#     return

# new_func("hello")

# def func1(num1):
#     if num1%2==0:
#         print("even number")
#     else:
#         print("odd number")
#         return

# func1(3)

# def func1(num1):
#     if num1<0:
#         return ("negative number")
#     else:
#         return ("positive number")
    

# print(func1(3))

# variable length argument
# def nwfun(a,*b):
#     print("a is",a)
#     for i in (b):
#         print(i)

# nwfun(10,20,30,40)  

# def fun1(lim1,lim2):
#     for i in range(lim1,lim2):
#         if i%2==0:
#             print(i)

# fun1(4,30)

# def fun1(limit):
#     list1=[]
#     for i in range(limit):
#         data=int(input("enter ur data"))
#         list1.append(data)
#     print(list1)
#     list1.sort()   
#     print(list1)     
#     print(list1[-2])

# fun1(3)

# list1=["apple",'apricot','banana']
# list2=[]    
# for i in list1:
#     if i[1]=="p":

#         list2.append(i)   
# print(list2)

        
# list1=["apple",'apricot','banana'] 
# list2=[i for i in list1 if i[1]=="p"]   
# print(list2)    

# lambda function

# list1=[-1,2,4,-6]
# newlist=list(filter(lambda x:x<0,list1))
# print(newlist)

# list1=[-1,2,4,-6]
# newlist=list(map(lambda x:x**2,list1))
# print(newlist)

# from functools import reduce

# list1=[1,2,3,4,5]
# result=reduce(lambda x,y:x+y,list1)
# print(result)

# decorators
# def hello_decor(func):
#     def inner():
#         print("before function")
#         func()
#         print("after function")
#     return inner

# @hello_decor
# def newfunc():
#     print("inside function")

# newfunc()

# to call variables
# def hello_decor(func):
#     def inner(*a):
#         print("before function")
#         func(*a)
#         print("after function")
#     return inner

# @hello_decor
# def newfunc(a,b):
#     print("inside function")
#     print(a+b)

# newfunc(3,4)
# @hello_decor
# def newfunc2(a,b,c):
#     print(a+b+c)

# newfunc2(3,4,5)
    

# import time
# def hello_decor(func):
#     def inner():
#         start=time.time()
#         func()
#         print(time.time()-start)
#     return inner

# @hello_decor
# def newfunc():
#     sum=0
#     for i in range (100000):
#         sum=sum+i
#     print(sum)

# newfunc()

# import time

# def calc_square(numbers):
#     print("calculate the square of the nuumbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("squares",n*n)

# def calc_cube(numbers):
#     print("calculate the cube of the nuumbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("cube",n*n*n)

# list1=[1,2,3,4,5]
# start=time.time()
# calc_square(list1)
# calc_cube(list1)
# print("done in",time.time()-start)

# to reduce the time of execution
# import time
# import threading

# def calc_square(numbers):
#     print("calculate the square of the nuumbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("squares",n*n)

# def calc_cube(numbers):
#     print("calculate the cube of the nuumbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("cube",n*n*n)

# list1=[1,2,3,4,5]
# start=time.time()
# t1=threading.Thread(target=calc_square,args=(list1,))
# t2=threading.Thread(target=calc_cube,args=(list1,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("done in",time.time()-start)

import _thread
import time

# define a function for the thread
def print_time(threadName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print("%s:%s"% (threadName,time.ctime(time.time())))
# create two threads
try:
    _thread.start_new_thread(print_time,("thread-1",2))
    _thread.start_new_thread(print_time,("thread-2",4))

except:
    print("Error:unable to start thread ")

while True:
    pass


