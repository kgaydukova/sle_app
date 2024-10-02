import streamlit as st

import numpy as np

# Coefficients and intercept
coefficients = np.array([0.51491513, 0.78037869, 0.26949064, 0.36336054])
intercept = np.array([0.26440086])

# Normalization parameters
mean_values = np.array([27.223300970873787, 4.650485436893204, 83.80388349514566, 0.42718446601941745])
std_values = np.array([9.942487078078907, 3.69126162520489, 86.01066531555992, 0.4946694836060969])



# Title of the app
st.markdown("""
    <h1 style="text-align: center; font-size: 36px;">
        Calculate probability of steroid resistance for patient
    </h1>
""", unsafe_allow_html=True)

# Getting input from the user
age_at_diagnosis = st.number_input('Enter Age at the Diagnosis value:')
sleday = st.number_input('Enter SLEDAY-2K value:')
antidsdna = st.number_input('Enter Anti-dsDNA (currently) value:')
anf = st.number_input('Enter ANF (currently) value:')

if anf >= 640:
	anf = 1
else:
	anf = 0

# Perform a calculation (example: sum)
#result = value1 + value2 + value3 + value4

# New examples (replace with your actual values)
new_examples = np.array([
    [age_at_diagnosis, sleday, antidsdna, anf]  # Replace with your actual values
    # ... add more new examples if needed
])

# Normalize the new examples using the provided normalization parameters
normalized_new_examples = (new_examples - mean_values) / std_values

# Calculate the linear combination of features and coefficients
linear_combination = np.dot(normalized_new_examples, coefficients) + intercept

# Apply the logistic function to get the predicted probabilities
predicted_probabilities = 1 / (1 + np.exp(-linear_combination))

# Convert predicted probabilities to predicted classes (0 or 1)
predicted_classes = np.round(predicted_probabilities)

result_proba = np.round(predicted_probabilities[0] )

if predicted_probabilities < 0.5:
	result_message = 'This patient more probably do NOT have steroid resistance.'
	color = "green"
else:
	result_message = 'This patient more probably have steroid resistance.'
	color = "red"

# Display button to calculate
if st.button('Calculate!'):  # This will trigger the calculation only when clicked
    # Displaying the result in larger font and centered
    st.markdown(f"""
    <div style="text-align: center; font-size: 24px; font-weight: bold;">
        The predicted probability is: {int(result_proba)}%
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align: center; font-size: 24px; font-weight: bold; color: {color};">
        Model prediction: {result_message}
    </div>
    """, unsafe_allow_html=True)


