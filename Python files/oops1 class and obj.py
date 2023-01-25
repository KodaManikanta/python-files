class Student:
    student_name=" no name "
    def __init__(self,name):
        print("obj created")
        print(name)#obj returns from 
        
        
        print(self.student_name)#returns from the class
s1=Student("jay") #returns from the obj created       