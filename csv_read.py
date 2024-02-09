print('start CSV uitlezen met pandas')
import pandas

df = pandas.read_csv('pokemon.csv')
# print(df['Name'])

for i, row in df.iterrows():
    print(row['Name'], 'Attack: ', row['Attack'])