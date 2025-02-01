# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

from itertools import combinations

dict_mass_of_things = {
    "палатка": 5.8,
    "спички": 0.05,
    "стул": 1.5,
    "вода питьевая": 2,
    "спрей от комаров": 0.3,
    "овощи": 1.2,
    "гречка": 0.8,
    "рис": 1,
    "тушёнка": 0.7,
    "сменная одежда": 1.4,
    "огниво": 0.3,
    "полотенце": 0.6,
    "фонарик": 0.4
}

while True:
    option = input("Введите 1 для ознакомления со словарём вещей или что-либо другое для продолжения работы: ")
    if option == '1':
        for k, v in dict_mass_of_things.items():
            print(k, v, "кг")

    load_capacity = input("Введите общую грузоподъёмность рюкзака в килограммах: ")
    try:
        load_capacity = float(load_capacity)
    except ValueError:
        print("Ошибка: введите числовое значение для грузоподъёмности.")
        break

    if load_capacity>= sum(dict_mass_of_things.values()):
        print("Все вещи поместятся в рюкзак")
    else:
        list_of_things = list(dict_mass_of_things.keys())
        all_combinations = []

        for r in range(1, len(list_of_things) + 1):
            for combination in combinations(list_of_things, r):
                total_weight = sum(dict_mass_of_things[item] for item in combination)
                remaining_capacity = load_capacity - total_weight
                remaining_items = set(list_of_things) - set(combination)
                if remaining_items:
                    min_remaining_item_weight = min(dict_mass_of_things[item] for item in remaining_items)
                    if remaining_capacity >= min_remaining_item_weight:
                        continue
                if total_weight <= load_capacity:
                    all_combinations.append((tuple(sorted(combination)), total_weight))

        all_combinations = sorted(set(all_combinations), key=lambda x: x[0])

        if all_combinations:
            print("\nВозможные варианты вещей, которые можно взять:")
            for combo, weight in all_combinations:
                print(f"Вещи: {', '.join(combo)} | Общий вес: {weight:.2f} кг")
        else:
            print("Нет комбинаций вещей, которые можно взять с такой грузоподъёмностью.")


