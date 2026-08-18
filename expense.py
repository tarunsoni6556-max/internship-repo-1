import streamlit as st

st.set_page_config(
    page_title="Expense Tracker",
    page_icon=":money_with_wings:",
    layout="wide"
)

st.title("Expense Tracker")
st.write("Welcome to expense tracker")

col1, col2 = st.columns(2)
with col1, col2:
    st.header("Add Expense")
    with st.form("expense_form"):
        expense_name = st.text_input("Expense Name")
        expense_amount = st.number_input("Expense Amount", min_value=0.0, step=0.01)
        expense_category = st.selectbox("Expense Category", ["Food", "Transport", "Entertainment", "Other"])
        submit_button = st.form_submit_button(label="Add Expense")

    if submit_button:
        st.success(f"Added expense: {expense_name} - ${expense_amount:.2f} in category {expense_category}")
st.button("View Expenses")
with st.expander("View Expenses"):
    st.write("Here you can view your expenses.")
    # Placeholder for displaying expenses
    st.write("No expenses to display yet.")
   