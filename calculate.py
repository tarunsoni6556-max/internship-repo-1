import streamlit as st 

st.set_page_config(
    page_title="Calculate",
    page_icon=":calculate:",
    layout="centered"
)

col1, col2 = st.columns(2)
with col1:
    st.header("Calculate")
    with st.form("calculate_form"):
        number1 = st.number_input("Enter first number", value=0.0)
        number2 = st.number_input("Enter second number", value=0.0)
        operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])
        submit_button = st.form_submit_button(label="Calculate")

    if submit_button:
        if operation == "Add":
            result = number1 + number2
        elif operation == "Subtract":
            result = number1 - number2
        elif operation == "Multiply":
            result = number1 * number2
        elif operation == "Divide":
            if number2 != 0:
                result = number1 / number2
            else:
                result = "Error: Division by zero"
        
        st.success(f"Result: {result}")
        st.button("Clear Result")

