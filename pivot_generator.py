import pandas as pd

def generate_pivot(df, index_cols, column_cols, values_col, aggfunc='sum'):
    pivot = pd.pivot_table(
        df,
        index=index_cols,
        columns=column_cols if column_cols else None,
        values=values_col,
        aggfunc=aggfunc,
        fill_value=0
    )
    return pivot.reset_index()
