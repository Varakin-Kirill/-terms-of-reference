import pandas as pd

data = {
    'Отдел': [1, 1, 2, 3, 1, 3],
    'Сотрудник': [1, 2, 3, 6, 7, 6]
}

df = pd.DataFrame(data)

df['Cnt'] = df.groupby('Отдел')['Сотрудник'].transform('nunique')

print(df)
