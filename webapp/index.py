import streamlit as sl
import json
import requests

id = sl.text_input('Booking ID : ', '1')

if id:
    req = requests.get("0.0.0.0:80/")
    sl.write(req.text)
