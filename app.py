import streamlit as st
from time import strftime
import pandas as pd
import tensorflow as tf
import numpy as np
import datetime

#Read the CSV file
df=pd.read_csv("BTC-USD.csv")
#Load the Tensorflow Model
model=tf.keras.models.load_model("model.h5")

def time_predictor(y_test,time_step):
  import numpy

  initial=y_test[-7:]
  predictions = []
  for _ in range(time_step):
    prediction = model.predict(tf.expand_dims(initial,axis=0))[0]

    initial=numpy.append(initial,prediction)

    predictions.append(prediction)

    initial=initial[-7:]

  return predictions

time=strftime("%m/%d/%Y--%H:%M")

st.markdown(f"""<h2 style="text-align: left;">BTC PREDICTOR : {time}</h2>""", unsafe_allow_html=True)

st.image("https://images6.alphacoders.com/912/thumb-1920-912465.jpg")

#Display the data in streamlit Data format
d = st.date_input(f"Todays's Date: {strftime('%m/%d/%Y')}",datetime.date(2015, 9, 7))
st.dataframe(df[df["Date"] >= str(d)])

#Ask the User for number of days that he wants to predict.
number = st.number_input('How many days u want to predict?', min_value=1, max_value=14, value=1, step=1)

if st.button('Predict'):
     arr= time_predictor(df["Close"].values,number)
     count=0
     for i in arr:
      count+=1
      st.write(f"Day {count}-",i[0])

     import matplotlib.pyplot as plt

     fig, ax = plt.subplots()
     ax.plot(arr)

     st.pyplot(fig)
    
else:
     st.write('Predicted value')

# st.image("1.jpeg")

st.header("Disclaimer")
st.write("BTCPricePrediction (here in after referred to as ‘BTCPricePrediction.com’, ‘The Company’ or ‘We’ ). Information provided on this website is simply for general or educational purpose. We suggest users to learn about risk involved in BTC investment as BTC world is very volatile and unpredictable. Kindly go through next section about Investment. We keep our right to update this disclaimer time to time basis.")

st.header("Invest at Your Own Risk")
st.write("We warn you to do not use any information provided here at BTCPricePrediction.com as investment guideline or advice. We suggest you have a professional guidance or financial advisors help to make any investment related decisions. We do not accept any kind of liabilities for your any losses in cryptocurrency investments. Cryptocurrency investment is highly volatile and risky as it depends up on market situation. You should NEVER invest money that you are not capable of handling situation to lose them 100%.")

st.header("Accuracy of Data")
st.write("We try to provide accurate data on this website but at same time we do not provide any guarantee or warranty of it. We will not be responsible for any incorrect, missing or incomplete information. We keep our right to change information on this website at any point of time without any notice.")

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}
a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #010917;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p style="color: white;">Developed with ❤ by <a style='display: block; text-align: center;' >Sherwin Roger</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)