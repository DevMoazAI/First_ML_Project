import pandas as pd

# Input Data
p_df = pd.read_csv('D:\Internship\Problems\Task 1\Production.csv')

# Employee Dataset
e_df = pd.read_csv('D:\Internship\Problems\Task 1\Employees.csv')

# Convert to DataFrames
df_main = pd.DataFrame(p_df)
df_employee = pd.DataFrame(e_df)

# Split EmployeeIDs into lists
df_main['EmployeeIDs'] = df_main['EmployeeIDs'].apply(lambda x: x.split(', '))

# Function to calculate mean Age and Experience
def calculate_means(employee_ids, employee_df):
    selected_employees = employee_df[employee_df['EmployeeID'].isin(employee_ids)]
    mean_age = selected_employees['Age'].mean()
    mean_experience = selected_employees['Experience (Years)'].mean()
    return round(mean_age, 1), round(mean_experience, 1)

# Add Mean Age and Experience Columns
df_main[['Mean Age', 'Mean Experience']] = df_main['EmployeeIDs'].apply(
    lambda x: pd.Series(calculate_means(x, df_employee))
)

# Expand EmployeeIDs as comma-separated strings again
df_main['EmployeeIDs'] = df_main['EmployeeIDs'].apply(lambda x: ', '.join(x))

# Display Final DataFrame
print("Processed Dataset:")
print(df_main.head(10))
