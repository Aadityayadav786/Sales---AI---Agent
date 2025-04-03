import streamlit as st
from agents import process_lead, send_email

st.title("AI-Powered Lead Engagement System")
st.write("Fill in the details below to receive a personalized response.")

with st.form("lead_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    interest = st.selectbox("Your Interest", ["", "Product Inquiry", "Demo Request", "Pricing Information", "Offers"])
    expectations = st.text_area("What do you expect from us?")
    submitted = st.form_submit_button("Submit")

if submitted:
    if name and email:
        lead_data = {"name": name, "email": email, "interest": interest, "expectations": expectations}
        result = process_lead(lead_data) 
        if result:
            subject = result["subject"]
            body = result["body"]
            send_email(email, subject, result["body"])
            st.success("Email sent successfully!")
            st.subheader("Generated Email:")
            st.text_area("Email Content", result["body"], height=300)
            st.subheader("Lead Score:")
            st.write(result["lead_score"])
        else:
            st.error("No potential lead found.")
    else:
        st.error("Please enter your name and email.")
