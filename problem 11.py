import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Load the production dataset
p_df = pd.read_csv("D:/Internship/Problems/Task 1/Production.csv")

# Standardize the Date format and ensure it's in datetime format
p_df['Date'] = pd.to_datetime(p_df['Date'], errors='coerce')  # Convert to datetime, invalid dates become NaT
p_df['Date'] = p_df['Date'].dt.strftime('%Y-%m-%d')  # Format as 'YYYY-MM-DD'

# Filter out rows where Date is NaT after conversion
p_df = p_df.dropna(subset=['Date'])

# Map the Shift column to Day=1 and Night=0
p_df['Shift'] = p_df['Shift'].map({'Day': 1, 'Night': 0}).astype(int)

# Ensure there are no NaN values in the Shift column after mapping
p_df = p_df.dropna(subset=['Shift'])

# GarmentType Ordinal Encoding (Ensure the order of garments)
garment_type_order = ['Jeans', 'T-Shirt', 'Dress', 'Shirt', 'Jacket']  # Define the order
garment_type_order = [garment_type_order]  # Wrapping it inside a list for encoder
p_garment_type_encoder = OrdinalEncoder(categories=garment_type_order)
p_df['GarmentType'] = p_garment_type_encoder.fit_transform(p_df[['GarmentType']]).astype(int)

# Ensure TargetUnits is treated as an integer
p_df['TargetUnits'] = p_df['TargetUnits'].astype(int)

# Drop the EmployeeIDs column as it's not needed for the merge
# p_df = p_df.drop(columns=['EmployeeIDs'])
p_df = p_df.drop(columns=['EmployeeIDs','GarmentType', 'TargetUnits'])

# Check for missing values in the production dataset
# print(f"Missing values in production dataset before merge:\n{p_df.isnull().sum()}")

# Display the first few rows of the production dataset after preparation
print(p_df.head())
