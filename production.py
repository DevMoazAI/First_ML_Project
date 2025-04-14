import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

p_df = pd.read_csv('D:\Internship\Problems\Task 1\Production.csv')

def standardize_date_format(df, col):
    df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
    df[col]= pd.to_datetime(df[col], format='%Y-%m-%d')
    # df['Date'] = pd.to_datetime(df['Date'])
    return df

df = standardize_date_format(p_df, 'Date')
p_df['Shift'] = p_df['Shift'].map({'Day': 1, 'Night': 0}).astype(int)

#producation
garment_type_order =['Jeans','T-Shirt','Dress','Shirt','Jacket']
garment_type_order = [['Jeans', 'T-Shirt', 'Dress', 'Shirt', 'Jacket']]
p_garment_type_encoder = OrdinalEncoder(categories=garment_type_order)
p_df['GarmentType'] = p_garment_type_encoder.fit_transform(p_df[['GarmentType']]).astype(int)

# Function to convert list to string with a custom delimiter (e.g., semicolon)
def convert_to_string(employee_ids_list):
    return '; '.join(employee_ids_list)

# Apply the function to the EmployeeIDs column
df['EmployeeIDs'] = df['EmployeeIDs'].apply(lambda x: convert_to_string(x.split(", ")))


print(p_df.head(5))

print(df.dtypes)