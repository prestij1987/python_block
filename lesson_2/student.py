
'''На выполнение заданий по питону студент предполагает потратить ч часов м минут (
получить с клавиатуры). Во сколько самое позднее ему следует начать, чтобы оставить на дорогу 
1 час и успеть к 19:00 на занятия? Ответ оформить.'''

task_hour = 4;
task_min = float(input('Vvedite minuty; '));
time_puti = 1
time_zanyt = 19 

all_time = time_zanyt - (task_hour + task_min);
max_time = all_time - time_puti;

print('time', float(max_time))





