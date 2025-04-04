from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd

def apply_kmeans(df, features, n_clusters):
    kmodel = KMeans(n_clusters=n_clusters, random_state=42)
    kmodel.fit(df[features])
    df['Cluster'] = kmodel.labels_
    return df, kmodel

def get_elbow_data(df, features, k_range=range(2,11)):
    WCSS = []
    for k in k_range:
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(df[features])
        WCSS.append(model.inertia_)
    return pd.DataFrame({'Clusters': list(k_range), 'WSS_Score': WCSS})

def get_silhouette_data(df, features, k_range=range(2,11)):
    scores = []
    for k in k_range:
        model = KMeans(n_clusters=k, random_state=42)
        labels = model.fit_predict(df[features])
        score = silhouette_score(df[features], labels)
        scores.append(score)
    return pd.DataFrame({'Clusters': list(k_range), 'Silhouette_Score': scores})
