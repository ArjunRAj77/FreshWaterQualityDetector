import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the saved machine learning model from the .pkl file
with open('fwd-classifier.pkl', 'rb') as f:
    model = pickle.load(f)

# Create a function that will take in the input features and return a prediction
def predict_fresh_water_quality(input_features):
    input_features = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_features)
    # Map the predictions to the quality label
    quality_labels = {0: "Bad", 1: "Good"}
    quality = [quality_labels[predict] for predict in prediction]

    # Print the quality of the water
    st.write("Quality of water: ",quality)
    return prediction

# Define the main function for the app
def main():
    # Write the main page header
    st.write("## Fresh Water Quality Prediction")
    pH = st.number_input("pH", value=7.0000, min_value=0.000, max_value=14.000)
    expander = st.expander("Minerals present in water")
    with expander:
         col1, col2, col3 = st.columns(3)
         with col1:
            Nitrate = st.number_input("Nitrate", value=0.000, min_value=0.000, max_value=100.000)
            Chloride = st.number_input("Chloride", value=0.000, min_value=0.000, max_value=1000.000)
            Fluoride = st.number_input("Fluoride", value=0.000, min_value=0.000, max_value=10.000)
            Sulfate = st.number_input("Sulfate", value=0.000, min_value=0.000)
            
         with col2:
                  Iron = st.number_input("Iron", value=0.000, min_value=0.000, max_value=10.000)
                  Zinc = st.number_input("Zinc", value=0.000, min_value=0.000, max_value=100.000)
                  Copper = st.number_input("Copper", value=0.000, min_value=0.000, max_value=100.000)
                  Chlorine = st.number_input("Chlorine", value=0.000, min_value=0.000)
         with col3:
                  Lead = st.number_input("Lead", value=0.000, min_value=0.000, max_value=10.000)
                  Turbidity = st.number_input("Turbidity", value=0.000, min_value=0.000, max_value=100.000)
                  Odor = st.number_input("Odor", value=0.000, min_value=0.000, max_value=10.000)
                  Manganese = st.number_input("Manganese", value=0.000, min_value=0.000)
    temp_expander = st.expander("Temperature")
    with temp_expander:
      col1, col2 = st.columns(2)
      with col1:
            Water_Temperature = st.number_input("Water Temperature (°C)",value=0.000)
      with col2:
            Air_Temperature = st.number_input("Air Temperature (°C)",value=0.000)
    prop_expander = st.expander("Water Properties")
    with prop_expander:
      col1, col2 = st.columns(2)
      with col1:
           Conductivity = st.number_input("Conductivity", value=0.000, min_value=0.000)
           Source_string = st.selectbox("Source", ['NA','Lake', 'River', 'Ground', 'Spring', 'Stream', 'Aquifer',
            'Reservoir', 'Well'])
           source_dict = {name: index for index, name in enumerate(['NA','Lake', 'River', 'Ground', 'Spring', 'Stream', 'Aquifer',
            'Reservoir', 'Well'])}
           Source = source_dict[Source_string]
      with col2:
            Total_Dissolved_Solids = st.number_input("Total Dissolved Solids", value=0.000, min_value=0.000)
            Color_string = st.selectbox("Color", ['Colorless', 'Faint Yellow', 'Light Yellow', 'Near Colorless',
               'Yellow','NA'])
            color_dict = {name: index for index, name in enumerate(['Colorless', 'Faint Yellow', 'Light Yellow', 'Near Colorless',
               'Yellow','NA'])}
            Color = color_dict[Color_string]    
    
    date_expander = st.expander("Date")
    with date_expander:
      col1, col2,col3 = st.columns(3)
      with col1:
            Month = st.selectbox("Month", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
      with col2:
            Day = st.selectbox("Day", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])   
      with col3:
            Time_of_Day = st.selectbox("Time of Day", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    # Create a submit button
    submit = st.button("Submit")

    # If the submit button is clicked, make the prediction
    if submit:
        # Prepare the input data as a list
        index=1
        input_data = [index,pH, Iron, Nitrate, Chloride, Lead, Zinc, Color, Turbidity, Fluoride, Copper, Odor, Sulfate, Conductivity, Chlorine, Manganese,Total_Dissolved_Solids,Source,Water_Temperature,Air_Temperature,Month,Day,Time_of_Day]
        quality_checker=predict_fresh_water_quality(input_data)
        # Print the prediction

        st.write("The predicted quality of the water is: ", quality_checker)
main()