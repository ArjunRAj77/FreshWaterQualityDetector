import streamlit as st
import pandas as pd
import base64

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

# Define Streamlit app
def main():
    st.title('💧 Fresh Water Quality Detector (FWD)')
    
    # Allow user to upload CSV file
    uploaded_file = st.file_uploader('Upload a CSV file', type='csv')
    
    # Display sample template for user to download
    sample_template = pd.DataFrame({'Column 1': ['value1', 'value2', 'value3'], 'Column 2': ['value4', 'value5', 'value6']})
    st.markdown(download_csv(sample_template, 'sample_template'), unsafe_allow_html=True)
        
    # Read uploaded CSV file
    if uploaded_file is not None:
        df = read_csv(uploaded_file)
        st.write('Uploaded CSV file:')
        st.write(df)
    else:
        st.info('Download the above template and fill in your data.')
if __name__ == '__main__':
    main()
    