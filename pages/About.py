import streamlit as st
from streamlit_option_menu import option_menu as om

st.set_page_config(page_icon="Pictures/ajfa.png" , page_title="AJF" , layout="wide" , initial_sidebar_state="auto")





st.markdown("""
<style>
        .st-emotion-cache-1es31n7.ezrtsby2{
            visibility: hidden;
        }
        .st-emotion-cache-1waqu2p.ezrtsby2{
            visibility: hidden;
        } 
        .block-container.st-emotion-cache-1jicfl2.ea3mdgi5{
            margin-top: -110px;
        }
            img[data-testid="stLogo"] {
            height: 6.5rem;
}                     
</style>
""" , unsafe_allow_html=True)




st.markdown("""

<style>
        .st-emotion-cache-1laooe4.eczjsme9{
            visibility: hidden;
        }
        .st-emotion-cache-79elbk.eczjsme10{
            margin-top:-85px;
        }
        .st-emotion-cache-j7qwjs.eczjsme7{
            margin-top:-5px;
        }
</style>

""" , unsafe_allow_html=True)

with st.sidebar:
    btn = st.button(":material/emoji_objects:" , use_container_width=True)
    
    dark = '''
        <style>
            .stApp {
            background-color: "#1f1f21";
            color: white;
            body {
            color: white;
            }

            h1 {
            color: white;
            }

            div {
              color: white;
            }

                }
            }
        </style>
        '''

    light = '''
        <style>
            .stApp {
           
            .st-emotion-cache-15eij9r.eqpbllx1:hover{
            background-color: #3480de;
            }
            background-color:#e3e4e8;
            color: black;

            p{
            color: black;
            }
           
            h1 {
            color: black;
            text-align: center;
            font-size: 200px;
            }
            h2 {
            color: black;
            }
            h3 {
            color: black;
            }
            h4 {
            color: black;
            }
            h5 {
            color: black;
            }
            h6 {
            color: black;
            }

           

                }
        </style>'''

    st.markdown(dark, unsafe_allow_html=True)
    # Create a toggle button
    # Use a global variable to store the current theme
    if "theme" not in st.session_state:
        st.session_state.theme = "#1f1f21"
    # Change the theme based on the button state
    if btn:
        if st.session_state.theme == "#e3e4e8":
            st.session_state.theme = "#1f1f21"
        else:
            st.session_state.theme = "#e3e4e8"    # fffffffff

    # Apply the theme to the app
    if st.session_state.theme == "#1f1f21":
        st.markdown(dark, unsafe_allow_html=True)
    else:
        st.markdown(light, unsafe_allow_html=True)
        st.logo("Pictures/icon.ico")





import time


st.markdown("""
<style>
        p {
  font-size: 30px;
}        
</style>
""" , unsafe_allow_html=True)


_LOREM_IPSUM = """
My name is **Alireza Jafari** and I am a computer engineering student from the electronics department




For the e-commerce course, I made an implementation with Pinon programming language to collect a data set from Azad University students of the e-commerce unit in relation to the topic of how to research the e-commerce unit students, and then we extracted the data visually so that I could I will use it in my research
"""
def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.1)
  
time.sleep(1)
st.write_stream(stream_data)


st.markdown("""

<style>
        .st-emotion-cache-geq37u.eczjsme9{
            visibility: hidden;
        }
        .st-emotion-cache-79elbk.eczjsme10{
            margin-top:-95px;
        }
</style>

""" , unsafe_allow_html=True)









def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html=True)
load_css("style/footer_style.css")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.divider()
with st.container():
    c1 , c2 , c3 = st.columns([1,1,1])

    with c1:
        st.header("Mission")
        st.markdown("<h4>The goal of AJF AI is to advance and develop web apps in line with the development of researches in the field of computer engineering.</h4>" , unsafe_allow_html=True)
    with c2:
        c4,c5,c6 = st.columns([1,1,1])
        with c5:
            st.header("Pages")
            st.page_link("pages/Home.py" , label="Home")
            st.page_link("pages/About.py" , label="About")
            st.page_link("pages/Blog.py" , label="Blog")
            st.page_link("pages/ED1.py" , label="Q&A")
            st.page_link("pages/Contact.py" , label="Contact")
        #st.markdown("<div style='text-align:center;'><a>Home</a></div>" , unsafe_allow_html=True)
        #st.markdown("<div style='text-align:center;'><a>About</a></div>" , unsafe_allow_html=True)
        #st.markdown("<div style='text-align:center;'><a>Blog</a></div>" , unsafe_allow_html=True)
        #st.markdown("<div style='text-align:center;'><a>Contact</a></div>" , unsafe_allow_html=True)
        
        
        
       
    with c3:
        c4,c5,c6 = st.columns([1,2.5,0.4])
        with c5:
            st.header("Contact Info")
        css_icon="""
        <div style='text-align:center;'>

        <i class="fa-solid fa-envelope"> </i> admin@ajfai.com

        <i class="fa-sharp fa-solid fa-phone"></i> +98 9120638732

        <i class="fa-solid fa-location-dot"></i> Karaj-Alborz-Iran
        </div>
        """
        st.markdown(css_icon , unsafe_allow_html=True)

        c4,c5,c6 = st.columns([1,2.5,0.2])
        with c5:
            st.header("Social Media")
        css_icon1="""
        <div style='text-align:center;'>

        <a style='color:#3480de; text-decoration: none;' href='https://instagram.com'><i class="fa-brands fa-instagram"></i></a>
        <a style='color:#3480de; text-decoration: none;' href='https://twitter.com'><i class="fa-brands fa-x-twitter"></i></a>
        <a style='color:#3480de; text-decoration: none;' href='https://youtube.com'><i class="fa-brands fa-youtube"></i></a>
        <a style='color:#3480de; text-decoration: none;' href='https://linkedin.com'><i class="fa-brands fa-linkedin"></i></a>
        <a style='color:#3480de; text-decoration: none;' href='https://github.com'><i class="fa-brands fa-github"></i></a>
        </div>
        """
        st.markdown(css_icon1 , unsafe_allow_html=True)




































