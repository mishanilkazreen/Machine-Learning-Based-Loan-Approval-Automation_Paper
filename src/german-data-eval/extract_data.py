import os
import pandas as pd
from ucimlrepo import fetch_ucirepo

# fetch dataset
statlog_german_credit_data = fetch_ucirepo(id=144)

# data (as pandas dataframes)
X = statlog_german_credit_data.data.features
y = statlog_german_credit_data.data.targets

# metadata
print(statlog_german_credit_data.metadata)

# variable information
print(statlog_german_credit_data.variables)

# combine features and target into one dataframe
df = pd.concat([X, y], axis=1)

# save to CSV in the same folder as this script
output_path = os.path.join(os.path.dirname(__file__), "german_credit_data.csv")
df.to_csv(output_path, index=False)

print(f"Data saved to {output_path}")
print(f"Shape: {df.shape}")
