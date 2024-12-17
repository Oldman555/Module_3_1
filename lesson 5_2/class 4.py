class House:

    houses_history = []

    def __new__(cls,*args,**kwargs):
        cls.houses_history.append(args[0])
        return object. __new__(cls)

    def __init__(self, name,number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floor

    # def __str__(self):
    #     return f'Название : {self.name}, количество этажей:{self.number_of_floor}'
    #
    # def __eq__(self, other):
    #     if isinstance(other.number_of_floor,int) and self.number_of_floor == self.number_of_floor:
    #         return True
    #     else:
    #         return False
    #
    # def __lt__(self, other):
    #     if isinstance(other.number_of_floor, int) and self.number_of_floor < self.number_of_floor:
    #         return True
    #     else:
    #         return False
    #
    # def __gt__(self, other):
    #     if isinstance(other.number_of_floor, int) and self.number_of_floor  > self.number_of_floor:
    #         return True
    #     else:
    #         return False
    #
    # def __le__(self, other):
    #     if isinstance(other.number_of_floor, int) and self.number_of_floor <= self.number_of_floor:
    #         return True
    #     else:
    #         return False
    #
    # def __ge__(self, other):
    #     if isinstance(other.number_of_floor, int) and self.number_of_floor >= self.number_of_floor:
    #         return True
    #     else:
    #         return False
    #
    # def __ne__(self, other):
    #     if isinstance(other.number_of_floor, int) and self.number_of_floor != self.number_of_floor:
    #         return True
    #     else:
    #         return False
    #
    # def __add__(self, value):
    #     if isinstance(value, int):
    #         self.number_of_floor = self.number_of_floor + value
    #         return self
    #
    # def __radd__(self, value):
    #     if isinstance(value, int):
    #         self.number_of_floor = self.number_of_floor + value
    #         return self
    #
    # def __iadd__(self, value):
    #     if isinstance(value, int):
    #         self.number_of_floor = self.number_of_floor+value
    #         return self
    #

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)
#
h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)

del h2

del h3

print(House.houses_history)


