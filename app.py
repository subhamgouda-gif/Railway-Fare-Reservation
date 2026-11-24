import contextlib
import io
import runpy

import streamlit as st

st.set_page_config(page_title="Railway Fare Reservation", layout="wide")
st.title("Railway Fare Reservation")
output = io.StringIO()
with contextlib.redirect_stdout(output):
    runpy.run_path("main.py", run_name="__main__")
st.text(output.getvalue())
