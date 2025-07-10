import streamlit as st

st.title("📧 CleanMail: Email Address Cleaner")

input_emails = st.text_area("Paste your email addresses here (separated by comma or newline):")

def clean_email(email):
    local, domain = email.strip().split("@")
    local = local.split("+")[0]  # remove after +
    local = local.replace(".", "")  # remove dots
    return f"{local}@{domain}"

if st.button("Clean Emails"):
    raw_emails = [e.strip() for e in input_emails.replace(",", "\n").splitlines() if e.strip()]
    cleaned_emails = set(clean_email(email) for email in raw_emails)
    
    st.subheader("✅ Cleaned Unique Emails")
    st.write("\n".join(cleaned_emails))
    st.success(f"Total unique emails: {len(cleaned_emails)}")

    email_text = "\n".join(cleaned_emails)
    
    st.download_button(
        label="📥 Download Cleaned Emails",
        data=email_text,
        file_name='cleaned_emails.txt',
        mime='text/plain'
    )

