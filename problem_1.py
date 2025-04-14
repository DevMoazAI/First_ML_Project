import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
# import seaborn as sns
# import matplotlib.pyplot as plt 

# load data
p_df = pd.read_csv('D:\Internship\Problems\Task 1\Production.csv')
q_df = pd.read_csv('D:\Internship\Problems\Task 1\Quality.csv')
m_df = pd.read_csv('D:\Internship\Problems\Task 1\Machines.csv')
e_df = pd.read_csv('D:\Internship\Problems\Task 1\Employees.csv')


def standardize_date_format(df, col):
    df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
    df[col]= pd.to_datetime(df[col], format='%Y-%m-%d')
    return df

df = standardize_date_format(m_df, 'Date')
df = standardize_date_format(q_df, 'Date')
df = standardize_date_format(p_df, 'Date')

# print(p_df.head(5))

# Define the order for ordinal encoding
#empolye
education_order = ['High School', 'Diploma', 'Bachelor\'s Degree', 'Master\'s Degree']
training_status_order = ['Low', 'Medium', 'High']

#machine
make_order= ['Singer','Brother','Juki']
model_order=['S1000','B2000','J3000']

m_encoder = OrdinalEncoder(categories=[make_order, model_order])
m_df[['Make', 'Model']] = m_encoder.fit_transform(m_df[['Make', 'Model']]).astype(int)

#producation
garment_type_order =['Jeans','T-Shirt','Dress','Shirt','Jacket']
garment_type_order = [['Jeans', 'T-Shirt', 'Dress', 'Shirt', 'Jacket']]
p_garment_type_encoder = OrdinalEncoder(categories=garment_type_order)
p_df['GarmentType'] = p_garment_type_encoder.fit_transform(p_df[['GarmentType']]).astype(int)

# Replace 'Day' with 1 and 'Night' with 0
# df = array_shift_change_value[q_df,m_df]
# df['Shift'] = df['Shift'].map({'Day': 1, 'Night': 0})
# p_df['Shift'] = p_df['Shift'].astype(int)
# q_df['Shift'] = q_df['Shift'].astype(int)

for df in [p_df, q_df, m_df]:
    df['Shift'] = df['Shift'].map({'Day': 1, 'Night': 0}).astype(int)
m_df['Assigned (Yes/No)'] = m_df['Assigned (Yes/No)'].map({'Yes': 1, 'No': 0})

# Initialize the encoder
encoder = OrdinalEncoder(categories=[education_order, training_status_order])

# Apply encoding to the Education and Training Status columns
e_df[['Education', 'Training Status']] = encoder.fit_transform(e_df[['Education', 'Training Status']]).astype(int)

# Drop EmployeeID column and reset index
# e_df = e_df.drop(columns=['EmployeeID']).reset_index(drop=True)
# e_df = e_df.drop(columns=['EmployeeID'])
# m_df = m_df.drop(columns=['MachineID'])
# p_df = p_df.drop(columns=['EmployeeIDs'])

for df, col in zip([e_df, m_df, p_df], ['EmployeeID', 'MachineID', 'EmployeeIDs']):
    df.drop(columns=[col], inplace=True)


p_q_merged = pd.merge(p_df, q_df, on=['Date', 'Shift'], how='left')
# p_q_m_merged = pd.merge(p_q_merged, m_df, on=['Date', 'Shift'], how='left')
# p_q_m_e_merged = pd.merge(p_q_m_merged, e_df)


print(p_q_merged.head(5))


# a = p_df['GarmentType'].value_counts()
# print(a)


# avg_experience = selected_employees['Experience (Years)'].mean()



# Display the updated DataFrame
# print(e_df.head(5))
# print(p_df.head(5))
# print(m_df.head(5))
# print(q_df.head(5))


