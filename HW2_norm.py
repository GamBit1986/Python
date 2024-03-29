# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
#import math
#list1 = [33, 44, -89, 49, -5, 64, 121, 854]
#list2 = []
##   if item > 0 and sqrt(item) % 1 == 0:
#        list2.append(int(math.sqrt(item)))
#print(list2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

start_data = "01.11.2004"
data_list = start_data.split(".")
months = {
"01": "января",
"02": "февраля",
"03": "марта",
"04": "апреля",
"05": "мая",
"06": "июня",
"07": "июля",
"08": "августа",
"09": "сентября",
"10": "октября",
"11": "ноября",
"12": "декабря",
}
days = {
"01": "первое", "02": "второе", "03": "третье", "04": "четвёртое", "05": "пятое",
"06": "шестое", "07": "седьмое", "08": "восьмое", "09": "девятое", "10": "десятое",
"11": "одиннадцатое", "12": "двенадцатое", "13": "тринадцатое", "14": "четырнадцатое", "15": "пятнадцатое",
"16": "шестнадцатое", "17": "семнадцатое", "18": "восемнадцатое", "19": "девятнадцатое", "20": "двадцатое",
"21": "двадцать первое", "22": "двадцать второе", "23": "двадцать третье", "24": "двадцать четвёртое",
"25": "двадцать пятое", "26": "двадцать шестое", "27": "двадцать седьмое", "28": "двадцать восьмое",
"29": "двадцать девятое", "30": "тридцатое", "31": "тридцать первое",
}
for key in days:
    if data_list[0] == key:
        data_list[0] = days[key]

for key in months:
    if data_list[1] == key:
        data_list[1] = months[key]

answer_data = data_list[0] + " " + data_list[1] + " " + data_list[2] + " " "года"
print(answer_data)

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


import random
n = int(input('Сколько хотите элементов в список?: '))
rand_list = []
for el in range(n):
    rand_list.append(random.randint(-100, 100))
print(rand_list)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

#a)
list1 = [1, 2, 3, 4, 8, 10 ,12, 1, 11, 2, 12, 3]
list2 = []
for i in list1:
  if i not in list2:
    list2.append(i)
print(list2)

#б)

list3 = []
for item in list1:
    if list1.count(item) == 1:
        list3.append(item)
print(list3)

