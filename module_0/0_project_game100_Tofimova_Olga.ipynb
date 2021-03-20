{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 5 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED один и тот же набор отобранных random чисел, чтобы эксперимент был воспроизводим.\n",
    "    random_array = np.random.randint(1,101, size=(1000))\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)\n",
    "\n",
    "\n",
    "def game_core(number):\n",
    "    '''Сначала берем для проверки середину интервала, выясняем больше она или меньше загаданного числа, сдвигаем границы поиска,\n",
    "       каждый раз отсекая интервал, который точно не содержит загаданное число (оно точно больше или точно меньше).\n",
    "       Функция принимает загаданное число и возвращает число попыток, озволившее угадать число'''\n",
    "    count = 1\n",
    "    left = 1 #задаем первоначальные границы диапазона, в котором может быть установленное  random число\n",
    "    right = 100\n",
    "    \n",
    "    predict = (right+left)//2 #определяем середину интервала - это число проверим первым в цикле\n",
    "       \n",
    "    while number != predict:\n",
    "        count += 1\n",
    "        if number > predict:\n",
    "            left = predict #сужаем диапазон поиска, указывая левую границу\n",
    "        else: \n",
    "            right = predict #сужаем диапазон поиска, указывая правую границу\n",
    "        predict = (right+left)//2 #выбираем для следующей проверки середину нового диапазона\n",
    "    return(count) # выход из цикла, если угадали\n",
    "\n",
    "score_game(game_core)        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
