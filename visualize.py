import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(df, x_col, y_col, cluster_col='Cluster'):
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=cluster_col, palette='Set2', ax=ax)
    ax.set_title("Cluster Visualization")
    return fig

def plot_elbow(elbow_df):
    fig, ax = plt.subplots()
    sns.lineplot(data=elbow_df, x='Clusters', y='WSS_Score', marker='o', ax=ax)
    ax.set_title("Elbow Plot (WSS vs Clusters)")
    return fig

def plot_silhouette(silhouette_df):
    fig, ax = plt.subplots()
    sns.lineplot(data=silhouette_df, x='Clusters', y='Silhouette_Score', marker='o', ax=ax)
    ax.set_title("Silhouette Score vs Clusters")
    return fig
