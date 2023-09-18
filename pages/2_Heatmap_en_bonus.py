

import pandas as pd
import numpy as np

# Create sample data for employee absences and vacations
np.random.seed(42)

# Generate random data for three departments: HR, Sales, and IT
departments = ['HR', 'Sales', 'IT']
dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
data = []

for date in dates:
    for department in departments:
        absences = np.random.randint(0, 5)  # Random daily absences (0 to 4)
        vacations = np.random.randint(0, 3)  # Random daily vacations (0 to 2)
        data.append([date, department, absences, vacations])

# Create a DataFrame
employee_data = pd.DataFrame(data, columns=['Date', 'Department', 'Absences', 'Vacations'])
                

import streamlit as st
import plotly.express as px

# Create the Streamlit app
st.title('Employee Absences and Vacations Heatmap')

# Create filters for department and month
selected_department = st.selectbox('Select Department:', ['HR', 'Sales', 'IT'])
selected_month = st.selectbox('Select Month:', ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Filter the data based on user selections
filtered_data = employee_data[(employee_data['Department'] == selected_department) & (employee_data['Date'].dt.strftime('%B') == selected_month)]

# Pivot the filtered data for plotting
heatmap_data = filtered_data.pivot(index='Department', columns='Date', values='Absences')

# Create an interactive heatmap using Plotly Express
fig = px.imshow(
    heatmap_data,
    x=heatmap_data.columns,
    y=heatmap_data.index,
    color_continuous_scale='Viridis',  # You can choose different color scales
    title=f'Employee Absences Heatmap for {selected_department} in {selected_month}'
)
fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Department')

# Show the plot in Streamlit
st.plotly_chart(fig)



