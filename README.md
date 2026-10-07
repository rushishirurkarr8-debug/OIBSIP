\# OASIS INFOBYTE - Data Analytics



\## Task 1: Exploratory Data Analysis (EDA) on Retail Sales Data



\### Project Overview



This project performs Exploratory Data Analysis (EDA) on a retail sales dataset using Python. The objective is to understand sales patterns, customer behaviour, product category performance, and relationships between numerical variables.



\### Tools and Technologies



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn



\### Dataset



The dataset contains 1,000 retail transactions with information including:



\- Transaction ID

\- Date

\- Customer ID

\- Gender

\- Age

\- Product Category

\- Quantity

\- Price per Unit

\- Total Amount



\### Data Quality Check



The dataset was checked for:



\- Missing values

\- Duplicate records

\- Data types

\- Descriptive statistics

\- Numerical ranges



Results:



\- Total records: 1,000

\- Missing values: 0

\- Duplicate records: 0



\### Analysis Performed



The following analyses were performed:



1\. Monthly sales trend analysis

2\. Quarterly sales trend analysis

3\. Sales by product category

4\. Sales by gender

5\. Sales by age group

6\. Correlation analysis using a heatmap



\### Visualizations



The project generated the following visualizations:



\- Monthly Sales Trend

\- Quarterly Sales Trend

\- Sales by Product Category

\- Sales by Gender

\- Sales by Age Group

\- Correlation Heatmap



All visualizations are available in the `output` folder.



\### Key Statistics



\- Number of transactions: 1,000

\- Average customer age: 41.39 years

\- Average quantity per transaction: 2.51

\- Average price per unit: 179.89

\- Average transaction amount: 456

\- Maximum transaction amount: 2,000



\### Business Insights



1\. Sales vary across different months and quarters, indicating changes in purchasing activity over time.



2\. Product categories contribute differently to total sales, helping identify stronger-performing categories.



3\. Customer demographics such as gender and age group can be used to understand purchasing behaviour.



4\. Correlation analysis helps identify relationships between numerical variables such as age, quantity, price, and total amount.



\### Business Recommendations



1\. Focus marketing campaigns on high-performing product categories to increase revenue.



2\. Use customer demographic insights to create targeted promotions for different age groups and customer segments.



3\. Monitor monthly and quarterly sales trends to identify high-demand periods and plan inventory and promotional campaigns accordingly.



\### Project Structure



```text

DataAnalytics-Level1-Task1-EDA-Retail-Sales/

│

├── dataset/

│   └── retail\_sales\_dataset.csv

│

├── output/

│   ├── age\_group\_sales.png

│   ├── category\_sales.png

│   ├── correlation\_heatmap.png

│   ├── gender\_sales.png

│   ├── monthly\_sales\_trend.png

│   └── quarterly\_sales.png

│

├── task1.py

└── README.md

