import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
path_to_dataset = 'D:/Semester 5th/AI lab/Week 11/'
iris_df = pd.read_csv(path_to_dataset + 'IRIS.csv')

# Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(iris_df.head())

# Summary statistics of the dataset
print("\nSummary statistics of the dataset:")
print(iris_df.describe())

# Check for missing values
print("\nMissing values in the dataset:")
print(iris_df.isnull().sum())

# Visualize the distribution of the target variable (species)
sns.countplot(x='species', data=iris_df)
plt.title('Distribution of Iris Species')
plt.show()

# Pairplot to visualize relationships between variables
sns.pairplot(iris_df, hue='species', markers=['o', 's', 'D'])
plt.suptitle('Pairplot of Iris Dataset', y=1.02)
plt.show()

# Boxplot to visualize the distribution of features for each species
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.boxplot(x='species', y='sepal_length', data=iris_df)
plt.subplot(2, 2, 2)
sns.boxplot(x='species', y='sepal_width', data=iris_df)
plt.subplot(2, 2, 3)
sns.boxplot(x='species', y='petal_length', data=iris_df)
plt.subplot(2, 2, 4)
sns.boxplot(x='species', y='petal_width', data=iris_df)
plt.suptitle('Boxplots of Iris Features by Species', y=1.02)
plt.show()
