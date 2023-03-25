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
    st.write("The processed data is : ")
    st.table(combined_df) 

    # Creating a downloadable button for Ouput CSV
    csv = convert_df(combined_df)
    st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='Output.csv',
    mime='text/csv')

    # Summary of output data
    st.write("---")
    st.header("Data Overview")

    st.subheader("1. Output Overview")
    piechartexpander = st.expander("🔎 Click here to view the graph")
    with piechartexpander :
        quality_counts = combined_df['Quality'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(quality_counts.values, labels=quality_counts.index, autopct='%1.1f%%')
        ax.set_title('Distribution of Output Results in Dataset')
        st.pyplot(fig)

    st.subheader("2. Distribution of pH levels in Data")
    phexpander = st.expander("🔎 Click here to view the graph")
    with phexpander:
        ph_data=combined_df[['pH']]
        st.line_chart(ph_data)

    st.subheader("3. Distribution of mineral elements in water")
    distributionexpander = st.expander("🔎 Click here to view the graph")
    with distributionexpander:
        chart_data=combined_df[['pH','Iron','Nitrate','Chloride','Lead','Zinc','Color','Turbidity','Fluoride','Copper','Sulfate','Chlorine','Manganese']]
        st.bar_chart(chart_data)

    st.subheader("4. Distribution of water properties")
    propertyexpander = st.expander("🔎 Click here to view the graph")
    with propertyexpander:
        prop_data=combined_df[['Color','Conductivity','Total_Dissolved_Solids']]
        st.area_chart(prop_data)
    
    st.subheader("5. Temperature Distribution")
    tempexpander = st.expander("🔎 Click here to view the graph")
    with tempexpander :
        prop_data=combined_df[['Water_Temperature','Air_Temperature']]
        st.line_chart(prop_data)



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
     # Converting to CSV as downloadable button
    template_content = convert_df(sample_template)
    st.download_button(
    label="Click here to download the template file",
    data=template_content,
    file_name='Sample-template.csv',
    mime='text/csv')

    # Read uploaded CSV file
    if uploaded_file is not None:
        test_data = read_csv(uploaded_file)
        expander = st.expander("🔎 Click to view uploaded file content")
        with expander:
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

# Function to convert DF to CSV
def convert_df(df):
    return df.to_csv().encode('utf-8')

if __name__ == '__main__':
    main()
    