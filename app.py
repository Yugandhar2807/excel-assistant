import streamlit as st
import pandas as pd

from data_cleaning import drop_missing, fill_missing, remove_duplicates, lowercase_columns, strip_whitespace
from pivot_generator import generate_pivot
from graph_visualizer import plot_pivot_bar
from chatbot import chatbot_ui

st.set_page_config(page_title="Excel Assistant", layout="wide")

def clean_data_ui(df):
    st.subheader("🧹 Data Cleaning Options")

    if st.checkbox("Drop rows with missing values"):
        df = drop_missing(df)
        st.success("Dropped rows with missing values")

    if st.checkbox("Fill missing values"):
        fill_value = st.text_input("Enter value to fill missing values with (number or string):", "")
        if fill_value != "":
            try:
                fill_val_converted = pd.to_numeric(fill_value)
                df = fill_missing(df, fill_val_converted)
            except:
                df = fill_missing(df, fill_value)
            st.success(f"Filled missing values with '{fill_value}'")

    if st.checkbox("Remove duplicate rows"):
        df = remove_duplicates(df)
        st.success("Duplicate rows removed")

    if st.checkbox("Lowercase column names"):
        df = lowercase_columns(df)
        st.success("Column names converted to lowercase")

    if st.checkbox("Strip whitespace in text columns"):
        df = strip_whitespace(df)
        st.success("Whitespace stripped from text columns")

    st.subheader("🗂 Cleaned Data Preview")
    st.dataframe(df)

    return df


def generate_pivot_ui(df):
    st.subheader("📊 Pivot Table Generator")
    index_cols = st.multiselect("Select row (index) columns", options=df.columns.tolist())
    column_cols = st.multiselect("Select column columns", options=df.columns.tolist())
    values_col = st.selectbox("Select values column", options=df.columns.tolist())
    aggfunc = st.selectbox("Select aggregation function", options=["sum", "mean", "count", "min", "max"], index=0)

    if st.button("Generate Pivot Table"):
        if values_col and index_cols:
            pivot_df = generate_pivot(df, index_cols=index_cols, column_cols=column_cols if column_cols else None, values_col=values_col, aggfunc=aggfunc)
            st.session_state['pivot_df'] = pivot_df
            st.dataframe(pivot_df)
        else:
            st.error("Please select at least one index column and a values column")

    return st.session_state.get('pivot_df', None)


def visualize_graph_ui():
    pivot_df = st.session_state.get('pivot_df', None)
    if pivot_df is None:
        st.info("Generate a pivot table first to visualize graphs.")
        return

    st.subheader("📈 Graph Visualizer")

    x_col = st.selectbox("Select X-axis column", options=pivot_df.columns.tolist(), index=0)
    y_cols = st.multiselect("Select Y-axis columns", options=[col for col in pivot_df.columns if col != x_col])

    if st.button("Plot Bar Chart"):
        if y_cols:
            plot_pivot_bar(pivot_df, x_col, y_cols)
        else:
            st.error("Select at least one Y-axis column to plot")


def main():
    st.title("🧠 Excel Assistant - Smart Excel Analyzer")

    uploaded_file = st.file_uploader("Upload your Excel, CSV, TXT, JSON or XML file", type=["xlsx", "xls", "csv", "txt", "json", "xml"])

    if uploaded_file:
        file_type = uploaded_file.name.split('.')[-1].lower()
        try:
            if file_type in ['xlsx', 'xls']:
                if file_type == 'xls':
                    df = pd.read_excel(uploaded_file, engine='xlrd')
                else:
                    df = pd.read_excel(uploaded_file, engine='openpyxl')
            elif file_type in ['csv', 'txt']:
                df = pd.read_csv(uploaded_file)
            elif file_type == 'json':
                df = pd.read_json(uploaded_file)
            elif file_type == 'xml':
                df = pd.read_xml(uploaded_file)
            else:
                st.error(f"Unsupported file type: .{file_type}")
                st.stop()

            st.subheader("🔍 Original Data")
            st.dataframe(df)

            st.markdown("---")
            df_cleaned = clean_data_ui(df)

            st.markdown("---")
            pivot_df = generate_pivot_ui(df_cleaned)

            st.markdown("---")
            visualize_graph_ui()

            st.markdown("---")
            chatbot_ui(df_cleaned)

        except Exception as e:
            st.error(f"Error reading the file: {e}")
    else:
        st.info("Please upload a file to get started.")


if __name__ == "__main__":
    main()
