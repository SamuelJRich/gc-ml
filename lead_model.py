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

