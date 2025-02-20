import matplotlib.pyplot as plt
import seaborn as sns

import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),"..")))

def plot_sales(df):
    # Plotting EV Sales by Year
    sales_by_year = df.groupby('Year')['EV_Sales_Quantity'].sum()
    sns.lineplot(x=sales_by_year.index, y=sales_by_year.values)
    plt.title('EV Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Total Sales')
    plt.show()

def plot_vehicle_classification(df):
    # Plotting vehicle classification
    sns.countplot(x='Vehicle_Class', data=df)
    plt.title('Distribution of Vehicle Class')
    plt.xlabel('Vehicle Class')
    plt.ylabel('Count')
    plt.show()
