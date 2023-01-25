class A:
    def person(self):
        print("good")
class B:
    def person(self):
        print("Bad")
class C(A,B): #the 1st letter in the paranthesis decides , which parent class is to be inherit in the child class
    pass
obj=C()
obj.person() # when function defined, we should not print the statements  
#we just call the function                
