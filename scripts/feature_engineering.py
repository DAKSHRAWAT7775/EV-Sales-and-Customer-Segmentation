from sklearn.model_selection import train_test_split
import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),"..")))
def preprocess_data(df):
    # Handle missing values, scaling, etc.
    df.dropna(subset=['EV_Sales_Quantity'], inplace=True)  # Example: Drop rows with missing sales quantity
    df['Year'] = df['Year'].astype(str)  # Example: Make sure 'Year' is in string format
    df = pd.get_dummies(df, columns=['Vehicle_Class', 'Vehicle_Type'])  # Example: Encoding categorical data
    return df
