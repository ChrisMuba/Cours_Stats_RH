
# Import necessary libraries

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn import linear_model

# Create a Streamlit web app
st.title("Multiple Regression Analysis with Streamlit and Plotly")

# Generate a synthetic dataset

np.random.seed(0)
n_samples = 100
X1 = np.random.rand(n_samples) * 10  # Independent variable 1
X2 = np.random.rand(n_samples) * 5   # Independent variable 2
Y = 2 * X1 + 3 * X2 + np.random.randn(n_samples) * 2  # Dependent variable (with some noise)

# Create a DataFrame from the synthetic data

data = pd.DataFrame({'X1': X1, 'X2': X2, 'Y': Y})

# Sidebar for user input

st.sidebar.header("Regression Parameters")
X1_weight = st.sidebar.slider("Weight of X1", min_value=0.1, max_value=5.0, value=2.0, step=0.1)
X2_weight = st.sidebar.slider("Weight of X2", min_value=0.1, max_value=5.0, value=3.0, step=0.1)

# Perform multiple regression analysis

X = data[['X1', 'X2']]
y = data['Y']
regr = linear_model.LinearRegression()
regr.fit(X, y)

# Calculate predicted values

predicted_y = regr.predict(X)

# Display regression coefficients

st.write("### Regression Coefficients")
st.write(f"Weight of X1: {X1_weight}")
st.write(f"Weight of X2: {X2_weight}")
st.write(f"Intercept: {regr.intercept_}")

# Visualize the data and regression line using Plotly

fig = px.scatter(data, x='X1', y='Y', title='Scatter Plot with Regression Line')
fig.add_trace(go.Scatter(x=data['X1'], y=predicted_y, mode='lines', name='Regression Line'))
st.plotly_chart(fig)

# Calculate and display R-squared value

r_squared = regr.score(X, y)
st.write("### R-squared Value")
st.write(f"R-squared: {r_squared:.2f}")

# Calculate predicted Y for user-defined weights

user_defined_y = X1_weight * data['X1'] + X2_weight * data['X2'] + regr.intercept_

# Visualize the user-defined regression line

fig_user_defined = px.scatter(data, x='X1', y='Y', title='Scatter Plot with User-Defined Regression Line')
fig_user_defined.add_trace(go.Scatter(x=data['X1'], y=user_defined_y, mode='lines', name='User-Defined Regression Line'))
st.plotly_chart(fig_user_defined)

# Provide interpretation and recommendations

st.write("### Interpretation and Recommendations")
if r_squared >= 0.7:
    st.write("The model explains a significant portion of the variance in the data.")
    st.write("Recommendation: Consider using this model for predictive purposes.")
else:
    st.write("The model explains a limited portion of the variance in the data.")
    st.write("Recommendation: Further investigation and data collection may be needed to improve the model.")
