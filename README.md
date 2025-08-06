# DATA-PIPELINE-DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS  

*NAME*: MANISHA KUMARI  

*INTERN ID*: CT12DN310  

*DOMAIN*: DATA SCIENCE 

*DURATION*: 12 WEEKS  

*MENTOR*: NEELA SANTHOSH KUMAR 

# ETL Pipeline - Kaggle Superstore Dataset

## Project Overview
This project performs an ETL (Extract, Transform, Load) operation on the Kaggle Superstore dataset.  
It reads raw data, cleans and preprocesses it, and saves the cleaned output for further use.

## Technologies Used
- Python  
- Pandas  
- Scikit-learn  

## ETL Workflow
### 1. Extract
- Reads the dataset `Sample - Superstore.csv` using pandas.

### 2. Transform
- Converts `Order Date` and `Ship Date` to datetime format.
- Drops unnecessary ID columns (`Row ID`, `Order ID`, `Customer ID`, `Postal Code`).
- Handles missing values:
  - Numeric columns → Mean imputation + Standard scaling
  - Categorical columns → Most frequent imputation + One-hot encoding

### 3. Load
- Saves the cleaned dataset as `Superstore_Cleaned.csv`.

## How to Run
1. Install dependencies  
```bash
pip install pandas scikit-learn
```
2. Run the ETL script  
```bash
python etl-supestore-pipeline.py
```
3. Output file will be generated: `Superstore_Cleaned.csv`

## Example Output
**Before Cleaning (Sample)**  
| Order Date | Ship Date | Sales | Category |
|------------|-----------|-------|----------|
| 2017-11-08 | 2017-11-11 | 261.96 | Furniture |

**After Cleaning**
- Dates formatted correctly
- Columns encoded/scaled
- Missing values handled

