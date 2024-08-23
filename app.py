from dotenv import load_dotenv 
import  google.generativeai as  genai
load_dotenv()  #load all the environment variable from .env 

import streamlit as st
import os 
from PIL import Image
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#function to load the Gemini Pro vision:

model=genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(input,image,prompt):
    response =model.generate_content([input,image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        #read the files into bytes:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type, #get the mime type of the image
                "data":bytes_data

            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

#initializing the app:

st.set_page_config(page_title='MultiLanguage Invoice Extractor App')
st.header('Multilanguage Invoice Extractor')
input=st.text_input('Input prompt:',key='input')
uploaded_file=st.file_uploader("Choose an image of the invoice...",type=['jpg','jpeg','png'])
image=''
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption='Uploaded Image',use_column_width=True)

submit=st.button('Tell me about the invoice')

input_prompt='''
You are an expert in understanding invoices.we will upload an image as invoices you will have to answer any questions based on the 
uploaded invoice image'''

#if submit button is clicked:

if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader('The Response is ')
    st.write(response)

