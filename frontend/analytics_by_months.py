import streamlit as st
import requests
import pandas as pd
API_URL = "http://localhost:8000"

def analytics_by_month_tab():
    response = requests.post(f"{API_URL}/analytics/monthly")

    if response.status_code != 200:
        st.error("Failed to fetch monthly analytics")
        st.text(response.text)
        return

    data = response.json()

    # Build a dict: month -> total
    month_totals = {}
    for month, categories in data.items():
        if isinstance(categories, dict):
            # If categories is a dict of category totals
            total_amount = sum(details["total"] for details in categories.values())
        else:
            # If it's already a float (total for the month)
            total_amount = categories
        month_totals[month] = total_amount

    # Convert to DataFrame
    df = pd.DataFrame(list(month_totals.items()), columns=["Month", "Total"])

    # Convert YYYY-MM → datetime for proper sorting
    df["Month_dt"] = pd.to_datetime(df["Month"], format="%Y-%m")
    df = df.sort_values("Month_dt").drop(columns=["Month_dt"])

    # Optional: display Month nicely
    df["Month"] = pd.to_datetime(df["Month"], format="%Y-%m").dt.strftime("%B %Y")

    st.title("Expense Breakdown by Months")

    # Bar chart
    st.bar_chart(
        df.set_index("Month")["Total"],
        use_container_width=True
    )

    # Format table
    df["Total"] = df["Total"].map("{:,.2f}".format)
    st.table(df)
