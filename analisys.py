import pandas as pd
data = {'city': ['kyiv', 'Lviv', 'Odessa'], 'sales': [1200, 950, 500]}
df = pd.DataFrame(data)
print("Продажі по містах (тимчасова версія)")
print(df)
print("Середнє значення", df['sales'].mean())