
class Parent1:
    def __init__(self, id, name, age,**kwargs):
        print("parent 1 initalized")
        self.age = age
        self.id = id
        self.name = name
        # key
        super().__init__(**kwargs)
        

    # def shout(self):
    #     print(f"I am {self.name} and age is {self.age}")

class Parent2:
    def __init__(self, job,**kwargs):
        print("parent 2 initalized")
        self.job = job
        super().__init__(**kwargs)
        #self.id = id
        #self.name = name

    def shout(self):
        print(f"my job is {self.job}")

class Child(Parent1, Parent2):
    def __init__(self, id, name, age,job,**kwargs):
        kwargs["job"]=job
        kwargs["age"]=age
        #key
        super().__init__(id=id,name=name,  **kwargs)


    def shout(self):
        super().shout()

print(Child.__mro__)

child = Child(id="1", name="jon",age=24,job="coder")
print(child.id)
print(child.name)
print(child.age)
child.shout()
