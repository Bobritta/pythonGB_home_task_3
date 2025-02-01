# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

from collections import Counter
import re

data = input("Введите длинную строку: ")
data = re.sub(r'[^\w\s]', '', data).lower().split()
counter = Counter(data)
top_10 = counter.most_common(10)
print(top_10)