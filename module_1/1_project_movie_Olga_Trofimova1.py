#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


# In[23]:


data = pd.read_csv('movie_bd_v5.csv')
data.sample(5)


# In[24]:


data.describe()


# # Предобработка

# In[25]:


answers = {} # создадим словарь для ответов


data['profit']=data.revenue-data.budget # добавим в датафрейм столбец profit = revenue - budget


#функция для перевода данных в столбцах в формaт списка
def str_to_list(str_column):
    result_list = str_column.str.split('|')
    return result_list


#the time given in the dataset is in string format.
#So we need to change this in datetime format
data['release_date']=pd.to_datetime(data['release_date'], format="%m/%d/%Y")


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[26]:


# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = '723. Pirates of the Caribbean: On Stranger Tides (tt1298650)' # "+"


# In[27]:


# тут пишем ваш код для решения данного вопроса:
data[data.budget == data.budget.max()] # "+"


# ВАРИАНТ 2

# In[ ]:


# можно добавлять разные варианты решения


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[28]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = '1157. Gods and Generals (tt0279111)' # "+"


# In[29]:


data[data.runtime == data.runtime.max()]


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[30]:


answers['3'] = '768. Winnie the Pooh (tt1449283)' # "+"


data[data.runtime == data.runtime.min()]


# # 4. Какова средняя длительность фильмов?
# 

# In[31]:


answers['4'] = 109.658549 # "+"
#среднее уже видим выше через метод .describe (строка 'mean', столбец 'runtime')
#Можем рассчитать отдельно
data.runtime.mean()


# # 5. Каково медианное значение длительности фильмов? 

# In[32]:


answers['5'] = 107.000000 # "+"
# медиана уже выведена в .describe (строка '50%')
#Можем рассчитать отдельно
data.runtime.median()


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[33]:


answers['6'] = '239. Avatar (tt0499549)' #"+"


data[data.profit == data.profit.max()]


# # 7. Какой фильм самый убыточный? 

# In[34]:


answers['7'] = '1245. The Lone Ranger (tt1210819)' #"+"


data[data.profit == data.profit.min()]


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[35]:


answers['8'] = 1478 #"+"


data[data.profit > 0].profit.count()


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[36]:


answers['9'] = '599. The Dark Knight (tt0468569)' #"+"


data[data.release_year == 2008].sort_values(['revenue'],ascending=False).head(1)


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[38]:


answers['10'] = '1245. The Lone Ranger (tt1210819)' #"+"


data[(data.release_year >= 2012) & (data.release_year <= 2014)].sort_values(['profit']).head(1)


# # 11. Какого жанра фильмов больше всего?

# ВАРИАНТ 

# In[39]:


answers['11'] = 'Drama'#"+"


data['genres_list']=str_to_list(data['genres'])
Counter(data['genres_list'].sum()).most_common(1)


# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[40]:


answers['12'] = 'Drama'#"+"


Counter(data.query('profit> 0')['genres_list'].sum()).most_common(1)


# # 13. У какого режиссера самые большие суммарные кассовые сборы?

# In[41]:


answers['13'] = 'Peter Jackson'#"+"

data['director_list']=str_to_list(data['director'])#c помощью функции добавим стобец с именами режиссеров в форме списка

# скопируем в новый датафрейм, разбив на подстроки по столбцу director
data_director_exploded=data.explode('director_list').copy()
data_director_exploded.groupby(['director_list'])['revenue'].sum().sort_values(ascending=False)


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[42]:


answers['14'] = 'Robert Rodriguez' #"+"

director_count_action=data_director_exploded[data_director_exploded['genres'].
                      str.contains('Action')].director_list.value_counts()
director_count_action


# In[43]:


#вариант 2
Counter(data[data['genres'].str.contains('Action')]['director_list'].sum()).most_common(5)


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[44]:


answers['15'] = 'Chris Hemsworth' #"+"

data['cast_list']=str_to_list(data['cast'])#c помощью функции добавим стобец с именами актеров в форме списка


data_cast_exploded=data.explode('cast_list').copy()# скопируем в новый датафрейм данные, разбив на подстроки по столбцу cast
data_cast_exploded[data_cast_exploded.release_year == 2012].groupby(['cast_list'])['revenue'].sum().sort_values(ascending=False)


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[45]:


#Примечание: в фильмах, где бюджет выше среднего по данной выборке.
answers['16'] ='Matt Damon' #"+"

data_cast_exploded[data_cast_exploded.budget > data_cast_exploded.budget.mean()]['cast_list'].value_counts()


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[46]:


answers['17'] = 'Action' #"+"

Counter(data[data['cast'].str.contains('Nicolas Cage')]['genres_list'].sum()).most_common(5)


# # 18. Самый убыточный фильм от Paramount Pictures

# In[47]:


answers['18'] = '925. K-19: The Widowmaker (tt0267626)' #'+'

#c помощью функции добавим стобец с названиями произодителей в форме списка
data['production_companies_list']=str_to_list(data['production_companies'])
# скопируем в новый датафрейм данные, разбив на подстроки по столбцу production_companies
data_companies_exploded=data.explode('production_companies_list').copy()
data_companies_exploded[data_companies_exploded['production_companies_list'].
                        str.contains('Paramount Pictures')].sort_values(['profit']).head(1)


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[48]:


answers['19'] = 2015 #'+'

data.groupby(['release_year'])['revenue'].sum().sort_values(ascending=False)


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[49]:


answers['20'] = 2014 #'+'

data_companies_exploded[data_companies_exploded['production_companies_list'].
                        str.contains('Warner Bros')].groupby(['release_year'])['profit'].sum().sort_values(ascending=False)


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[50]:


answers['21'] = 'сентябрь' #'+'


data.release_date.dt.month.value_counts(ascending=False)


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[51]:


answers['22'] = 450 #'+'


data.release_date.dt.month.value_counts().loc[[6,7,8]].sum()


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[53]:


answers['23'] = 'Peter Jackson' #'+'


data_director_exploded[(data_director_exploded.release_date.dt.month == 1) 
                      | (data_director_exploded.release_date.dt.month == 2) 
                      | (data_director_exploded.release_date.dt.month == 12)]['director_list'].value_counts(ascending=False)


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[54]:


answers['24'] = 'Four By Two Productions' #'+'

#добавим столбец с данными о длине названия
data_companies_exploded['title_len']=data_companies_exploded.original_title.apply(lambda x: len(x))
data_companies_exploded.groupby(['production_companies_list'])['title_len'].mean().sort_values(ascending=False)


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[55]:


answers['25'] = 'Midnight Picture Show' #'+'

#добавим столбец с данными о длине описания по числу слов
data_companies_exploded['overview_len']=data_companies_exploded.overview.apply(lambda x: len(x.split()))
data_companies_exploded.groupby(['production_companies_list'])['overview_len'].mean().sort_values(ascending=False)


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[56]:


answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave' #'+'

#отберем из датафрейма строки с vote_average больше 99го персинтиля
data[data.vote_average > np.percentile(data['vote_average'], 99)][['original_title','vote_average']]


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# 

# In[61]:


answers['27'] = 'Daniel Radcliffe, Rupert Grint' #'+'


from itertools import combinations
#итератор сформирует уникальные  пары/кортежи из списка актеров по каждому фильму, список отсортирован по алфавиту при создании
##объекты  itertools сразу переводим в формат списков
data['cast_cortege'] = data.cast_list.apply(lambda x: list(combinations(x, 2))) 
#по спискам кортежей из всех строк 'cast_cortege' просчитаем суммарно частоту вхождений кортежа в список, выберем самые частые  
Counter(data['cast_cortege'].sum()).most_common(10)


# # Submission

# In[62]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[63]:


# и убедиться что ни чего не пропустил)
len(answers)


# In[ ]:





# In[ ]:




