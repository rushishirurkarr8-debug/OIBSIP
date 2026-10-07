import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/retail_sales_dataset.csv")

print("========== DATASET INFORMATION ==========")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Create output folder
import os
os.makedirs("output", exist_ok=True)


# ==================================================
# 1. MONTHLY SALES TREND
# ==================================================

monthly_sales = df.groupby(
    df["Date"].dt.to_period("M")
)["Total Amount"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/monthly_sales_trend.png")
plt.close()


# ==================================================
# 2. SALES BY PRODUCT CATEGORY
# ==================================================

category_sales = df.groupby(
    "Product Category"
)["Total Amount"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/category_sales.png")
plt.close()


# ==================================================
# 3. SALES BY GENDER
# ==================================================

gender_sales = df.groupby(
    "Gender"
)["Total Amount"].sum()

plt.figure(figsize=(6, 5))
gender_sales.plot(kind="bar")
plt.title("Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/gender_sales.png")
plt.close()


# ==================================================
# 4. CORRELATION HEATMAP
# ==================================================

numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(8, 6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("output/correlation_heatmap.png")
plt.close()


# ==================================================
# 5. AGE GROUP ANALYSIS
# ==================================================

df["Age Group"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65"]
)

age_sales = df.groupby(
    "Age Group",
    observed=False
)["Total Amount"].sum()

plt.figure(figsize=(8, 5))
age_sales.plot(kind="bar")
plt.title("Sales by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/age_group_sales.png")
plt.close()


# ==================================================
# 6. QUARTERLY SALES TREND
# ==================================================

quarterly_sales = df.groupby(
    df["Date"].dt.to_period("Q")
)["Total Amount"].sum()

plt.figure(figsize=(8, 5))
quarterly_sales.plot(kind="bar")
plt.title("Quarterly Sales Trend")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/quarterly_sales.png")
plt.close()


# ==================================================
# FINAL SUMMARY
# ==================================================

print("\n========== EDA SUMMARY ==========")

print("\nTotal Sales:", df["Total Amount"].sum())

print(
    "Average Sales:",
    round(df["Total Amount"].mean(), 2)
)

print(
    "Highest Single Transaction:",
    df["Total Amount"].max()
)

print(
    "\nBest Performing Category:",
    category_sales.idxmax()
)

print(
    "Best Category Sales:",
    category_sales.max()
)

print(
    "\nBest Performing Gender:",
    gender_sales.idxmax()
)

print(
    "Best Gender Sales:",
    gender_sales.max()
)

print("\n========== GRAPHS SAVED ==========")

print("1. monthly_sales_trend.png")
print("2. category_sales.png")
print("3. gender_sales.png")
print("4. correlation_heatmap.png")
print("5. age_group_sales.png")
print("6. quarterly_sales.png")

print("\nEDA ANALYSIS COMPLETED SUCCESSFULLY!")