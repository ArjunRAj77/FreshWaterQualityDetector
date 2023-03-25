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

    if val == 'Suitable' or val == 'Excellent' or val == 'Good' or val=='Fair' :
        color = 'green'
    elif val == 'Danger' or val == 'Unacceptable' or val == 'Very Poor' :
        color = 'red'
    elif val == 'Permissible limit' or val == 'Poor':
        color = 'orange'
    elif val == 'Not recommended':
        color = 'orange'
    else:
        color = 'black'
    return f'color: {color}'

# Define the Streamlit app
def app():
    st.title('Water Quality Standards :droplet: ')
    st.subheader(" ✔ Level Charts for Drinking Water")
    st.write("Below contains various standards for drinking water as per the Indian Standards for Safe Drinking Water.")
    st.subheader(":diamond_shape_with_a_dot_inside: TDS [Total Dissolved solids]")
    tds_expander = st.expander(":snowflake: More info")
    with tds_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("Total Dissolved solids (TDS) are a measure of the dissolved combined content of all inorganic and organic materials present in a liquid in molecular, ionized, or micro-granular (colloidal sol) suspended form.")
      with col2:
        # Display the DataFrame as a table
        df_table = df.style.applymap(color_table, subset=['Suitability for Drinking Water'])
        df_table.set_table_styles([{ 'selector': 'th', 'props': [('font-weight', 'bold')] }])
        st.write(df_table)
        # Display tables

    st.subheader(":diamond_shape_with_a_dot_inside: Fluoride")
    fluoride_expander = st.expander(":snowflake: More info")
    with fluoride_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("Fluoridation of water is a controlled adjustment of fluoride to the public water supply to reduce tooth decay.\n\n Fluoride-containing water contains fluoride at a level that is effective at blocking cavities; This can occur naturally or by adding fluoride.")
      with col2:
        fluoride_table = fluoride.style.applymap(color_table, subset=['Suitability'])
        st.write(fluoride_table)

    st.subheader(":diamond_shape_with_a_dot_inside: Arsenic")
    arsenic_expander = st.expander(":snowflake: More info")
    with arsenic_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("Arsenic is a naturally occurring element found in soil and rock, and can be present in water sources.\n\n It is considered a toxic substance that can cause various health issues such as skin lesions, cancer, and cardiovascular disease when consumed at high levels over long periods of time.")
      with col2:
        arsenic_table = arsenic.style.applymap(color_table, subset=['Suitability'])
        st.write(arsenic_table)

    st.subheader(":diamond_shape_with_a_dot_inside: Iron")
    iron_expander = st.expander(":snowflake: More info")
    with iron_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("Iron is typically measured as part of the assessment of the aesthetic quality of the water, as it can cause discoloration, staining, and a metallic taste or odor.\n\n Excessive levels of iron in water can also lead to clogging of pipes and fixtures, reduced water flow, and damage to water treatment equipment. ")
      with col2:
        iron_table = iron.style.applymap(color_table, subset=['Suitability'])
        st.write(iron_table)

    st.subheader(":diamond_shape_with_a_dot_inside: Nitrate")
    nitrate_expander = st.expander(":snowflake: More info")
    with nitrate_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("Nitrate is a compound that is formed naturally when nitrogen combines with oxygen or ozone. \n\nA high concentration of nitrate in well water often results in good construction, well location, and overuse of chemical fertilizers, or improper disposal of human and animal waste.")
      with col2:
        nitrate_table = nitrate.style.applymap(color_table, subset=['Suitability'])
        st.write(nitrate_table)

    st.subheader(":diamond_shape_with_a_dot_inside: pH")
    ph_expander = st.expander(":snowflake: More info")
    with ph_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("PH Value indicates the hydrogen-ion concentration of a solution. \n\nIn the form of acids and the bases in the solution dissociate to produce hydrogen ions [H +] And hydroxyl ions [OH-] Respectively, pH is used to indicate the intensity of an acidic or alkaline state.")
      with col2:
        ph_table = ph.style.applymap(color_table, subset=['Suitability'])
        st.write(ph_table)

    st.subheader(":diamond_shape_with_a_dot_inside: Chloride")
    chloride_expander = st.expander(":snowflake: More info")
    with chloride_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("High levels of chloride in drinking water can affect its taste and may cause health concerns for people on low-sodium diets. \n\nIn addition, elevated chloride levels in freshwater bodies can be harmful to aquatic organisms and can contribute to the degradation of freshwater ecosystems.")
      with col2:
        chloride_table = chloride.style.applymap(color_table, subset=['Suitability'])
        st.write(chloride_table)

    st.subheader(":diamond_shape_with_a_dot_inside: Lead")
    lead_expander = st.expander(":snowflake: More info")
    with lead_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("lead is a heavy metal that can be found in drinking water sources. It can be harmful to human health if ingested in high levels over time.\n\n Lead is often introduced into water systems through old pipes and plumbing fixtures, as well as from industrial activities and pollution.")
      with col2:
        lead_table = lead.style.applymap(color_table, subset=['Suitability'])
        st.write(lead_table)

    st.subheader(":diamond_shape_with_a_dot_inside: Zinc")
    zinc_expander = st.expander(":snowflake: More info")
    with zinc_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("Zinc is naturally present in water. The average zinc concentration in seawater is 0.6–5 ppb.")
      with col2:
        zinc_table = zinc.style.applymap(color_table, subset=['Suitability'])
        st.write(zinc_table)

    st.subheader(":diamond_shape_with_a_dot_inside: Copper")
    copper_expander = st.expander(":snowflake: More info")
    with copper_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("Copper is a common contaminant that can affect the quality of water. It can enter water sources through industrial processes, plumbing systems, and natural deposits.\n\n In high concentrations, copper can cause a metallic taste in water and can be toxic to humans and aquatic organisms.")
      with col2:
        copper_table = copper.style.applymap(color_table, subset=['Suitability'])
        st.write(copper_table)

    st.subheader(":diamond_shape_with_a_dot_inside: Sulphate")
    sulphate_expander = st.expander(":snowflake: More info")
    with sulphate_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("Sulphates are a combination of sulphur and oxygen and are part of the minerals found naturally in some soil and rock formations that include groundwater.")
      with col2:
        sulphate_table = sulphate.style.applymap(color_table, subset=['Suitability'])
        st.write(sulphate_table)

    st.subheader(":diamond_shape_with_a_dot_inside: Chlorine")
    chlorine_expander = st.expander(":snowflake: More info")
    with chlorine_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("Chlorine levels of up to 4 mg per litter (mg / L or 4 parts per million (ppm)) in drinking water are considered safe. At this stage, harmful health effects are unlikely to occur. ")
      with col2:
        chlorine_table = chlorine.style.applymap(color_table, subset=['Suitability'])
        st.write(chlorine_table)

    st.subheader(":diamond_shape_with_a_dot_inside: Manganese")
    manganese_expander = st.expander(":snowflake: More info")
    with manganese_expander:
      col1, col2 = st.columns([2, 2])
      with col1:
        st.write("Manganese is a naturally occurring element that can be found in rocks, soil, water, and air.\n\n In water quality analysis, manganese is an important parameter to measure as it can affect the taste, color, and odor of water.\n\n High levels of manganese in drinking water can also be harmful to human health, particularly for people with liver and kidney disorders.")
      with col2:
        manganese_table = manganese.style.applymap(color_table, subset=['Suitability'])
        st.write(manganese_table)

def main():
    app()

if __name__ == "__main__":
    main()