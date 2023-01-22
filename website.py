import streamlit as st
import functions
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Recipe Rcommendation", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_tll0j4bb.json")

# ---- HEADER SECTION ----
with st.container():
    st.title("Recipe Recommendation Website")
    st.subheader("Are you missing ideas about recipes? Let us recommend it to you!")
    st.write("This website is designed to enhance your enjoyment of life.")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How this web will help you?")
        st.write("##")
        st.write(
            '''
            Do you have a few ingredients but no clue how to cook with them? 
            Do you want to try some new recipes? 
            Let the recipe recommendations help you! 
            All you have to do is enter the ingredients you want to use below 
            and we'll suggest some great recipe ideas for you!
            '''
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


def add_ingredient():
    ingredient = st.session_state["new_ingredient"] + "\n"
    ingredientList.append(ingredient)
    functions.write_ingredients(ingredientList)
ingredientList = functions.get_ingredients()

with st.container():
    st.write("---")
    st.header("Please type the ingredients you want to use")
    st.empty()
    st.text_input(label="", placeholder="Add an ingredient...",
                           on_change=add_ingredient, key='new_ingredient')

    if ingredientList:
        for index, ingredient in enumerate(ingredientList):
            checkbox = st.checkbox(ingredient, key=ingredient)
            if checkbox:
                ingredientList.pop(index)
                functions.write_ingredients(ingredientList)
                del st.session_state[ingredient]
                st.experimental_rerun()

import re
collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]

numbers = st.text_input("PLease enter numbers")
st.write(collect_numbers(numbers))

fixed_numbers = st.multiselect("Please select numbers", [1, 2, 3, 4, 5])
st.write(fixed_numbers)