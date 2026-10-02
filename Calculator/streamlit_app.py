"""Streamlit web UI for calculator.py (keep both files in the same folder)."""

import time

import streamlit as st

from calculator import OPERATIONS, format_time

st.set_page_config(page_title="Python Calculator", page_icon="🧮")
st.title("🧮 Python Calculator")

# Map the readable operation name to its function
ops = {name: func for name, func in OPERATIONS.values()}

op_name = st.selectbox("Operation", list(ops.keys()))

col1, col2 = st.columns(2)
a = col1.number_input("First number", value=0.0, step=1.0, format="%g")
b = col2.number_input("Second number", value=0.0, step=1.0, format="%g")

if st.button("Calculate", type="primary"):
    start = time.perf_counter_ns()
    try:
        result = ops[op_name](a, b)
        elapsed = time.perf_counter_ns() - start
        st.success(f"Result: {result}")
    except ZeroDivisionError as err:
        elapsed = time.perf_counter_ns() - start
        st.error(str(err))
    st.metric("Runtime", format_time(elapsed))
