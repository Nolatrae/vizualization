import pandas as pd

# Загрузка данных из CSV файла в DataFrame
df = pd.read_csv('characters.csv')

# Вывод списка названий столбцов
print(df.columns)
