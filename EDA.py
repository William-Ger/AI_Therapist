import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the data and display the first few rows
data = pd.read_csv('LiveLongerData_Cleaned.csv')
data.head()

# Step 2: Perform basic statistical analyses to summarize the data

# Getting summary statistics of the numerical columns
numerical_summary = data.describe()

# Checking the distribution of categorical columns
categorical_distribution = data.select_dtypes(include=['object']).nunique()

numerical_summary, categorical_distribution

# Step 3: Visualize the data to identify any patterns or insights

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Initialize the figure
plt.figure(figsize=(18, 5))

# Create subplots: 1 row, 3 columns
plt.subplot(1,3,1)

# Plot 1: Histogram of the years gained or lost
sns.histplot(data['years_gained_lost'], bins=15, kde=True)
plt.title('Distribution of Years Gained or Lost')
plt.xlabel('Years Gained or Lost')
plt.ylabel('Frequency')

# Plot 2: Bar plot of average years gained or lost per strength of science category
plt.subplot(1, 3, 2)
sns.barplot(x='strength_of_science', y='years_gained_lost', data=data, errorbar=None)
plt.title('Average Years Gained or Lost by Strength of Science')
plt.xlabel('Strength of Science')
plt.ylabel('Average Years Gained or Lost')

# Plot 3: Bar plot of average years gained or lost per sex affected
plt.subplot(1, 3, 3)
sns.barplot(x='sexes affected', y='years_gained_lost', data=data, errorbar=None)
plt.title('Average Years Gained or Lost by Sex Affected')
plt.xlabel('Sexes Affected')
plt.ylabel('Average Years Gained or Lost')

# Rotate the x labels for better visibility
plt.xticks(rotation=45)

# Display the plots
plt.tight_layout()
plt.show()

# Step 4: Investigate the data

# Correlation Matrix

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Display the correlation matrix
correlation_matrix

# Step 5: Indentify all of the factors

# List all the unique factors in the dataset
factors = data['factor'].unique()
factors_df = pd.DataFrame(factors, columns=['Factors'])
factors_df

