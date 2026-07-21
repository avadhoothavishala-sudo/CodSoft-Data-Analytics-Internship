## to load the datset
import pandas as pd
df = pd.read_csv("titanic-dataset.csv")

## to view the dataset
print(df.head())

## to know the dataset
df.info()

## to identify where the missing values are present 
print(df.isnull().sum())

## Handling Missing values
## Fill missing age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

## to check, after replacing values with median can we find any null values or not
print(df["Age"].isnull().sum())

## Drop Cabin column due to a larger number of missing values
df.drop(columns=["Cabin"], inplace=True)

## Fill missing age values with most frequent values
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save the cleaned dataset
df.to_csv("cleaned_titanic_dataset.csv", index=False)

print("Cleaned dataset saved successfully!")


