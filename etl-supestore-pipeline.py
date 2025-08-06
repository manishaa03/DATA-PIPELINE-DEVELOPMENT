# Internship Task - ETL Pipeline (Kaggle Superstore Dataset)

# 1. IMPORT REQUIRED LIBRARIES
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# 2. EXTRACT: READ CSV FILE
file_path = "Sample - Superstore.csv"   # Change file name if different
data = pd.read_csv(file_path, encoding='latin1')

print("Original Data Sample:")
print(data.head(), "\n")
print(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}")

# 3. TRANSFORM: CLEANING & PREPROCESSING

# Date Formatting
data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
data['Ship Date'] = pd.to_datetime(data['Ship Date'], errors='coerce')

# Drop unnecessary ID columns (optional)
drop_cols = ['Row ID', 'Order ID', 'Customer ID', 'Postal Code']
data.drop(columns=[col for col in drop_cols if col in data.columns], inplace=True)

# Separate numeric and categorical columns
numeric_features = data.select_dtypes(include=['int64', 'float64']).columns
categorical_features = data.select_dtypes(include=['object']).columns

# Numeric transformer: Handle missing values and scale
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Categorical transformer: Handle missing values and encode
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# Combine transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# Create pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor)])

# Fit and transform
processed_data = pipeline.fit_transform(data)

# 4. LOAD: SAVE CLEANED DATA
# Convert processed data back to DataFrame
processed_df = pd.DataFrame(
    processed_data.toarray() if hasattr(processed_data, "toarray") else processed_data
)

# Save to CSV
output_file = "Superstore_Cleaned.csv"
processed_df.to_csv(output_file, index=False)

print(f"Cleaned data saved as '{output_file}'")
