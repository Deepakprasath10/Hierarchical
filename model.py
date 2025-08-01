import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

def cluster_energy_data(df, n_clusters):
    features = df.drop(['HouseholdID'], axis=1)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(features)

    clustering = AgglomerativeClustering(n_clusters=n_clusters, metric='euclidean', linkage='ward')
    df['Cluster'] = clustering.fit_predict(scaled_data)

    return df
