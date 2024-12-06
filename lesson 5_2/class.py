class House:
    def __init__(self, self_name,number_of_floor):
        self.name = self_name
        self.number_of_floor = number_of_floor

    def go_to (self,new_floor):
        if new_floor > self.number_of_floor  or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(0,new_floor):
                print(i+1)


h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h2.go_to(10)

