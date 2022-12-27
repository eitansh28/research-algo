from abc import ABC, abstractmethod


class MyStruct(ABC):    #Class of the main structure that appears in the main function
    def __init__(self, argu):
        self.struct = argu

    def get_item(self, i):   #function to get a value
        return self.struct[i]

    def set_item(self, curr: int, New: int):  #A function to insert some value into a particular cell
        self.struct[curr] = New

    def swap(self, a: int, b: int):  #A function to insert a value found in a certain cell into another cell
        self.struct[a] = self.struct[b]

    def length(self):
        return len(self.struct)

    def __str__(self):
        return f"{self.struct}"


class MyList(MyStruct):  #A list structure that inherits from the main structure
    def __init__(self, l: list):
        super().__init__(l)


class MyDict(MyStruct):   #A structure of a dictionary (only its values) inheriting from the main structure
    def __init__(self, d: dict):
        super().__init__(list(d.values()))

