import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import seaborn as sns  # Импортируем seaborn

# Загрузка данных
df = pd.read_csv('characters.csv')

# Создание графиков
fig, axes = plt.subplots(nrows=2, ncols=2)

# График 1: Круговая диаграмма цвета кожи персонажей
skin_color_counts = df[df['Цвет кожи'] != 'None']['Цвет кожи'].value_counts(normalize=True) * 100
axes[0, 0].set(title='Соотношение цвета кожи персонажей')
axes[0, 0].pie(skin_color_counts, labels=skin_color_counts.index)

# График 2: Облако тегов профессий персонажей
wordcloud = WordCloud(background_color='black', colormap='spring', width=600, height=300,
                      prefer_horizontal=1, relative_scaling=0.6, collocations=False,
                      stopwords=STOPWORDS).generate(' '.join(df['Профессия'].fillna('')))
axes[0, 1].imshow(wordcloud, interpolation='bilinear')
axes[0, 1].set(title='Облако тегов профессий персонажей')
axes[0, 1].axis('off')

# График 3: Тепловая карта распределения профессий в зависимости от цвета кожи
pivot_table = df.pivot_table(index='Профессия', columns='Вид', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, cmap='coolwarm', annot=True, fmt='d', linewidths=.5, ax=axes[1, 0])
axes[1, 0].set(title='Распределение профессий в зависимости от цвета кожи')

# График 4: Гистограмма топ-10 видов персонажей
top_species = df['Вид'].value_counts().head(10)
top_species.plot(kind='bar', color='#8B0000', ax=axes[1, 1])
axes[1, 1].set(title='Топ-10 видов по количеству персонажей')

# Настройка стиля и размеров графиков
plt.rcParams['font.size'] = '12'
fig.set_facecolor('lightgray')
fig.set_figwidth(12)  # ширина Figure
fig.set_figheight(8)  # высота Figure

plt.tight_layout()
plt.show()
