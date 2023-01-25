class Sea():
    def types(self):
        print("water living animals")
class Whale():
    def style(self):
        print("Swimming")
class mammals(Whale):
    breathe="Air"
class snakes(Sea,Whale):
    structure="no wings to their boddy"
obj=snakes()
obj.types()
obj.style()               