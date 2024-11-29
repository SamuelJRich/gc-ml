## This is for muscle group based exercise training, as well as intensity/training level. ##
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier

# Read the csv data and store it as a DataFrame.
df = pd.read_csv("d1.csv")

print(df.isnull().sum())
# Drop the irrelevant columns that won't be required for the model.
df = df.drop(columns=['Desc', 'Rating', 'RatingDesc', 'Unnamed: 0'])

# This drops the rows where the data is equatable to NaN in 'Title', 'Equipment', and 'Level'.
df = df.dropna(subset=['Title', 'Equipment', 'Level'])

# Handle missing values in 'Level' before encoding (optional, as dropna already handles it)
mode_value = df['Level'].mode()[0]  # Get the most frequent value in 'Level'
df['Level'] = df['Level'].fillna(mode_value)  # Fill NaN values with the mode

# Check if there are any remaining NaN values and ensure the data type of 'Level' is correct
print("NaN values after filling 'Level':", df['Level'].isnull().sum())
print("Data types of columns:", df.dtypes)

# Inspect the 'Level' column to ensure it's ready for encoding
print("Unique values in 'Level' before encoding:", df['Level'].unique())

# Ensure no leading/trailing spaces or unexpected characters in the 'Level' column
df['Level'] = df['Level'].str.strip()

# Double check for any unexpected values
print("Unique values in 'Level' after cleaning:", df['Level'].unique())

# Encode any categorical data into numeric values, due to restraints of text data.
ohe = OneHotEncoder(sparse_output=False)
oe = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)  # Use -1 for unknown values

df_ohe = pd.DataFrame(ohe.fit_transform(df[['Type', 'BodyPart', 'Equipment']]), 
                      columns=ohe.get_feature_names_out(['Type', 'BodyPart', 'Equipment']))
print(f"Shape of df_ohe: {df_ohe.shape}")

df = pd.concat([df, df_ohe], axis=1).drop(columns=['Type', 'BodyPart', 'Equipment'])

# Now encode the 'Level' column (string values: 'Beginner', 'Intermediate', 'Expert')
df['Level'] = oe.fit_transform(df[['Level']])

# Check the encoded 'Level' values
print("Encoded Level values:", df['Level'].unique())

# Check for any NaN values in 'Level' after encoding
print("NaN values after encoding:")
print(df['Level'].isnull().sum())
