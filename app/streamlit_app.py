import altair as alt
import pandas as pd
import streamlit as st
import os
import europa


#import variable environnement
storage_account_name = os.environ["STORAGE_ACCOUNT_NAME"]
storage_account_key = os.environ["STORAGE_ACCOUNT_KEY"]

result = europa.manipulate_table(storage_account_name,
                 storage_account_key,
                 "test",
                 "read")

st.set_page_config(
    page_title="SALEFORCE -  TABLEMANAGER", page_icon="⬇", layout="centered"
)

st.title("Table Manager Saleforce")


edited_df = st.data_editor(result, num_rows="dynamic")
