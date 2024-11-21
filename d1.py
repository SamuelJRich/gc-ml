## This is for muscle group based exercise training, as well as intensity/training level. ##
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder


# df is dataframe
df = pd.read_csv("d1.csv")

# .drop removes the respective columns, .dropna removes any rows that contain NaN within the data.
df = df.drop(columns=['Desc', 'Rating', 'RatingDesc'])
