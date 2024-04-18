import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

df = pd.read_csv('characters.csv')
#!!!обязательно устанавливаем collocations=False - игнорирование биграмм!!!
wordcloud = WordCloud(background_color='black', # цвет фона
                      colormap = 'spring',      # цветовая палитра
                      width = 600,
                      height = 300,
                      prefer_horizontal = 1,
                      relative_scaling  = 0.6,
                      collocations = False,     # рассматривает слова в отдельности
                      stopwords = STOPWORDS).generate(' '.join(df['Профессия'].fillna('')))

# Рисуем результат
plt.figure(figsize=(10,5))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()