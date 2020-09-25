class animals:
    def feed(self):
        return 'Животное покормлено'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight  # kg


class dairy_cattle(animals):
    def milk(self):
        return 'Животное подоено'


class cows(dairy_cattle):
    voice = 'Му-у-у'


class goats(dairy_cattle):
    voice = 'Ме-е-е'


class shear_animals(animals):
    def shear_wool(self):
        return 'Животное подстрижено'


class sheep(shear_animals):
    voice = 'Бе-е-е'


class birds(animals):
    def collect_eggs(self):
        return 'Яйца собраны'


class gooses(birds):
    voice = 'Га-га-га'


class hens(birds):
    voice = 'Ко-ко-ко'


class ducks(birds):
    voice = 'Кря-кря'


cow = cows('Манька', 500)
goat_1 = goats('Рога', 90)
goat_2 = goats('Копыта', 110)
sheep_1 = sheep('Барашек', 80)
sheep_2 = sheep('Кудрявый', 105)
goose_1 = gooses('Серый', 3)
goose_2 = gooses('Белый', 2.5)
hen_1 = hens('Ко-Ко', 1)
hen_2 = hens('Кукареку', 0.8)
duck = ducks('Кряква', 1.6)


weight_list = []
weight_list.append([cow.name, cow.weight])
weight_list.append([goat_1.name, goat_1.weight])
weight_list.append([goat_2.name, goat_2.weight])
weight_list.append([sheep_1.name, sheep_1.weight])
weight_list.append([sheep_2.name, sheep_2.weight])
weight_list.append([goose_1.name, goose_1.weight])
weight_list.append([goose_2.name, goose_2.weight])
weight_list.append([hen_1.name, hen_1.weight])
weight_list.append([hen_2.name, hen_2.weight])
weight_list.append([duck.name, duck.weight])

weight_sum = 0
for animal_name, weight in weight_list:
    weight_sum += weight
print(f'Общий вес всех животных составляет: {weight_sum} кг')

max_weight = 0
for animal_name, weight in weight_list:
    if weight > max_weight:
        max_weight = weight
        print(f'Самое тяжёлое животное: {animal_name}, вес составляет {max_weight} кг')