import pandas as pd
import matplotlib.pyplot as plt
from math import pi
from ipywidgets import interact, widgets

# Загрузка данных из CSV файла в DataFrame
df = pd.read_csv('characters.csv')


# Функция для создания радарного графика
def create_radar_chart(character1, character2):
    # Выбираем данные для указанных персонажей
    data = df[df['Имя персонажа'].isin([character1, character2])]
    data = data[['Имя персонажа', 'Рост', 'Дата рождения']]

    # Сортируем по столбцу 'Дата рождения', чтобы определить старшего персонажа
    data = data.sort_values(by='Дата рождения')

    # Определяем параметры для радарного графика
    categories = data['Имя персонажа']
    values = data['Рост']

    # Создаем фигуру и оси для радарного графика
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Вычисляем углы для каждой оси
    angles = [angle / len(categories) * 2 * pi for angle in range(len(categories))]
    angles += angles[:1]

    # Построение радарного графика для каждого персонажа
    for i, (character, values) in enumerate(zip(data['Имя персонажа'], data['Рост'])):
        # Значения должны быть представлены как список, дублирующий первое значение, чтобы создать замкнутую фигуру
        values = list(values)
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=character)

    # Добавляем легенду
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

    # Удаляем рамку
    ax.spines['polar'].set_visible(False)

    # Добавляем название графика
    plt.title('Характеристики персонажей в радарном графике', loc='center')

    # Отображаем график
    plt.show()


# Создаем список всех персонажей
all_characters = df['Имя персонажа'].unique()

# Создаем выпадающие списки для выбора персонажей
character1_dropdown = widgets.Dropdown(options=all_characters, description='Персонаж 1:')
character2_dropdown = widgets.Dropdown(options=all_characters, description='Персонаж 2:')

# Создаем интерактивную форму для выбора персонажей и отображения радарного графика
interact(create_radar_chart, character1=character1_dropdown, character2=character2_dropdown);
