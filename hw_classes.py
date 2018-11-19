class Animals:
    name = 'Имя'
    weight = 0
    animal_sound = ''
    satiety = False
    utility = 0
    counter = 0
    list_instances = []
    dict_instances = {}

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Animals.counter += 1
        Animals.list_instances.append(self.weight)
        Animals.dict_instances[name] = weight

    def feeding(self, feed_volume):
        self.satiety = True

    def collect_utility(self, collect_volume):
        self.utility -= collect_volume


class Geese(Animals):
    animal_sound = 'Га га га'
    utility = 20  # яиц


class Cows(Animals):
    animal_sound = 'Мууу'
    utility = 10  # литров молока


class Sheeps(Animals):
    animal_sound = 'Бе бе бе'
    utility = 3  # кг шерсти


class Chickens(Animals):
    animal_sound = 'Ко ко ко'
    utility = 15  # яиц


class Goats(Animals):
    animal_sound = 'Меееэ'
    utility = 5  # литров молока


class Ducks(Animals):
    animal_sound = 'Кря кря'
    utility = 5  # яиц


goose_1 = Geese('Серый', 5)
goose_2 = Geese('Белый', 6)
cow_1 = Cows('Манька', 150)
sheep_1 = Sheeps('Барашек', 30)
sheep_2 = Sheeps('Кудрявый', 35)
chicken_1 = Chickens('Ко-Ко', 12)
chicken_2 = Chickens('Кукареку', 10)
goat_1 = Goats('Рога', 34)
goat_2 = Goats('Рога', 33)
duck_1 = Ducks('Кряква', 9)

goose_1.feeding(2)
goose_2.feeding(5)
cow_1.feeding(45)
sheep_1.feeding(3)
sheep_2.feeding(4)
chicken_1.feeding(4)
chicken_2.feeding(5)
goat_1.feeding(6)
goat_2.feeding(7)
duck_1.feeding(1)

goose_1.collect_utility(2)
goose_2.collect_utility(5)
cow_1.collect_utility(45)
sheep_1.collect_utility(3)
sheep_2.collect_utility(4)
chicken_1.collect_utility(4)
chicken_2.collect_utility(5)
goat_1.collect_utility(6)
goat_2.collect_utility(7)
duck_1.collect_utility(1)

total_weight_list = []
for weight in Animals.list_instances:
    total_weight_list.append(weight)

print('Суммарный вес животных на ферме: {} кг\n'
      'Самое тяжелое животное: {} кг'
      .format(sum(total_weight_list), max(total_weight_list)))

for name, weight in Animals.dict_instances.items():
    if max(total_weight_list) == weight:
        print('Самое тяжелое животное зовут {}'.format(name))
