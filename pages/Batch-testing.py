import streamlit as st
import pandas as pd
import base64
import pickle
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the saved machine learning model from the .pkl file
with open('fwd-classifier.pkl', 'rb') as f:
    model = pickle.load(f)

# Predicting function
def predict_fresh_water_quality(input_data):
    # Initialize empty list to store results
    results = []
    
    # Iterate through each row in input DataFrame
    for index, row in input_data.iterrows():
        # Reshape input features and make prediction
        input_features = np.array(row).reshape(1, -1)
        prediction = model.predict(input_features)[0]
        
        # Map prediction to quality label and append to results list
        quality_labels = {0: "Bad", 1: "Good"}
        quality = quality_labels[prediction]
        results.append(quality)
        
        
    return results

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

def output(input_data,quality):

    input_df = pd.DataFrame(input_data)
    combined_df = pd.concat([input_df, pd.DataFrame({'Quality': quality})], axis=1)

    st.subheader("Output 💧")
    st.table(combined_df) 
    # add a download button for the table
    csv = combined_df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="output.csv">Download the output</a>'
    st.markdown(href, unsafe_allow_html=True)
    # create scatter plot matrix for pH, Iron, Nitrate, and Chloride variables
    sns.pairplot(data=input_data[['pH', 'Iron', 'Nitrate', 'Chloride']])


    st.subheader("Prediciton Overview")
    # create bar chart of quality ratings
    quality_counts = combined_df['Quality'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(quality_counts.index, quality_counts.values)
    ax.set_xlabel('Quality Rating')
    ax.set_ylabel('Number of Samples')
    st.pyplot(fig)

    st.subheader("pH level frequency")
    # create histogram of pH levels
    fig, ax = plt.subplots()
    ax.hist(combined_df['pH'], bins=20)
    ax.set_xlabel('pH Value')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    st.subheader("Distribution of pH, Iron, Nitrate, and Chloride variables")
    # create scatter plot matrix for pH, Iron, Nitrate, and Chloride variables
    fig = sns.pairplot(data=combined_df[['pH', 'Iron', 'Nitrate', 'Chloride']])
    st.pyplot(fig)

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
        submit = st.button("Check  Quality 🔬",type="primary")

        # If the submit button is clicked, make the prediction
        if submit:
            process_data=processed_data(test_data)
            quality_checker=predict_fresh_water_quality(process_data)
            output(process_data,quality_checker)
            # Print the prediction
            st.balloons()
    else:
        st.info('Download the above template and fill in your data.')
        # Set page footer 
    st.write("\n\nMade with :heart: by Team Humanoids 🤖")
    st.write("Intel® oneAPI Hackathon for Open Innovation 2023.")
if __name__ == '__main__':
    main()
    