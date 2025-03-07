import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def stats(data):
    '''Creates a table of statistics for the data
    Args: dataframe
    Returns: None
    '''
    st.header('Data Statistics:')
    st.write(df.describe())      

def data_head(data):
    '''Displays the first 5 rows of the data
    Args: dataframe
    Returns: None
    '''
    st.header('Data Header:')
    st.write(df.head())

def plots(data):
    '''Creates a histogram and scatter plot
    Args: dataframe
    Returns: None
    '''
    st.header('Histogram of Magnitude:')
    fig = px.histogram(df, x=df['Magnitude'], color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_traces(nbinsx=20, selector=dict(type='histogram'))
    fig.update_layout(bargap=0.1)
    st.plotly_chart(fig)                    #displaying the histogram

    st.header('Scatter plot of Depth vs Magnitude:')
    fig1 = px.scatter(df, x=df['Depth'], y=df['Magnitude'], color=df['Magnitude'], color_continuous_scale='viridis')
    fig1.update_layout(xaxis_title='Depth (M)', yaxis_title='Magnitude')
    st.plotly_chart(fig1)                    #displaying the scatter plot

def interactive_plots(data):
    '''Creates interactive plots
    Args: dataframe
    Returns: None
    '''
    st.header('Select Chart Type')
    chart_type = st.radio('Chart Type:', ['Scatter', 'Bar', 'Histogram'])

    st.markdown('**Select the X and Y values for the plot:**')

    if chart_type == 'Histogram':
        x = st.selectbox('X value', sorted(df.columns))
    else:
        x = st.selectbox('X value', sorted(df.columns))
        y = st.selectbox('Y value', sorted(df.columns))
    if st.button('Create Plot'):
        if chart_type == 'Scatter':
            fig = px.scatter(df, x=x, y=y, color= y, color_continuous_scale='viridis')
        elif chart_type == 'Histogram':
            fig = px.histogram(df, x=x, nbins=10)
            fig.update_layout(bargap=0.1)
        elif chart_type == 'Bar':
            fig = px.bar(df, x=x, y=y, color_continuous_scale='viridis')
        st.plotly_chart(fig)


st.title('Earthquake Data Explorer')

st.sidebar.title('Navigation')
uploaded_file = st.sidebar.file_uploader("Please add your earthquake data file:") 
if uploaded_file:
    df = pd.read_csv(uploaded_file)  # reading the file
options = st.sidebar.radio('Pages', options=['Home', 'Stats', 'Data Header', 'Plots', 'Interactive Plots'])

if options == 'Stats':
    stats(df)
elif options == 'Data Header':
    data_head(df)
elif options == 'Plots':
    plots(df)
elif options == 'Home':
    st.subheader('Please Upload a file then select a page from the sidebar to begin exploring the data')   
    st.write('The file uploader is also located in the sidebar :)')
elif options == 'Interactive Plots':
    interactive_plots(df)