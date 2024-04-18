import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv('characters.csv')

# Создание сводной таблицы с количеством персонажей для каждой пары цвета кожи и профессии
pivot_table = df.pivot_table(index='Профессия', columns='Вид', aggfunc='size', fill_value=0)

# Построение тепловой карты
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table, cmap='coolwarm', annot=True, fmt='d', linewidths=.5)
plt.title('Распределение профессий в зависимости от цвета кожи')
plt.xlabel('Цвет кожи')
plt.ylabel('Профессия')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()
