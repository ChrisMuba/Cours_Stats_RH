
import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.subheader("📈Suite Chap.2-C/ Techniques graphiques📉")

st.subheader("Suite Données qualitatives et quantitatives")


st.markdown("")


st.markdown("- **Cartes thermiques** : Une carte thermique est une visualisation utilisée pour présenter de grands ensembles de données avec des valeurs d'intensité codées par couleur.")


st.markdown("**Cas d’usage** des cartes thermique : Elles peuvent être utilisées pour montrer la répartition des employés entre différentes fonctions et services, pour visualiser comment les employés évaluent leur satisfaction suivant différents aspects de leur travail, etc...")
st.markdown("Les Heatmaps peuvent aussi être utilisées pour améliorer le processus de recrutement en visualisant où les offres d’emploi génèrent le plus de clics, et permettre ainsi l'identification des canaux de recrutement les plus efficaces.")


st.markdown("")
    

st.markdown("**🏀Application 14**")
st.markdown("un service RH mène une enquête annuelle sur le climat social dans l'entreprise à l'aide de l'indicateur eNPS (employee Net Promoter Score), et souhaite identifier quels services ont les niveaux de satisfaction des employés les plus élevés. Une carte thermique peut représenter les scores de satisfaction de chaque service, avec des couleurs indiquant le niveau de satisfaction.")


st.markdown("")


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

st.markdown("")
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")

def redirect_button(url: str, text: str= None, color="#FD504D"):
    st.markdown(
    f"""
    <a href="{url}" target="_blank">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div
    </a>
    """,
    unsafe_allow_html=True
    )
redirect_button("https://cours-stats-rh.streamlit.app/Quiz_2_-_Statistiques_descriptives📉","Quiz du chapitre 2")



