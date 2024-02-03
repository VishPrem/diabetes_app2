# Show complete dataset and summary in 'diabetes_home.py'
# Import the streamlit modules.
import streamlit as st

# Define a function 'app()' which accepts 'diabetes_df' as an input.
def app(diabetes_df):
    # Set the title to the home page contents.
    st.title('Early Diabetes Prediction Web App')
    # Provide a brief description for the web app.
    st.markdown("Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy. There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes. This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier.")
    # Add the 'beta_expander' to view full dataset 
    st.subheader('View Data')
    # with st.beta_expander('View Data'):
    #   st.dataframe(diabetes_df)
    # Add a checkbox in the first column. Display the column names of 'diabetes_df' on the click of checkbox.
    col_1, col_2, col_3 = st.beta_columns(3)
    with col_1:
      if st.checkbox('Show all column names'):
        st.table(diabetes_df.columns)
    # Add a checkbox in the second column. Display the column data-types of 'diabetes_df' on the click of checkbox.
    with col_2:
      if st.checkbox('View column data-type'):
        st.table(diabetes_df.dtypes)
    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with col_3:
      col = st.selectbox('Select column', tuple(diabetes_df.columns))
      st.write(diabetes_df[col])      
