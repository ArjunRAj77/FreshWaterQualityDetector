import streamlit as st
import pandas as pd

# Define the data
data = {
    'TDS in Water (PPM)': [50, 150, 250, 300, 500, 1200],
    'Suitability for Drinking Water': ['Excellent', 'Good', 'Fair', 'Poor', 'Poor', 'Unacceptable']
}
# Define table data
fluoride = pd.DataFrame({
    'Fluoride (mg/litre)': ['<1.5', '>1.5', '~1.5'],
    'Suitability': ['Suitable', 'Danger', 'Not recommended']
})
arsenic = pd.DataFrame({
    'Arsenic (mg/litre)': ['<0.01', '>0.01', '~0.01'],
    'Suitability': ['Suitable', 'Danger', 'Permissible limit']
})
iron = pd.DataFrame({
    'Iron (mg/litre)': ['<1.0', '>1.0', '~1.0'],
    'Suitability': ['Suitable', 'Danger', 'Not recommended']
})
nitrate = pd.DataFrame({
    'Nitrate (mg/litre)': ['<45', '>45', '~45'],
    'Suitability': ['Suitable', 'Danger', 'Permissible limit']
})
ph = pd.DataFrame({
    'pH': ['6.5 to 8.5', '>8.5', '<6.5'],
    'Suitability': ['Suitable', 'Alkaline', 'Acidic']
})
chloride = pd.DataFrame({
    'Chloride (mg/litre)': ['<250', '>250', '~250'],
    'Suitability': ['Suitable', 'Danger', 'Permissible limit']
})
lead = pd.DataFrame({
    'Lead (µg/litre)': ['<0.05', '>0.05', '~0.05'],
    'Suitability': ['Suitable', 'Danger', 'Permissible limit']
})
zinc = pd.DataFrame({
    'Zinc (µg/litre)': ['<0.2', '>0.2', '~0.2'],
    'Suitability': ['Suitable', 'Danger', 'Permissible limit']
})
copper = pd.DataFrame({
    'Copper (µg/litre)': ['<40', '>80', '40 to 80'],
    'Suitability': ['Suitable', 'Danger', 'Permissible limit']
})
sulphate = pd.DataFrame({
    'Sulphate (µg/litre)': ['<250', '>250', '~250'],
    'Suitability': ['Suitable', 'Danger', 'Permissible limit']
})
chlorine = pd.DataFrame({
    'Chlorine (ppm)': ['<0.4', '>0.4', '0.4'],
    'Suitability': ['Suitable', 'Danger', 'Permissible limit']
})
manganese = pd.DataFrame({
    'Manganese (µg/litre)': ['<0.1', '>0.1', '~0.1'],
    'Suitability': ['Suitable', 'Danger', 'Permissible limit']
})
# Create a DataFrame from the data
df = pd.DataFrame(data)

# Define the Streamlit app
def app():
    st.title('Water Quality Standards')
    st.subheader('TDS Level Chart for Drinking Water')
    # Display the DataFrame as a table
    st.table(df)
    # Display tables
    st.subheader('Fluoride')
    st.table(fluoride)
    st.subheader('Arsenic')
    st.table(arsenic)
    st.subheader('Iron')
    st.table(iron)
    st.subheader('Nitrate')
    st.table(nitrate)
    st.subheader('pH')
    st.table(ph)
    st.subheader('Chloride')
    st.table(chloride)
    st.subheader('Lead')
    st.table(lead)
    st.subheader('Zinc')
    st.table(zinc)
    st.subheader('Copper')
    st.table(copper)
    st.subheader('Sulphate')
    st.table(sulphate)
    st.subheader('Chlorine')
    st.table(chlorine)
    st.subheader('Manganese')
    st.table(manganese)

def main():
    app()

if __name__ == "__main__":
    main()