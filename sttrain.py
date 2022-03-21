from sklearn.metrics import adjusted_mutual_info_score
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

st.set_page_config(layout="wide")

st.title('This is Title of this page')
st.code("st.title('This is Title of this page')")

st.header('This is Header')

st.subheader('This is subheader')

st.text('This is text')

st.code("""
if(a = ax + d2)
ad
""")

st.caption("this is caption")

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

st.line_chart(df)

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Column

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


# Column dua
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.sidebar.text('Testing')
