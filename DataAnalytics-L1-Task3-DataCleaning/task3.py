import pandas as pd
import os

# ==============================
# TASK 3 - DATA CLEANING
# ==============================

input_file = "dataset/online_retail.csv"
output_file = "output/cleaned_online_retail.csv"
report_file = "output/data_cleaning_report.txt"

print("Loading dataset...")

df = pd.read_csv(input_file)

print("Original Dataset Shape:", df.shape)

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# ------------------------------
# 1. Check missing values
# ------------------------------

missing_before = df.isnull().sum()
total_missing_before = missing_before.sum()

print("\nMissing values before cleaning:")
print(missing_before)

# ------------------------------
# 2. Remove duplicate rows
# ------------------------------

duplicates_before = df.duplicated().sum()

df = df.drop_duplicates()

duplicates_removed = duplicates_before

print("\nDuplicate rows removed:", duplicates_removed)

# ------------------------------
# 3. Remove rows with missing CustomerID
# ------------------------------

missing_customer_rows = df["CustomerID"].isnull().sum()

df = df.dropna(subset=["CustomerID"])

# ------------------------------
# 4. Convert InvoiceDate
# ------------------------------

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce"
)

# Remove invalid dates
invalid_dates = df["InvoiceDate"].isnull().sum()

df = df.dropna(subset=["InvoiceDate"])

# ------------------------------
# 5. Remove invalid Quantity
# ------------------------------

invalid_quantity = (df["Quantity"] <= 0).sum()

df = df[df["Quantity"] > 0]

# ------------------------------
# 6. Remove invalid UnitPrice
# ------------------------------

invalid_price = (df["UnitPrice"] <= 0).sum()

df = df[df["UnitPrice"] > 0]

# ------------------------------
# 7. Create TotalAmount
# ------------------------------

df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# ------------------------------
# 8. Check missing values after cleaning
# ------------------------------

missing_after = df.isnull().sum()
total_missing_after = missing_after.sum()

# ------------------------------
# 9. Save cleaned dataset
# ------------------------------

df.to_csv(output_file, index=False)

# ------------------------------
# 10. Create cleaning report
# ------------------------------

with open(report_file, "w", encoding="utf-8") as file:

    file.write("DATA CLEANING REPORT\n")
    file.write("====================\n\n")

    file.write(f"Original rows: {missing_before.shape[0]}\n")
    file.write(f"Original dataset shape: {missing_before.shape}\n\n")

    file.write(f"Missing values before cleaning: {total_missing_before}\n")
    file.write(f"Duplicate rows removed: {duplicates_removed}\n")
    file.write(f"Rows with missing CustomerID removed: {missing_customer_rows}\n")
    file.write(f"Invalid dates removed: {invalid_dates}\n")
    file.write(f"Invalid Quantity rows removed: {invalid_quantity}\n")
    file.write(f"Invalid UnitPrice rows removed: {invalid_price}\n")
    file.write(f"Missing values after cleaning: {total_missing_after}\n\n")

    file.write(f"Final dataset shape: {df.shape}\n")

print("\n======================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY!")
print("======================================")

print("\nFinal Dataset Shape:", df.shape)

print("\nOutput files created:")
print("1. cleaned_online_retail.csv")
print("2. data_cleaning_report.txt")