import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Input Data Production
p_df = pd.read_csv('D:\Internship\Problems\Task 1\Production.csv')
# Employee Dataset
e_df = pd.read_csv('D:\Internship\Problems\Task 1\Employees.csv')
# Quality dataset
q_df = pd.read_csv('D:\Internship\Problems\Task 1\Quality.csv')

# Split EmployeeIDs into lists
p_df['EmployeeIDs'] = p_df['EmployeeIDs'].apply(lambda x: x.split(', '))

# Function to calculate mean Age and Experience
def calculate_means(employee_ids, employee_df):
    selected_employees = employee_df[employee_df['EmployeeID'].isin(employee_ids)]
    mean_age = selected_employees['Age'].mean()
    mean_experience = selected_employees['Experience (Years)'].mean()
    return round(mean_age, 1), round(mean_experience, 1)

# Add Mean Age and Experience Columns
p_df[['Mean Age', 'Mean Experience']] = p_df['EmployeeIDs'].apply(
    lambda x: pd.Series(calculate_means(x, e_df))
)

# Expand EmployeeIDs as comma-separated strings again
p_df['EmployeeIDs'] = p_df['EmployeeIDs'].apply(lambda x: ', '.join(x))

# date format standard
def standardize_date_format(df, col):
    df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
    df[col]= pd.to_datetime(df[col], format='%Y-%m-%d')
    # df['Date'] = pd.to_datetime(df['Date'])
    return df

df = standardize_date_format(p_df, 'Date')
df = standardize_date_format(q_df, 'Date' )
# q_df.drop(columns=['Date'], inplace=True)

p_df['Shift'] = p_df['Shift'].map({'Day': 1, 'Night': 0}).astype(int)
q_df['Shift'] = q_df['Shift'].map({'Day': 1, 'Night': 0}).astype(int)
q_df['DefectsCount'] = q_df['DefectsCount'].astype(int)

#change the garments type as ordinal catagories 
garment_type_order =['Jeans','T-Shirt','Dress','Shirt','Jacket']
garment_type_order = [['Jeans', 'T-Shirt', 'Dress', 'Shirt', 'Jacket']]
p_garment_type_encoder = OrdinalEncoder(categories=garment_type_order)
p_df['GarmentType'] = p_garment_type_encoder.fit_transform(p_df[['GarmentType']]).astype(int)

pe_q_merged_df = pd.merge(p_df, q_df, on=['Date','Shift'], how='left')


# Display Final DataFrame
print("Processed Dataset:")
# print(p_df.head(10))
print(pe_q_merged_df.head(10))

print(pe_q_merged_df.dtypes)



# Display rows 20 to 40
# specific_rows = p_df.iloc[40:]  # iloc uses zero-based indexing, so 20:41 gives rows 20 to 40
# print(specific_rows)

#check the numerer of row and column
rows, columns = p_df.shape
print(f"Total Rows: {rows}")
print(f"Total Columns: {columns}")