import pandas as pd

# load all dataset
pro_df = pd.read_csv('D:\Internship\Problems\Task 1\Production.csv')
qua_df = pd.read_csv('D:\Internship\Problems\Task 1\Quality.csv')
mac_df = pd.read_csv('D:\Internship\Problems\Task 1\Machines.csv')
emp_df = pd.read_csv('D:\Internship\Problems\Task 1\Employees.csv')

# print all dataset
print(pro_df.head())
print(qua_df.head())
print(mac_df.head())
print(emp_df.head())

# check the info of all dataset
print("Production dataset",pro_df.info())
print("Quality dataset",qua_df.info())
print("Machine dataset",mac_df.info())
print("Empolye dataset",emp_df.info())

#change date format of production and quality
pro_df['Date'] = pd.to_datetime(pro_df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
qua_df['Date'] = pd.to_datetime(qua_df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Production and Quality Merge Dataset on the base on Data and Shift Column
merged_df = pd.merge(pro_df, qua_df, on=['Date', 'Shift'], how='left')

# merged_df['Date'] = merged_df['Date'].dt.strftime('%Y-%m-%d')


print(merged_df.head())
print(merged_df.dtypes)

# rows, columns = merged_df.shape
# print(f"Total Rows: {rows}")
# print(f"Total Columns: {columns}")

# print(pro_df.head())
# print(qua_df.head())
# print(pro_df.dtypes)
# print(qua_df.dtypes)