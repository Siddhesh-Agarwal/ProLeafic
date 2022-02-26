import streamlit as st

st.title("Diagnostic Test")

q1 = st.selectbox(
    label="What is the type of crop?",
    options=["Cash crops", "Ornamental plants", "Long-term plants"],
)
if q1 == "Cash crops":
    q2 = st.selectbox(
        label="What is the crop?",
        options=[
            "Broccoli",
            "Cucumber",
            "Potatoes",
            "Raspberry",
            "Strawberry",
            "Squash",
            "Sugarcane",
            "Tomatoes",
        ],
    )
    if q2 == "Tomatoes":
        q3 = st.multiselect(
            label="What is/are the symptoms?",
            options=["mottled yellow and green leaves", "curled and distorted leaves"],
        )
        if set(q3) == {
            "mottled yellow and green leaves",
            "curled and distorted leaves",
        }:
            endpoint = "mosaic-virus"
if q1 == "Ornamental plants":
    q2 = st.selectbox(
        label="What is the plant?",
        options=[
            "Lupines",
            "Roses",
        ],
    )
if q1 == "Long-term plants":
    q2 = st.selectbox(
        label="What is the plant?",
        options=[
            "Apple",
            "Apricots",
            "Cherries",
            "Haskaps",
            "Gooseberry",
            "Maple",
            "Peaches",
            "Plums",
        ],
    )


st.markdown(
    "[Click here to see results](../Diseases/#{endpoint})", unsafe_allow_html=True
)
