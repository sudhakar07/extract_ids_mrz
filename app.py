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
from passporteye.mrz.image import MRZPipeline

from passporteye import read_mrz
import pytesseract


#https://github.com/rohankokkula/TEATH
#https://www.doubango.org/SDKs/mrz/docs/Data_validation.html
#https://discuss.streamlit.io/t/i-get-an-error-everytime-i-change-anything-in-my-code/4706

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sudhakar\AppData\Local\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
#pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR/tesseract.exe"
#pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Tesseract-OCR/tesseract.exe"
#pytesseract.pytesseract.tesseract_cmd = r"https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe"
activities = ["Home","Extract Ids","About"]	
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

FILE_TYPES = ["csv", "py", "png", "jpg"]

st.subheader("This App for recognizing machine readable zones (MRZ) from scanned identification documents. in around 90% of the cases, whenever there is a clearly visible MRZ on a page, it will recognize it and extract the text to the best of the abilities of the underlying OCR engine.so one of the easiest methods is to recognize it from an image file. \n 10% failed examples seem to be most often either clearly badly scanned documents. \n ")
if choice == 'Home':
	st.subheader("TD1 Format")
	st.image("images/td1_image.jpg",width=500, height=600)
	st.image("images/td1_format.jpg",width=500, height=600)
	
	st.subheader("TD2 Format")
	st.image("images/td2_image.jpg",width=500, height=600)
	st.image("images/td2_format.jpg",width=500, height=600)
	
	st.subheader("TD3 Format")
	st.image("images/td3_image.jpg",width=500, height=600)
	st.image("images/td3_format.jpg",width=500, height=600)
	
if choice == 'Extract Ids':
	st.subheader("Extract Ids")
	upload = st.file_uploader("Upload a Travel Id (images only)", type=FILE_TYPES)
	show_file = st.empty()
	#imgs = np.array(Image.open(data))
	if upload is not None:
	    
		data = upload.read()
		show_file.image(data)
		#show_file.image(img_file_buffer)
		#image = Image.open(img_file_buffer)
		#data = st.file_uploader("Upload a Ids", type=["png", "jpg"])
		
		
		#mrz = read_mrz("images/7.jpg")
		mrz = read_mrz(data, save_roi=True)
		st.subheader("Machine-Readable Zone(MRZ) Image")
		imgs = np.array(mrz.aux['roi'])
		st.image(imgs)
		st.subheader("Machine-Readable Zone(MRZ) Text")
		st.write(mrz.aux['text'])
		if mrz is None:
			show_file.info("Can not read image")


		# Obtain image
		mrz_data = mrz.to_dict()
		st.subheader("KYC instantly")
		st.write(mrz_data)
		#st.write(mrz.aux['roi'])
		
		st.write(MRZPipeline(data).result)
		#st.write(mrz.aux)
		st.subheader("\n \n")
		btn = st.button("Click Me #HappyLearning.")
		if btn:
			st.balloons()


elif choice == 'About':
	#st.subheader("About")
	
	st.subheader("About")
	st.success("Connecting ML&AI Workstation With Sudhakar")
	#st.info("Sudhakar Govindaraj")
	st.info("sudhakargk74@gmail.com")