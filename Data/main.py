import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

# Print the first 5 rows of the DataFrame
print(df.head())

# Print the shape of the DataFrame (number of rows and columns)
print(df.shape)

# Print the column names of the DataFrame
print(df.columns)

# Print the descriptive statistics of the DataFrame
print(df.describe())

#Clean Data
df.drop_duplicates(inplace=True)

#Rename
df.rename(columns={
    "Name": "Title",
    "Year": "Publication Year",
    "User Rating": "Rating"
}, inplace=True)

#Convert data types
df["Price"] = df["Price"].astype(float)

#Analyze
author_counts = df['Author'].value_counts()
print(author_counts)

avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

#Export Result
author_counts.head(10).to_csv("bestsellers_with_categories_2022_03_27.csv")
avg_rating_by_genre.to_csv("bestsellers_with_categories_2022_03_27.csv")
