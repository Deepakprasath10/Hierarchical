import matplotlib.pyplot as plt
import seaborn as sns
import os

def save_cluster_plot(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='AvgDailyUsage(kWh)', y='NightUsage(kWh)', hue='Cluster', palette='Set2', data=df)
    plt.title('Energy Consumption Clusters')
    plt.xlabel('Average Daily Usage (kWh)')
    plt.ylabel('Night Usage (kWh)')
    plt.legend(title='Cluster')
    plt.tight_layout()
    plt.savefig('static/cluster_plot.png')
    plt.close()
