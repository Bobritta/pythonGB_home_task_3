# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from collections import Counter

print("Вас приветствует программа по вычислению дубликатов")
lst = []
flag = True
while flag:
    temp = input("Введите следующий элемент списка или ! для завершения ввода: ")
    if temp != "!":
        lst.append(temp)
    else:
        flag = False
print("Получился список: ", *lst)

lst_item_counter = dict(Counter(lst))
lst_doubles = []
for k, v in lst_item_counter.items():
    if v > 1:
        lst_doubles.append(k)

print("Список дубликатов: ", *lst_doubles)


