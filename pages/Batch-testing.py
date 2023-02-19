import streamlit as st
import pandas as pd
import base64
import pickle
import numpy as np

# Load the saved machine learning model from the .pkl file
with open('fwd-classifier.pkl', 'rb') as f:
    model = pickle.load(f)

# Predicting function
def predict_fresh_water_quality(input_features):
    input_features = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_features)
    # Map the predictions to the quality label
    quality_labels = {0: "Bad", 1: "Good"}
    quality = [quality_labels[predict] for predict in prediction]
    
    # Print the quality of the water
    st.write("Quality of water: ",quality)
    return prediction

# Define function to download CSV file
def download_csv(dataframe, filename):
    csv = dataframe.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download the FWD CSV template here!</a>'
    return href

# Define function to read uploaded CSV file
def read_csv(file):
    df = pd.read_csv(file)
    return df

def processed_data(test_data):
    
    # Define dictionary mapping color strings to their corresponding number values
    color_mapping = {'Colorless': 0, 'Faint Yellow': 1, 'Light Yellow': 2,
                    'Near Colorless': 3, 'Yellow': 4, 'NA': 5}

    # Replace color strings with number values
    test_data['Color'] = test_data['Color'].replace(color_mapping)
    return test_data
        
# Define Streamlit app
def main():
    st.title('💧 Fresh Water Quality Detector (FWD)')
    
    # Allow user to upload CSV file
    uploaded_file = st.file_uploader('Upload a CSV file', type='csv')
   
   # Define default values
    default_values = {
        'pH': 7.0,
        'Iron': 0.0,
        'Nitrate': 0.0,
        'Chloride': 0.0,
        'Lead': 0.0,
        'Zinc': 0.0,
        'Color': 'Colorless',
        'Turbidity': 0.0,
        'Fluoride': 0.0,
        'Copper': 0.0,
        'Odor': 0.0,
        'Sulfate': 0.0,
        'Conductivity': 0.0,
        'Chlorine': 0.0,
        'Manganese': 0.0,
        'Total_Dissolved_Solids': 0.0,
        'Water_Temperature': 0.0,
        'Air_Temperature': 0.0
    }

    # Display sample template for user to download
    sample_template = pd.DataFrame(default_values, index=[0])
    st.markdown(download_csv(sample_template, 'sample_template'), unsafe_allow_html=True)
        
    # Read uploaded CSV file
    if uploaded_file is not None:
        test_data = read_csv(uploaded_file)
        st.write('Uploaded CSV file:')
        st.write(test_data)
            # Create a submit button
        submit = st.button("Check  Quality 🔬")

        # If the submit button is clicked, make the prediction
        if submit:
            process_data=processed_data(test_data)
            quality_checker=predict_fresh_water_quality(process_data)
            # Print the prediction
            st.write("The predicted quality of the water is: ", quality_checker)
    else:
        st.info('Download the above template and fill in your data.')
if __name__ == '__main__':
    main()
    