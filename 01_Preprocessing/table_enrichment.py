import pandas as pd

data = pd.read_csv('diabetes_dataset.csv')

print(data)

data.info()
print(data.isnull().sum())
print(data.Glucose.sum())