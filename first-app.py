"""
# My first app
Here's my attempt at using streamlit
"""

import streamlit as st
import pandas as pd

"# Magic heading 🤩"

df = pd.DataFrame(
    {"students": ["Steve", "Mike", "Chelsea", "Brad"], "second": [77, 52, 81, 60]}
)

df

st.write({"name": "streamlit", "coolness_factor": "⭐⭐⭐⭐⭐"})

"# Styling a Dataframe 😎"

import numpy as np

arr_2d = np.random.randn(10, 20)

df = pd.DataFrame(arr_2d, columns=[f"col-{idx}" for idx in range(20)])

st.dataframe(df.style.highlight_max(axis=0))

# st.table(df)

"# Drawing charts and maps 📉"

"## Line chart"

chart_data = pd.DataFrame(data=np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)


"# Widgets 🧩"

"## Slider"
x = st.slider(label="x")
st.write(x, "squared is", np.square(x))


"## Input"
st.text_input(label="Please enter your name", key="user_name")

if st.session_state.user_name:
    f"### Hi👋, {st.session_state.user_name}!"

"## Checkbox"
if st.checkbox("Show map"):
    "## Map 🗺️"

    map_data = pd.DataFrame(
        data=np.random.randn(1000, 2) / [50, 50] + [-1.2921, 36.8219],
        columns=["lat", "lon"],
    )
    st.map(map_data)


st.sidebar.write("# Layouts 📐")

contact = st.sidebar.selectbox(
    label="How can we contact you?", options=["📧 Email", "📠 Fax", "☎️ Phone"]
)

"# More layouts 📐"

left_col, right_col = st.columns(2)

with left_col:
    "## Selectbox"
    df = pd.DataFrame(
        {
            "gender": ["male", "female", "prefer not to say"],
            "nationality": ["🇰🇪", "🇺🇸", "🇩🇪"],
        }
    )

    gender = st.selectbox("What's your gender", df["gender"])
    nationality = st.selectbox("What's your nationality", df["nationality"])

right_col.write("## You selected:")
right_col.write(f"Gender: {gender} &  Nationality: {nationality}")