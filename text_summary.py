def generate_cluster_summary(df, features, cluster_col='Cluster'):
    summaries = []
    for cluster in sorted(df[cluster_col].unique()):
        sub_df = df[df[cluster_col] == cluster]
        count = len(sub_df)
        summary = f"**Cluster {cluster}** has **{count}** customers.\n"

        for feature in features:
            avg = sub_df[feature].mean()
            summary += f"- Average {feature.replace('_', ' ')}: **{avg:.2f}**\n"

        summaries.append(summary)

    return summaries
