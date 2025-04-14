import pandas as pd

q_df = pd.read_csv('D:\Internship\Problems\Task 1\Quality.csv')

def standardize_date_format(df, col):
    df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
    df[col]= pd.to_datetime(df[col], format='%Y-%m-%d')
    return df
df = standardize_date_format(q_df, 'Date')

q_df['Shift'] = q_df['Shift'].map({'Day': 1, 'Night': 0})

# q_df['DefectsCount'] = q_df['DefectsCount'].astype(int)


print(q_df.head(5))

print(df.dtypes)