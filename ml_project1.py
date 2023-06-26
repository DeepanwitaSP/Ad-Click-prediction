# -*- coding: utf-8 -*-
"""ml project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WEdWTKwGxXohy_h_y_GfBaMkPaH4Q1gD
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

ad_df = pd.read_csv('advertising.csv')
ad_df.head()

ad_df.info()

from google.colab import drive
drive.mount('/content/drive')

ad_df.describe()

plt.figure(figsize=(8, 6))
s = sns.heatmap(ad_df.corr(),
                annot=True,
                cmap='RdBu',
                vmin=-1,
                vmax=1)
s.set_xticklabels(s.get_xticklabels(), rotation=90)
plt.title('Correlation Matrix')
plt.show()

plt.figure(figsize=(8,6))
sns.histplot(data=ad_df, x='Age', bins=20, kde=True, hue='Clicked on Ad')
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(10,8))
plt.figure(figsize=(12, 8))
sns.histplot(data=ad_df, x='Daily Time Spent on Site', bins=20, kde=True, hue='Clicked on Ad', ax=axs[0])
sns.histplot(data=ad_df, x='Daily Internet Usage', bins=20, kde=True, hue='Clicked on Ad', ax=axs[1])

plt.show()

#fig, axs = plt.subplots(1, 2, figsize=(12, 8))
plt.figure(figsize=(12, 8))
sns.histplot(data=ad_df, x='Daily Internet Usage', bins=20, kde=True, hue='Clicked on Ad')
plt.show()

X = ad_df.drop(labels=['Ad Topic Line','City','Country','Timestamp','Clicked on Ad'], axis=1)
y = ad_df['Clicked on Ad']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state = 42)
lr_model = LogisticRegression(solver='lbfgs', max_iter=100)
lr_model.fit(X_train, y_train)

lr_predict = lr_model.predict(X_test)

print(classification_report(y_test, lr_predict))

print(accuracy_score(lr_predict, y_test)*100)

customer_data = {
    'Daily Time Spent on Site': 68.0,
    'Age': 49,
    'Area Income': 29000.94,
    'Daily Internet Usage': 143.81,
    'Male': 1
}

customer_df = pd.DataFrame([customer_data])
prediction = lr_model.predict(customer_df)
print(prediction)
if prediction[0] == 1:
    print("The customer is predicted to click on the ad.")
else:
    print("The customer is predicted not to click on the ad.")
