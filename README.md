# 🏦 Intelligent Bank Management System

### *An Object-Oriented, GUI-Driven Financial Application*

---

## 📌 Overview

This project is a **modular banking system** implemented in Python, designed using **Object-Oriented Programming (OOP)** principles and enhanced with a **Streamlit-based graphical user interface (GUI)**.

The system simulates real-world banking operations including:

* Account creation (Saving / Commercial)
* Secure login system
* Deposit & withdrawal operations
* Balance management
* Account updates
* Interest (benefit) application
* Persistent data storage (CSV)

The architecture follows a **layered design pattern**, enabling scalability, maintainability, and future integration with databases or APIs.

---

## 🎯 Objectives

* Apply **advanced OOP concepts** in a real-world system
* Build a **user-friendly GUI** using Streamlit
* Implement **data persistence** using Pandas
* Design a system following **clean architecture principles**
* Provide a foundation for **future AI / FinTech extensions**

---

## 🧠 Core Concepts Applied

| Concept                    | Implementation                                 |
| -------------------------- | ---------------------------------------------- |
| Abstract Classes           | `AbstractBankAccount`                          |
| Encapsulation              | Private attributes (`__balance`, `__password`) |
| Inheritance                | `SavingAccount`, `CommercialAccount`           |
| Polymorphism               | Overriding `take()` method                     |
| Data Abstraction           | Data handling layer (`data_handler.py`)        |
| Separation of Concerns     | Model / Service / Data / UI                    |
| State Management           | `st.session_state` (Streamlit)                 |
| Vectorized Data Processing | Pandas DataFrame operations                    |

---

## 🏗️ System Architecture

```text
┌───────────────────────┐
│     Streamlit GUI     │   ← app.py
└──────────┬────────────┘
           │
┌──────────▼────────────┐
│    Service Layer      │   ← bank_service.py
└──────────┬────────────┘
           │
┌──────────▼────────────┐
│     Data Layer        │   ← data_handler.py
└──────────┬────────────┘
           │
┌──────────▼────────────┐
│     Model Layer       │   ← bank_account.py
└───────────────────────┘
```

---

## 📂 Project Structure

```bash
project/
│
├── bank_account.py      # Core OOP classes (Model Layer)
├── data_handler.py      # CSV data management (Data Layer)
├── bank_service.py      # Business logic (Service Layer)
├── app.py               # Streamlit GUI (Presentation Layer)
│
└── data/
    └── information.csv  # Persistent storage
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/RayanShaiaa-cmd/Bank-System-GUI-Python-.git
cd "Bank System GUI"
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit pandas
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Then open the local URL provided by Streamlit (usually):

```
http://localhost:8501
```

---

## 🖥️ Features

### 🔐 Authentication

* Register new accounts
* Login validation using stored credentials

### 💰 Financial Operations

* Deposit (with transaction fee)
* Withdraw (with validation)
* Overdraft support (Commercial Account)

### 📊 Account Management

* View account details
* Update balance manually
* Update account credentials

### 📈 Smart Features

* Apply benefit (interest) for Saving Accounts
* Dynamic account type handling

---

## 🧪 Example Workflow

1. Register a new account
2. Login using credentials
3. Perform transactions:

   * Deposit funds
   * Withdraw funds
4. Apply benefit (Saving account only)
5. Update account details
6. Persist all changes automatically

---

## 🔐 Security Considerations

⚠️ Current implementation stores passwords in **plain text**.

### Recommended Upgrade:

Use hashing:

```python
import hashlib
hashed_password = hashlib.sha256(password.encode()).hexdigest()
```

---

## 📊 Data Storage Format

Stored in:

```
data/information.csv
```

### Schema:

| Column       | Description           |
| ------------ | --------------------- |
| Name         | Account holder        |
| Password     | User password         |
| Account type | Saving / Commercial   |
| Created date | Account creation date |
| Balance      | Current balance       |

---

## 🚀 Future Enhancements

### 🔧 Backend Improvements

* Replace CSV with **PostgreSQL / MySQL**
* Add ORM (SQLAlchemy)

### 🤖 AI Integration

* Chatbot banking assistant
* Fraud detection model
* Spending analysis

### 📊 Data Visualization

* Transaction analytics dashboard
* Monthly reports (charts)

### 🌐 Deployment

* Deploy via Streamlit Cloud / Docker
* Convert into REST API (FastAPI)

---

## 📈 Performance Considerations

* Uses **vectorized Pandas operations** instead of loops
* Minimal I/O operations via centralized data handler
* Modular structure supports scalability

---

## 🧑‍💻 Developer Notes

* Designed for **educational + production transition**
* Code is structured for:

  * Easy debugging
  * Clear extensibility
  * Clean separation of logic

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍🎓 Author

**Rayan Shaiaa**
AI Student | Python Developer | Future ML Engineer

---

## ⭐ Final Note

This project is not just a banking simulation —
it is a **foundation for building real financial systems** using:

* Clean Architecture
* OOP Best Practices
* GUI Development
* Data Handling

---

> 💡 *If you found this useful, consider starring the repository.*
