# переменные
# int
number = 5

# float
fnumber = 5.7

# str
name = "John Doe"
age = 107

# Экранирование символов
print( "Вася \"плохой\" человек" )
print( 'Вася \"плохой\" человек' )

# Перевод строки
print ( 'Перевод \n строки' )

# Конкатенация
print( "Привет, меня зовуут " + name + "! Мне " + str(age) + "лет!")


# Комптляция программы
# pip install pyinstaller
# cd %path_to_script% 
# pyinstaller -F name.py
# exe появляется в папке dist

# очистить терминал
import os
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
