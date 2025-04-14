import pandas as pd

# Sample data (as per the dataset you provided)
e_df = pd.read_csv('D:/Internship/Problems/Task 1/Employees.csv')
p_df = pd.read_csv('D:\Internship\Problems\Task 1\Production.csv')

print(e_df.head(10))
print(e_df.dtypes)