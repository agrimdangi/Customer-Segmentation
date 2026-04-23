```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os


if not os.path.exists("output"):
    os.makedirs("output")


df = pd.read_csv("data/customers.csv")

print("\n📌 Data Preview:")
print(df.head())


X = df[["Annual Income", "Spending Score"]]


wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)


plt.figure()
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.savefig("output/elbow.png")


kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X)


df["Cluster"] = y_kmeans


plt.figure()

plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y_kmeans)
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            s=200, marker='X')

plt.title("Customer Segmentation")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")

plt.savefig("output/clusters.png")


df.to_csv("output/segmented_customers.csv", index=False)

print("\n✅ Clustering complete!")
print("📊 Charts saved in 'output/' folder")
print("📄 Segmented data saved as CSV")


print("\n🔍 Cluster Summary:")
print(df.groupby("Cluster")[["Annual Income", "Spending Score"]].mean())
```
