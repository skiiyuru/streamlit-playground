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
