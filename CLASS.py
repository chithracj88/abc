# class NewClass:
#     x=5

#     def NewFun(self):
#         print(self.x)
#         print("hello")
# obj1=NewClass()
# print(obj1.x)
# obj1.NewFun()

# class Book:
#     # constructor
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#     def printdata(self):
#         print("name of the boof %s is by %s and price is %s"%(self.title,self.author,self.price))

# newbk=Book("punmia","eng","400")
# newbk.printdata()


# class vehicle:
#     # constructor
#     def __init__(self,speed,milage):
#         self.speed=speed
#         self.milage=milage
     
#     def printdata(self):
#         print("speed of the car %s  and milage is %s"%(self.speed,self.milage))

# car1=vehicle("100","15km")
# car1.printdata()


# class BankAccount:
#     # constructor
#     def __init__(self,Account_number,name,balance):
#         self.Account_number=Account_number
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print("Balance"+str(self.balance))

        
#     def withdrawel(self,amount):
#         if amount<self.balance:
#             self.balance=self.balance-amount
#             print("Balance"+str(self.balance))
#         else:
#             print("insufficient amount")
#     def Bankfees(self,fees):
#         self.balance=self.balance-self.balance*0.05
#         print("balance"+str(self.balance))
        

#     def printdata(self):
#         print("Account Number %s  and name is %s and balance %s"%(self.Account_number,self.name,self.balance))

# chithra=BankAccount("1234","chit",1000)
# chithra.Bankfees(200)

# inheritance
# class Parent:

#     def __init__(self,name):
#         self.name=name
#     def printname(self):
#         print(self.name)
# class Child(Parent):
#     def __init__(self,name,age):
#         Parent.__init__(self,name)
#         self.age=age

#     def printage(self):
#         print(self.age)

# obj1=Child("anu",20)
# obj1.printname()
# obj1.printage()

# class Parent1:

#     def __init__(self,name):
#         self.name=name
#     def printname(self):
#         print(self.name)

# class Parent2:
#     def __init__(self,gender):
#         self.gender=gender
#     def printgender(self):
#         print(self.gender)

# class Child(Parent1,Parent2):
#     def __init__(self,name,gender,age):
#         Parent1.__init__(self,name)
#         Parent2.__init__(self,gender)
#         self.age=age

#     def printage(self):
#         print(self.age)

# obj1=Child("anu","girl",20)
# obj1.printname()
# obj1.printgender()
# obj1.printage()

# overloading= last function will only be read

# class NewClass:
#     def newfunction(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a+self.b)


#     def newfunction(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#         print(self.a+self.b+self.c)

# obj1=NewClass()
# obj1.newfunction(2,3,4)

# class Area:
#     def newfunction(self,a,b=None):
        
#         if b is not None:
          
#             print("Area of the rectangle",a*b)
#         else: 
#             print("Area of the square",a*a)
        
    
# obj1=Area()
# obj1.newfunction(2,3)
# obj1.newfunction(2)

# access modifiers
# class Newclass:
#     def __init__(self,a,b,c):
#         self.a=a
#         self._b=b
#         self.__c=c
# obj1=Newclass("x","y","z")
# print(obj1.a)
# print(obj1._b)
# print(obj1.__c)
    
# from abc import ABC, abstractmethod

# class parentClass(ABC):
#     @abstractmethod
#     def do_something(self):
#         print("inside abstract")

# class SubClass(parentClass):
#     def do_something(self):
#         super().do_something()
#         print("another subclaass")

# y=SubClass()
# y.do_something()



# class Student():
#     counter=0

#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#         Student.counter=Student.counter+1 
#     def msg(self):
#         print(self.name+" got "+str(self.mark)+"mark")
#     @classmethod

#     def obj_count(cls):
#         return cls.counter

#     @staticmethod
#     def highmark(grade):
#         if grade=="A":
#             print("class topper")
#         else:
#             print("just pass mark")

# obj1=Student("anu",23)
# obj2=Student("bini",25)
# print(Student.obj_count())
# Student.highmark("B")

# class Family():
#     def __init__(self)
#     print("new family member")

#     father=family()




