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
    output(quality,input_features)

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
            Nitrate = st.number_input("Nitrate", value=30.000, min_value=0.000, max_value=100.000)
            Chloride = st.number_input("Chloride", value=200.000, min_value=0.000, max_value=1000.000)
            Fluoride = st.number_input("Fluoride", value=0.800, min_value=0.000, max_value=10.000)
            Sulfate = st.number_input("Sulfate", value=0.000, min_value=0.000)
            
         with col2:
                  Iron = st.number_input("Iron", value=0.500, min_value=0.000, max_value=10.000)
                  Zinc = st.number_input("Zinc", value=0.000, min_value=0.000, max_value=100.000)
                  Copper = st.number_input("Copper", value=20.000, min_value=0.000, max_value=100.000)
                  Chlorine = st.number_input("Chlorine", value=0.000, min_value=0.000)
         with col3:
                  Lead = st.number_input("Lead", value=0.000, min_value=0.000, max_value=10.000)
                  Turbidity = st.number_input("Turbidity", value=0.000, min_value=0.000, max_value=100.000)
                  Odor = st.number_input("Odor", value=0.000, min_value=0.000, max_value=10.000)
                  Manganese = st.number_input("Manganese", value=0.000, min_value=0.000)
    temp_expander = st.expander(" ☃ Temperature (°C)")
    with temp_expander:
      col1, col2 = st.columns(2)
      with col1:
            Water_Temperature = st.number_input("Water Temperature (°C)",value=0.000)
      with col2:
            Air_Temperature = st.number_input("Air Temperature (°C)",value=0.000)
    prop_expander = st.expander("🌌 Water Properties (mg/litre)")
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
            Total_Dissolved_Solids = st.number_input("Total Dissolved Solids 🧫", value=50.000, min_value=0.000)

    # Create a submit button
    st.info("👉 Click ""Submit"" to see the predicted quality of your water!")
    submit = st.button("Submit 🔬",type="primary")

    # If the submit button is clicked, make the prediction
    if submit:
        # Prepare the input data as a list
        input_data = [pH, Iron, Nitrate, Chloride, Lead, Zinc, Color, Turbidity, Fluoride, Copper, Odor, Sulfate, Conductivity, Chlorine, Manganese,Total_Dissolved_Solids,Water_Temperature,Air_Temperature]
        print(input_data)
        predict_fresh_water_quality(input_data)


# Function for displaying the output layout
def output(quality,input_features):
    # Print the quality of the water
    st.subheader("Output 💧")
    if quality[0] == "Bad":
        st.write("🚨 Alert! 🚨")
        st.write("The predicted drinkability of your water is below safe levels. We recommend that you do not drink this water and take necessary precautions to ensure your health and safety. ")
        st.write("Please consult with a water expert or local authorities for further guidance.")
    else :
        st.write("👍 Great news! 👍")
        st.write("The predicted drinkability of your water is above safe levels. This means your water is of good quality and safe to drink. Keep up the good work in maintaining your water source and ensuring the health and safety of yourself and those around you.")
    st.subheader("Detailed Analysis: ")
    regulatory_limit_check(input_features)
    st.snow()

def regulatory_limit_check(input_features):

    # Intialising the input factors
    phvalue=input_features[0][0]
    ironvalue=input_features[0][1]
    nitratevalue=input_features[0][2]
    chloridevalue=input_features[0][3]
    leadvalue=input_features[0][4]
    zincvalue=input_features[0][5]
    colorvalue=input_features[0][6]
    turbidityvalue=input_features[0][7]
    fluoridevalue=input_features[0][8]
    coppervalue=input_features[0][9]
    odorvalue=input_features[0][10]
    sulfatevalue=input_features[0][11]
    conductivityvalue=input_features[0][12]
    chlorinevalue=input_features[0][13]
    manganesevalue=input_features[0][14]
    tsdvalue=input_features[0][15]
    watertempvalue=input_features[0][16]
    airtempvalue=input_features[0][17] 
    st.subheader("pH")
    if phvalue >= 6.5 and phvalue <=8.5:
        st.info("Congratulations! The pH of the water is within the recommended range for drinking water. \n\n This means that the water is safe to drink and should not cause any adverse health effects.")
    elif phvalue > 8.5 :  
        st.warning(" The water is too alkaline, which may affect its taste and quality. \n\n If the pH is consistently high, it may cause health issues such as skin irritation and gastrointestinal problems. \n\n To make the water more drinkable, you could consider adding an acidifying agent like lemon juice or vinegar. However, if the pH is too high due to underlying environmental factors like limestone bedrock, it may be difficult to adjust the pH.")
    else :
        st.warning("The water is too acidic, which can also affect its taste and quality. \n\n Low pH levels can cause corrosion of plumbing fixtures and release toxic metals like lead and copper into the water. \n\n To make the water more drinkable, you could consider adding an alkalizing agent like baking soda or calcium carbonate. However, if the pH is consistently low, it may be a sign of underlying environmental factors like acid rain or nearby industrial pollution, which should be addressed to ensure safe drinking water.")
    
    st.subheader("Iron")
    if ironvalue >=0.3 and ironvalue <=1.0:
        st.warning("The water may have a metallic taste, and there may be slight staining of clothes and fixtures. \n\n  In this case, treatment may not be necessary, but installing an iron filter can help improve the taste and quality of water.") 
    elif ironvalue > 1.0:
        st.warning("If the iron levels in your water are above 1.0 mg/litre, it is considered dangerous and should be treated. \n\n High levels of iron in drinking water can cause staining of clothes and fixtures and affect the taste and odor of water. \n\n Treatment options include aeration, oxidation, and filtration. An iron filter can be installed to remove the excess iron from the water.")
    else :
        st.info("If the iron levels are below 0.3 mg/litre, the water is considered safe to drink, and no treatment is necessary.")
    
    st.subheader("Nitrate")
    if nitratevalue >= 45 :
        st.warning("If the nitrate level in water is above 45 mg/litre, it is not safe for drinking, particularly for infants under six months old. \n\n Nitrate can cause methemoglobinemia, a condition in which the blood is unable to carry oxygen properly. This can result in bluish skin and lips, shortness of breath, and even death in severe cases. \n\n  To make the water safe for drinking, treatment methods such as reverse osmosis, distillation, or ion exchange can be used to remove excess nitrates from the water. It is also important to identify and address the source of nitrate pollution, such as reducing the use of fertilizers or properly managing animal waste.")
    else:
        st.info("The nitrate level of water is well within the safe for drinking.")
    
    st.subheader("Chloride")
    if chloridevalue >=250:
        st.warning("Chloride levels above 250 mg/litre may affect the taste of water and cause corrosion in pipes and fixtures. However, it is not considered dangerous for human health.\n\n To reduce high Chloride levels in water, you can consider using a water softener or reverse osmosis filtration system. It's recommended to consult a water treatment specialist to determine the best solution for your specific situation.")
    else:
        st.info("Chloride levels below 250 mg/litre are considered safe and suitable for drinking water.")
    
    st.subheader("Lead")
    if leadvalue >=0.05:
        st.warning("If the lead level in drinking water is above the recommended limit of 0.05 µg/litre, it can be harmful to human health. \n\nLong-term exposure to high levels of lead can cause serious health problems such as developmental delays, neurological damage, and damage to vital organs such as the liver and kidneys. If you suspect that your water contains high levels of lead, it is important to take immediate action to reduce the exposure.\n\n Solutions to reduce the levels of lead in drinking water include installing a lead removal water filter or replacing lead pipes with non-toxic materials. In addition, running the tap for a few minutes before using the water can also help to flush out any lead that may have accumulated in the pipes.")
    else:
        st.info("the lead level in drinking water is within the recommended limit of 0.05 µg/litre, so it is safe to drink.")
    
    st.subheader("Zinc")
    if zincvalue >0.2:
        st.warning("Zinc levels above 0.2 mg/litre are considered dangerous and can cause stomach cramps, nausea, and vomiting. \n\n To reduce the levels of zinc in water, treatment methods such as reverse osmosis or activated carbon filtration can be used. It is important to consult with a water treatment professional to determine the most appropriate treatment method for your specific situation.")
    else:
        st.info("Zinc levels below 0.2 mg/litre are suitable for drinking water.")
    
    st.subheader("Sulphate")
    if sulfatevalue >=250:
        st.warning(" Sulfate levels above 250 µg/litre are considered dangerous and should be treated to reduce the levels.\n\n  There are different approaches to treating high sulfate levels in water, depending on the specific situation. One common method is ion exchange, which involves exchanging sulfate ions for chloride ions. Reverse osmosis is another effective treatment method that removes sulfate ions from water by passing it through a membrane. \n\n  In some cases, blending water sources or diluting high sulfate water with lower sulfate water may be a solution. It's important to consult with a water treatment professional to determine the best approach for your specific situation.")
    else:
        st.info("Sulfate levels below 250 µg/litre are considered safe to drink.")
    
    st.subheader("Conductivity")
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
