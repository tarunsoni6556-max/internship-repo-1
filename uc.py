import streamlit as st 

st.set_page_config(
    page_title="unit converter",
    page_icon=":ruler:",
    layout="centered"
)
with st.form("unit_converter_form"):
    st.header("Unit Converter")
    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input("Enter value", value=0.0)
        from_unit = st.selectbox("From unit", ["Meters", "Kilometers", "Miles"])
    with col2:
        to_unit = st.selectbox("To unit", ["Meters", "Kilometers", "Miles"])
    submit_button = st.form_submit_button(label="Convert")
    st.write("Note: This converter only supports Meters, Kilometers, and Miles.")
    st.write("Conversion rates: 1 Kilometer = 1000 Meters, 1 Mile = 1609.34 Meters")
st.display = st.write("Result: ")   

