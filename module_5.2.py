class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def   __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

house_JR = House('Жигулина Роща',16)
house_GM = House('Город Мира',9)

print(str(house_JR))
print(str(house_GM))
print(len(house_JR))
print(len(house_GM))



