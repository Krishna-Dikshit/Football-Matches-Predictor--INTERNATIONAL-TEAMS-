"""
FIFA World Cup Match Outcome Prediction

This file serves as a simple entry point for the project.
The complete data analysis, feature engineering, and machine
learning workflow is available in:

    notebooks/notebook.ipynb
"""

import pandas as pd

def main():
    df = pd.read_csv("data/WorldCupMatches.csv")
    print("Dataset loaded successfully!")
    print(f"Matches: {len(df)}")
    print(f"Columns: {len(df.columns)}")

if __name__ == "__main__":
    main()