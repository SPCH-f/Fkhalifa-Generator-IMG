import pandas as pd
import os

file_path = 'C:/Project/Myproject/Myapp/Test_Demo_DATA.xlsx'
try:
    xl = pd.ExcelFile(file_path)
    print(f"Sheet names: {xl.sheet_names}")
    for sheet in xl.sheet_names:
        df = xl.parse(sheet, nrows=2)
        print(f"\n--- Sheet: {sheet} ---")
        print(f"Columns: {list(df.columns)}")
except Exception as e:
    print(f"Error: {e}")
