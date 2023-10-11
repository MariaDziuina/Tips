# Графики


###############
### SEABORN ###

# если исходные данные есть в формате data frame

# distribution плотность распределения
sns.set_theme(style="darkgrid")
tbl=intro_tbl[(intro_tbl['game_name']=='Ghosts')]
g = sns.displot(data=tbl, x="playtime", kde=True, binwidth=1, height=7, facet_kws=dict(margin_titles=True))
g.set(xlabel='Cutscene Time',
       ylabel='N Game Starts',
       title='Cutscene Time Distribution Ghosts')

# histplot гистограмма распределения
sns.histplot(data=abdf, x="Metric", hue="Sample")


# bar plot с доверительными интервалами
sns.set_theme(style="whitegrid")
tbl=intro_tbl[(intro_tbl['platform']=='Android')]
# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 10))
# Plot the total crashes
g = sns.barplot(x="child_age", y="playtime", data=tbl, palette="Set2")
g.set_xlabel("Child Age Group")
g.set_ylabel("Catscene Time") 
g.set_title("Android")


# горизонтальный boxplot 
from pylab import rcParams
rcParams['figure.figsize'] = 16, 15
sns.set_theme(style="ticks", palette="pastel")
# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="loading_time", y="game_name", orient="h"
            , data=loading_time_all_events_and_games)
sns.despine(offset=10, trim=True)


# boxplot с точками для каждого наблюдения
f, ax = plt.subplots(figsize=(7, 6))
ax.set_xscale("linear")
sns.boxplot(x="Metric", y="Sample", data=abdf,
            whis=[0, 100], width=.6, palette="vlag")
sns.stripplot(x="Metric", y="Sample", data=abdf,
              size=4, color=".3", linewidth=0)
# Tweak the visual presentation
ax.xaxis.grid(True)
sns.despine(trim=True, left=True)


# Линейный график c гистограммой
import seaborn as sns
sns.set_theme(style="darkgrid")

def game_place_plt(game):
    df=game_table(game)
    fig, ax = plt.subplots(figsize=(15, 8))
    # Plot the responses for different events and regions
    ax = sns.lineplot(x='date', y='place',
                 data=df, markers=True, dashes=False)
    ax2 = ax.twinx()
    ax2.bar('date', 'players', data=df, color="green", alpha = 0.2)
    ax.set_xticks(df['date'])
    ax.set_ylim(ymin=0, ymax=40)
    ax.invert_yaxis()
    ax.set(title=game + ' ' + 'Place Dynamic')
    # считаем стандартное отклонение
    return np.around(np.std(df['rating']),decimals=2)




##################
### MATPLOTLIB ###

# линейный график с областью доверительного интервала 
def level_interest_plot(df, title):
    from pylab import rcParams
    rcParams['figure.figsize'] = 15, 10

    df['int']=df[['total_starts', 'share_rem']].apply(lambda x: interval_binom(x[0], x[1], 0.90), axis=1)
    df['high']=df['share_rem']+df['int']
    df['low']=df['share_rem']-df['int']

    ax = df[['share_rem']].plot(marker='o',
                                 label='share_rem',
                                 title=title,
                                 colormap='tab10',
                                 markersize=0)
    x_ticks = df.index
    ax.fill_between(df.index,
                    df['low'],
                    df['high'],
                    color='b',
                    alpha=.2,
                    lw=0,
                    label='interval')
    ax.set_xticks(x_ticks)
    ax.set_ylim(ymin=0, ymax=1)
    ax.legend()


######
# plotly
# линейный график с дов.интервалами

import plotly.graph_objects as go

df['conf_int_min'] = df['value'] - 2 * np.sqrt(df['value'] * (1 - df['value']) / df['auths'])
df['conf_int_max'] = df['value'] + 2 * np.sqrt(df['value'] * (1 - df['value']) / df['auths'])

fig = px.line(df, x="dt", y="value", title="Динамика конверсии с доверительным интервалом", color = 'ab_target')
fig.add_trace(
    go.Scatter(
        x=df.query("ab_target == 'exp_65_group_1'")["dt"].tolist() + df.query("ab_target == 'exp_65_group_1'")["dt"].tolist()[::-1],
        y=df.query("ab_target == 'exp_65_group_1'")["conf_int_min"].tolist() 
            + df.query("ab_target == 'exp_65_group_1'")["conf_int_max"].tolist()[::-1],
        fill='toself',
        fillcolor='rgba(0, 117, 255, 0.1)',
        line=dict(color='rgba(255, 255, 255, 0)'),
        name="Доверительный интервал"
    )
)

fig.add_trace(
    go.Scatter(
        x=df.query("ab_target == 'exp_65_group_2'")["dt"].tolist() + df.query("ab_target == 'exp_65_group_2'")["dt"].tolist()[::-1],
        y=df.query("ab_target == 'exp_65_group_2'")["conf_int_min"].tolist() 
            + df.query("ab_target == 'exp_65_group_2'")["conf_int_max"].tolist()[::-1],
        fill='toself',
        fillcolor='rgba(255, 0, 0, 0.1)',
        line=dict(color='rgba(255, 0, 0, 0)'),
        name="Доверительный интервал"
    )
)

fig.update_layout(hovermode = 'x')
fig.show()




###################
### ОБЛАКО СЛОВ ###

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





#############################
### ВИДЕО АНИМАЦИЯ ГРАФИК ###

# BAR RACING
import plotly.express as px
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
init_notebook_mode(connected=True)

g['event_date']=g['event_date'].astype('str')
g=g.sort_values(by='victory_share')
fig = px.bar(g, y="game_name", x="victory_share", color="victory_share", orientation='h',
  animation_frame="event_date", animation_group="game_name")
fig.layout.update(title_text="Victory share in days",title_font_size=30)
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 10000
fig.write_html("animation_001.html")
fig.show()

