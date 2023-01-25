from abc import ABC,abstractmethod
class Animal(ABC):   #abc is package and ABC means Abstract Based Class
    @abstractmethod  #abstract method does not have any body inside of it,, if it has it considered to be nothing
    def skills(self):
        print("animal skills")
class dog(Animal):
    def skills(self):       #method name should be same for every function
        print("Dog can smell better")
class cat(Animal):
    def skills(self):    #skills is a method name
        print("Cat can escape better")
obj=dog()
obj.skills() #method name should be used to call the function
obj2 = cat()
obj2.skills()
