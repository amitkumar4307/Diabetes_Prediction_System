import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#set page configration
st.set_page_config(page_title="Health Assistant",layout="wide")

#working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

#loading of the saved model

diabetes_model = pickle.load(open('diabetes.csv','rb'))
	
#sidebar for navigations
with st.sidebar:
	selected =option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction'],menu_icon='hospital-fill',icons=['activity','heart'],default_index=0)

if selected=='Diabetes Prediction':
	st.title("Diabetes Prediction using ML")
	col1,col2,col3 =st.columns(3)

	glucose = col1.slider('Glucose Levl',0,600,120)
	bloodpressure=col2.slider("Blood Pressure Value",0,200,120)
	skinthickness=col3.slider("Skin Thickness Value",0,100,20)
	insulin = col1.slider("Insuline Level",0,500,30)
	bmi =col2.slider("BMI Value",0.0,70.0,0,25.0)
	dpf=col3.slider("Diabetes Pedigree Fuction Value",0.0,2.5,0.5)
	age= col1.slider("Age of the person",0,100,25)

	if st.button("Diabetes Test Result"):
		user_input=[glucose,bloodpressure,skinthickness,insulin,bmi,dpf,age]
		diab_prediction = diabetes_model.predict([user_input])
		diab_diagnosis = "The Person is Diabetes" if diab_prediction [0]== 1 else 'The Person is Diabetic'
		st.success(diab_diagnosis)

if selected=='Heart Disease Prediction':
	st.title("Comming soon !!!")


	