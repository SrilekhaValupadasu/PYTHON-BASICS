class person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("hello,my name is",self.name)
p=person("sash")
p1=person("hello")
p3=person("hi srilekha")
p.say_hi()
p1.say_hi()
p3.say_hi()