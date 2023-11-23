import numpy as np 
import pandas as pd 
from scipy import stats
from pandas.core.base import duplicated
import matplotlib.pyplot as plt 
import seaborn as sns 



def categorical_univariate(data, column):
    # Countplot
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x=column)
    plt.title(f'Countplot of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

  

    # Pie chart
    plt.figure(figsize=(8, 6))
    data[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title(f'Pie Chart of {column}')
    plt.ylabel('')
    plt.show()


def categorical_bivariate(data, x_column, y_column):
    # Bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x=x_column, y=y_column)
    plt.title(f'Bar Chart: {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.xticks(rotation=45)
    plt.show()

    # Box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x=x_column, y=y_column)
    plt.title(f'Box Plot: {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.xticks(rotation=45)
    plt.show()