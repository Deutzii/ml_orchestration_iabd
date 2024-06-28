import streamlit as st
import requests

st.title("FastAPI and Streamlit Integration")

# Fetch data from the FastAPI endpoint
response = requests.get("http://127.0.0.1:8000/")
if response.status_code == 200:
    data = response.json()
    st.write(data)
else:
    st.write("Failed to fetch data from FastAPI")

# Fetch data for a specific item
item_id = st.number_input("Enter item ID", min_value=0, value=0)
if st.button("Get Item"):
    response = requests.get(f"http://127.0.0.1:8000/items/{item_id}")
    if response.status_code == 200:
        item_data = response.json()
        st.write(item_data)
    else:
        st.write("Item not found")
