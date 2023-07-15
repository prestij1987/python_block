'''zаписать программу, которая спрашивает возраст, 
выбрасывает исключение, если введенное число отрицательное, 
в противном случае считает год рождения.'''

'''try:
    my_age = int(input('VVtdite vash vozrast(0-30): '))
except(ValueError):
    if my_age > 0:
        print('Vi ne rodilis: ') '''
   
age = int(input('Vvedite god(0-30): ')) 
year = 2023
year = int(2023)
'''if age > 0: 

    my_age = year - age
    print('Vash vozrast: ', my_age) 
if age % 2 == 0:
    print(ValueError(age))'''    

try:
    age = int(input('Vvedite god(0-30): ')) 
    if age > 0:
        print('vash god rojdenya: ', year - age)
    elif age > 30:
        print('error')    
except ValueError:
    if age < 0:
        age_not = age % 2 == 0
        print(age_not)    
print('Oshibka vi ne rodilis')        