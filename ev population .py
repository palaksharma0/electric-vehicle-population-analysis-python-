import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Electric.csv")

# Set style for plots
sns.set_style("whitegrid")

# 1. Analyze EV Adoption Trends
plt.figure(figsize=(12, 6))
df['County'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Counties with Most EV Registrations')
plt.xlabel('County')
plt.ylabel('Number of EVs')
plt.xticks(rotation=45)
plt.show()

# 2. Assess the Impact of Clean Energy Policies
plt.figure(figsize=(8, 6))
sns.countplot(data=df, y='Clean Alternative Fuel Vehicle (CAFV) Eligibility', palette='coolwarm')
plt.title('CAFV Eligibility Distribution')
plt.xlabel('Count')
plt.ylabel('CAFV Eligibility')
plt.show()

# 3. Study Electric Vehicle Range and Usage
plt.figure(figsize=(10, 6))
sns.histplot(df['Electric Range'], bins=30, kde=True, color='green')
plt.title('Distribution of Electric Vehicle Range')
plt.xlabel('Electric Range (Miles)')
plt.ylabel('Frequency')
plt.show()

# 4. Understand Market Dynamics of EVs
plt.figure(figsize=(12, 6))
top_makes = df['Make'].value_counts().head(10)
sns.barplot(x=top_makes.index, y=top_makes.values, palette='viridis')
plt.title('Top 10 EV Manufacturers by Registration')
plt.xlabel('EV Manufacturer')
plt.ylabel('Number of Vehicles')
plt.xticks(rotation=45)
plt.show()

# 5. Optimize EV Infrastructure Planning
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df.sample(1000), x='Postal Code', y='Electric Range', alpha=0.5, color='red')
plt.title('EV Range vs. Postal Code (Sample)')
plt.xlabel('Postal Code')
plt.ylabel('Electric Range (Miles)')
plt.show()
