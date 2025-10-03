# Netflix Data Analysis Project
# Author: Your Name
# Description: Basic EDA using Pandas & Matplotlib with cleaned date handling

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Step 1: Load the Dataset
# -------------------------------
df = pd.read_csv("netflix_titles.csv")

# -------------------------------
# Step 2: Basic Info
# -------------------------------
print("Dataset shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# -------------------------------
# Step 3: Clean 'date_added' Column
# -------------------------------
df['date_added'] = df['date_added'].astype(str).str.strip()  # remove spaces
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')  # convert, invalid dates become NaT
df['year_added'] = df['date_added'].dt.year  # extract year

# -------------------------------
# Step 4: Movies vs TV Shows
# -------------------------------
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type', palette='coolwarm')
plt.title("Movies vs TV Shows on Netflix")
plt.show()

# -------------------------------
# Step 5: Year-wise Content Added
# -------------------------------
plt.figure(figsize=(10,5))
df['year_added'].value_counts().sort_index().plot(kind='bar', color='green')
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

# -------------------------------
# Step 6: Top 10 Countries Producing Netflix Content
# -------------------------------
plt.figure(figsize=(10,5))
df['country'].value_counts().head(10).plot(kind='bar', color='purple')
plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()

# -------------------------------
# Step 7: Most Common Genres
# -------------------------------
plt.figure(figsize=(10,5))
df['listed_in'].value_counts().head(10).plot(kind='barh', color='orange')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.show()

# -------------------------------
# Optional: See rows with missing dates
# -------------------------------
missing_dates = df[df['date_added'].isna()][['title', 'date_added']]
if not missing_dates.empty:
    print("\nTitles with missing/invalid dates:")
    print(missing_dates)
