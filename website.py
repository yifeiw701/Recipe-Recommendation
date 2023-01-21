import streamlit as st
import functions

def add_ingredient():
    ingredient = st.session_state["new_ingredient"] + "\n"
    ingredientList.append(ingredient)
    functions.write_ingredients(ingredientList)

ingredientList = functions.get_ingredients()

st.title("Recipe Recommendation Website")
st.subheader("Are you missing ideas about recipes? Let us recommend it to you!")
st.write("This website is designed to enhance your enjoyment of life.")

if ingredientList:
    for index, ingredient in enumerate(ingredientList):
        checkbox = st.checkbox(ingredient, key=ingredient)
        if checkbox:
            ingredientList.pop(index)
            functions.write_ingredients(ingredientList)
            del st.session_state[ingredient]
            st.experimental_rerun()

placeholder = st.empty()
placeholder.text_input(label = "", placeholder = "Add another ingredient...",
              on_change = add_ingredient, key= 'new_ingredient')

