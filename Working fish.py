# coding: utf-8
# наше всё
import numpy as np
import pandas as pd

import seaborn as sns
import datetime

#настройки pandas, с которыми лучше почти всегда
pd.set_option('display.max_rows', 45000)
pd.set_option('display.max_columns', 50000)
pd.set_option('display.max_colwidth', 5000)

# добавить папку с собственными библиотеками (если они у тебя есть)
import sys
# ддя windows
sys.path.append('C:\\Users\\Maria\\Documents\\Python\\analytics')
sys.path.append('C:\\Users\\marii\\Documents\\Python\\analytics')



# собственные библиотеки
from data_load import *

from pylab import rcParams
rcParams['figure.figsize'] = 12, 9

%load_ext jupyternotify





###############################################################
### РАБОТА С ВНЕШНИМИ ИСТОЧНИКАМИ ДАННЫХ, ЗАГРУЗКА И СОХРАНЕНИЕ

### google tables
# забираем данные из google doc
games_params=gd.read('1o0DP_VYgpt3RRsFr5CTE3kq_A1zs80iyyDIBnm8HpyM', "Games!A2:ZZ500")
cols=gd.read('1o0DP_VYgpt3RRsFr5CTE3kq_A1zs80iyyDIBnm8HpyM', "Games!A1:ZZ1")
games_params.columns=cols.values[0]

# заливка в гугл док
url='1qg2qghHUggPFhRBVq1vtXobBJDNPdSHAbeknVSMpo4g'
gd.write(url, "A_technical!A2:ZZ5000", a_df)
gd.write(url, "B_gd!A2:ZZ5000", b_df)
gd.write(url, "C_prod!A2:ZZ5000", c_df)


# Загрузка csv
coh_a.to_csv('coh_a.csv', index=False)


# заливка в sql
engine=get_engine()
games_params.to_sql('game_params', con=engine, if_exists='replace', index=False, schema='dash')


### работа с файлами ###
# чтение текстового файла
with open('text.txt', 'r') as f:
    key = f.read()
# пример    
winrate = execute_clickhouse_query(open('query.sql').read().format('2022-03-01', '2022-04-10', 'show_conditions'))
print('В итоговом датафрейме {} строк'.format(winrate.shape[0]))
winrate.name = 'winrate'
display(winrate.info())
display(winrate.head(4))
    
# запись переменной в файл
txt='New string'
with open('readme.md', 'w') as f:
    f.write(txt)
    f.close()
    
# запись в json
import json
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

# json to dataframe
# чтение json файла
import json
js = json.loads(strng)
df=pd.DataFrame(js)


################################
### Работа с NaN, null, NULL ###

# фильтр на null
df=df[(pd.isnull(df['field'])==False)]

# исключить нули null
df_vals = df_vals[~df_vals['education'].isnull()] 

# посчитать количество NA в каждом столбце
df.isna().sum()

# Работа с NULL
df['event_time']=df['event_time'].fillna('Unknown')

# считаем доли нулей в столбцах
df_join.isnull().mean()


################################
### PANDAS DATA FRAMES DF ###

# формат данных
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.display.float_format = '${:,.2f}'.format
df['cost'] = df['cost'].map('${:,.2f}'.format)

${:,.2f}  = $100.00
{:,.2f}% = 27.23% и вроде можно так {:,.2f%} = 27.23%
${:,.2f} = $10,000.00


### multi-index мультииндексы ###
# удалить второй уровень индекса столбцов 
pv.columns = pv.columns.droplevel(1)
# строк
df2.index = df2.index.droplevel(1)

# объединить индексы столбцов
pv.columns = pv.columns.map('|'.join).str.strip('|')

# Отображать все колонки в таблицах
pd.set_option('display.max_columns', None)

# добавить бинарный признак
df['Many_service_calls'] = (df['Customer service calls'] > 3).astype('int')


### DATAFRAME ###

# Информация о data frame
print(df.info())

# сводная статистика по df
df.describe()

# процентное измение
users=users.sort_values(by = ['subscription_type', 'month_']).reset_index(drop=True)
users['Percentage_Change'] = users['user_id'].pct_change().round(3)*100

# быстро получить данные среднего по дням и сделать график
sl_dyn = sessions_df.groupby(['Room', 'Date']).mean()[['SessionLengthMinutes']].reset_index()
sns.lineplot(data=sl_dyn, 
             x='Date', 
             y='SessionLengthMinutes', 
             hue='Room')
gg = plt.xticks(rotation=45)


# убираем тех, кто пришел менее недели назад
# взять сегодняшнюю дату
from datetime import date, timedelta
tbl0=tbl0[(tbl0['FirstGameTime']<=(date.today()-pd.DateOffset(7)))]


#преобразование типа данных в таблице
df['fd_starts']=df['fd_starts'].astype('float')
df['user_id']=df['user_id'].astype('Int64')
df['first_pur_date'] = pd.to_datetime(df['first_pur_date'])


 # убираем дубликаты
  df=df[['user_id', 'first_pur_date', 'platform']].drop_duplicates()

# поиск дубликатов дублирующиеся строки
duplicateRowsDF = timespend[timespend.duplicated(['user_id', 'app_instance_orig'])]
duplicateRowsDF=duplicateRowsDF.sort_values(by=['user_id', 'app_instance_orig', 'timespend']
                                           ).reset_index(drop=True)
len(duplicateRowsDF)


# переименование столбцов
df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)

# задать название столбцам
df2 = df.set_axis(['user_id', 'group'], axis=1)

# cчитаем кол-во уникальных значений
tbl['PlayerID'].nunique()

# смена формата данных для pandas
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.display.float_format = '${:,.2f}'.format
df['cost'] = df['cost'].map('${:,.2f}'.format)

# cмена индекса
prs=prf.sort_values(by=['game_time'], 
                  ascending=[True]).reset_index()
prs['index']=prs.index

# выбрать столбцы по номерам (до второго, т.е. 0 и 1)
df1 = df.iloc[:, 0:2]

# фильтр по multiply values несколько значений переменной
cash_types=['NL', 'PLO5', 'PLO', 'MTT']
Cash=tbl[tbl['GameType'].isin(cash_types)]

#группировка и подсчет количества юзеров
g=df.groupby(['f1', 'f2']).agg(
                {
                    'id': lambda x: x.nunique(),
                    'revenue': np.sum
                }).reset_index().sort_values(by='id', ascending=False)

# группировка по какому-то признаку и вывод основных статистик
columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']
df.groupby(['Churn'])[columns_to_show].describe(percentiles=[])

# еще один вариант группировки с выводом определенных статистик
columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']
df.groupby(['Churn'])[columns_to_show].agg([np.mean, np.std, np.min, np.max])

# еще один вариант сгруппировать данные
top_3_revenue = (
    df_sales_detail
    .groupby('good')['price'].sum()
    .sort_values()[-3:].index.tolist()
)

# соединяем два data frames
# параметр для merge, который проще скопировать, чем написать без ошибок
res=df1.merge(df2, 'left', on='device_id', suffixes=('_lft', '_rght'))


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



# сортировка
gt=gt.sort_values(by=['event_number',
                      'platform'], 
                  ascending=[True, False])

# Заменить значения в столбце
dig["level"] = dig["level"].str.replace('Tutorial', '0')

# задать условия на замену нескольких значений в столбце
d = {'No' : False, 'Yes' : True}
df['International plan'] = df['International plan'].map(d)
df.head()


### ТАБЛИЦЫ СОПРЯЖЕННОСТИ ###

pd.crosstab(df['Churn'], df['International plan'])
# либо
pd.crosstab(df['Churn'], df['Voice mail plan'], normalize=True)


### СВОДНЫЕ ТАБЛИЦЫ PIVOT ###

# максимум параметров для pivot сводная таблица
pv=df.pivot_table(index='date', columns='dd', values='revenue', aggfunc=np.sum).fillna(0).cumsum(axis=1).reset_index()





### СОЗДАНИЕ НОВЫХ ПЕРЕМЕННЫХ ###

#рассчет доли и создание нового столбца на основе двух
gt['share']=gt['user_id']/gt['user_id_total']

# создаем переменную по нескольким условиям результатам сравнения
conditions = [ (comp['Exception_share_old']>comp['Exception_share']) & (comp['_merge'].eq('both')),
              (comp['Exception_share_old']<=comp['Exception_share']) & (comp['_merge'].eq('both')),
              comp['_merge'].eq('left_only'),
              comp['_merge'].eq('right_only')   
]
choices = ['got better', 'same situation', 'new exception', 'good']
comp['Conclusion']=np.select(conditions, choices, default='no')
comp=comp[['Platform', 'Exception', 'Exception_share', 'Exception_share_old', 'Conclusion']]


# Преобразование столбца df в список (list)
ages_df=prf[['child_age']].sort_values( by = ['child_age'], ascending=[True]).drop_duplicates()
ages=ages_df['child_age'].to_list()

# mean
Cash_then_MTT_agg=Cash_then_MTT_daily.groupby(['PlayerID', 'IsTournament', 'IsCashAfterMTT']).agg(
                {'GameID': lambda x: x.mean()
                }).reset_index()


# расчет доли по таблице
# пример:
fg_p=tbl0.groupby(['FirstGameType']).agg(
                {
                    'PlayerID': lambda x: x.nunique()
                }).reset_index()
# если не сработает, то добавить np.sum(fg_p['PlayerID'], axis=1). 
# Это означает, что он будет делать это по столбцам, а не  построчкам( по строчкам = 0)
fg_p['Share']=fg_p['PlayerID']/np.sum(fg_p['PlayerID'])
fg_p




###############################
### ПРОЧИЕ ПОЛЕЗНЫЕ ФУНКЦИИ ###


# создание таблицы в цикле
 paths=[]
for user in user_list:
    table=get_usertable(df=ds, user=user)
    paths.append(get_path(table))

  
#функция, которая создает таблицы для каждого юзера с определенными фильтрами
def get_usertable(df, user):
    table=df[(df['is_game_start']==1)&
        (df['event_number']<=5)&
        (df['user_id']==user)]
    return table

  
#функция, которая создает список из пользовательских путей, как элементов списка 
def get_path(df):
    result=''
    df=df.sort_values(by='event_number')
    for game in df['game_name'].values:
        result=result+game+" - "
    #убираем три последних символа для того, чтобы полученная строка не заканчивалась на пробел-дефис-пробел
    return result[:-3]
 
  
 # функция которая выдает процентный интервал для выборки
def interval_binom(n, p, confidence):
    import scipy.stats
    import math
    # доверительный интервал биноминального распределения
    h = scipy.stats.t.interval(confidence, n-1, loc=0, scale=1)[1]*math.sqrt((p*(1-p))/n)
    return h


# функция, которая выдает нижнюю и верхнюю границу доверительного интервала биномиального
def interval_binom_boarders(s, n, confidence):
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    # доверительный интервал биноминального распределения
    b = sm.stats.proportion_confint(s, n, alpha=0.05, method='wilson')
    low = b[0]
    high= b[1]
    return print('нижняя граница {}%, верхняя граница {}%'.format(low, high))



# функция для расчета средневзвешенного
def w_avg(df, values, weights):
    d = df[values]
    w = df[weights]
    return (d * w).sum() / w.sum()


# функция для сравнения метрик до и после и проверка на стат. значимость
def get_metrics_and_signif(metrics, table, hue='IsExperiment', arg0=0, arg1=1
                           , sample0name='Before', sample1name='After'):
    
    sample0=table[(table[hue]==arg0)]
    sample1=table[(table[hue]==arg1)]
    
    lst=[]
    df1 = pd.DataFrame()
    s=table.reset_index().groupby(hue).agg({'index': lambda x: x.nunique()}).values
    pl=table.reset_index().groupby(hue).agg({'PlayerID': lambda x: x.nunique()}).values
    
    for i in metrics:
        m=table.groupby(hue).agg({i: lambda x: x.mean()}).values
        mw=st.mannwhitneyu(sample1[i], sample0[i], alternative='two-sided').pvalue
        tt=st.ttest_ind(sample1[i], sample0[i], alternative='two-sided').pvalue
        dif=m[1,0]-m[0,0]
        difp=100*(m[1,0]-m[0,0])/m[0,0]
        difp_abs=abs(100*(m[1,0]-m[0,0])/m[0,0])
        lst.append([i, m[0,0], m[1,0], dif, difp, difp_abs, mw, tt])

    df1=pd.DataFrame(lst, columns=['Metrics', sample0name, sample1name, 'Diff', 'Diff%', 'Diff%_abs', 'mw', 'tt']
                    ).sort_values(by=['mw', 'tt', 'Diff%_abs'], ascending=[True, True, False])
    
    new_row = {'Metrics':'SampleSize', sample0name: s[0,0], sample1name: s[1,0]}
    df1 = df1.append(new_row, ignore_index=True)
    new_row1 = {'Metrics':'Players', sample0name: pl[0,0], sample1name: pl[1,0]}
    df1 = df1.append(new_row1, ignore_index=True)


    conditions = [ (df1['mw']<0.1) & (df1['tt']<0.1) & (df1['Diff']>0),
                  (df1['mw']<0.1) & (df1['tt']<0.1) & (df1['Diff']<=0),
                  (df1['mw']>=0.1) & (df1['tt']<0.1),
                  (df1['mw']<0.1) & (df1['tt']>=0.1),
                  (df1['mw']>0.1) & (df1['tt']>0.1)
                ]
    choices = ['significantly raised', 'significantly reduce'
               , 'partially significant', 'partially significant'
               , 'not significant']
    df1['Conclusion']=np.select(conditions, choices, default='')
    df1=df1.drop(columns = ['Diff%_abs'],axis = 1)
    return df1




reset_index(drop=True)
multiindex level =0
value_counts(normalize=True)
value_counts(normalize=True).rename('HandCount')
value_counts(dropna=False)
unstack() vs pivot
to_frame()
notna()
draw_intervals
np.select


