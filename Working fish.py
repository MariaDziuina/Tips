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
