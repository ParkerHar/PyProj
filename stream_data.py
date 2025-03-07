import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

df= pd.read_csv('/Users/parkerharalds/Downloads/temp.csv')

#print(df.head())
#print(df.columns)


def scatter_chart (df, x, y):
    fig = px.scatter(df, x=df[x], y=df[y], title=f'{x} vs {y}')
    fig.update_traces(name='country_name',selector=dict(type='scatter', mode='markers'))    
    fig.show()

scatter_chart(df, 'date', 'value_formatted')