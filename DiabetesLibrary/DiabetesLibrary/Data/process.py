#block 1
import numpy as np
import pandas as pd
import os

# Load the data.

def read_data():
    return pd.read_csv('sample_diabetes_mellitus_data.xlsx', on_bad_lines=False)


#Remove those rows that contain NaN values in the columns: age, gender, ethnicity.
def remove_nan(df):
    subset = ['age', 'gender', 'ethnicity']
    for i in subset:
        df = df.dropna(subset=[i])
    return df


#Fill NaN with the mean value of the column in the columns: height, weight.
def fill_nan(df):
    subset = ['height', 'weight']
    for i in subset:
        df[i] = df[i].fillna(df[i].mean())
    return df


#Create a binary variable for gender M/F.
def binary_gender(df):
    df['gender'] = df['gender'].replace(['F'], 1)
    df['gender'] = df['gender'].replace(['M'], 0)
    df['female'] = df['gender']
    df.drop(['gender'], axis=1)
    return df


#Generate dummies for ethnicity column (One hot encoding).
def generate_dummies(df):
    s='ethnicity'
    df = pd.get_dummies(df, prefix = s)
    return df
