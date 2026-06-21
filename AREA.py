import streamlit as st

st.set_page_config(
    page_title="Circle Area Calculator",
    page_icon="⭕",
    layout="centered"
)

st.title("⭕ Circle Area Calculator")

st.write("Enter the radius of a circle and calculate its area.")

radius = st.number_input(
    "Please enter radius of circle:",
    min_value=0.0,
    step=0.1
)

if st.button("Calculate Area"):
    area = 3.14 * radius * radius

    st.success(f"Area of circle is: {area:.2f}")