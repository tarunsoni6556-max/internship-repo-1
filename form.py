import streamlit as st

st.title("Feedback Form")

with st.form("form_id"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("full name")
        email = st.text_input("email")
    with col2:
        phone_number = st.text_input("phone number")
        gender = st.radio("gender", ["male", "female", "other"])
        st.write(f"you selected {gender}")
        
        feedback = st.text_area("Your Feedback" , max_chars=300)
        st.caption(f"{len(feedback)}/300 characters")
        submitted = st.form_submit_button("Submit feedback")

        if submitted:
            st.success(f"Thanks: {name} : your feedback has been submitted successfully")
            