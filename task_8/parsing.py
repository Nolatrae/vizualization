import requests
from bs4 import BeautifulSoup
import csv


# Функция для парсинга страницы и извлечения данных
def parse_page(url, data_source):
    # Отправляем GET-запрос к странице
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Извлекаем информацию
        info = soup.find('div', {'data-source': data_source})
        if info:
            value = info.find('div', class_='pi-data-value pi-font')
            if value:
                return value.get_text(strip=True)
            else:
                return None
        else:
            return None
    else:
        # Если запрос неудачен, выводим сообщение об ошибке
        print("Ошибка при получении страницы:", response.status_code)
        return None


# Функция для парсинга страницы персонажа и извлечения данных
def parse_character_page(url):
    # Парсим страницу и получаем данные о персонаже
    born = parse_page(url, 'born')
    species = parse_page(url, 'species')
    skin_color = parse_page(url, 'skin color')
    height = parse_page(url, 'height')
    occupation = parse_page(url, 'occupation')  # Добавляем парсинг для столбца occupation

    return born, species, skin_color, height, occupation  # Возвращаем дополнительное значение


# Функция для парсинга страницы и извлечения данных о персонажах
def parse_characters(url):
    # Отправляем GET-запрос к странице
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Находим все ссылки с атрибутом class="category-page__member-link"
        links = soup.find_all('a', class_='category-page__member-link')

        # Создаем список для хранения данных
        data = []

        # Инициализируем индекс персонажа
        index = 1

        # Проходимся по найденным ссылкам
        for link in links:
            # Получаем имя персонажа из атрибута title
            character_name = link.get('title')

            # Проверяем, не содержит ли имя персонажа подстроку "Category:"
            if 'Category:' not in character_name:
                # Получаем ссылку на персонажа из атрибута href
                character_link = 'https://intothespiderverse.fandom.com' + link.get('href')
                # Парсим страницу персонажа и извлекаем данные
                born, species, skin_color, height, occupation = parse_character_page(character_link)  # Обновляем вызов функции
                # Выводим информацию о персонаже
                print("Имя персонажа:", character_name)
                print("Ссылка на персонажа:", character_link)
                print("Дата рождения:", born)
                print("Вид:", species)
                print("Цвет кожи:", skin_color)
                print("Рост:", height)
                print("Профессия:", occupation)
                print("--------------------------------")
                # Добавляем данные в список
                data.append([index, character_name, character_link, born, species, skin_color, height, occupation])  # Обновляем список
                # Увеличиваем индекс персонажа
                index += 1

        return data
    else:
        # Если запрос неудачен, выводим сообщение об ошибке
        print("Ошибка при получении страницы:", response.status_code)
        return None


# Функция для сохранения данных в CSV-файл
def save_to_csv(data, filename):
    # Открываем файл для записи данных
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        # Создаем объект writer
        writer = csv.writer(file)
        # Записываем заголовки столбцов
        writer.writerow(['Index', 'Имя персонажа', 'Ссылка', 'Дата рождения', 'Вид', 'Цвет кожи', 'Рост', 'Профессия'])  # Обновляем заголовки
        # Записываем данные
        writer.writerows(data)
    print("Данные успешно сохранены в", filename)


# URL страницы для парсинга
url = 'https://intothespiderverse.fandom.com/wiki/Category:Characters'

# Парсим страницу и получаем данные о персонажах
parsed_data = parse_characters(url)

if parsed_data:
    # Сохраняем данные в CSV-файл
    save_to_csv(parsed_data, 'characters.csv')
