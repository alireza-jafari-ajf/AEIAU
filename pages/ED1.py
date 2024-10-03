import streamlit as st
import hmac
from time import sleep
from pandas import DataFrame , read_sql_query
from plotly import express as px
from streamlit_option_menu import option_menu as om
from db import create_table , add_data , view_all_data , get_task , view_unique_task , add_data1 , add_data2 , add_data3 , add_data4 , add_data2_foreign , add_data3_foreign , add_data4_foreign , add_data2_irf , add_data3_irf

st.set_page_config(page_icon="Pictures/ajfa.png" , page_title="Entry Data Sets 1" , layout="wide" , initial_sidebar_state="auto")

st.markdown("""
<style>
        .st-emotion-cache-1es31n7.ezrtsby2{
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
        .st-emotion-cache-1waqu2p.ezrtsby2{
            visibility: hidden;        
</style>
""" , unsafe_allow_html=True)


#----------------------------------------------------------Sidebar------------------------------------------------------------

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

            div.user-select-none.svg-container{
            background-color: white;
            }
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
    page1 = om(menu_title="The First Article",
                     options=["Entry Data Sets" , "Article 1"],
                     default_index=0,
                     icons=["folder", "book"],
                     orientation="horizontal",
                     styles={

                                   "icon": {"color": "white", "font-size": "20px"}, 
                                   "nav-link": {"font-size": "20px", "margin-right":"40px" ,"--hover-color": "#002562"},

        }
              )
    


#----------------------------------------------------------Pages------------------------------------------------------------

st.markdown("""

<style>
        .st-emotion-cache-1z0x1vh.eczjsme6{
            visibility: hidden;
        }           
</style>
""" , unsafe_allow_html=True)

#----------------------------------------------------------Main------------------------------------------------------------

t1 , t2 , t3 = st.tabs(["Entry Form for Data Sets" , "Data Visualition" , "Data Set"])

with t1:
    try:
        with st.container(border=True):
            c1 , c2 = st.columns(2)
            create_table()
            with c1:
                fname = st.text_input(label="Q1: Please enter your first name: *" , max_chars=20 , placeholder="Alireza")
                lname = st.text_input(label="Q2: Please enter your last name: *" , max_chars=20 , placeholder="Jafari")
                age = st.number_input(label="Q3: How old are you? *" , min_value=18 , placeholder=22 , max_value=99)
            with c2:
                sex = st.selectbox(label="Q4: What is your gender? *" , options=[None , "Male" , "Female"] , index=0)
                education = st.selectbox(label="Q5: Please select your degree: *" , options=[None ,"Diploma" , "Associate degree" , "Bachelors degree" , "Master degree" , "PHD (Doctorate)" , "Postdoctoral Researcher"] , index=0)
                job = st.text_input(label="Q6: What is your Field of study in your university? *" , placeholder="Computer Engineering")

            use_academic_ai_tool = st.selectbox(label="Q7: Do you use a site to download articles to advance your academic work? *" , options=[None , "Yes" , "No"] , index=0)
            if use_academic_ai_tool == "Yes":
                app_or_web = st.selectbox("ًًQ8: Did you use Iranian sites or foreign sites? *" , options=[None , "Iranian sites" , "Foreign sites" , "Both"] , index=0)
                if app_or_web != None:

                    if app_or_web == "Iranian sites":
                        iranian_site = st.selectbox("Q9: Which Iranian sites do you use? *" , options=[None , "Civilica" , "MagIran" , "SID" , "Iranpaper" , "Freepaper" , "Irandoc"] , index=0)
                        if iranian_site != None:
                            web_browser = st.selectbox("Q10: In which web browser do you use this site the most? *" , options=[None , "Google Chrome" , "Firefox"] , index=0)
                            if web_browser != None:
                                mainq = st.selectbox(label=f"Q11: Were you satisfied with {iranian_site} site? *" , options=[None , "Yes" , "No"] , index=0)
                                if mainq != "No" and mainq != None:
                                    why_use = st.selectbox(label=f"Q12: Why do you use {iranian_site}? *" , options=[None , "Excellent specialized content" , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0)
                                    if why_use == "Other":
                                        another_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason")

                    if app_or_web == "Foreign sites":
                        foreign_site = st.selectbox("Q9: Which Foreign sites do you use? *" , options=[None , "Google Scholar" , "Springer" , "IEEE" , "sci-hub" , "Z-LIBRARY" , "Library Genesis" , "Unpaywall" , "ScienceDirect"] , index=0)
                        if foreign_site != None:
                            web_browser = st.selectbox("Q10: In which web browser do you use this site the most? *" , options=[None , "Google Chrome" , "Firefox"] , index=0)
                            if web_browser != None:
                                mainq = st.selectbox(label=f"Q11: Were you satisfied with {foreign_site} site? *" , options=[None , "Yes" , "No"] , index=0)
                                if mainq != "No" and mainq != None:
                                    why_use = st.selectbox(label=f"Q12: Why do you use {foreign_site}? *" , options=[None , "Excellent specialized content" , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0)
                                    if why_use == "Other":
                                        another_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason")

                    if app_or_web == "Both":
                        iranian_site = st.selectbox("Q9/1: Which Iranian sites do you use? *" , options=[None , "Civilica" , "MagIran" , "SID" , "Iranpaper" , "Freepaper" , "Irandoc"] , index=0)
                        foreign_site = st.selectbox("Q9/2: Which Foreign sites do you use? *" , options=[None , "Google Scholar" , "Springer" , "IEEE" , "sci-hub" , "Z-LIBRARY" , "Library Genesis" , "Unpaywall" , "ScienceDirect"] , index=0)
                        if iranian_site != None and foreign_site != None:

                            web_browser = st.selectbox("Q10: In which web browser do you use this sites the most? *" , options=[None , "Google Chrome" , "Firefox"] , index=0)
                            if web_browser != None:
                                mainq = st.selectbox(label="Q11: Were you satisfied with sites? *" , options=[None , "Yes" , "No"] , index=0)
                                if mainq != "No" and mainq != None:
                                    why_use = st.selectbox(label=f"Q12: Why do you use {iranian_site} and {foreign_site}? *" , options=[None , "Excellent specialized content" , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0)
                                    if why_use == "Other":
                                        another_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason")

            sbtn = st.button(label=":blue[Submit]" , type="primary")
            if sbtn:
            
                #----------------------------------Error-------------------------------------------
                if all(x.isalpha() == False or x.isspace() for x in fname):
                    st.error("Please enter your First Name (Q1)")
                    st.stop()

                if all(x.isalpha() == False or x.isspace() for x in lname):
                    st.error("Please enter your Last Name (Q2)")
                    st.stop()
                if sex == None:
                    st.error("Please Select your (Q4)")
                if education == None:
                    st.error("Please Select your (Q5)")
                if all(x.isalpha() == False or x.isspace() for x in job):
                    st.error("Please enter your Job (Q6)")
                    st.stop()


                if age == 30 and education== "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                if age == 29 and education== "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                if age == 28 and education== "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                if age == 27 and education== "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                if age == 26 and education== "PHD (Doctorate)":
                    st.error("You can not choose these options based on tradition [PHD (Doctorate)")
                    st.stop()
                elif age == 26 and education == "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                elif age ==25 and education == "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                elif age ==25 and education== "PHD (Doctorate)":
                    st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                    st.stop()
                elif age == 24 and education == "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                elif age == 24 and education== "PHD (Doctorate)":
                    st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                    st.stop()
                elif age ==23 and education == "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                elif age ==23 and education== "PHD (Doctorate)":
                    st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                    st.stop()
                elif age ==23 and education== "Master degree":
                    st.error("You can not choose these options based on tradition [Master degree]")
                    st.stop()
                elif age == 22 and education == "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                if age == 22 and education== "PHD (Doctorate)":
                    st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                    st.stop()
                elif age == 22 and education== "Master degree":
                    st.error("You can not choose these options based on tradition [Master degree]")
                    st.stop()
                elif age == 21 and education == "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                elif age == 21 and education== "PHD (Doctorate)":
                    st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                    st.stop()
                elif age == 21 and education== "Master degree":
                    st.error("You can not choose these options based on tradition [Master degree]")
                    st.stop()
                elif age == 21 and education == "Bachelors degree":
                    st.error("You can not choose these options based on tradition [Bachelors degree]")
                    st.stop()
                elif age == 20 and education == "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                elif age == 20 and education== "PHD (Doctorate)":
                    st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                    st.stop()
                elif age == 20 and education== "Master degree":
                    st.error("You can not choose these options based on tradition [Master degree]")
                    st.stop()
                elif age == 20 and education == "Bachelors degree":
                    st.error("You can not choose these options based on tradition [Bachelors degree]")
                    st.stop()
                elif age == 20 and education =="Associate degree":
                    st.error("You can not choose these options based on tradition [Associate degree]")
                    st.stop()
                elif age == 19 and education == "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                elif age == 19 and education== "PHD (Doctorate)":
                    st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                    st.stop()
                elif age == 19 and education== "Master degree":
                    st.error("You can not choose these options based on tradition [Master degree]")
                    st.stop()
                elif age == 19 and education == "Bachelors degree":
                    st.error("You can not choose these options based on tradition [Bachelors degree]")
                    st.stop()
                elif age == 19 and education =="Associate degree":
                    st.error("You can not choose these options based on tradition [Associate degree]")
                    st.stop()
                elif age == 18 and education == "Postdoctoral Researcher":
                    st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                    st.stop()
                elif age == 18 and education== "PHD (Doctorate)":
                    st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                    st.stop()
                elif age == 18 and education== "Master degree":
                    st.error("You can not choose these options based on tradition [Master degree]")
                    st.stop()
                elif age == 18 and education == "Bachelors degree":
                    st.error("You can not choose these options based on tradition [Bachelors degree]")
                    st.stop()
                elif age == 18 and education =="Associate degree":
                    st.error("You can not choose these options based on tradition [Associate degree]")
                    st.stop()

                if use_academic_ai_tool == None:
                    st.error("Please choose  some options (Q7)")
                if use_academic_ai_tool == "No":
                                add_data1(fname , lname , age , sex , education , job ,  use_academic_ai_tool)
                                st.success("Item Added")
                                st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("Home.py")

                if use_academic_ai_tool == "Yes":
                
                    if app_or_web == None:
                        st.error("Please Select your (Q8)")
                        st.stop()
                    if app_or_web == "Iranian sites":
                        if iranian_site == None:
                            st.error("Please Select your (Q9)")
                            st.stop()
                        if web_browser == None:
                            st.error("Please Select your (Q10)")
                            st.stop()
                        if mainq == None:
                            st.error("Please Select your (Q11)")
                            st.stop()
                        if mainq == "No":
                            add_data2(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , iranian_site , mainq)
                            st.success("Item Added")
                            st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                            sleep(8)
                            st.switch_page("Home.py")
                        if mainq == "Yes":
                            if why_use == None:
                                st.error("Please Select your (Q12)")
                                st.stop()
                            if why_use != "Other":
                                add_data3(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , iranian_site , why_use , mainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("Home.py")
                            if why_use == "Other":
                                if all(x.isalpha() == False or x.isspace() for x in another_reason):
                                    st.error("Please Select your (Q13)")
                                    st.stop()
                                if another_reason:
                                    add_data4(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , iranian_site , why_use , another_reason , mainq)
                                    st.success("Item Added")
                                    st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                    sleep(8)
                                    st.switch_page("Home.py")


                    if app_or_web == "Foreign sites":
                        if foreign_site == None:
                            st.error("Please Select your (Q9)")
                            st.stop()
                        if web_browser == None:
                            st.error("Please Select your (Q10)")
                            st.stop()
                        if mainq == None:
                            st.error("Please Select your (Q11)")
                            st.stop()
                        if mainq == "No":
                            add_data2_foreign(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , foreign_site , mainq)
                            st.success("Item Added")
                            st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                            sleep(8)
                            st.switch_page("Home.py")
                        if mainq == "Yes":
                            if why_use == None:
                                st.error("Please Select your (Q12)")
                                st.stop()
                            if why_use != "Other":
                                add_data3_foreign(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , foreign_site , why_use , mainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("Home.py")
                            if why_use == "Other":
                                if all(x.isalpha() == False or x.isspace() for x in another_reason):
                                    st.error("Please Select your (Q13)")
                                    st.stop()
                                if another_reason:
                                    add_data4_foreign(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , foreign_site , why_use , another_reason , mainq)
                                    st.success("Item Added")
                                    st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                    sleep(8)
                                    st.switch_page("Home.py")


                    if app_or_web == "Both":
                        if iranian_site == None:
                            st.error("Please Select your (Q9/1)")
                            st.stop()
                        if foreign_site == None:
                            st.error("Please Select your (Q9/1)")
                            st.stop()
                        if web_browser == None:
                            st.error("Please Select your (Q10)")
                            st.stop()
                        if mainq == None:
                            st.error("Please Select your (Q11)")
                            st.stop()
                        if mainq == "No":
                            add_data2_irf(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser ,iranian_site ,  foreign_site , mainq)
                            st.success("Item Added")
                            st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                            sleep(8)
                            st.switch_page("Home.py")
                        if mainq == "Yes":
                            if why_use == None:
                                st.error("Please Select your (Q12)")
                                st.stop()
                            if why_use != "Other":
                                add_data3_irf(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser ,iranian_site ,  foreign_site , why_use , mainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("Home.py")
                            if why_use == "Other":
                                if all(x.isalpha() == False or x.isspace() for x in another_reason):
                                    st.error("Please Select your (Q13)")
                                    st.stop()
                                if another_reason:
                                    add_data(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser ,iranian_site ,  foreign_site , why_use , another_reason , mainq)
                                    st.success("Item Added")
                                    st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                    sleep(8)
                                    st.switch_page("Home.py")

    except Exception as e:
        st.info("We will fix it")         
         
         
            
                
            #if mainq == None:
            #    st.error("Please Select your (Q10)")
            #    st.stop()
            #add_data(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , web_browser , operating_system , why_use , another_reason , mainq)
            #st.success("Item Added")
            #st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
            #sleep(5)
            #st.switch_page("Home.py")
    result = view_all_data()
    df = DataFrame(result , columns=["first_name" , "last_name" , "age" , "gender" , "education" , "job" ,  "use_site_for_academic_work" , "Iranian_Site_Or_foreign_Site" , "web_browser" , "Iranian_site" , "Foreign_site" ,  "why_use" , "another_reason" , "ai_ssp"])
    with st.expander("AI_SSP status"):
        tast_df1 = df["ai_ssp"].value_counts().to_frame()
        tast_df1 = tast_df1.reset_index()
        st.dataframe(tast_df1)
        p1 = px.pie(tast_df1 , names="ai_ssp" , values="count")
        st.plotly_chart(p1)
    
    with st.expander("Gender status"):
        tast_df2 = df["gender"].value_counts().to_frame()
        tast_df2 = tast_df2.reset_index()
        st.dataframe(tast_df2)
        p1 = px.pie(tast_df2 , names="gender" , values="count")
        st.plotly_chart(p1)
    
    with st.expander("Age status"):
        tast_df3 = df["age"].value_counts().to_frame()
        tast_df3 = tast_df3.reset_index()
        st.dataframe(tast_df3)
        p1 = px.pie(tast_df3 , names="age" , values="count")
        st.plotly_chart(p1)
    
    with st.expander("Education status"):
        tast_df4 = df["education"].value_counts().to_frame()
        tast_df4 = tast_df4.reset_index()
        st.dataframe(tast_df4)
        p1 = px.pie(tast_df4 , names="education" , values="count")
        st.plotly_chart(p1)
    
    with st.expander("Field of study"):
        tast_df5 = df["job"].value_counts().to_frame()
        tast_df5 = tast_df5.reset_index()
        st.dataframe(tast_df5)
        p1 = px.pie(tast_df5 , names="job" , values="count")
        st.plotly_chart(p1)
    
    #with st.expander("Tool status"):
    #    tast_df6 = df["tool"].value_counts().to_frame()
    #    tast_df6 = tast_df6.reset_index()
    #    st.dataframe(tast_df6)
    #    p1 = px.pie(tast_df6 , names="tool" , values="count")
    #    st.plotly_chart(p1)

    

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



#---------------------------------------------Tab2---------------------------------------------------------

with t2:
    st.markdown("""
                    <style>
                        h1{
                text-align: center;
                        }
                </style>
                """ , unsafe_allow_html=True)
    st.title("Data Visualization") 
    result = view_all_data()
    df = DataFrame(result , columns=["first_name" , "last_name" , "age" , "gender" , "education" , "Field_of_study" ,  "use_site_for_academic_work" , "Iranian_Site_Or_foreign_Site" , "web_browser" , "Iranian_site" , "Foreign_site" ,  "why_use" , "another_reason" , "ai_ssp"])
    tast_df1 = df["age"].value_counts().to_frame()
    tast_df1 = tast_df1.reset_index()
    #st.dataframe(tast_df1)
    tast_df2 = df["gender"].value_counts().to_frame()
    tast_df2 = tast_df2.reset_index()

    tast_df3 = df["education"].value_counts().to_frame()
    tast_df3 = tast_df3.reset_index()

    tast_df4 = df["Field_of_study"].value_counts().to_frame()
    tast_df4 = tast_df4.reset_index()
    
    tast_df5 = df["use_site_for_academic_work"].value_counts().to_frame()
    tast_df5 = tast_df5.reset_index()
    
    tast_df6 = df["Iranian_Site_Or_foreign_Site"].value_counts().to_frame()
    tast_df6 = tast_df6.reset_index()
    
    tast_df7 = df["web_browser"].value_counts().to_frame()
    tast_df7 = tast_df7.reset_index()
    
    tast_df8 = df["why_use"].value_counts().to_frame()
    tast_df8 = tast_df8.reset_index()
    
    tast_df9 = df["Iranian_site"].value_counts().to_frame()
    tast_df9 = tast_df9.reset_index()
    
    tast_df10 = df["Foreign_site"].value_counts().to_frame()
    tast_df10 = tast_df10.reset_index()
    
    tast_df11 = df["ai_ssp"].value_counts().to_frame()
    tast_df11 = tast_df11.reset_index()
    

    c1,c2 = st.columns(2) 
    with c1:
        p1 = px.bar(tast_df1 , x="age" , y="count" , color="age" , text_auto=True)
        st.plotly_chart(p1)
    with c2:
        p2 = px.bar(tast_df2 , x="gender" , y="count" , color="gender" , text_auto=True)
        st.plotly_chart(p2)

    c3,c4 = st.columns(2) 
    with c3:
        p3 = px.bar(tast_df3 , x="education" , y="count", color="education" , text_auto=True)
        st.plotly_chart(p3)
    with c4:
        p4 = px.bar(tast_df4 , x="Field_of_study" , y="count", color="Field_of_study" , text_auto=True)
        st.plotly_chart(p4)

    c5,c6 = st.columns(2) 
    with c5:
        p5 = px.bar(tast_df5 , x="use_site_for_academic_work" , y="count", color="use_site_for_academic_work" , text_auto=True)
        st.plotly_chart(p5)
    with c6:
        p6 = px.bar(tast_df6 , x="Iranian_Site_Or_foreign_Site" , y="count", color="Iranian_Site_Or_foreign_Site" , text_auto=True)
        st.plotly_chart(p6)
    
    c7,c8 = st.columns(2) 
    with c7:
        p7 = px.bar(tast_df7 , x="web_browser" , y="count", color="web_browser" , text_auto=True)
        st.plotly_chart(p7)
    with c8:
        p8 = px.bar(tast_df8 , x="why_use" , y="count", color="why_use" , text_auto=True)
        st.plotly_chart(p8)
   
    c9,c10 = st.columns(2) 
    with c9:
        p9 = px.bar(tast_df9 , x="Iranian_site" , y="count", color="Iranian_site" , text_auto=True)
        st.plotly_chart(p9)
    with c10:
        p10 = px.bar(tast_df10 , x="Foreign_site" , y="count", color="Foreign_site" , text_auto=True)
        st.plotly_chart(p10)
   
     
  
    
    p11 = px.bar(tast_df11 , x="ai_ssp" , y="count", color="ai_ssp" , text_auto=True)
    st.plotly_chart(p11)

    



#---------------------------------------------Tab2---------------------------------------------------------

with t3:
    def check_password():
        """Returns `True` if the user had a correct password."""

        def login_form():
            """Form with widgets to collect user information"""
            with st.form("Credentials"):
                st.text_input("Username", key="username")
                st.text_input("Password", type="password", key="password")
                st.form_submit_button("Log in", on_click=password_entered)

        def password_entered():
            """Checks whether a password entered by the user is correct."""
            if st.session_state["username"] in st.secrets[
                "passwords"
            ] and hmac.compare_digest(
                st.session_state["password"],
                st.secrets.passwords[st.session_state["username"]],
            ):
                st.session_state["password_correct"] = True
                del st.session_state["password"]  # Don't store the username or password.
                del st.session_state["username"]
            else:
                st.session_state["password_correct"] = False

        # Return True if the username + password is validated.
        if st.session_state.get("password_correct", False):
            return True

        # Show inputs for username + password.
        login_form()
        if "password_correct" in st.session_state:
            st.error("😕 User not known or password incorrect")
        return False


    if not check_password():
        st.stop()




    st.title("Welcome To Admin Panel") 
    Admin_Panel = st.selectbox(label="Admin Panel" , options=[None , "Create" , "Read" , "Update" , "Delete" , "About"] , index=0)
    create_table()
    if Admin_Panel == "Create":
        st.subheader("Create New Record")
        try:
            with st.container(border=True):
                c1 , c2 = st.columns(2)
                create_table()
                with c1:
                    fname = st.text_input(label="Q1: Please enter your first name: *" , max_chars=20 , placeholder="Alireza" , key="yname")
                    lname = st.text_input(label="Q2: Please enter your last name: *" , max_chars=20 , placeholder="Jafari", key="ylname")
                    age = st.number_input(label="Q3: How old are you? *" , min_value=18 , placeholder=22 , key="yage")
                with c2:
                    sex = st.selectbox(label="Q4: What is your gender? *" , options=[None , "Male" , "Female"] , index=0 , key="ygenfer")
                    education = st.selectbox(label="Q5: Please select your degree: *" , options=[None ,"Diploma" , "Associate degree" , "Bachelors degree" , "Master degree" , "PHD (Doctorate)" , "Postdoctoral Researcher"] , index=0 , key="dgreee")
                    job = st.text_input(label="Q6: What is your Field of study in your university? *" , placeholder="Computer Engineering" , key="fieldf")

                use_academic_ai_tool = st.selectbox(label="Q7: Do you use a site to download articles to advance your academic work? *" , options=[None , "Yes" , "No"] , index=0 , key="yacademic")
                if use_academic_ai_tool == "Yes":
                    app_or_web = st.selectbox("ًًQ8: Did you use Iranian sites or foreign sites? *" , options=[None , "Iranian sites" , "Foreign sites" , "Both"] , index=0 , key="irorf")
                    if app_or_web != None:

                        if app_or_web == "Iranian sites":
                            iranian_site = st.selectbox("Q9: Which Iranian sites do you use? *" , options=[None , "Civilica" , "MagIran" , "SID" , "Iranpaper" , "Freepaper" , "Irandoc"] , index=0 , key="ir1")
                            if iranian_site != None:
                                web_browser = st.selectbox("Q10: In which web browser do you use this site the most? *" , options=[None , "Google Chrome" , "Firefox"] , index=0 , key="web1")
                                if web_browser != None:
                                    mainq = st.selectbox(label=f"Q11: Were you satisfied with {iranian_site} site? *" , options=[None , "Yes" , "No"] , index=0 , key="hapy1")
                                    if mainq != "No" and mainq != None:
                                        why_use = st.selectbox(label=f"Q12: Why do you use {iranian_site}? *" , options=[None , "Excellent specialized content" , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0 , key="why1")
                                        if why_use == "Other":
                                            another_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason" , key="an1")

                        if app_or_web == "Foreign sites":
                            foreign_site = st.selectbox("Q9: Which Foreign sites do you use? *" , options=[None , "Google Scholar" , "Springer" , "IEEE" , "sci-hub" , "Z-LIBRARY" , "Library Genesis" , "Unpaywall" , "ScienceDirect"] , index=0 , key="f1")
                            if foreign_site != None:
                                web_browser = st.selectbox("Q10: In which web browser do you use this site the most? *" , options=[None , "Google Chrome" , "Firefox"] , index=0 , key="web2")
                                if web_browser != None:
                                    mainq = st.selectbox(label=f"Q11: Were you satisfied with {foreign_site} site? *" , options=[None , "Yes" , "No"] , index=0 , key="hapy2")
                                    if mainq != "No" and mainq != None:
                                        why_use = st.selectbox(label=f"Q12: Why do you use {foreign_site}? *" , options=[None , "Excellent specialized content" , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0 , key="why2")
                                        if why_use == "Other":
                                            another_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason" , key="an2")

                        if app_or_web == "Both":
                            iranian_site = st.selectbox("Q9/1: Which Iranian sites do you use? *" , options=[None , "Civilica" , "MagIran" , "SID" , "Iranpaper" , "Freepaper" , "Irandoc"] , index=0 , key="ir2")
                            foreign_site = st.selectbox("Q9/2: Which Foreign sites do you use? *" , options=[None , "Google Scholar" , "Springer" , "IEEE" , "sci-hub" , "Z-LIBRARY" , "Library Genesis" , "Unpaywall" , "ScienceDirect"] , index=0 , key="f3")
                            if iranian_site != None and foreign_site != None:

                                web_browser = st.selectbox("Q10: In which web browser do you use this sites the most? *" , options=[None , "Google Chrome" , "Firefox"] , index=0 , key="web5")
                                if web_browser != None:
                                    mainq = st.selectbox(label="Q11: Were you satisfied with sites? *" , options=[None , "Yes" , "No"] , index=0 , key="hapy8")
                                    if mainq != "No" and mainq != None:
                                        why_use = st.selectbox(label=f"Q12: Why do you use {iranian_site} and {foreign_site}? *" , options=[None , "Excellent specialized content" , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0 , key="why7")
                                        if why_use == "Other":
                                            another_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason" , key="an10")

                sbtn = st.button(label="Submit" , type="primary" , key="btnyn")
                if sbtn:

                    #----------------------------------Error-------------------------------------------
                    if all(x.isalpha() == False or x.isspace() for x in fname):
                        st.error("Please enter your First Name (Q1)")
                        st.stop()

                    if all(x.isalpha() == False or x.isspace() for x in lname):
                        st.error("Please enter your Last Name (Q2)")
                        st.stop()
                    if sex == None:
                        st.error("Please Select your (Q4)")
                    if education == None:
                        st.error("Please Select your (Q5)")
                    if all(x.isalpha() == False or x.isspace() for x in job):
                        st.error("Please enter your Job (Q6)")
                        st.stop()


                    if age == 30 and education== "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    if age == 29 and education== "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    if age == 28 and education== "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    if age == 27 and education== "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    if age == 26 and education== "PHD (Doctorate)":
                        st.error("You can not choose these options based on tradition [PHD (Doctorate)")
                        st.stop()
                    elif age == 26 and education == "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    elif age ==25 and education == "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    elif age ==25 and education== "PHD (Doctorate)":
                        st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                        st.stop()
                    elif age == 24 and education == "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    elif age == 24 and education== "PHD (Doctorate)":
                        st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                        st.stop()
                    elif age ==23 and education == "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    elif age ==23 and education== "PHD (Doctorate)":
                        st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                        st.stop()
                    elif age ==23 and education== "Master degree":
                        st.error("You can not choose these options based on tradition [Master degree]")
                        st.stop()
                    elif age == 22 and education == "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    if age == 22 and education== "PHD (Doctorate)":
                        st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                        st.stop()
                    elif age == 22 and education== "Master degree":
                        st.error("You can not choose these options based on tradition [Master degree]")
                        st.stop()
                    elif age == 21 and education == "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    elif age == 21 and education== "PHD (Doctorate)":
                        st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                        st.stop()
                    elif age == 21 and education== "Master degree":
                        st.error("You can not choose these options based on tradition [Master degree]")
                        st.stop()
                    elif age == 21 and education == "Bachelors degree":
                        st.error("You can not choose these options based on tradition [Bachelors degree]")
                        st.stop()
                    elif age == 20 and education == "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    elif age == 20 and education== "PHD (Doctorate)":
                        st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                        st.stop()
                    elif age == 20 and education== "Master degree":
                        st.error("You can not choose these options based on tradition [Master degree]")
                        st.stop()
                    elif age == 20 and education == "Bachelors degree":
                        st.error("You can not choose these options based on tradition [Bachelors degree]")
                        st.stop()
                    elif age == 20 and education =="Associate degree":
                        st.error("You can not choose these options based on tradition [Associate degree]")
                        st.stop()
                    elif age == 19 and education == "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    elif age == 19 and education== "PHD (Doctorate)":
                        st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                        st.stop()
                    elif age == 19 and education== "Master degree":
                        st.error("You can not choose these options based on tradition [Master degree]")
                        st.stop()
                    elif age == 19 and education == "Bachelors degree":
                        st.error("You can not choose these options based on tradition [Bachelors degree]")
                        st.stop()
                    elif age == 19 and education =="Associate degree":
                        st.error("You can not choose these options based on tradition [Associate degree]")
                        st.stop()
                    elif age == 18 and education == "Postdoctoral Researcher":
                        st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                        st.stop()
                    elif age == 18 and education== "PHD (Doctorate)":
                        st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                        st.stop()
                    elif age == 18 and education== "Master degree":
                        st.error("You can not choose these options based on tradition [Master degree]")
                        st.stop()
                    elif age == 18 and education == "Bachelors degree":
                        st.error("You can not choose these options based on tradition [Bachelors degree]")
                        st.stop()
                    elif age == 18 and education =="Associate degree":
                        st.error("You can not choose these options based on tradition [Associate degree]")
                        st.stop()

                    if use_academic_ai_tool == None:
                        st.error("Please choose  some options (Q7)")
                    if use_academic_ai_tool == "No":
                                    add_data1(fname , lname , age , sex , education , job ,  use_academic_ai_tool)
                                    st.success("Item Added")
                                    st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                    sleep(8)
                                    st.switch_page("Home.py")

                    if use_academic_ai_tool == "Yes":

                        if app_or_web == None:
                            st.error("Please Select your (Q8)")
                            st.stop()
                        if app_or_web == "Iranian sites":
                            if iranian_site == None:
                                st.error("Please Select your (Q9)")
                                st.stop()
                            if web_browser == None:
                                st.error("Please Select your (Q10)")
                                st.stop()
                            if mainq == None:
                                st.error("Please Select your (Q11)")
                                st.stop()
                            if mainq == "No":
                                add_data2(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , iranian_site , mainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("Home.py")
                            if mainq == "Yes":
                                if why_use == None:
                                    st.error("Please Select your (Q12)")
                                    st.stop()
                                if why_use != "Other":
                                    add_data3(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , iranian_site , why_use , mainq)
                                    st.success("Item Added")
                                    st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                    sleep(8)
                                    st.switch_page("Home.py")
                                if why_use == "Other":
                                    if all(x.isalpha() == False or x.isspace() for x in another_reason):
                                        st.error("Please Select your (Q13)")
                                        st.stop()
                                    if another_reason:
                                        add_data4(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , iranian_site , why_use , another_reason , mainq)
                                        st.success("Item Added")
                                        st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                        sleep(8)
                                        st.switch_page("Home.py")


                        if app_or_web == "Foreign sites":
                            if foreign_site == None:
                                st.error("Please Select your (Q9)")
                                st.stop()
                            if web_browser == None:
                                st.error("Please Select your (Q10)")
                                st.stop()
                            if mainq == None:
                                st.error("Please Select your (Q11)")
                                st.stop()
                            if mainq == "No":
                                add_data2_foreign(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , foreign_site , mainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("Home.py")
                            if mainq == "Yes":
                                if why_use == None:
                                    st.error("Please Select your (Q12)")
                                    st.stop()
                                if why_use != "Other":
                                    add_data3_foreign(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , foreign_site , why_use , mainq)
                                    st.success("Item Added")
                                    st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                    sleep(8)
                                    st.switch_page("Home.py")
                                if why_use == "Other":
                                    if all(x.isalpha() == False or x.isspace() for x in another_reason):
                                        st.error("Please Select your (Q13)")
                                        st.stop()
                                    if another_reason:
                                        add_data4_foreign(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser , foreign_site , why_use , another_reason , mainq)
                                        st.success("Item Added")
                                        st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                        sleep(8)
                                        st.switch_page("Home.py")


                        if app_or_web == "Both":
                            if iranian_site == None:
                                st.error("Please Select your (Q9/1)")
                                st.stop()
                            if foreign_site == None:
                                st.error("Please Select your (Q9/1)")
                                st.stop()
                            if web_browser == None:
                                st.error("Please Select your (Q10)")
                                st.stop()
                            if mainq == None:
                                st.error("Please Select your (Q11)")
                                st.stop()
                            if mainq == "No":
                                add_data2_irf(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser ,iranian_site ,  foreign_site , mainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("Home.py")
                            if mainq == "Yes":
                                if why_use == None:
                                    st.error("Please Select your (Q12)")
                                    st.stop()
                                if why_use != "Other":
                                    add_data3_irf(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser ,iranian_site ,  foreign_site , why_use , mainq)
                                    st.success("Item Added")
                                    st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                    sleep(8)
                                    st.switch_page("Home.py")
                                if why_use == "Other":
                                    if all(x.isalpha() == False or x.isspace() for x in another_reason):
                                        st.error("Please Select your (Q13)")
                                        st.stop()
                                    if another_reason:
                                        add_data(fname , lname , age , sex , education , job ,  use_academic_ai_tool  , app_or_web , web_browser ,iranian_site ,  foreign_site , why_use , another_reason , mainq)
                                        st.success("Item Added")
                                        st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                        sleep(8)
                                        st.switch_page("Home.py")

        except Exception as e:
            st.info("We will fix it")         
         
         
            
                
            #if mainq == None:
            #    st.error("Please Select your (Q10)")
            #    st.stop()
            #add_data(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , web_browser , operating_system , why_use , another_reason , mainq)
            #st.success("Item Added")
            #st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
            #sleep(5)
            #st.switch_page("Home.py")
        result = view_all_data()
        df = DataFrame(result , columns=["first_name" , "last_name" , "age" , "gender" , "education" , "job" ,  "use_site_for_academic_work" , "Iranian_Site_Or_foreign_Site" , "web_browser" , "Iranian_site" , "Foreign_site" ,  "why_use" , "another_reason" , "ai_ssp"])
        with st.expander("AI_SSP status"):
            tast_df1 = df["ai_ssp"].value_counts().to_frame()
            tast_df1 = tast_df1.reset_index()
            st.dataframe(tast_df1)
            p1 = px.pie(tast_df1 , names="ai_ssp" , values="count")
            st.plotly_chart(p1)

        with st.expander("Gender status"):
            tast_df2 = df["gender"].value_counts().to_frame()
            tast_df2 = tast_df2.reset_index()
            st.dataframe(tast_df2)
            p1 = px.pie(tast_df2 , names="gender" , values="count")
            st.plotly_chart(p1)

        with st.expander("Age status"):
            tast_df3 = df["age"].value_counts().to_frame()
            tast_df3 = tast_df3.reset_index()
            st.dataframe(tast_df3)
            p1 = px.pie(tast_df3 , names="age" , values="count")
            st.plotly_chart(p1)

        with st.expander("Education status"):
            tast_df4 = df["education"].value_counts().to_frame()
            tast_df4 = tast_df4.reset_index()
            st.dataframe(tast_df4)
            p1 = px.pie(tast_df4 , names="education" , values="count")
            st.plotly_chart(p1)

        with st.expander("Field of study"):
            tast_df5 = df["job"].value_counts().to_frame()
            tast_df5 = tast_df5.reset_index()
            st.dataframe(tast_df5)
            p1 = px.pie(tast_df5 , names="job" , values="count")
            st.plotly_chart(p1)

            #with st.expander("Tool status"):
            #    tast_df6 = df["tool"].value_counts().to_frame()
            #    tast_df6 = tast_df6.reset_index()
            #    st.dataframe(tast_df6)
            #    p1 = px.pie(tast_df6 , names="tool" , values="count")
            #    st.plotly_chart(p1)




    if Admin_Panel == "Read":
        st.subheader("View Item")
        result = view_all_data()
        df = DataFrame(result , columns=["first_name" , "last_name" , "age" , "gender" , "education" , "Field_of_study" ,  "use_site_for_academic_work" , "Iranian_Site_Or_foreign_Site" , "web_browser" , "Iranian_site" , "Foreign_site" ,  "why_use" , "another_reason" , "ai_ssp"])
        with st.expander("View Data"):
            st.dataframe(df)


    if Admin_Panel == "Update":
        st.subheader("Edit/Update Item")
        st.subheader("View Item")
        result = view_all_data()
        df = DataFrame(result , columns=["first_name" , "last_name" , "age" , "gender" , "education" , "job" ,  "use_site_for_academic_work" , "Iranian_Site_Or_foreign_Site" , "web_browser" , "Iranian_site" , "Foreign_site" ,  "why_use" , "another_reason" , "ai_ssp"])
        with st.expander("Current Data"):
            st.dataframe(df)
        st.dataframe(view_unique_task())

    if Admin_Panel == "Delete":
        st.subheader("Delete Item")

    if Admin_Panel == "About":
        st.subheader("About")


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











