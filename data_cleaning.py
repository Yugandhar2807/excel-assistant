import pandas as pd

def drop_missing(df):
    return df.dropna()

def fill_missing(df, value):
    return df.fillna(value)

def remove_duplicates(df):
    return df.drop_duplicates()

def lowercase_columns(df):
    df.columns = [col.lower() for col in df.columns]
    return df

def strip_whitespace(df):
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()
    return df
