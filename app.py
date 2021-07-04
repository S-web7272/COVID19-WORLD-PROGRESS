import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st


def load_data():
    return pd.read_csv('data/country_vaccinations.csv',parse_dates=['date'],dayfirst=True, index_col='date')

st.set_page_config(layout="wide")
df = load_data()

st.title("covid-19 world vaccination progress visualisation")

st.sidebar.subheader("change over time (Univariate analysis)")
cols = ['country','iso_code','total_vaccinations','people_vaccinated','people_fully_vaccinated','daily_vaccinations_raw','daily_vaccinations','total_vaccinations_per_hundred','people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred','daily_vaccinations_per_million','vaccines','source_name','source_website']

col = st.sidebar.selectbox("select a column",cols)

fig = px.line(df, x=df.index, y=col,)
st.plotly_chart(fig,use_container_width=True)