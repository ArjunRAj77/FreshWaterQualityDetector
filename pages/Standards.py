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
    st.subheader("TDS Level Chart for Drinking Water")
    # Display the DataFrame as a table
    df_table = df.style.applymap(color_table, subset=['Suitability for Drinking Water'])
    df_table.set_table_styles([{ 'selector': 'th', 'props': [('font-weight', 'bold')] }])
    st.write(df_table)
    # Display tables
    st.subheader("Fluoride")
    flouride_table = fluoride.style.applymap(color_table, subset=['Suitability'])
    st.write(flouride_table)

    st.subheader("Arsenic")
    arsenic_table = arsenic.style.applymap(color_table, subset=['Suitability'])
    st.write(arsenic_table)

    st.subheader("Iron")
    iron_table = iron.style.applymap(color_table, subset=['Suitability'])
    st.write(iron_table)

    st.subheader("Nitrate")
    nitrate_table = nitrate.style.applymap(color_table, subset=['Suitability'])
    st.write(nitrate_table)

    st.subheader("pH")
    ph_table = ph.style.applymap(color_table, subset=['Suitability'])
    st.write(ph_table)

    st.subheader("Chloride")
    chloride_table = chloride.style.applymap(color_table, subset=['Suitability'])
    st.write(chloride_table)

    st.subheader("Lead")
    lead_table = lead.style.applymap(color_table, subset=['Suitability'])
    st.write(lead_table)

    st.subheader("Zinc")
    zinc_table = zinc.style.applymap(color_table, subset=['Suitability'])
    st.write(zinc_table)

    st.subheader("Copper")
    copper_table = copper.style.applymap(color_table, subset=['Suitability'])
    st.write(copper_table)

    st.subheader("Sulphate")
    sulphate_table = sulphate.style.applymap(color_table, subset=['Suitability'])
    st.write(sulphate_table)

    st.subheader("Chlorine")
    chlorine_table = chlorine.style.applymap(color_table, subset=['Suitability'])
    st.write(chlorine_table)

    st.subheader("Manganese")
    manganese_table = manganese.style.applymap(color_table, subset=['Suitability'])
    st.write(manganese_table)

def main():
    app()

if __name__ == "__main__":
    main()