#Задание 1: Работа с списками и срезами

#Создайте список из 10 элементов с разными типами данных (строки, числа и булевы значения) и выведите его на экран.
a = [5, 'mango', 123, True, 3.59, 'питон', 12, False, 'c', 'qwe']

# 5, mango, 123, True, 3.59, питон, 12, False, c, qwe'  - список
# 0   1      2    3     4      5     6    7    8   9   - индексы

print (a)
print (*a)
print (*a,sep="/")

#Используя срезы, выведите на экран первые 5 элементов списка, последние 3 элемента списка и каждый второй элемент списка.
print (a[0:5])
print (a[7:10])
print (a[1:10:2])

#Измените 3 элемент списка на новое значение и выведите измененный список на экран.
a.insert(2,'Ivan')
print (a)