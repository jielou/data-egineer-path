"""
reference:  
1. https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work
2. https://www.programiz.com/python-programming/property
3. https://www.freecodecamp.org/news/python-property-decorator/

why use protected?

otherwise, it give recursion error...
"""
class Team:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        self._name = name
        if len(self._name)>10:
            raise ValueError("name too long")
    @name.deleter
    def name(self):
        del self._name


if __name__ == "__main__":
    team = Team()
    team.name = "yy"
    print(team.name)
    # team.name = "ssssssssssssssss"
    # print(team.name)
    del team.name
    # print(team.name)
