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

    output(quality,prediction)

    # Add the prediction to the history
    if 'prediction_history' not in st.session_state:
        st.session_state.prediction_history = []
    st.session_state.prediction_history.append(quality)
    
    # Display the history
    if st.session_state.prediction_history:
        prediction_history = pd.DataFrame(st.session_state.prediction_history, columns=['Predictions'])
        st.subheader(" 💾 Prediction History")
        st.dataframe(prediction_history)
    
    # Set page footer 
    st.write("\n\nMade with :heart: by Team Humanoids 🤖")
    st.write("Intel® oneAPI Hackathon for Open Innovation 2023")
    

def fwd():
    pH = st.number_input("🧊 pH Value", value=7.0000, min_value=0.000, max_value=14.000)
    expander = st.expander("💎 Minerals present in water")
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
    temp_expander = st.expander(" ☃ Temperature")
    with temp_expander:
      col1, col2 = st.columns(2)
      with col1:
            Water_Temperature = st.number_input("Water Temperature (°C)",value=0.000)
      with col2:
            Air_Temperature = st.number_input("Air Temperature (°C)",value=0.000)
    prop_expander = st.expander("🌌 Water Properties")
    with prop_expander:
      col1, col2 = st.columns(2)
      with col1:
           Conductivity = st.number_input("Conductivity 🧫", value=0.000, min_value=0.000)
      #      Source_string = st.selectbox("Source", ['NA','Lake', 'River', 'Ground', 'Spring', 'Stream', 'Aquifer',
      #       'Reservoir', 'Well'])
      #      source_dict = {name: index for index, name in enumerate(['NA','Lake', 'River', 'Ground', 'Spring', 'Stream', 'Aquifer',
      #       'Reservoir', 'Well'])}
      #      Source = source_dict[Source_string]
           Color_string = st.selectbox("Color", ['Colorless', 'Faint Yellow', 'Light Yellow', 'Near Colorless',
               'Yellow','NA'])
           color_dict = {name: index for index, name in enumerate(['Colorless', 'Faint Yellow', 'Light Yellow', 'Near Colorless',
               'Yellow','NA'])}
           Color = color_dict[Color_string]    
    
      with col2:
            Total_Dissolved_Solids = st.number_input("Total Dissolved Solids 🧫", value=0.000, min_value=0.000)

    # Create a submit button
    st.info("👉 Click ""Submit"" to see the predicted quality of your water!")
    submit = st.button("Submit 🔬",type="primary")

    # If the submit button is clicked, make the prediction
    if submit:
        # Prepare the input data as a list
        input_data = [pH, Iron, Nitrate, Chloride, Lead, Zinc, Color, Turbidity, Fluoride, Copper, Odor, Sulfate, Conductivity, Chlorine, Manganese,Total_Dissolved_Solids,Water_Temperature,Air_Temperature]
        print(input_data)
        predict_fresh_water_quality(input_data)


# Function for the 
def output(quality,prediction):
    # Print the quality of the water
    st.subheader("Output 💧")
    if quality[0] == "Bad":
        st.write("🚨 Alert! 🚨")
        st.write("The predicted drinkability of your water is below safe levels. We recommend that you do not drink this water and take necessary precautions to ensure your health and safety. ")
        st.write("Please consult with a water expert or local authorities for further guidance.")
    else :
        st.write("👍 Great news! 👍")
        st.write("The predicted drinkability of your water is above safe levels. This means your water is of good quality and safe to drink. Keep up the good work in maintaining your water source and ensuring the health and safety of yourself and those around you.")
    st.write("Detailed Analysis: ", prediction)
    st.snow()

# Define the main function for the app
def main():
    # Write the main page header
    st.title("💧 Fresh Water Quality Detector (FWD)🚰🔮")
    st.subheader("")
    st.subheader(" 💧 Fill out fields to predict water quality: 👉")
    st.info("👉 Want to predict the drinkability of multiple values at once? 👀, check  our Batch-testing page!")
    fwd()
    
if __name__ == '__main__':
    main()
