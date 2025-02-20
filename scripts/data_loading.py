import pandas as pd
import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),"..")))

def load_data():
    # Adjust these file paths as per your file locations
    ev_sales_df = pd.read_csv('path_to_data/EV Sales and Customer Segmentation.csv')
    return ev_sales_df
