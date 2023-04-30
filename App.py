import pandas as pd
import numpy as np
import streamlit as st
import pickle
from PIL import Image

model = pickle.load(open("salary.pkl", "rb"))
app_mode = st.sidebar.radio('Select Page', ['Home', 'Prediction'])
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)
if app_mode == 'Home':
    html_temp = """
        <div style='background-color: #f9d000; padding:3px'>
        <h2 style='color:white;-webkit-text-stroke: 1px black; text-align:center;'>HR Salary Prediction: </h2>
        <h3 style='black:white;-webkit-text-stroke: 0.7px white; text-align:center;'>Above 50K$ / Below 50K$. </h3>
        
        </div>"""
    st.markdown(html_temp, unsafe_allow_html=True)

    st.image("https://i.imgur.com/tisRASe.jpeg",caption='HR Prediction Model For Predicting The Salaries Of Different People.')

elif app_mode == 'Prediction':
    def add_bg_from_url():
        st.markdown(
            f"""
                     <style>
                     .stApp {{
                         background-image: url("https://res.cloudinary.com/jerrick/image/upload/c_scale,q_auto/5e68f566ddce58001c542e16.jpg");
                         background-attachment: fixed;
                         background-size: cover
                     }}
                     </style>
                     """,
            unsafe_allow_html=True
        )


    add_bg_from_url()
    st.title('Salary Predicton Of Employees')
    st.markdown("For predicting if 'Salary' is above or below 50K$.")
    st.subheader('Enter the details:')
    sex = st.radio('Mention Your Gender?', options=['Male', 'Female'])
    if sex == 'Female':
        sex = 1
    else:
        sex = 0


    age = st.number_input('Enter Your Age Between 17 to 90',min_value=17,max_value=90,step=1)

    marital___status = st.radio('Are You Married Now?', options=['Yes', 'No'])
    if marital___status  == 'Yes':
        marital___status = 1
    else:
        marital___status = 0

    relationship=st.selectbox('What Is Your Relationship-Status?',
                        ('Select', 'Not-in-family', 'Husband', 'Wife', 'Own-child', 'Unmarried',
                        'Other-relative'))
    relationship_Husband,relationship_Not___in___family = 0,0
    relationship_Other___relative,relationship_Own___child =0,0
    relationship_Unmarried,relationship_Wife = 0,0

    if relationship == 'Not-in-family':
        relationship_Not___in___family = 1
    elif relationship  == 'Husband':
        relationship_Husband = 1
    elif relationship  == 'Wife':
        relationship_Husband = 1
    elif relationship  == 'Own-child':
        relationship_Husband = 1
    elif relationship  == 'Unmarried':
        relationship_Husband = 1
    elif relationship  == 'Other-relative':
        relationship_Husband = 1


    race = st.selectbox('What Is Your Race?',
                        ('Select', 'White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo','Other'))

    race_Amer___Indian___Eskimo,race_Asian___Pac___Islander = 0,0
    race_Black,race_Other,race_White = 0,0,0




    if race == 'White':
        race_White = 1
    elif race == 'Black':
        race_Black = 1
    elif race == 'Asian-Pac-Islander':
        race_Asian___Pac___Islander = 1
    elif race == 'Amer-Indian-Eskimo':
        race_Amer___Indian___Eskimo = 1
    elif race == 'Other':
         race_Other = 1



    native___country= st.radio('From Which Country You Are?', options=['United-States', 'Other'])
    if native___country  == 'United-States':
        native___country = 0
    else:
        native___country = 1

    education= st.selectbox('What Is Your Highest Education?',
                        ('Select', 'Doctorate','Masters', 'Bachelors', 'Some-college','12th','11th','10th',
                         '9th','Prof-school','HS-grad','Assoc-acdm','Assoc-voc','7th-8th',
                          '5th-6th', '1st-4th', 'Preschool'))

    education_10th, education_11th = 0,0
    education_12th, education_1st___4th, education_5th___6th = 0,0,0
    education_7th___8th, education_9th, education_Assoc___acdm = 0,0,0
    education_Assoc___voc, education_Bachelors, education_Doctorate = 0,0,0
    education_HS___grad, education_Masters, education_Preschool = 0,0,0
    education_Prof___school, education_Some___college = 0,0


    if education == 'Doctorate':
        education_Doctorate = 1
    elif education == 'Masters':
        education_Masters = 1
    elif education == 'Bachelors':
        education_Bachelors = 1
    elif education == 'Some-college':
        education_Some___college = 1
    elif education == '12th':
        education_12th = 1
    elif education == '11th':
        education_11th = 1
    elif education == '10th':
         education_10th = 1
    elif education == '9th':
        education_9th  = 1
    elif education == 'Prof-school':
        education_Prof___school = 1
    elif education == 'HS-grad':
        education_HS___grad = 1
    elif education == 'Assoc-acdm':
        education_Assoc___acdm = 1
    elif education == 'Assoc-voc':
        education_Assoc___voc = 1
    elif education == '7th-8th':
        education_7th___8th = 1
    elif education == '5th-6th':
        education_5th___6th = 1
    elif education == '1st-4th':
        education_1st___4th = 1
    elif education == 'Preschool':
        education_Preschool = 1

    occupation=st.selectbox('What Is Your Occupation?',
                        ('Select','Adm-clerical', 'Exec-managerial', 'Handlers-cleaners',
                        'Prof-specialty', 'Other-service', 'Sales', 'Craft-repair',
                        'Transport-moving', 'Farming-fishing', 'Machine-op-inspct',
                        'Tech-support', 'Protective-serv', 'Armed-Forces',
                        'Priv-house-serv'))

    occupation_Adm___clerical,occupation_Armed___Forces = 0,0
    occupation_Craft___repair, occupation_Exec___managerial = 0,0
    occupation_Farming___fishing,occupation_Handlers___cleaners = 0,0
    occupation_Machine___op___inspct, occupation_Other___service = 0,0
    occupation_Priv___house___serv, occupation_Prof___specialty = 0,0
    occupation_Protective___serv, occupation_Sales = 0,0
    occupation_Tech___support, occupation_Transport___moving = 0,0

    if occupation == 'Adm-clerical':
        occupation_Adm___clerical= 1
    elif occupation == 'Exec-managerial':
        occupation_Exec___managerial = 1
    elif occupation == 'Handlers-cleaners':
        occupation_Handlers___cleaners = 1
    elif occupation == 'Prof-specialty':
        occupation_Prof___specialty = 1
    elif occupation == 'Other-service':
        occupation_Other___service = 1
    elif occupation == 'Sales':
        occupation_Sales = 1
    elif occupation == 'Craft-repair':
        occupation_Craft___repair = 1
    elif occupation == 'Transport-moving':
        occupation_Transport___moving = 1
    elif occupation == 'Farming-fishing':
        occupation_Farming___fishing = 1
    elif occupation == 'Machine-op-inspct':
        occupation_Machine___op___inspct = 1
    elif occupation == 'Tech-support':
        occupation_Tech___support = 1
    elif occupation == 'Protective-serv':
        occupation_Protective___serv = 1
    elif occupation == 'Armed-Forces':
        occupation_Armed___Forces = 1
    elif occupation == 'Priv-house-serv':
        occupation_Priv___house___serv, = 1


    workclass =st.selectbox('What Sector Your Job Falls To ?',
                            ('Select','State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov',
                        'Local-gov','Self-emp-inc', 'Without-pay', 'Never-worked'))

    workclass_Federal___gov,workclass_Local___gov = 0,0
    workclass_Never___worked, workclass_Private,workclass_Self___emp___inc  = 0,0,0
    workclass_Self___emp___not___inc,workclass_State___gov  = 0,0
    workclass_Without___pay = 0


    if workclass == 'State-gov':
        workclass_State___gov = 1
    elif workclass == 'Self-emp-not-inc':
        workclass_Self___emp___not___inc = 1
    elif workclass == 'Private':
        workclass_Private = 1
    elif workclass == 'Federal-gov':
        workclass_Federal___gov = 1
    elif workclass == 'Local-gov':
        workclass_Local___gov = 1
    elif workclass == 'Self-emp-inc':
        workclass_Self___emp___inc = 1
    elif workclass == 'Without-pay':
        workclass_Without___pay = 1
    elif workclass == 'Never-worked':
        workclass_Never___worked = 1






    hours___per___week=st.number_input('Enter The Total Working Hours Per Week',min_value=1,max_value=99,step=1)

    inputs = [[age, marital___status, sex, hours___per___week, native___country,
       workclass_Federal___gov, workclass_Local___gov,
       workclass_Never___worked, workclass_Private,workclass_Self___emp___inc,
       workclass_Self___emp___not___inc,workclass_State___gov,
       workclass_Without___pay,education_10th,education_11th,
       education_12th, education_1st___4th, education_5th___6th,
       education_7th___8th,education_9th, education_Assoc___acdm,
       education_Assoc___voc,education_Bachelors, education_Doctorate,
       education_HS___grad,education_Masters,education_Preschool,
       education_Prof___school,education_Some___college,
       occupation_Adm___clerical, occupation_Armed___Forces,
       occupation_Craft___repair,occupation_Exec___managerial,
       occupation_Farming___fishing,occupation_Handlers___cleaners,
       occupation_Machine___op___inspct, occupation_Other___service,
       occupation_Priv___house___serv, occupation_Prof___specialty,
       occupation_Protective___serv, occupation_Sales,
       occupation_Tech___support,occupation_Transport___moving,
       relationship_Husband,relationship_Not___in___family,
       relationship_Other___relative, relationship_Own___child,
       relationship_Unmarried, relationship_Wife,
       race_Amer___Indian___Eskimo,race_Asian___Pac___Islander, race_Black,
       race_Other, race_White]]

    result = model.predict(inputs)
    if st.button('Get Your Prediction'):


        if result == 0:
            st.error('The Salary 💰 Will Be Below Or Equal to 50K$ 👏👏')
        else:
            st.success('The Salary 💰 Is Above 50K$ 👏👏')