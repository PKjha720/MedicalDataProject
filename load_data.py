import pandas as pd

# Load the data from the Excel file
file_path = r'C:\Users\prabhat.j\Downloads\medical\diabetes_012_health_indicators_BRFSS2015.csv'  
df = pd.read_csv(file_path)

# Display the first few rows of the dataset to confirm it loaded correctly
print(df.head())
