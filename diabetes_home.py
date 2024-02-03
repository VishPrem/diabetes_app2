# Import the streamlit modules.
import streamlit as st

# Define a function 'app()' which accepts 'diabetes_df' as an input.
def app(diabetes_df):
    # Set the title to the home page contents.
    st.title('Early Diabetes Prediction Web App')
    # Provide a brief description for the web app.
    st.markdown("Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy. There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes. This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in the future by analyzing the values of several features using the Decision Tree Classifier.")

    # Add more content to fill the entire page
    st.header('Why Use This App?')
    st.markdown("This web app utilizes a machine learning model to provide an early prediction of diabetes based on various health features. By identifying individuals at risk, proactive measures can be taken to manage and reduce the impact of diabetes.")
    
    st.header('How to Use')
    st.markdown("1. **Input Features:** Enter the necessary health parameters such as glucose levels, blood pressure, BMI, etc., in the input fields.")
    st.markdown("2. **Prediction:** Click on the 'Predict' button to obtain the model's prediction.")
    st.markdown("3. **Interpret Results:** The app will display whether the individual is predicted to have diabetes or not.")
    
    st.header('About the Model')
    st.markdown("The predictive model is built using a Decision Tree Classifier. It has been trained on a dataset containing information about individuals with and without diabetes.")
    
    st.header('Disclaimer')
    st.markdown("This web app provides predictions based on a machine learning model. It is not a substitute for professional medical advice, diagnosis, or treatment. Consult with a healthcare professional for accurate health assessments.")
