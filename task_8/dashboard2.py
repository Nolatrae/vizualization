import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import seaborn as sns
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Загрузка данных
df = pd.read_csv('characters.csv')

# График 1: Круговая диаграмма цвета кожи персонажей
skin_color_counts = df[df['Цвет кожи'] != 'None']['Цвет кожи'].value_counts(normalize=True) * 100

fig1 = go.Figure(data=[go.Pie(labels=skin_color_counts.index, values=skin_color_counts, hole=0.3)])
fig1.update_layout(title='Соотношение цвета кожи персонажей', title_font_color='white', paper_bgcolor='black')

# График 2: Облако тегов профессий персонажей
wordcloud = WordCloud(background_color='black', colormap='spring', width=600, height=300,
                      prefer_horizontal=1, relative_scaling=0.6, collocations=False,
                      stopwords=STOPWORDS).generate(' '.join(df['Профессия'].fillna('')))

fig2 = go.Figure(go.Image(z=wordcloud.to_array()))
fig2.update_layout(title='Облако тегов профессий персонажей', title_font_color='white', paper_bgcolor='black')

# График 3: Тепловая карта распределения профессий в зависимости от цвета кожи
pivot_table = df.pivot_table(index='Профессия', columns='Вид', aggfunc='size', fill_value=0)
fig3 = go.Figure(data=go.Heatmap(z=pivot_table.values, x=pivot_table.columns, y=pivot_table.index,
                                  colorscale='RdBu', colorbar=dict(title='Количество')))
fig3.update_layout(title='Распределение профессий в зависимости от цвета кожи', title_font_color='white',
                   xaxis=dict(title='Цвет кожи', tickangle=45), yaxis=dict(title='Профессия'),
                   paper_bgcolor='black')

# График 4: Гистограмма топ-10 видов персонажей
top_species = df['Вид'].value_counts().head(10)
fig4 = go.Figure(data=[go.Bar(x=top_species.index, y=top_species, marker=dict(color='#8B0000'))])
fig4.update_layout(title='Топ-10 видов по количеству персонажей', title_font_color='white',
                   xaxis=dict(title='Вид'), yaxis=dict(title='Количество персонажей'),
                   paper_bgcolor='black')

# Объединение графиков в дашборд
fig = make_subplots(rows=2, cols=2, subplot_titles=['Облако тегов профессий персонажей',
                                                    'Распределение профессий в зависимости от цвета кожи',
                                                    'Топ-10 видов по количеству персонажей'])
fig.add_trace(fig2.data[0], row=1, col=1)
fig.add_trace(fig3.data[0], row=1, col=2)
fig.add_trace(fig4.data[0], row=2, col=1)

# Update layout
fig.update_layout(height=1080, width=1920, title_text="Дашборд персонажей", title_font_color='white',
                  plot_bgcolor='black', paper_bgcolor='black')
fig.show()

# Display pie chart separately
fig1.show()
