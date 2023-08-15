# Text zadaniya


'''Выяснить, какие номера символов не совпадают в двух введенных строках (вернуть список)
Выяснить, сколько символов второй строки встречается в первой
Создать случайную строку заданной длины из неповторяющихся символов
Запросить пользователя строку. Проверить её на соответствие "алфавиту" (самое простое - цифры)
Красиво оформить игру по алгоритму:
сгенерить строку
в цикле: спросить попытку, проверить и выдать диагностику'''

from random import randint


a = randint(0,9)
b = randint(0,9)
c = randint(0,9)
d = randint(0,9)

chislo = str(a + b + c + d)

print(chislo)
print(chislo)


'''while True:
    popit = 0
    if len(chislo) != 4:
        print('Vvedite 4 chisla:')
        continue
        
    
    val = input('Vvtdite chetyreh znachnoe chislo: ')
    val_1 = (val)
    for i in val_1:
        if val_1 == chislo:
            print('Vi ugadali chislo')
            break
            



    def bulls (): # chitaem bykov
        ask = val_1
        bull = 0
        for i in ask:
            ask_1 = str(i)
            if val_1[0] == ask_1[0] or val_1[1] == ask_1[1]:
                bull += 1
                print('kolvo bykov: ', bull)
            elif val_1 in ask_1:
                print('sovpadeniy net: ')

    def cows():
        cow = 0
        ask_2 = 
        for j in:'''

dig = input('Zadayte 4etyrex zyacnuy cifry: ')

while chislo == dig:
    def num ():
        if len(dig) != 4:
            return dig
            print('malo cifr')
            
        elif len(dig) > 4:
            print('Vi vveli mnogo cifr')    
            continue
    print(num)        
    def kolvo_byk ():
        kolvo = 0
        byk = 0
        kow = 0
        for zapros_1 in dig:
            if zapros_1 == chislo:
                byk += 1
                                
            elif zapros_1 in chislo:
                kow += 1
            else:
                kolvo += 1
                print('Dobavte', kolvo)
            return zapros_1        
        print(kolvo_byk)

        #def kolvo_korov():
            #kolvo = 0
            #kow = 0 
            #for zapros_2 in dig:
                #if zapros_2[0:4] == chislo[0:4]:
                    #kow += 1
                #else:
                    #kolvo += 1
                    #print('Dobavit', kolvo)    
