# EDA Pkgs
import pandas as pd 
import numpy as np 
import time,json

# Data Viz Pkg
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns 
import streamlit as st 
import os
from PIL import Image


from passporteye import read_mrz
import pytesseract

#https://github.com/rohankokkula/TEATH
#https://discuss.streamlit.io/t/i-get-an-error-everytime-i-change-anything-in-my-code/4706

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sudhakar\AppData\Local\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
#pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR/tesseract.exe"
#pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Tesseract-OCR/tesseract.exe"
#pytesseract.pytesseract.tesseract_cmd = r"https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe"
activities = ["Extract Ids","About"]	
choice = st.sidebar.selectbox("Select Activities",activities)
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showPyplotGlobalUse', False)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if choice == 'Extract Ids':
	st.subheader("Extract Ids")
	img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
	image = Image.open(img_file_buffer)
	#data = st.file_uploader("Upload a Ids", type=["png", "jpg"])
	
	#mrz = read_mrz("images/7.jpg")
	mrz = read_mrz(image)

	if mrz is None:
		print("Can not read image")


	# Obtain image
	mrz_data = mrz.to_dict()
	st.write(mrz_data)
	#st.write(mrz_data.get('sex'))


elif choice == 'About':
	st.subheader("About")