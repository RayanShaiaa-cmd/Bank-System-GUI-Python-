import pandas as pd
import os

FILE_PATH = "data/information.csv"


def load_data():
    if not os.path.exists("data"):
        os.mkdir("data")

    if not os.path.exists(FILE_PATH):
        return pd.DataFrame(
            columns=["Name", "Password", "Account type", "Created date", "Balance"]
        )

    return pd.read_csv(FILE_PATH)


def save_data(df):
    df.to_csv(FILE_PATH, index=False)


def save_info(name, balance, password="", account_type="", created_date=""):
    df = load_data()

    if name in df["Name"].values:
        df.loc[df["Name"] == name, "Balance"] = balance
    else:
        new_row = pd.DataFrame(
            [
                {
                    "Name": name,
                    "Password": password,
                    "Account type": account_type,
                    "Created date": created_date,
                    "Balance": balance,
                }
            ]
        )
        df = pd.concat([df, new_row], ignore_index=True)

    save_data(df)


def update_info(old_name, password, new_name, new_password):
    df = load_data()

    mask = (df["Name"] == old_name) & (df["Password"].astype(str) == str(password))

    df.loc[mask, "Name"] = new_name
    df.loc[mask, "Password"] = new_password

    save_data(df)


def login(name, password):
    df = load_data()

    user = df[
        (df["Name"] == name) & (df["Password"].astype(str) == str(password))
    ]

    if user.empty:
        return False, None

    row = user.iloc[0]

    return True, (
        row["Name"],
        row["Password"],
        row["Account type"],
        row["Created date"],
        row["Balance"],
    )