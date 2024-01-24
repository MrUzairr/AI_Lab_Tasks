import pandas as pd

# Replace 'path_to_dataset' with the actual path where you extracted the dataset
path_to_dataset = 'D:/Semester 5th/AI lab/Week 11/'

# Read the CSV file into a DataFrame
iris_df = pd.read_csv(path_to_dataset + 'IRIS.csv')

# Display the first few rows of the DataFrame
print(iris_df.head())
