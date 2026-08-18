import streamlit as st

st.set_page_config(
    page_title="Phone Number Counter",
    page_icon="📞"
)
st.title("Phone Number Counter")
st.write("This app counts the number of phone numbers in a given text.")    
st.header("Input Text")
text_input = st.text_area("Enter your text here:", height=200)
st.header("Count Phone Numbers")
st.write("The app will count the number of phone numbers in the text you provided.")
st.write("Note: The app recognizes phone numbers in the format (XXX) XXX-XXXX, XXX-XXX-XXXX, or XXXXXXXXXX.")
if st.button("Count Phone Numbers"):    
    import re
    phone_number_pattern = r'(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{10})'
    phone_numbers = re.findall(phone_number_pattern, text_input)
    count = len(phone_numbers)
    st.success(f"Number of phone numbers found: {count}")
    if count > 0:
        st.write("Phone Numbers Found:")
        for number in phone_numbers:
            st.write(number)
            st.write("Note: The app may not recognize all phone number formats. Please ensure your phone numbers are in the correct format for accurate counting.")
