import pandas as pd 

# Data Frame Object 
df = pd.read_csv('bestsellers.csv')

# Outputs Amazon's 50 Bestseller Books

print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())

df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
df["Price"] = df["Price"].astype(float)

# Outputs Authour Popularity
authour_counts = df['Author'].value_counts()
print(authour_counts)

# Outputs Average Rating by Genre 
avg_rating_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_genre)

# Export top 10 Authours and Average Rating by Genre to new .csv files 
authour_counts.head(10).to_csv("top_authours.csv")
avg_rating_genre.to_csv("avg_rating_genre.csv")