class A():
    name="raju"
    age=65
    gender="male"
class B(A):
    name="teja"
obj=B()
print(obj.name)
print(obj.age) 
class C(B): 
    lang="telugu"
obj=C()
#print(obj.name)# there is no need to create object every time, only if neded
#print(obj.age) 
#print(obj.gender)
class python(C):
    pass
obj=python()
print(obj.lang)
print(obj.name)  