import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

m_df = pd.read_csv('D:\Internship\Problems\Task 1\Machines.csv')

def standardize_date_format(df, col):
    df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
    df[col]= pd.to_datetime(df[col], format='%Y-%m-%d')
    return df

df = standardize_date_format(m_df, 'Date')

#machine
make_order= ['Singer','Brother','Juki']
model_order=['S1000','B2000','J3000']
m_encoder = OrdinalEncoder(categories=[make_order, model_order])
m_df[['Make', 'Model']] = m_encoder.fit_transform(m_df[['Make', 'Model']]).astype(int)

m_df['Shift'] = m_df['Shift'].map({'Day': 1, 'Night': 0}).astype(int)
m_df['Assigned (Yes/No)'] = m_df['Assigned (Yes/No)'].map({'Yes': 1, 'No': 0}).astype(int)

print(m_df.head(5))

print(df.dtypes)