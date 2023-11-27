from textwrap import fill
import pickle
import streamlit as st
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder


html_temp = """
<div style="background-color:rgb(20 83 45);padding:16px">
<h2 style="color:white;text-align:center;">Car Price Prediction Using ML Cloud App 💪 </h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)



filename = 'Final-Streamlit'
model = pickle.load(open(filename, 'rb'))


with st.sidebar:
    st.subheader(' Welcome to our car price :red[prediction] ')




Comfort_Convenience=st.sidebar.slider("What is the Comfort Convenience of your car:",1, 33, step=5)
age=st.sidebar.selectbox("What is the age of your car:",(0,1,2,3))
hp=st.sidebar.slider("What is the hp_kw of your car?", 40, 294, step=5)
km=st.sidebar.slider("What is the km of your car",0 ,317000, step=1000)
Gears=st.sidebar.slider('Select gear of your car', 5, 8, step=1)
car_model=st.sidebar.selectbox("Select model of your car", ('Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))



my_dict = {
    "Comfort_Convenience": Comfort_Convenience,
    "age": age,
    "hp_kW": hp,
    "km": km,
    'Gears':Gears,
    "make_model": car_model
    
}

df = pd.DataFrame.from_dict([my_dict])

st.header("The values you selected is :red[below] ")
st.table(df)





# Prediction with user inputs
st.subheader("Press predict if the inputs are okay")
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(result[0])
    st.balloons()

    


