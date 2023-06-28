print('privet')


'''god_now = '2023' 
year = input(int('Vvedite god: '));
moth = input('Vvedite meciac: ')
moth = int(moth)
day = input('Vvedite day: ');

if (year > str(2000)):
   elif (moth > 0):
          tek_date = year + moth
      print(moth)

my_age = (god_now - int(god_now));

print(my_age);'''

imya = input('Vvedite imya: ')
rost = int(input('Vvedite rost: '))

if (rost > 90 and rost < 120):
       print('vam dostupna zelenaya trassa', rost)
elif (rost > 110 and rost < 130):
       print('Dostupna chernay trassa', rost)       
elif (rost > 130 and rost < 150):
       print('Vam dostupna krasnay trassa', rost)       
else:
       print('Vam dostupna sinya trasa', imya,  rost)
