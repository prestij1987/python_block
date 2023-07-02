speed_plane = int(input('Vvedite skorost samoleta: '));
name_city_1 = input('Vvtdite gorod: ');
name_city_2 = input('Vvtdite gorod: ');
vremy_puti = int(input('Vvedite vremy v puti: '))

rast_city = speed_plane * vremy_puti;
print('Ot', name_city_1, 'do', name_city_2, rast_city, 'km')
