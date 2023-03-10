import streamlit as st
import pandas as pd
import numpy as np

"# Widgets π§©"

"## Slider"
x = st.slider(label="x")
st.write(x, "squared is", np.square(x))


"## Input"
st.text_input(label="Please enter your name", key="user_name")

if st.session_state.user_name:
    f"### Hiπ, {st.session_state.user_name}!"

"## Checkbox"
if st.checkbox("Show map"):
    "## Map πΊοΈ"

    map_data = pd.DataFrame(
        data=np.random.randn(1000, 2) / [50, 50] + [-1.2921, 36.8219],
        columns=["lat", "lon"],
    )
    st.map(map_data)


st.sidebar.write("# Layouts π")

contact = st.sidebar.selectbox(
    label="How can we contact you?", options=["π§ Email", "π  Fax", "βοΈ Phone"]
)
