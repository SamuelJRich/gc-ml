# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier


df = pd.read_csv('main_ds.csv')
print("Number of null values ", df.isnull().sum())


df = df.drop(columns=['Desc', 'Type', 'Level', 'Rating', 'RatingDesc' ])
df = df.drop(columns=['Unnamed: 0'])
print(df.head())

print("Number of null values ", df.isnull().sum())

df.dropna(inplace=True)
print("Number of null values ", df.isnull().sum())

# +

df.rename(columns={
    'Title': 'ExerciseName',
    'BodyPart': 'TargetMuscle',
}, inplace=True)

print(df.head())

# -

print(df.columns)

print("Number of null values ", df.isnull().sum())

# +
# See screenshot 'catboost results'

target_output = 'ExerciseName'
df.dropna(inplace=True)
X = df.drop(columns=[target_output])
y = df[target_output]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=30)


categorical = ['TargetMuscle', 'Equipment']

# Initialise CatBoost model
catboost_model = CatBoostClassifier(
    iterations=150,         # Number of boosting rounds
    depth=6,               # Depth of trees
    learning_rate=0.1,      # Learning rate
    cat_features=categorical,
    random_state=30,
    verbose=15,
    task_type='GPU', # Enables GPU Acceleration
    devices = [0] # Use the first available GPU (Index of 0)
)
