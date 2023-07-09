
'''В общественном транспорте действует система скидок. 
Если Вы старше 50 лет или младше 14-ти - проезд бесплатный. 
Если Вы студент (14-24 года), проезд за полцены. Программа 
предлагает ввести год рождения и тариф "час", "неделя", "месяц" или "год". 
Час стоит 60 рублей, неделя 300 рублей, месяц 1000 рублей и год 10 тысяч 
для взрослого человека, не попадающего в льготную категорию. 
Вычислить стоимость проездного указанного тарифа 
для рассматриваемого гражданина и вывести сообщение на экран.'''


god= int(input('Vvdeite god(1970-2015): '))
god_now = 2023
vozr = god_now - god

tarif_chas = 60
tarif_nedelya = 300
tarif_mesyc = 1000
tarif_god = 10000

if vozr < 14 or vozr > 50:
    print('Vam proezd besplatny: ')
elif 14 < vozr < 24:
    tarif_st_chas = tarif_chas / 2
    tarif_st_ned = tarif_nedelya / 2
    tarif_st_mes = tarif_mesyc / 2
    tarif_st_god = tarif_god / 2
    res_st = tarif_st_chas, tarif_st_ned, tarif_st_mes, tarif_st_god

    print('Vi student:', res_st)
else:
    print('Oplachivayte polnuy cenu:')    