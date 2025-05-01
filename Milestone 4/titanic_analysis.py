import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Clean data: Fill missing ages with median age
df['Age'].fillna(df['Age'].median(), inplace=True)

# Survival analysis by Sex and Class
survival_sex = df.groupby('Sex')['Survived'].mean()
survival_class = df.groupby('Pclass')['Survived'].mean()

# Plot survival rates
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
survival_sex.plot(kind='bar', color=['pink', 'lightblue'])
plt.title('Survival Rate by Sex')
plt.ylabel('Survival Rate')

plt.subplot(1, 2, 2)
survival_class.plot(kind='bar', color=['gold', 'silver', 'brown'])
plt.title('Survival Rate by Class')

plt.tight_layout()
plt.savefig('survival_analysis.png')

# Age distribution histogram
plt.figure()
df[df['Survived'] == 1]['Age'].hist(alpha=0.5, label='Survived', bins=20)
df[df['Survived'] == 0]['Age'].hist(alpha=0.5, label='Died', bins=20)
plt.title('Age Distribution: Survived vs Died')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()
plt.savefig('age_distribution.png')

print("Done! Check 'survival_analysis.png' and 'age_distribution.png'")