import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_pivot_bar(pivot_df, x_col, y_cols):
    plt.figure(figsize=(10, 6))
    for y_col in y_cols:
        sns.barplot(data=pivot_df, x=x_col, y=y_col, label=y_col)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
