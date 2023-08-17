import pandas as pd

# Follow along: https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/

# Create a data frame
# data = {
#     'apples': [3, 2, 0, 1], 
#     'oranges': [0, 3, 7, 2]
# }

# purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

# print(purchases)
# print(purchases.loc['June'])

# Read in Data (CSV)

# df = pd.read_csv('purchases.csv', index_col=0)

# print(df)

# Read in Data (JSON)
# df = pd.read_json('purchases.json')

# print(df)

#! Data Frame Operations===========================================================
movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")

# print(movies_df.head())
# print(movies_df.tail())
# print(movies_df.info())
# print(movies_df.shape)

# print(movies_df.columns)

movies_df.rename(columns={
        'Runtime (Minutes)': 'Runtime', 
        'Revenue (Millions)': 'Revenue_millions'
    }, inplace=True)

# print(movies_df.columns)

# print(movies_df.isnull())
# print(movies_df.isnull().sum())

# Imputation
# revenue = movies_df['Revenue_millions']
# revenue_mean = revenue.mean()
# print(revenue.mean())
# revenue.fillna(revenue_mean, inplace=True)
# print(movies_df.isnull().sum())
# print(movies_df.describe())
# print(movies_df['Genre'].value_counts().head(10))
# print(movies_df.corr())

# DataFrame slicing, selecting, extracting

# genre_col = movies_df['Genre']
# print(type(genre_col))

# prom = movies_df.loc["Prometheus"]
# prom = movies_df.iloc[1]

# print(prom)

# movie_subset = movies_df.loc['Prometheus':'Sing']

# movie_subset = movies_df.iloc[1:4]

# print(movie_subset)

# Conditional Selections

# condition = (movies_df['Director'] == "Ridley Scott")

# print(condition.head())

# print(movies_d f[movies_df['Director'] == "Ridley Scott"])

print(movies_df[movies_df['Rating'] >= 8.6].head(3))
print(movies_df[(movies_df['Director'] == 'Christopher Nolan') | (movies_df['Director'] == 'Ridley Scott')].head())

movies_df[
    ((movies_df['Year'] >= 2005) & (movies_df['Year'] <= 2010))
    & (movies_df['Rating'] > 8.0)
    & (movies_df['Revenue_millions'] < movies_df['Revenue_millions'].quantile(0.25))]

