"""
# My first app
Here's my attempt at using streamlit
"""

import streamlit as st
import pandas as pd

"# Magic heading π€©"

df = pd.DataFrame(
    {"students": ["Steve", "Mike", "Chelsea", "Brad"], "second": [77, 52, 81, 60]}
)

df

st.write({"name": "streamlit", "coolness_factor": "β­β­β­β­β­"})

"# Styling a Dataframe π"

import numpy as np

arr_2d = np.random.randn(10, 20)

df = pd.DataFrame(arr_2d, columns=[f"col-{idx}" for idx in range(20)])

st.dataframe(df.style.highlight_max(axis=0))

# st.table(df)

"# More layouts π"

left_col, right_col = st.columns(2)

with left_col:
    "## Selectbox"
    df = pd.DataFrame(
        {
            "gender": ["male", "female", "prefer not to say"],
            "nationality": ["π°πͺ", "πΊπΈ", "π©πͺ"],
        }
    )

    gender = st.selectbox("What's your gender", df["gender"])
    nationality = st.selectbox("What's your nationality", df["nationality"])

right_col.write("## You selected:")
right_col.write(f"Gender: {gender} &  Nationality: {nationality}")
