import streamlit as st
from data_loader import load_data
from clustering import apply_kmeans, get_elbow_data, get_silhouette_data
from visualize import plot_clusters, plot_elbow, plot_silhouette
from text_summary import generate_cluster_summary
import logging

# App settings
st.set_page_config(page_title="Customer Clustering", page_icon="🧠")
st.title("🛍️ Mall Customer Segmentation")
logging.basicConfig(level=logging.INFO)

# === Load Data ===
try:
    df = load_data()
except Exception as e:
    st.error(f"❌ Failed to load data: {e}")
    st.stop()

# === Feature Selection ===
st.subheader("1. Select Clustering Features")
features = st.multiselect("Choose features for clustering", options=['Age', 'Annual_Income', 'Spending_Score'], default=['Annual_Income', 'Spending_Score'])

if len(features) < 2:
    st.warning("Please select at least 2 features.")
    st.stop()

# === Cluster Selection ===
st.subheader("2. Choose Number of Clusters (K)")
k = st.slider("Number of Clusters", min_value=2, max_value=10, value=5)

# === Apply KMeans and Visualize ===
if st.button("Apply KMeans"):
    try:
        df_clustered, model = apply_kmeans(df.copy(), features, k)
        st.success("✅ Clustering applied successfully!")

        st.subheader("📊 Cluster Visualization")
        fig = plot_clusters(df_clustered, features[0], features[1])
        st.pyplot(fig)

        st.subheader("📋 Cluster Summary")
        summaries = generate_cluster_summary(df_clustered, features)
        for summary in summaries:
            st.markdown(summary)
            st.markdown("---")

    except Exception as e:
        st.error(f"⚠️ Error during clustering: {e}")

# === Optional Plots ===
st.subheader("3. 📉 Elbow Method & Silhouette Score")

if st.checkbox("Show Elbow Plot"):
    elbow_df = get_elbow_data(df, features)
    fig = plot_elbow(elbow_df)
    st.pyplot(fig)

if st.checkbox("Show Silhouette Score Plot"):
    silhouette_df = get_silhouette_data(df, features)
    fig = plot_silhouette(silhouette_df)
    st.pyplot(fig)
