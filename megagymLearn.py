## This is for muscle group based exercise training, as well as intensity/training level. ##
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# df is dataframe
df = pd.read_csv("megaGymDataset.csv")

# .drop removes the respective columns, .dropna removes any rows that contain NaN within the data.
df = df.drop(columns=['Desc', 'Rating', 'RatingDesc'])
df = df.dropna()

#print("All types of:\n", df['Level'].unique())
print("50 rows:\n", df[2280:2290])