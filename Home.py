# for animation use Lottie files
# importing libraries:-
# Pillow library for inserting images
# to insert a fully function contact form use the free service of form submit
# for icons go to the bootstrap icon website

from PIL import Image
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
# webFx site name for icon go there and insert the code name

st.set_page_config(
    page_title= "Home Page",
    page_icon = ":tada:",
    layout="wide",
)

# a new function to acess the data from the lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("C:\\Users\\Acer\\OneDrive\\Desktop\\Webpage\\style\\style.css")

# --- Load Assets --- (from lottiefiles.com)
lottie_coding = load_lottieurl(
    "https://lottie.host/8e891be2-7fff-461f-83e2-5138d8edfbcc/6ZiNes5DlB.json"
)
img_lottie_animation = Image.open(
    "C:\\Users\\Acer\\OneDrive\\Desktop\\Webpage\\images\\file1.png"
)
img_contact_form = Image.open(
    "C:\\Users\\Acer\\OneDrive\\Desktop\\Webpage\\images\\file2.png"
)

# Header section
with st.container():
    st.subheader("Hi, I am Himanshu :wave:")
    st.title("A student form India")
    st.write(
        "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
    )
    st.write("[Learn more >](https://www.youtube.com/channel/UCgnqUY7tNvgCMyqijuqOH-w)")

# --- What I do ---
with st.container():
    st.write("---")  # we use this to add divider
    left_column, right_cloumn = st.columns(2)
    with left_column:
        st.header("Know About Us")
        st.write("##")  # we use this to add space in our website
        st.write(
            """
        Welcome to [Website Name], your go-to destination for comprehensive video topic solutions and video mock test solutions. We are passionate about helping students and learners excel in their studies by providing high-quality educational resources that cater to a variety of subjects and topics."""
        )
        st.write("[Youtube Link >](https://www.youtube.com/)")

    with right_cloumn:
        st_lottie(lottie_coding, height=300, key="education")

#  Projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns(
        (1, 2)
    )  # this shows the second column should be twice as big as the image
    with image_column:
        st.image(img_lottie_animation)

    with text_column:
        st.subheader("Some of my work is projected here")
        st.write(
            """
            It looks like you're requesting information related to mathematics. Could you please provide more specific details about what you're looking for? Are you looking for explanations of specific math concepts, equations, formulas, or something else related to mathematics? The more details you provide, the better I can assist you with your math-related inquiry.
            """
        )
        st.markdown(
            "[Watch Video...](https://youtube.com/@amrendrachaudhary4795?si=cXl-gMp293NkgTDt)"
        )

with st.container():
    st.write("##")
    image_column, text_column = st.columns(
        (1, 2)
    )  # this shows the second column should be twice as big as the image
    with image_column:
        st.image(img_contact_form)

    with text_column:
        st.subheader("Some of my work is projected here")
        st.write(
            """
            To resolve this issue, you need to ensure that the paths in your code are correctly formatted to avoid Unicode escape errors. Here are a few steps you can take
            """
        )
        st.markdown(
            "[Watch Video...](https://youtube.com/@amrendrachaudhary4795?si=cXl-gMp293NkgTDt)"
        )

# Contact form
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/htechinfoes@gmail.com.com" method="POST">
        <input type = "hidden" name = "_captcha" value= "false" >
        <input type="text" name="name" placeholder = "Your name" required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name = "message" placeholder = "Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_cloumn = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_cloumn:
        st.empty()

# # 1. as side bar menu
# with st.sidebar:
#     selected = option_menu(
#         menu_title=None,  # required
#         options=["Home", "Topic-wise", "Mock-Test"],  # required
#         icons=["house", "play-btn", "file-pdf"],
#         menu_icon="cast",
#         default_index=0,
#         styles={
#             "container": {"padding": "0!important", "background-color": "#fafafa"},
#             "icon": {"color": "orange", "font-size": "25px"},
#             "nav-link": {
#                 "font-size": "25px",
#                 "text-align": "left",
#                 "margin": "0px",
#                 "--hover-color": "#eee",
#             },
#             "nav-link-selected": {"background-color": "green"},
#         },
#     )

# # 2. as horizontal
# # with st.sidebar:
# #     selected = option_menu(
# #         menu_title="Main Menu", #required
# #         options=["Home", "Videos", "Pdf"], # required
# #         icons = ["house", "play-btn", "file-pdf"],
# #         menu_icon= "cast",
# #         default_index=0,
# #         orientation= "horizontal",
# #     )

# if selected == "Home":
#     st.title(f"You have selected {selected}")
# if selected == "Topic-wise":
#     st.title(f"You have selected {selected}")
# if selected == "Mock-Test":
#     st.title(f"You have selected {selected}")

