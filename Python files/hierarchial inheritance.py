class Company():
    type="Private institute"
    position=" working Employee"
    skills="codining abilities vth good communication skills"
class Team_captain(Company):
    print("best empl0yee of the Rien prepacademy")
    name="Rajiv"
    age="26"
    gender="male"
obj=Team_captain()
print(obj.name)    
class Team_member1(Team_captain) :
    name="sai"
    age="20"  
class Team_member2(Team_captain):
    name="Jagadeesh"
obj=Team_member2()
print("best hard worker of the Rien prepacademy")
print(obj.name)
print(obj.type)
print(obj.position)
print(obj.skills)           