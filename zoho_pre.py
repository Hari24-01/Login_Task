import streamlit as st
import pandas as pd
import pymongo

def login():
    st.write("### Login Page")
    log=st.text_input(label="Login",value="")
    pas=st.text_input(label="Password",value="",type="password")
    if st.button("Login"):
        if pas=="" and log=="":
            st.stop() 
        elif data.find_one(log) and data.find_one(pas)==pas:
            st.success("Login success")
    
        

    

def reg():
    st.write("### New Register")
    #try:
    name=st.text_input(label="Name",value="")
    age=st.text_input(label="Age",value="")
    number=st.text_input(label="Phone_number",value="")
    email=st.text_input(label="Login_ID",value="")
    pas=st.text_input(label="Passcode",value="",type="password")
    #st.write(":red[The password should have two lower case letter,two Upper case letter,two digit and special character !!]")
    compas=st.text_input(label="Com_Pass",value="",type="password")
    if st.button("Enter"): 
        data.insert_many([{"Name":name,"Age":age,"Phone_number":number,"Login_ID":email,"Password":pas}])
        st.success("Uploaded Successfully")

    elif pas=="" and compas=="":
        st.stop() 
        

    #except:
       # st.error("Enter vaild password")

data=pymongo.MongoClient("mongodb+srv://hsquarehariharan:H24hariharan@cluster0.lmpu5lp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").Zoho.Login_Data    


tabs1,tabs2=st.tabs(["Register_Page","Login_page"])
with tabs1:
    reg()

with tabs2:
    login()
