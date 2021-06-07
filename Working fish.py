# coding: utf-8
# наше всё
import numpy as np
import pandas as pd

#настройки pandas, с которыми лучше почти всегда
pd.set_option('display.max_rows', 45000)
pd.set_option('display.max_columns', 50000)
pd.set_option('display.max_colwidth', 5000)

# добавить папку с собственными библиотеками (если они у тебя есть)
import sys
# ддя windows
sys.path.append('C:\\Users\\analytic\\python\\')
sys.path.append('//home//roman//python//analytics//')
sys.path.append('C:\\Users\\Maria\\Documents\\Python\\analytics')
sys.path.append('C:\\Users\\marii\\Documents\\Python\\analytics')

# собственные библиотеки
# обмен с гуглдоки
# import ts_gd as gd
# получение из sql
from data_load import *

import seaborn as sns
import datetime

from pylab import rcParams
rcParams['figure.figsize'] = 12, 9

%load_ext jupyternotify


# google

# забираем данные из google doc


# заливка в гугл док



# Информация о data frame
print(df.info())

#преобразование в float
strg['fd_starts']=strg['fd_starts'].astype('float') 


#группировка и подсчет количества юзеров
gt=ds[(ds['is_game_start']==1)].groupby(['platform',
             'lang',
             'user_type', 
             'child_age', 
             'game_from', 
             'event_number',
             'game_name']).agg(
                {
                    'user_id': lambda x: x.nunique(),
                }).reset_index()
                
# соединяем два data frames
gt=gt.merge(gt2, 'left', on=['event_number',
                             'platform',
                             'lang',
                             'user_type', 
                             'child_age', 
                             'game_from'], 
                suffixes=('', '_total'))

#рассчет доли и создание нового столбца на основе двух
gt['share']=gt['user_id']/gt['user_id_total']

# сортировка
gt=gt.sort_values(by=['event_number',
                      'platform',
                      'lang',
                      'user_type', 
                      'child_age', 
                      'game_from'], 
                  ascending=[True, False, False, False, True, False])


# заливка в sql таблицу
engine=get_engine()
way.to_sql('games_order', con=engine, if_exists='replace')


# Подсказки Ромы
# работа с pandas
# все нормальные параметры для группировки
g=df.groupby(['f1', 'f2']).agg(
                {
                    'id': lambda x: x.nunique(),
                    'revenue': np.sum
                }).reset_index().sort_values(by='id', ascending=False)

# максимум параметров для pivot
pv=df.pivot_table(index='date', columns='dd', values='revenue', aggfunc=np.sum).fillna(0).cumsum(axis=1).reset_index()

# параметр для merge, который проще скопировать, чем написать без ошибок
res=df1.merge(df2, 'left', on='device_id', suffixes=('_lft', '_rght'))

# смена формата данных для pandas
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.display.float_format = '${:,.2f}'.format
df['cost'] = df['cost'].map('${:,.2f}'.format)


pd.pivot_table(games_prop['kind'], games_prop['time_to_win'])

# переименовываем колонку с названием игры
games['game_name']=games['game']
games=games.drop('game', 1)



# подготовка структуры данных для облака слов
# отправляет слова, которые встретили не менее n раз
def prep_gr_word_cloud(words_df, group, n):
    common=words_df[
        (words_df['words']>n)&
        (words_df['group']==group)&
        # загулшку остутсвия данных не выводим
        (words_df['index']!='no')&(words_df['index']!='info')
            ][['index', 'words']].set_index('index').to_dict()['words']
    return common

  
  # функция строит облако слов и сохраняет её в файл
# для работы нужно pip install wordcloud
# https://github.com/amueller/word_cloud
def write_cloud(dct, file):
    from wordcloud import WordCloud
    from matplotlib import pyplot as plt
    wc = WordCloud(width=2600, height=2200, background_color="black", relative_scaling=1.0,
               collocations=False, min_font_size=10).generate_from_frequencies(dict(dct))
    plt.axis("off")
    plt.figure(figsize=(9, 6))
    plt.imshow(wc, interpolation="bilinear")
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    plt.savefig(file, format="png")
#     plt.show()



# ГРАФИКИ






# Работа с NULL
tb_g['event_time']=tb_g['event_time'].fillna('Unknown')

panda is null


# Смена индекса
prs=prf.sort_values(by=['game_time'], 
                  ascending=[True]).reset_index()

prs['index']=prs.index


# Преобразование столбца df в список
ages_df=prf[['child_age']].sort_values( by = ['child_age'], ascending=[True]).drop_duplicates()
ages=ages_df['child_age'].to_list()
ages



 # Убираем дубликаты
  pl['platform']=pl['platform'].fillna('0')
  
  # убираем дубликаты
  main_df_user=main_df[(main_df['first_game_played']!='Not a game')][['user_id', 'first_pur_date', 'platform','lang','child_age',
                      'total_games', 'total_victories', 'total_exits', 'total_unfocuses'
                     ]].drop_duplicates()
  
  # Работа с NULL
  panda is null
  
  # Меняем тип данных
  pl['user_id']=pl['user_id'].astype('Int64')
  
  
  # Отладка соединения таблиц
  
  pur2.groupby(['_merge']).agg(
                {
                    'user_id': lambda x: x.nunique(),
                }).reset_index()
  
  t=pur2[(pur2['_merge']=='left_only')].groupby(['user_id']).agg(
                {
                    'transaction_time': lambda x: x.nunique(),
                }).reset_index()
  
  len(t[(t['transaction_time']>1)])
  
