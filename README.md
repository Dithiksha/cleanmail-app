# 📧 CleanMail: Email Address Cleaner

A simple Streamlit app to clean and deduplicate email addresses by removing dots (`.`) and ignoring characters after plus signs (`+`) in the local part of the email.

---

## ✨ Features

- ✅ Clean messy email lists
- ✂️ Remove dots and `+` tags
- 🔁 Get unique email addresses
- 📥 Download cleaned results as `.txt`

---

## 🚀 How to Run This App

Make sure you have Python and Streamlit installed.

### 🧪 Step-by-step:

```bash
# 1. Install Streamlit if not already installed
pip install streamlit

# 2. Navigate to your app folder
cd C:\Users\hp\python\cleanmail-app\cleanmail-app

# 3. Run the app using Python's full path (your working one)
& "C:\Users\hp\AppData\Local\Microsoft\WindowsApps\python3.11.exe" -m streamlit run app.py

---

## 🧪 Test Cases

Try these sample inputs in the app after launching it (`http://localhost:8501`):

### ✅ Test Case 1: Simple duplicates

ab.c+hello@leetcode.com,
abc@leetcode.com,
a.bc+test@leetcode.com

**Expected Output:**

abc@leetcode.com


### ✅ Test Case 2: With spaces and similar addresses

user.name+tag@example.com,
user.name@example.com,
username@example.com

**Expected Output:**
username@example.com


### ✅ Test Case 3: Different domains
test.email+1@gmail.com,
test.email@gmail.com,
testemail@yahoo.com

**Expected Output:**
testemail@gmail.com
testemail@yahoo.com

### ✅ Test Case 4: Newline-separated input
hello.world+spam@abc.com
helloworld@abc.com


**Expected Output:**
helloworld@abc.com


### ✅ Final Tip:
After clicking "Clean Emails", hit the **📥 Download Cleaned Emails** button to get your `.txt` file of results.
