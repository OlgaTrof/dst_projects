#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np

        
def game_core(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    left = 0 #задаем первоначальные границы диапазона, в котором может быть установленное  random число
    right = 101
    while number != predict:
        count += 1
        if number > predict:
            left = predict #сужаем диапазон поиска, указывая левую границу
            predict = predict + (right-left)//2 #выбираем для следующей проверки середину нового диапазона
        elif number < predict: 
            right = predict #сужаем диапазон поиска, указывая правую границу
            predict = predict - (right-left)//2 #выбираем для следующей проверки середину нового диапазона
    return(count) # выход из цикла, если угадали
        
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
score_game(game_core)

