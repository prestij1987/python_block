 # Домашнее задание: используя только random.randint() или random.choice()
#   реализовать (придумать) алгоритм получения последовательности неповторяющихся цифр



from random import choice
from random import randint

# poluchem cluchaynoe chislo
a = randint(0,9)
b = randint(0,9)
c = randint(0,9)
d = randint(0,9)
e = randint(0,9)
itog = (a + b + c + d + e) # skladyvaem sluchaynoe chislo v odno chislo
print(itog)

def chislo (val='012345678', itog_len=4):
    result = choice(val, itog_len)
    return result





'''def zagadaika(alphebet='0123456789', word_len=4):  # ARGUMENTS?
    result = ''.join(random.sample(alphebet, word_len))
    # ['6', '2', '7', '9']turn 
    return result'''
    