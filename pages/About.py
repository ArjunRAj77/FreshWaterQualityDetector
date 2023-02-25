import streamlit as st

def about():
    st.set_page_config(page_title="About Fresh Water Quality Detector (FWD)", page_icon=":memo:", layout="centered")
    st.title("💧 Fresh  Quality Prediction Model")

    st.subheader("Introduction")
    st.write("💧 Access to clean drinking water is a fundamental human right, yet millions of people around the world still lack access to safe and reliable sources of water. Ensuring that our water supply is safe and healthy for consumption is crucial to prevent the spread of water-borne diseases and improve the overall quality of life. However, water quality can be affected by various factors such as natural and man-made contaminants, and monitoring water quality can be a complex and challenging task.")

    st.subheader("Motivation")
    st.write("🚰 To address the challenges of water quality monitoring, we have developed the Fresh Water Quality Detector (FWD), an AI-powered model that can accurately detect the quality of drinking water based on multiple input features such as pH, Iron, Nitrate, Chloride, Lead, Zinc, Color, Turbidity, Fluoride, Copper, Odor, Sulfate, Conductivity, Chlorine, Manganese, Total Dissolved Solids, Water Temperature, and Air Temperature.")
    st.write("")
    st.write("🔍 FWD uses advanced machine learning algorithms such as XGBoost and the Intel ONE API solution kit to provide a reliable and accurate assessment of water quality. By analyzing the input features and comparing them with established water quality standards, FWD can identify potential contaminants and issues with water quality in real-time, allowing for proactive measures to be taken to ensure clean and safe drinking water for all.")
    st.write("")
    st.write("🌟Overall, FWD is a valuable tool in the ongoing efforts to improve access to clean drinking water and protect public health.")

    st.subheader("Features")
    st.write("- 📈 ML Algorithm: We have used the powerful XGBoost algorithm for training our model, which is known for its high accuracy and efficiency. The accuracy recorded was 86.7%.")
    st.write("- 💻 Intel ONE API Solution Kit: To further enhance the performance of our model, we have integrated the Intel ONE API Solution Kit into our workflow. This has helped us to optimize our code and take advantage of the full potential of our hardware.")
    st.write("- 🌊 Input Features: Our FWD model takes into account several important factors that affect the quality of drinking water. These include pH, Iron, Nitrate, Chloride, Lead, Zinc, Color, Turbidity, Fluoride, Copper, Odor, Sulfate, Conductivity, Chlorine, Manganese, Total Dissolved Solids, Water Temperature, and Air Temperature. By considering all of these features together, our model is able to provide a comprehensive assessment of the water quality.")
    st.write("- 📊 Output: The output of our FWD model is a prediction of the overall quality of the drinking water, which is based on the input features. This prediction is presented as a yes/no model, but with indepth analysis on how the water can be improved for making it suitable for drinking.")    
    
    st.subheader(" About the ML model")

    st.write("🧪 The ML algorithm XGBoost is an open-source library for building and training gradient boosting models. It is well-known for its high accuracy and speed, and is used in many industries for various applications.")
    st.write("💻 The Intel ONE API solution kit is a set of software development tools designed to optimize performance and power efficiency across various hardware architectures. By using this kit along with XGBoost, we can accelerate the training of our ML model and achieve even faster and more accurate results.")
    st.write("🔍 The input features pH, Iron, Nitrate, Chloride, Lead, Zinc, Color, Turbidity, Fluoride, Copper, Odor, Sulfate, Conductivity, Chlorine, Manganese, Total_Dissolved_Solids, Water_Temperature, and Air_Temperature are all important factors that can affect the quality of drinking water. By analyzing these features using our ML model, we can determine the quality of water and take appropriate actions to ensure that it is safe for consumption.")
    st.write("📈 Our ML model has been trained on a large dataset of water quality measurements, and has been optimized to achieve high accuracy and performance. By using this model, we can quickly and easily assess the quality of drinking water and provide valuable insights to help ensure the safety of our communities.")
    st.write("🔮 With this model, we aim to help people determine the quality of their drinking water and make informed decisions to protect their health.")
    st.write("🚰 At the end of the day, our goal is to use technology to make our world a safer and healthier place. By leveraging the power of ML algorithms like XGBoost and tools like the Intel ONE API solution kit, we can achieve this goal and help ensure that everyone has access to clean and safe drinking water.")
   
    
    st.subheader("Meet the Team")
    st.write("\n\nMade with :heart: by Arjun Raj and Akhil Anil of Team Humanoids 🤖")
    st.write("Intel® oneAPI Hackathon for Open Innovation 2023.")

if __name__ == '__main__':
    about()
