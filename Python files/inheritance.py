class A:
    name="none"
    age=89
class B(A):#B acquires properties from the A
    
    age=78
obj=B()
print(obj.name)
print(obj.age)
