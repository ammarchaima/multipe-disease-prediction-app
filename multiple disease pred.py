# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 19:03:52 2022

@author: ASUS
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model= pickle.load(open('C:\\Users\ASUS\Desktop\multiple disease prediction\saved models/diabetes_model.sav','rb'))
heart_disease_model= pickle.load(open('C:\\Users\ASUS\Desktop\multiple disease prediction\saved models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('C:\\Users\ASUS\Desktop\multiple disease prediction\saved models/parkinsons_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multipe Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity','heart','person'],
                            default_index=0)
#diabetes prediction page
if(selected =='Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1 , col2 , col3 = st.columns(3)
    
    with col1:
        Pregnancies =st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose Level')
    with col3:
        BloodPressure=st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness=st.text_input('Skin Thickness value')
    with col2:
        Insulin=st.text_input('Insulin in Level')
    with col3:
        BMI=st.text_input('BMI value')
        
    
    
   
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age=st.text_input('Age of the person')
    
    
    
    #code for prediction
    diab_dignosis=''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction= diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
        if (diab_prediction[0]==1):
            diab_dignosis='The person is Diabetic'
        else:
            diab_dignosis='The person is Not Diabetic'
    st.success(diab_dignosis)
    
    
    
    
if(selected =='Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction using ML')
    
if(selected=='Parkinsons Prediction'):
    #page title
    st.title('Parkinsons Prediction using ML')
    
    
    
    
 #heart disease prediction page

if ( selected ==' Heart Disease Prediction ' ) :
  #page title
  st.title ( ' Heart Disease Prediction using ML ' )
  
  col1 , col2 , col3 = st.columns(3)
  with col1 :
     age=st.text_input ( ' Age ' )
  with col2 :
      sex =st.text_input ( ' Sex ' )
  with col3 :
      cp= st . text_input ( ' Chest Pain types ' )
  with col1 :
      trestbps= st.text_input ( ' Resting Blood Pressure ')
  with col2 :
       chol= st.text_input ( ' Serum Cholestoral in mg / dL ' )
  with col3 :
    fbs = st.text_input ( ' Fasting Blood Sugar > 120 mg / dL ' )
  with col1 :
      restecg = st.text_input ( ' Resting Electrocardiographic results' )
  with col2 :
    thalach =st.text_input ( ' Maximum Heart Rate achieved ' )
  with col3 :
    exang = st.text_input ( ' Exercise Induced Angina ' )
  with col1 :
    oldpeak = st.text_input ( ' ST depression induced by exercise ')
  with col2 :
    slope= st.text_input ( ' Slope of the peak exercise ST segment ')
  with col3 :
    ca = st.text_input ( ' Major vessels colored by flourosopy ' )
  with col1:
      thal=st.text_input('thal:0=normal;1=fixed defect;2=reversable defect')
      
#code for prediction
heart_diagnosis=''
if st.button('Heart Disease Test Result'):
    heart_prediction=heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca, thal]])
    if (heart_prediction[0]==1):
        heart_diagnosis='The person is having heart disease'
    else:
        heart_diagnosis='The person does not have any heart disease'
st.success(heart_diagnosis)
      
      
      
      
    
#parkinson's prediction page
if(selected=='Parkinsons Prediction'):
   # page title
   st.title ( ' Parkinson Disease Prediction using ML')
col1 , col2 , col3 , col4 , col5= st.columns ( 5 )
with col1 :
  fo =st.text_input ( ' NDVP : Fo ( Hz ) ' )
with col2 :
                     
  fhi =st . text_input ( ' MOVP : Phi ( Hz ) ')
with col3 :
  flo =st.text_input ( ' MOVP : FLO ( Hz ) ' )
with col4 :
  Jitter_percent = st . text_input ( ' MOVP : Jitter ( % ) ' )
with col5 :
  Jitter_Abs =st.text_input (' MDVP : Jitter ( Abs ) ')
with col1 :
  RAP =st.text_input ( ' MOVP : RAP ')
with col2 :
  PPQ =st . text_input ( ' MDVP : PPQ ' )
with col3 :
    DDP = st . text_input ( ' Jitter : DOP ' )
with col4 :
    Shimmer = st.text_input ( ' MDVP : Shimmer ' )
with col5 :
    Shimmer_dB =st.text_input ( 'MDVP : Shimmer (dB) ' )
with col1 :
   APQ3 =st.text_input ( ' Shimmer : APQ3 ' )
with col2 :
    APQS = st.text_input ( ' Shimmer : APQS ' )
with col3 :
   APQ =st . text_input ( ' MOVP : APQ ' )
with col4 :
    DDA = st.text_input ( ' Shimmer : DDA ')
with col5 :
    NHR = st.text_input ( ' NHR ' )
with col1 :
    HNR = st.text_input ( ' HNR ')
with col2 :
    RPDE = st.text_input ( ' RPDE ' )  
   
    
   
    
#code for parkinson
parkinson_diagnosis=''
if st.button('parkinson Test Result'):
    parkinson_prediction=parkinsons_model.predict([[fo,fhi, flo,Jitter_percent,Jitter_Abs, RAP , PPQ,DDP,Shimmer, APQ3, APQS, APQ,  DDA,NHR,HNR,RPDE]])
    if (parkinson_prediction[0]==1):
        parkinson_diagnosis='The person is having heart disease'
    else:
        parkinson_diagnosis='The person does not have any heart disease'
st.success(parkinson_diagnosis)
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    