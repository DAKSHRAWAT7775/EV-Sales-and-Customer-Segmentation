from sklearn.cluster import KMeans
import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),"..")))
def cluster_data(df):
    # Use KMeans for clustering based on a subset of features
    kmeans = KMeans(n_clusters=3)  # Assuming we want 3 clusters
    cluster_features = df[['Feature1', 'Feature2']]  # Example features for clustering
    kmeans.fit(cluster_features)
    return kmeans

from sklearn.linear_model import LinearRegression

def predict_sales(df):
    # Train a regression model to predict sales quantity based on features
    X = df.drop(columns=['EV_Sales_Quantity'])
    y = df['EV_Sales_Quantity']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model
