'''
Задание 2: Работа с условиями и циклами
Попросите пользователя ввести число с клавиатуры. 
Если число делится на 3 без остатка, выведите сообщение "Число делится на 3". 
Если число больше 10, выведите сообщение "Число больше 10". 
Если число не удовлетворяет ни одному из условий, выведите сообщение "Число не соответствует условиям".
'''

n=int(input("Введите число: "))

if n%3==0 and n>10:
    print ("Число делится на 3")
    print ("Число больше 10")
elif n%3==0:
    print ("Число делится на 3")
elif n>10:
else:
    print ("Число не соответствует условиям")