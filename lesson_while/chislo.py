
'''С клавиатуры вводятся числа. Остановиться, как только введён ноль. 
Посчитать количество введенных чисел


Усложнение: остановиться, как только введен "просто Enter"

Бинарный поиск: Вы загадываете число от 1 до 1000 и записываете 
его в тетрадь. Компьютер задаёт вам только вопросы типа "число 
больше 70?" или "число меньше 25?" Вы честно отвечаете "да" 
или "нет". Компьютер должен угадать ваше число. 
Сколько попыток ему потребовалось? 
Это количество зависит от загаданного числа?'''



val = int(input('Vvedite chislo(0-10): '))
#kolvo = 0
          
while val < 7:
    print(val)
    val += 1
    num_str = str(val)
    count = len(num_str)
    #kolvo_vvoda = [val]
    print('Kolvo chisla', count)
if val == 0:
    print('Cikll okonchen')    
    
    print('Kolvo popytok', val)
print('quit')

znachenie = int(input('Vvedite cifru(0-10): '))
while znachenie != 0:
    print('Povtorite vvod: ')
    chislo = int(input('Vvedite zanovo: '))
    chislo1 = str(chislo)
    num_chislo = len(chislo1)
    print('Kolvo popytok', num_chislo)    
print('Cikl')    