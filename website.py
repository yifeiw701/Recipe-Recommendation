import streamlit as st
import requests
from streamlit_lottie import st_lottie
from bs4 import BeautifulSoup

st.set_page_config(page_title="Recipe Rcommendation", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_coding1 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_jbt4j3ea.json")
lottie_coding2 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_tll0j4bb.json")

# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns([3, 2])
    with left_column:
        st.title("Recipe Recommendation Website")
        st.subheader("Are you missing ideas about recipes? Let us recommend it to you!")
        st.write("This website is designed to enhance your enjoyment of life.")
    with right_column:
        st_lottie(lottie_coding1, height=300, key="coding1")

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
        st_lottie(lottie_coding2, height=300, key="coding2")

with st.form("Search"):
    st.header("Please type the ingredients you want to use")
    keywords = st.text_input(label="", placeholder="Please type the ingredients you want to use").split(',')
    search = st.form_submit_button("Search")
    if search:
        page = 'https://www.delish.com/search/?q=' + keywords[0]
        html_text = requests.get(page).text
        soup = BeautifulSoup(html_text, 'lxml')
        recipes = soup.find_all('a', class_='enk2x9t2 css-1jsxw8p epl65fo4')

        counter = 0
        for recipe in recipes:
            recipe_link = 'http://www.delish.com' + recipe['href']
            recipe_text = requests.get(recipe_link).text
            soup1 = BeautifulSoup(recipe_text, 'lxml')

            ingredients = soup1.find_all('li', class_='css-1rmzm7g eno1xhi2')
            ingredient_str = ""
            for e in ingredients:
                ingredient = e.p.text
                ingredient_str += ingredient
                # ingredient_str = ingredient_str.replace(',', ' ')
            # ingredient_list = ingredient_str.split(' ')

            if all(x in ingredient_str for x in keywords):
                recipe_name = recipe.find('span', class_='css-13cdu9y e1rluvgc5').text
                st.write(f"[{recipe_name}](%s)" % recipe_link)
                recipe_img = recipe.find('div', class_='__resp-container lqip css-bc6d9y enk2x9t1').img[
                    'data-src']  # .split('?')[0]
                st.image(recipe_img)
                counter += 1
                if counter > 4:
                    break
