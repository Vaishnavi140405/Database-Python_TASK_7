# TASK 7: Basic Sales Summary using MySQL + Python
import  mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sales_db"
)

print("Database connection successful!")

query = """
SELECT product,
       SUM(quantity) AS total_quantity,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
"""

df = pd.read_sql(query, conn)

print("\nSales Summary:")
print(df)

df.plot(kind='bar', x='product', y='revenue')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

conn.close()