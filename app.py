import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st


def load_data():
    df =  pd.read_csv('data/country_vaccinations.csv',
                        parse_dates=['date'],
                        dayfirst=True,
                        index_col='date',
                        )
    df.drop(['iso_code'],axis=1,inplace=True)
    return df

st.set_page_config(layout="wide")
df = load_data()

if st.sidebar.checkbox('View raw data'):
    st.write(df.head())
    st.write(df.shape)
    st.write(df.describe())


st.title("covid-19 world vaccination progress visualisation")

st.sidebar.subheader("Columns in dataframe")
for col in df:
    st.sidebar.write(col, df[col].dtype)

st.header("Univariate analysis of numrical data")

cols = ['total_vaccinations','people_vaccinated','people_fully_vaccinated','daily_vaccinations_raw','daily_vaccinations','total_vaccinations_per_hundred','people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred','daily_vaccinations_per_million','']
c = st.beta_columns(2)
col = c[0].selectbox("select a column",cols)
gap = c[1].selectbox("select a range to display",['D','3D','W','2W','M','2M'])
sub_df = df[col].resample(gap).mean()
c = st.beta_columns(2)
c[0].write(sub_df)
fig =  px.bar(sub_df,x=sub_df.index,y=col)
c[1].plotly_chart(fig)

st.sidebar.subheader("geographic visualization")
cols = [
    
]
cols=st.sidebar.multiselect("select two columns",df.columns.tolist())



