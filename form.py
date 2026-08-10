import streamlit as st

st.title("Feedback form")

with st.form("form_id"):
	col1, col2 = st.columns(2)

	with col1:
		name = st.text_input("Full name")
		email = st.text_input("Email")

	with col2:
		phone_number = st.text_input("Phone number")
		gender = st.radio("Select your gender:", ["male", "female", "others"])
		st.write(f"You selected: {gender}")

	feedback = st.text_area("Your feedback", max_chars=300)
	st.caption(f"{len(feedback)}|300 characters")
	submitted = st.form_submit_button("Submit feedback")

if submitted:
	st.success(f"Thanks: {name}: your feedback has been received")
