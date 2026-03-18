"""
"""

class Computer:
    def config(self):
        print("hp computer")

comp1=Computer()
comp2=Computer()
print(type(comp1))
Computer.config(comp1)
Computer.config(comp2)
#comp1.config()
#comp2.config()


"""

"""
#object
class Computer:
    pass

a=10
print(type(a))
c1=Computer()
print(type(c1))
"""
"""
#every object having their attribute
class Computer:
    pcname="hp"
    ram="16gb"

c1=Computer()
print(c1.pcname)
print(c1.ram)
print(id(c1))
c2=Computer()
print(c2.pcname)
print(c2.ram)
print(id(c2))
"""

"""
#wap to find sum of two number
class Cal:
    def get(self):
        self.n1=int(input("Enter Number:"))
        self.n2 = int(input("Enter Number:"))
    def display(self):
        self.sum=self.n1+self.n2
        print(self.sum)

c1=Cal()
c1.get()   #call methode with self object
c1.display()

"""

"""
#constructor _init_
class Computer:
    def __int__(self):
        self.pcname="hp"
        self.pcram="16gb"

    def update(self):
        self.pcram="4gb"

c1=Computer()
print(c1.pcname)
print(c1.pcram)
c2=Computer()
print(c2.pcname)
print(c2.pcram)
c1.update()
print(c1.pcram)





"""
"""
#we create person class
class Person:
    name="XXX"
    age=0
    gender="Male"

#create 2 object p1 and p2 of person class
p1=Person()
p2=Person()
print("p1->name",p1.name,"p2->name",p2.age)
p1.name="yogesh"
p2.age=20
print("p1->name",p1.name,"p2->age->",p2.age)
#--------------------------------------------------------
"""
"""
#constructor in python
#initalize __init__() method->this fun is the constructor of obj
#here the init() 4 parameter.firste parameter is self
class Person:
    def __init__(self): #constructor
        self.myname="xxx"
        self.mygender="male"
        self.myage=32
    def update(self):  #methode
        self.myname="XXX"
#create object p1 and p2
p1=Person()
p2=Person()
print("p1 is ",p1.myname,"gender",p1.mygender,"age",p1.myage)
print("p2 is ",p2.myname,"gender",p2.mygender,"age",p2.myage)
p1.update()
print(p1.myname)
"""
"""
#also default value set in init
class Person:
    def __init__(self,name,gender,age):
        self.myname=name
        self.mygender=gender
        self.myage=age
    def update(self):
        self.myname="XXX"
#create object p1 and p2
p1=Person("Yogesh Katre","Male",32)
p2=Person("sanjay Katre","Female")
print("p1 is ",p1.myname,"gender",p1.mygender,"age",p1.myage)
print("p2 is ",p2.myname,"gender",p2.mygender,"age",p2.myage)
p1.update()
print(p1.myname)
#init==========================================================
"""
"""

#A class which has attributes as well as member function
class Person:
    def __init__(self,name,gender,age):
        self.myname=name
        self.mygender=gender
        self.myage=age
        self.lang="hindi"
    def setL(self,lang):
        self.lang=lang
    def getL(self):
        return self.lang
        

p1=Person("Yogesh Katre","Male",32)
print("Before setting language:",p1.getL())
p1.setL("English")
print("After setting language:",p1.getL())
"""

"""
#delete using constructor object
#_del_ is the destructor method in python.
class Car:
    def __init__(self,name="No name"):
        self.name= name
        print("Car created=",self.name)

    def __del__(self):
        print("Car destroy=",self.name)


#created object with one reference
c1=Car("Maruti")
"""
"""
#instance variable and class variable
class Car:
    wheel=4     #class variable its static
    def __init__(self):
        self.mil=10          #called instance variable
        self.carmodel="bmw"
c1=Car()
c2=Car()
print(c1.mil,"  ",c1.carmodel,"  ",c1.wheel)
print(c2.mil,"  ",c2.carmodel,"  ",c2.wheel)
Car.wheel=5
print(Car.wheel)

print(c1.mil,"  ",c1.carmodel,"  ",c1.wheel)
print(c2.mil,"  ",c2.carmodel,"  ",c2.wheel)
"""
"""
#methode=>instance methode,class methode,static metode
class Student:
    college="sbjain"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):      #instance methode
        return (self.m1+self.m2+self.m3)//3
    @classmethod
    def info(cls):           #class methode
        return cls.college
    @staticmethod
    def detail():            #static methode
        print("This is static ")


s1=Student(35,45,56)
s2=Student(34,67,89)

print(s1.average())
print(Student.info())
Student.detail()
"""

"""
#inheritance
#simple example
class A:
    def feature1(self):
        print("Feature 1 Working")
    def feature2(self):
        print("Feature 2 Working")
class B(A):
    def feature3(self):
        print("Feature 1 Working")
    def feature4(self):
        print("Feature 2 Working")



a1=A()
a1.feature1()
a1.feature2()

a2=B()
a2.feature1()
a2.feature2()

#above called as single levelinheritance
"""
"""
#multilevel inheritance
class A:
    def feature1(self):
        print("Feature 1 Working")
    def feature2(self):
        print("Feature 2 Working")
class B(A):
    def feature3(self):
        print("Feature 3 Working")
    def feature4(self):
        print("Feature 4 Working")
class C(B):
    def feature5(self):
        print("Feature 5 Working")
    def feature6(self):
        print("Feature 6 Working")


a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature1()
b1.feature2()

c1=C()
c1.feature1()
c1.feature2()

"""
"""
#multiple inheritance
class A:
    def feature1(self):
        print("Feature 1 Working")
    def feature2(self):
        print("Feature 2 Working")
class B:
    def feature3(self):
        print("Feature 3 Working")
    def feature4(self):
        print("Feature 4 Working")
class C(A,B):         #C inherit both A and B class
    def feature5(self):
        print("Feature 5 Working")
    def feature6(self):
        print("Feature 6 Working")


c1=C()
c1.feature1()
c1.feature2()
"""

"""
#how constructor behave in inheritance
#how to use super in inheritance
#methode resolution order
class A:
    def __init__(self):
        print("is A init")
    def feature1(self):
        print("Feature 1 Working")
    def feature2(self):
        print("Feature 2 Working")
class B(A):
    def __init__(self):
        super().__init__()
        print("is B init")
  
    def feature3(self):
        print("Feature 1 Working")
    def feature4(self):
        print("Feature 2 Working")
b1=B()

"""
"""
#methode resolution order
#multiple inheritance
class A:
    def __init__(self):
        print("is A init")
    def feature1(self):
        print("Feature 1 Working")
    def feature2(self):
        print("Feature 2 Working")
class B:
    def __init__(self):
        print("is B init")
    def feature3(self):
        print("Feature 3 Working")
    def feature4(self):
        print("Feature 4 Working")
class C(B,A):         #C inherit both A and B class
    def __init__(self):
        super().__init__() #this call a constructor because of MSE
        print("is C init")
    def feature5(self):
        print("Feature 5 Working")
    def feature6(self):
        print("Feature 6 Working")

c1=C()
"""
#Polymorphism
#1. Duck Typing
#2.Operator overloading
#3. Metode Overloading
#4. Method overiding
"""
#1. Duck Typing
class pycharm:
    def execute(self):
        print("Compiling")
        print("Runing")
class MyEditor:
    def execute(self):
        print("spell check")
        print("syntax check")
        print("Compiling")
        print("Runing")

class Laptop:
    def code(self,ide):
        ide.execute()

ide=pycharm()
ide=MyEditor()
L=Laptop()
L.code(ide)
"""
"""
class MyEditor:
    def execute(self):
        print("spell check")
        print("syntax check")
        print("Compiling")
        print("Runing")
"""
"""

#operator overloading

a=5
b=6
print(a+b)

print(int.__add__(a,b))  #inbuilt methode 
"""
"""
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):  # operator overloding
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3
s1=Student(56,68)              #<-Student.__add__(s1,s2)
s2=Student(45,54)
s3=s1+s2
print(s3.m1,s3.m2)
"""
"""
#methode overloading  not direct support in python
class Student:
    def sum(self, a=None, b=None, c=None):  # methode overloading
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s
s1=Student()
print(s1.sum(1))

"""
"""
def sum(self,a=None,b=None,c=None):  #methode overloading
       if a!=None and b!=None and c!=None:
           s=a+b+c
       elif a!=None and b!=None:
           s=a+b
       else:
           s=a
       return s
"""
"""
#last methode overiding
class A:
    def show(self):
        print("A show call")
class B(A):
    def show(self):  #we override the methode of A
        print("method overwrite")
b=B()
b.show()
"""

"""
