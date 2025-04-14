import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Load data (use raw string literals to avoid escape sequence warnings)
m_df = pd.read_csv("D:/Internship/Problems/Task 1/Machines.csv")
q_df = pd.read_csv("D:/Internship/Problems/Task 1/Quality.csv")
p_df = pd.read_csv("D:/Internship/Problems/Task 1/Production.csv")

# Function to standardize date format and shift values
def standardize_date_and_shift(df, date_col, shift_col):
    # Convert date column to datetime format
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce').dt.strftime('%Y-%m-%d')
    df[date_col] = pd.to_datetime(df[date_col], format='%Y-%m-%d')
    
    # Replace 'Day' with 1 and 'Night' with 0 in the Shift column
    df[shift_col] = df[shift_col].map({'Day': 1, 'Night': 0}).astype(int)
    
    # Check if there are any NaN values in Date or Shift columns
    # print(f"Missing values in {date_col} and {shift_col}: {df[[date_col, shift_col]].isnull().sum()}")
    
    return df

# Apply the function to both DataFrames
m_df = standardize_date_and_shift(m_df, 'Date', 'Shift')
q_df = standardize_date_and_shift(q_df, 'Date', 'Shift')
p_df = standardize_date_and_shift(p_df, 'Date', 'Shift')

# Step 3: Check Key Alignment Before Merge
# print("Unique combinations in m_df:")
# print(m_df[['Date', 'Shift']].drop_duplicates())

# print("Unique combinations in q_df:")
# print(q_df[['Date', 'Shift']].drop_duplicates())

# Remove duplicates from q_df to avoid repetition of DefectsCount values
# q_df = q_df.drop_duplicates(subset=['Date', 'Shift'])

# Machine make and model ordinal encoding
make_order= ['Singer','Brother','Juki']
model_order=['S1000','B2000','J3000']
m_encoder = OrdinalEncoder(categories=[make_order, model_order])
m_df[['Make', 'Model']] = m_encoder.fit_transform(m_df[['Make', 'Model']]).astype(int)

# Drop MachineID column
m_df = m_df.drop(columns=['MachineID'])

# Map 'Yes'/'No' to 1/0 in Assigned (Yes/No) column
m_df['Assigned (Yes/No)'] = m_df['Assigned (Yes/No)'].map({'Yes': 1, 'No': 0}).astype(int)

# GarmentType Ordinal Encoding (Ensure the order of garments)
# garment_type_order = ['Jeans', 'T-Shirt', 'Dress', 'Shirt', 'Jacket']  # Define the order
# garment_type_order = [garment_type_order]  # Wrapping it inside a list for encoder
# p_garment_type_encoder = OrdinalEncoder(categories=garment_type_order)
# p_df['GarmentType'] = p_garment_type_encoder.fit_transform(p_df[['GarmentType']]).astype(int)

# # Ensure TargetUnits is treated as an integer
# p_df['TargetUnits'] = p_df['TargetUnits'].astype(int)

# Drop the EmployeeIDs column as it's not needed for the merge
# p_df = p_df.drop(columns=['EmployeeIDs'])
# p_df = p_df.drop(columns=['EmployeeIDs','GarmentType', 'TargetUnits'])

# Merge m_df and q_df on Date and Shift using a left join
merged_df = pd.merge(m_df, q_df, on=['Date', 'Shift'], how='left')

# Remove duplicate entries from the final merged dataset
merged_df = merged_df.drop_duplicates()

# Reorder columns to move Date and Shift to the left side
# columns_order = ['Date', 'Shift', 'Make', 'Model', 'Assigned (Yes/No)', 'EmployeeIDs','GarmentType', 'TargetUnits','DefectsCount']
# merged_df = merged_df[columns_order]

# Print merged DataFrame to inspect the result
print(merged_df.head(20))

print()
# Check for NaN values after the merge
# print(f"Missing values after merge: {merged_df.isnull().sum()}")
