# Follow along: https://datagy.io/python-pivot-tables/

# Loading a Sample Pandas DataFrame
import openpyxl
import pandas as pd
df = pd.read_excel('https://github.com/datagy/mediumdata/raw/master/sample_pivot.xlsx', parse_dates=['Date'])
# print(df.head())

# # Creating your first Pandas pivot table
# pivot = pd.pivot_table(
#     data=df,
#     index='Region'
# )
# print(pivot)

# Aggreating Only A Single Column
# pivot = pd.pivot_table(
#     data=df,
#     index='Region',
#     values='Sales'
# )

# print(pivot)

# pivot = pd.pivot_table(
#     data=df,
#     index='Region',
#     aggfunc='sum'
# )

# print(pivot)

# Specify multiple aggregation methods
# pivot = pd.pivot_table(
#     data=df,
#     index='Region',
#     aggfunc=['mean', 'sum']
# )

# print(pivot)

# Specifying different aggregations per column 
# pivot = pd.pivot_table(
#     data=df,
#     index='Region',
#     aggfunc={'Sales': 'mean', 'Units': 'sum'}
# )

# print(pivot)

# Defining a custom function
# import numpy as np
# def mean_no_outliers(values):
#     no_outliers = values.quantile([0.1, 0.9])
#     mean = np.mean(no_outliers)
#     return mean


# # Specifying custom functions in a Pandas pivot table
# pivot = pd.pivot_table(
#     data=df,
#     index='Region',
#     aggfunc=['mean', mean_no_outliers],
#     values='Sales'
# )

# print(pivot)

# Adding Columns to Our Pandas Pivot Table
# pivot = pd.pivot_table(
#     data=df,
#     index='Region',
#     columns='Type',
#     values='Sales'
# )

# print(pivot)

# pivot = pd.pivot_table(
#     data=df,
#     index=['Region',df['Date'].dt.quarter],
#     columns='Type',
#     values='Sales'
# )

# print(pivot.head())

# # Accessing data in a multi-index pivot table
# print(pivot.loc[('East', 1), "Men's Clothing"])


# Adding totals to rows and columns
# pivot = pd.pivot_table(
#     data=df,
#     index='Region',
#     columns='Type',
#     values='Sales',
#     margins=True
# )

# print(pivot)

# # Renaming totals in a Pandas pivot table
# pivot = pd.pivot_table(
#     data=df,
#     index='Region',
#     columns='Type',
#     values='Sales',
#     margins=True,
#     margins_name='Total'
# )

# print(pivot)

# Adding and seeing missing data in a Pandas pivot table
import numpy as np
df.loc[(df['Region'] == 'East') & (df['Type'] == "Children's Clothing"), 'Sales'] = np.NaN

pivot = pd.pivot_table(
    data=df,
    index='Region',
    columns='Type',
    values='Sales',
)

print(pivot)

# Filling Missing Values in a Pandas Pivot Table
import numpy as np
df.loc[(df['Region'] == 'East') & (df['Type'] == "Children's Clothing"), 'Sales'] = np.NaN

pivot = pd.pivot_table(
    data=df,
    index='Region',
    columns='Type',
    values='Sales',
    fill_value=0
)

print(pivot)