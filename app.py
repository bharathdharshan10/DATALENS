import streamlit as st
import pandas as pd
from analysis import get_statistics, get_head, get_isnull,get_duplicate
from datavisual import create_chart

st.set_page_config(
    page_title="Data Lens | CSV Analyzer",
    page_icon="S",
    layout="wide",
    initial_sidebar_state="expanded"
)

left,right=st.columns([3,1])

with left:
    st.subheader("Your data, Your insights")
    st.caption("Upload.Analyze.Discover insights")

with right:
    st.markdown(
        "<h1 style='text-align: right; color: #A78BFA;'>◈ DataLens</h2>",
        unsafe_allow_html=True

    )
    st.markdown(
        "<p style='text-align: right;'>CSV ANALYZER</p>",
        unsafe_allow_html=True

    )
    st.divider()  

st.subheader("Welcome to your Workspace")
st.write("Explore Your dataset and uncover useful insights")

st.write("")  



uploaded_file= st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)
st.write(" ")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)

    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.metric("Total Rows:",data.shape[0])

    with col2:
        st.metric("Total_columns:",data.shape[1])

    with col3:
        st.metric("Missing Values:",int(data.isnull().sum().sum()))

    with col4:
        st.metric("Duplicate rows:",int(data.duplicated().sum()))        

    st.write(" ")
    st.subheader("Statistical Analysis:")
    stats=get_statistics(data)
    st.dataframe(stats)

    st.write(" ")
    st.subheader("First five Data's")
    heads=get_head(data)
    st.dataframe(heads)


    total_rows=data.shape[0]


    
    

    duplicate=get_duplicate(data)
    

    st.subheader("Data Visualization")

    x_column=st.selectbox("Select X-axis",data.columns)
    y_column=st.selectbox("Select Y-axix",data.columns)

    chart_type=st.selectbox(
    "Select Chart Type",
    ["Bar","Line","Scatter"]
    )
    button=st.button("Generate Chart")

    if button:
        fig=create_chart(data,x_column,y_column,chart_type)
        st.pyplot(fig)
else:
    st.info("uploade a CSV file to begin your analysis")