
'''На дом задано 3 задачи. На решение каждой 
следующей тратится вдвое меньше времени. 
Измерьте время, затраченное на первую задачу 
и оцените общее время выполнения ДЗ. Ответ снова оформить красиво. 
Сравнить с реальным значением'''

task_hour = int(input('Vvedite chasy zadachi: '));
task_min = float(input('Vvedite minuty: '));

task_1 = (task_hour + task_min) / 2;
task_2 = task_1 / 2;
task_3 = task_2 / 2;

print(float(task_1))
print(float(task_2))
print(float(task_3))




