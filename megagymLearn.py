## This is for muscle group based exercise training, as well as intensity/training level. ##
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

## This is for muscle group based exercise training, as well as intensity/training level.

# df is dataframe

df = pd.read_csv("megaGymDataset.csv")

print(df.head())

