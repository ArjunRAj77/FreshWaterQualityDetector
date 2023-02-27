import streamlit as st
import pandas as pd

# Define the data
data = {
    'TDS in Water (PPM)': [50, 150, 250, 300, 500, 1200],
    'Suitability for Drinking Water': ['Excellent', 'Good', 'Fair', 'Poor', 'Very Poor', 'Unacceptable']
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

def color_table(val):

    if val == 'Suitable':
        color = 'green'
    elif val == 'Danger':
        color = 'red'
    elif val == 'Permissible limit':
        color = 'yellow'
    elif val == 'Not recommended':
        color = 'yellow'
    else:
        color = 'black'
    return f'color: {color}'

# Define the Streamlit app
def app():
    st.title('Water Quality Standards ✔')
    st.markdown("<h3 style='text-align: left; color: black;'>TDS Level Chart for Drinking Water</h3>", unsafe_allow_html=True)
    # Display the DataFrame as a table
    df_table = df.style.applymap(color_table, subset=['Suitability for Drinking Water'])
    df_table.set_table_styles([{ 'selector': 'th', 'props': [('font-weight', 'bold')] }])
    st.write(df_table)
    # Display tables
    st.markdown("<h3 style='text-align: left; color: black;'>Fluoride</h3>", unsafe_allow_html=True)
    flouride_table = fluoride.style.applymap(color_table, subset=['Suitability'])
    st.write(flouride_table)
    st.markdown("<h3 style='text-align: left; color: black;'>Arsenic</h3>", unsafe_allow_html=True)
    arsenic_table = arsenic.style.applymap(color_table, subset=['Suitability'])
    st.write(arsenic_table)
    st.markdown("<h3 style='text-align: left; color: black;'>Iron</h3>", unsafe_allow_html=True)
    iron_table = iron.style.applymap(color_table, subset=['Suitability'])
    st.write(iron_table)
    st.markdown("<h3 style='text-align: left; color: black;'>Nitrate</h3>", unsafe_allow_html=True)
    nitrate_table = nitrate.style.applymap(color_table, subset=['Suitability'])
    st.write(nitrate_table)
    st.markdown("<h3 style='text-align: left; color: black;'>pH</h3>", unsafe_allow_html=True)
    ph_table = ph.style.applymap(color_table, subset=['Suitability'])
    st.write(ph_table)
    st.markdown("<h3 style='text-align: left; color: black;'>Chloride</h3>", unsafe_allow_html=True)
    chloride_table = chloride.style.applymap(color_table, subset=['Suitability'])
    st.write(chloride_table)
    st.markdown("<h3 style='text-align: left; color: black;'>Lead</h3>", unsafe_allow_html=True)
    lead_table = lead.style.applymap(color_table, subset=['Suitability'])
    st.write(lead_table)
    st.markdown("<h3 style='text-align: left; color: black;'>Zinc</h3>", unsafe_allow_html=True)
    zinc_table = zinc.style.applymap(color_table, subset=['Suitability'])
    st.write(zinc_table)
    st.markdown("<h3 style='text-align: left; color: black;'>Copper</h3>", unsafe_allow_html=True)
    copper_table = copper.style.applymap(color_table, subset=['Suitability'])
    st.write(copper_table)
    st.markdown("<h3 style='text-align: left; color: black;'>Sulphate</h3>", unsafe_allow_html=True)
    sulphate_table = sulphate.style.applymap(color_table, subset=['Suitability'])
    st.write(sulphate_table)
    st.markdown("<h3 style='text-align: left; color: black;'>Chlorine</h3>", unsafe_allow_html=True)
    chlorine_table = chlorine.style.applymap(color_table, subset=['Suitability'])
    st.write(chlorine_table)
    st.markdown("<h3 style='text-align: left; color: black;'>Manganese</h3>", unsafe_allow_html=True)
    manganese_table = manganese.style.applymap(color_table, subset=['Suitability'])
    st.write(manganese_table)

def main():
    app()

if __name__ == "__main__":
    main()