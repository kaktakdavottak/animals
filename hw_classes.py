class animals:
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
        animals.counter += 1
        animals.list_instances.append(self.weight)
        animals.dict_instances[name] = weight

    def feeding(self, feed_volume):
        self.satiety = True

    def collect_utility(self, collect_volume):
        self.utility -= collect_volume


class geese(animals):
    animal_sound = 'Га га га'
    utility = 20  # яиц


class cows(animals):
    animal_sound = 'Мууу'
    utility = 10  # литров молока


class sheeps(animals):
    animal_sound = 'Бе бе бе'
    utility = 3  # кг шерсти


class chickens(animals):
    animal_sound = 'Ко ко ко'
    utility = 15  # яиц


class goats(animals):
    animal_sound = 'Меееэ'
    utility = 5  # литров молока


class ducks(animals):
    animal_sound = 'Кря кря'
    utility = 5  # яиц


goose_1 = geese('Серый', 5)
goose_2 = geese('Белый', 6)
cow_1 = cows('Манька', 150)
sheep_1 = sheeps('Барашек', 30)
sheep_2 = sheeps('Кудрявый', 35)
chicken_1 = chickens('Ко-Ко', 12)
chicken_2 = chickens('Кукареку', 10)
goat_1 = goats('Рога', 34)
goat_2 = goats('Рога', 33)
duck_1 = ducks('Кряква', 9)

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
for weight in animals.list_instances:
    total_weight_list.append(weight)

print('Суммарный вес животных на ферме: {} кг\n'
      'Самое тяжелое животное: {} кг'
      .format(sum(total_weight_list), max(total_weight_list)))

for name, weight in animals.dict_instances.items():
    if max(total_weight_list) == weight:
        print('Самое тяжелое животное зовут {}'.format(name))
