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
