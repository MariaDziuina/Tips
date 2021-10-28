# Графики


###############
### SEABORN ###

# distribution
sns.set_theme(style="darkgrid")
tbl=intro_tbl[(intro_tbl['game_name']=='Ghosts')]
g = sns.displot(data=tbl, x="playtime", kde=True, binwidth=1, height=7, facet_kws=dict(margin_titles=True))
g.set(xlabel='Cutscene Time',
       ylabel='N Game Starts',
       title='Cutscene Time Distribution Ghosts')





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
g['event_date']=g['event_date'].astype('str')
g=g.sort_values(by='victory_share')
fig = px.bar(g, y="game_name", x="victory_share", color="victory_share", orientation='h',
  animation_frame="event_date", animation_group="game_name")
fig.layout.update(title_text="Victory share in days",title_font_size=30)
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 10000
fig.write_html("animation_001.html")
fig.show()

