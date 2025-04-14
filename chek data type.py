import pandas as pd


# Load data
p_df = pd.read_csv('D:\Internship\Problems\Task 1\Production.csv')
q_df = pd.read_csv('D:\Internship\Problems\Task 1\Quality.csv')
# m_df = pd.read_csv('D:\Internship\Problems\Task 1\Machines.csv')
# e_df = pd.read_csv('D:\Internship\Problems\Task 1\Employees.csv')

print(q_df.head(5))

print(q_df.dtypes)