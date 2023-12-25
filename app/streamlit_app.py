import altair as alt
import pandas as pd
import streamlit as st
import os
import europa


#import variable environnement


result = europa.manipulate_table("stodsalesforcemag000",
                 "",
                 "test",
                 "read")

st.set_page_config(
    page_title="SALEFORCE -  TABLEMANAGER", page_icon="⬇", layout="centered"
)

st.title("Table Manager Saleforce")
