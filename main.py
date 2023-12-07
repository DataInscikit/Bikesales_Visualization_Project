
#importing packages

import pandas as pd
import openpyxl

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

#reading excel file
df = pd.read_excel("/Users/lakshmi/Downloads/Excel Project Dataset.xlsx")
pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 1027)
pd.set_option('display.max_columns',15)
print(df.head(5))

#Deleting rows with na value and duplicate values
df = df.dropna()
df = df.drop_duplicates()

# Replacing values in Marital Status and Gender columns
df['Marital Status'] = df['Marital Status'].replace('M','Married')
df['Marital Status'] = df['Marital Status'].replace('S','Single')
df['Gender'] = df['Gender'].replace('M','Male')
df['Gender'] = df['Gender'].replace('F','Female')

# Creating new column 'Age Brackets' with age bins
bins = [-1,0,10,30,54,100]
labels = ['invalid', 'kid', 'adolescent', 'middle age', 'old']
df['Age Brackets'] = pd.cut(df['Age'], bins = bins, labels = labels, right = False)
print(df.head(5))

#correlation map of numeric variables
fig = plt.figure(figsize = (12,8 ))
Matrix = df.corr(method="pearson", numeric_only=True)
print(Matrix)
sns.heatmap(Matrix, annot=True, cmap='YlGnBu')
plt.show()

#bar plot showing gender and income per purchase

sns.barplot(x=df['Gender'], y=df['Income'], hue= df['Purchased Bike'], palette='YlGnBu',legend= True)
plt.title('Gender and Income of customers per purchase')
plt.xlabel('Gender')
plt.ylabel('Income')
plt.show()

#line plot showing bike purchase based on commute distance
sns.lineplot(x=df['Commute Distance'], y= df['Purchased Bike'], hue = df['Gender'], palette='YlGnBu',legend= True)
plt.title('Bike purchase based on commute distance and gender')
plt.xlabel('Commute distance')
plt.ylabel('Bike purchse count')
plt.show()

#bar plot showing Age brackets and income per purchase
sns.barplot(x=df['Age Brackets'], y= df['Income'], hue=df['Purchased Bike'], palette='YlGnBu',legend= True)
plt.title('Bike purchase based on Age brackets and Income')
plt.xlabel('Age Brackets')
plt.ylabel('Income')
plt.show()

#joint plot showing Income and Age distribution
sns.jointplot(x= df['Income'], y= df['Age'], data=df )
plt.title('Income and Age distribution ')
plt.xlabel('Income')
plt.ylabel('Age')
plt.show()

