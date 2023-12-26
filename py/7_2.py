'''Задание 1: Работа со списками и множествами

Условие: Вводятся два списка чисел, числа вводятся вручную. 
Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.
'''
spisok1=[15,20,25,10]
spisok2=[20,83,10,15]

rezult1=" ".join(str(i) for i in spisok1)
rezult2=" ".join(str(i) for i in spisok2)

print("Выведите первый список:", rezult1)
print("Выведите второй список:", rezult2)

set1=set(spisok1)
set2=set(spisok2)
result=set1.intersection(set2)
#result = set1&set2
print("Количество пересечений:", len(result))
