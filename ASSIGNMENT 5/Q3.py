import numpy as np
import matplotlib.pyplot as plt

# Q.3 You are given a weekly sales dataset and need to perform various operations using NumPy broadcasting.

# a) Generate your unique sales dataset
# Let's assume your initials are "A B" → ASCII sum = 65 + 66 = 131
X = 131
sales = np.array([X, X + 50, X + 100, X + 150, X + 200])
print("Sales array:", sales)

# b) Compute your personalized tax rate as ((X % 5) + 5) / 100
tax_rate = ((X % 5) + 5) / 100
print("Tax rate:", tax_rate)

# Use broadcasting to apply this tax rate to each sales value
taxed_sales = sales * (1 + tax_rate)
print("Taxed sales:", taxed_sales)

# c) Adjust sales based on discount
# If sales < X+100, apply a 5% discount
# If sales >= X+100, apply a 10% discount
discounted_sales = np.where(sales < X + 100, sales * 0.95, sales * 0.90)
print("Discounted sales:", discounted_sales)

# d) Expand sales data for multiple weeks
# Create a 3×5 matrix representing three weeks of sales by stacking sales three times using broadcasting
weekly_sales = np.vstack([sales, sales, sales])
print("Weekly sales (3 weeks):", weekly_sales)


weekly_sales_increased = weekly_sales * (1 + 0.02) ** np.arange(3)[:, np.newaxis]
print("Weekly sales increased by 2% per week:", weekly_sales_increased)

