import streamlit as st



pages = {
    "Main Page":[
        st.Page("pages/Home.py" , title="Home" , icon=":material/home:" , default=True)
    ],
    "Quick Access":[
        st.Page("pages/About.py" , title="About" , icon=":material/info:"),
        st.Page("pages/Blog.py" , title="Blog" , icon=":material/rss_feed:"),
        st.Page("pages/ED1.py" , title="Q&A" , icon=":material/psychology_alt:"),
        st.Page("pages/Contact.py" , title="Contact Us" , icon=":material/phone_in_talk:"),
    ],
}

st.logo("Pictures/image_2.png")
pg = st.navigation(pages)
pg.run()



