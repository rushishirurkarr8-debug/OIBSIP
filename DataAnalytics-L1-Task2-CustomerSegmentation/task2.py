import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# ==========================================
# 1. LOAD DATASET
# ==========================================

file_path = "dataset/online_retail.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())


# ==========================================
# 2. DATA CLEANING
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

# Remove customers with missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove cancelled/negative transactions
df = df[df["Quantity"] > 0]

# Remove invalid prices
df = df[df["UnitPrice"] > 0]

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Calculate total purchase amount
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

print("\nCleaned Dataset Shape:", df.shape)


# ==========================================
# 3. RFM ANALYSIS
# ==========================================

reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

rfm = df.groupby("CustomerID").agg({

    "InvoiceDate": lambda x:
        (reference_date - x.max()).days,

    "InvoiceNo": "nunique",

    "TotalAmount": "sum"
})

# Rename columns
rfm.columns = [
    "Recency",
    "Frequency",
    "Monetary"
]

print("\nRFM Analysis:")
print(rfm.head())


# ==========================================
# 4. REMOVE EXTREME OUTLIERS
# ==========================================

for column in ["Recency", "Frequency", "Monetary"]:

    lower = rfm[column].quantile(0.01)
    upper = rfm[column].quantile(0.99)

    rfm = rfm[
        (rfm[column] >= lower) &
        (rfm[column] <= upper)
    ]

print("\nRFM Shape after outlier removal:", rfm.shape)


# ==========================================
# 5. STANDARDIZATION
# ==========================================

scaler = StandardScaler()

rfm_scaled = scaler.fit_transform(rfm)

print("\nRFM data standardized successfully!")


# ==========================================
# 6. ELBOW METHOD
# ==========================================

inertia = []

for k in range(2, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(rfm_scaled)

    inertia.append(model.inertia_)


plt.figure(figsize=(8, 5))

plt.plot(
    range(2, 11),
    inertia,
    marker="o"
)

plt.title("Elbow Method for Optimal Number of Clusters")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.grid(True)

plt.savefig(
    "output/elbow_method.png",
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 7. K-MEANS CLUSTERING
# ==========================================

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

print("\nK-Means clustering completed!")


# ==========================================
# 8. CLUSTER CUSTOMER COUNT
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=rfm,
    x="Cluster"
)

plt.title("Customer Count by Cluster")
plt.xlabel("Customer Cluster")
plt.ylabel("Number of Customers")

plt.savefig(
    "output/cluster_customer_count.png",
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 9. CLUSTER PROFILE
# ==========================================

cluster_profile = rfm.groupby(
    "Cluster"
)[
    ["Recency", "Frequency", "Monetary"]
].mean()

print("\nCluster Profiles:")
print(cluster_profile)


# ==========================================
# 10. CUSTOMER SEGMENT VISUALIZATION
# ==========================================

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=rfm,
    x="Frequency",
    y="Monetary",
    hue="Cluster",
    palette="viridis",
    s=80
)

plt.title(
    "Customer Segmentation - Frequency vs Monetary"
)

plt.xlabel("Purchase Frequency")
plt.ylabel("Monetary Value")

plt.savefig(
    "output/customer_segments.png",
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 11. SAVE CUSTOMER SEGMENTS
# ==========================================

rfm.to_csv(
    "output/customer_segments.csv"
)


# ==========================================
# 12. SAVE CLUSTER PROFILES
# ==========================================

cluster_profile.to_csv(
    "output/cluster_profiles.csv"
)


# ==========================================
# 13. FINAL MESSAGE
# ==========================================

print("\n==========================================")
print("CUSTOMER SEGMENTATION COMPLETED SUCCESSFULLY!")
print("==========================================")

print("\nOutput files created:")

print("1. elbow_method.png")
print("2. cluster_customer_count.png")
print("3. customer_segments.png")
print("4. customer_segments.csv")
print("5. cluster_profiles.csv")