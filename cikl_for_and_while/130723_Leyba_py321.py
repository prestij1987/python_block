
'''1. Спросить человека маршрут ("как пройти в библиотеку"). 
Получить ответ в виде строки. Сохранить в переменную. 
Вывести первое слово ответа на экран
2. Спросить человека размеры поля (х * у), получить их 
ОДНИМ вводом '7x8', "нарисовать" поле буковками о без использования цикла.
3. Нарисовать только границу поля и пустую серединку.
4. Вывести на экран таблицу из 4 строк: три товара и сумма без использования цикла
5. С помощью только while сделать задачи 2, 3, 4'''

# Task 1

'''ask = input('Kak proyti d biblioteky: ')
otvet = ask.split()[0]
print(otvet)'''


# Task 2

from re import split


size_x = int(input('Vvedite razmer x: '))
size_y = int(input('Vvedite razmer y: '))

size_xy = (size_x, size_y)
size = str(size_xy)

size_1 = size[0] # получаем элементы по индексу
size_2 = size[1]
print(size_1, size_2)
word = '0'
word_1 = int(word)

pole_1 = size_1 * word_1
pole_2 = size_2 * word_1

for i in pole_1 + '1':
    fil_1 = int(i)
    if fil_1 < 10:
        print(fil_1)
        for item in pole_2 + '1':
            fil_2 = int(item)
            if fil_2 < 10:
                print(fil_2)
                print(fil_1, fil_2,)

    



