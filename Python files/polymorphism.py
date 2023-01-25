
#from random import random,randint
#player_score=0
#computer_score=0
#player_in=input()
#select_choice=['rock','paper','scissor']
class A():
    def method_1(self,a,b):
        print("Sum of two numbers:",a+b)
class B(A):
    def method_1(self,a,b):
        print(a*b)
obj=B()
obj.method_1(10,20)        
            