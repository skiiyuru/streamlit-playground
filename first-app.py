"""
# My first app
Here's my attempt at using streamlit
"""

import streamlit as st
import pandas as pd

df = pd.DataFrame(
    {"students": ["Steve", "Mike", "Chelsea", "Brad"], "second": [77, 52, 81, 60]}
)

df
