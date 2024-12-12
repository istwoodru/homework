class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):

        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('"Такого этажа не существует"')

    def __len__(self):
        return self.number_of_floors
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        self.number_of_floors = self.number_of_floors + other
        return self

    def __iadd__(self, other):
        self.number_of_floors = self.number_of_floors + other
        return self

    def __radd__(self, other):
        self.number_of_floors = self.number_of_floors + other
        return self
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)