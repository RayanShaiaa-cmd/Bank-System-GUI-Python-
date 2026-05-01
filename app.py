import streamlit as st
from bank_account import SavingAccount, CommercialAccount
from bank_service import BankService
import data_handler as db

st.set_page_config(page_title="Bank System", layout="centered")

st.title("🏦 Bank System")

menu = ["Register", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

# ================= REGISTER =================
if choice == "Register":
    st.subheader("Create Account")

    name = st.text_input("Name")
    password = st.text_input("Password", type="password")
    acc_type = st.selectbox("Account Type", ["Saving", "Commercial"])

    if st.button("Create Account"):
        if acc_type == "Saving":
            acc = SavingAccount(name, password)
            acc_type_str = "Saving Account"
        else:
            acc = CommercialAccount(name, password)
            acc_type_str = "Commercial Account"

        db.save_info(name, acc.balance, password, acc_type_str, acc.date)
        st.success("Account created successfully")

# ================= LOGIN =================
elif choice == "Login":
    st.subheader("Login")

    name = st.text_input("Name")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        status, data = db.login(name, password)

        if status:
            st.session_state["user"] = data
            st.success("Login successful")
        else:
            st.error("Invalid credentials")

# ================= DASHBOARD =================
if "user" in st.session_state:
    name, password, acc_type, date, balance = st.session_state["user"]

    if acc_type == "Saving Account":
        account = SavingAccount(name, password, date, balance)
    else:
        account = CommercialAccount(name, password, date, balance)

    service = BankService(account, acc_type)

    st.header("Dashboard")

    st.write(f"👤 Name: {account.name}")
    st.write(f"💰 Balance: {account.balance}")

    option = st.selectbox(
        "Choose Operation",
        [
            "Deposit",
            "Withdraw",
            "Update Balance",
            "Update Info",
            "Show Info",
            "Apply Benefit",
        ],
    )

    amount = st.number_input("Amount", min_value=0.0)

    if option == "Deposit" and st.button("Execute"):
        res = service.deposit(amount)
        st.success(res if res["status"] else res["msg"])

    elif option == "Withdraw" and st.button("Execute"):
        res = service.withdraw(amount)
        st.success(res if res["status"] else res["msg"])

    elif option == "Update Balance" and st.button("Execute"):
        new_balance = service.update_balance(amount)
        st.success(f"Updated: {new_balance}")

    elif option == "Update Info":
        new_name = st.text_input("New Name")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Update"):
            service.update_account(new_name, new_pass)
            st.success("Updated successfully")

    elif option == "Show Info":
        st.json(account.show_info())

    elif option == "Apply Benefit" and st.button("Execute"):
        res = service.apply_benefit()
        if res:
            st.success(res)
        else:
            st.error("Not available for this account")

    if st.button("Logout"):
        del st.session_state["user"]
        st.rerun()