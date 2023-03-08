import streamlit as st
import pandas as pd
import numpy as np


"# Drawing charts and maps 📉"

"## Line chart"

chart_data = pd.DataFrame(data=np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)
