import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv('characters.csv')

# Подсчет количества персонажей по видам и выбор топ-10
top_species = df['Вид'].value_counts().head(10)
total = top_species.sum()

# Построение черной диаграммы с темно-красными столбцами
plt.figure(figsize=(12, 6))
plt.gcf().set_facecolor('black')  # Задний фон черный
bars = plt.bar(top_species.index, top_species, color='#8B0000')  # Темно-красный цвет

# Изменение цвета текста на белый
plt.ylabel('Количество персонажей', color='white')
plt.title(f'Топ-10 видов по количеству персонажей', color='white')

# Добавление текста с общим количеством и процентным соотношением
ax = plt.gca()

for i, v in enumerate(top_species):
    ax.text(i, v * 1.05, f'{v}\n({v / total * 100:.1f} %)', ha='center', color='white')

# Установка максимального значения по оси y
plt.ylim([0, max(top_species) * 1.2])

# Удаление рамки у графика
ax.set(frame_on=False)

# Поворот подписей по оси x для лучшей читаемости
plt.xticks(rotation=45, ha='right', color='white')
ax.text(-0.25, 135, f'Всего: {total} (100%)', color='white')
plt.show()
