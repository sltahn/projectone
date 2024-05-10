import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Project #1 - Salaries")

DATA_URL = ('salaries.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.columns = data.columns.str.strip()
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data)

data['Annual Base Pay'] = pd.to_numeric(data['Annual Base Pay'], errors='coerce')

data['Years at Employer'] = pd.to_numeric(data['Years at Employer'], errors='coerce')

unexpected_values = data['Years at Employer'][pd.isna(data['Years at Employer']) == False][~data['Years at Employer'].astype(str).str.isdigit()].unique()

sort_by = st.selectbox("Sort Data By", data.columns)
sorted_data = data.sort_values(by=sort_by)

st.subheader('Sorted data')
st.write(sorted_data)

st.subheader('Summary Statistics')
st.write(data.describe())

st.subheader('Insights for Years of Experience and Years at Employer')

st.subheader('Distribution of Years of Experience')
st.bar_chart(data['Years of Experience'])

st.subheader('Distribution of Years at Employer')
st.bar_chart(data['Years at Employer'])

average_experience = data['Years of Experience'].mean()
average_tenure = data['Years at Employer'].mean()
st.write(f'Average Years of Experience: {average_experience:.2f}')
st.write(f'Average Years at Employer: {average_tenure:.2f}')
