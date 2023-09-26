


import streamlit as st

st.markdown("# Chapitre 5")
st.sidebar.markdown("# Chapitre 5")

st.title("Correlation et Regression")

st.markdown("**Comprendre la relation entre divers facteurs est crucial pour prendre des décisions éclairées**.")

st.markdown("La **corrélation** et **l'analyse de régression** sont des outils statistiques puissants, qui peuvent aider les services RH à mieux comprendre les liens entre différentes variables et à prédire les résultats.")  

st.markdown("Dans ce chapitre, nous explorerons les bases de l'analyse de **corrélation** et de **régression**, et illustrerons leurs applications en RH, notamment dans la prévision des performances et du turnover des employés.")

if st.button("Cliquez pour acceder au Chap.5 - **A/ Analyse de corrélation : dévoiler les relations**"):
    
    st.subheader("📈Chap.5-A/ Analyse de corrélation📉")
    
    st.markdown("**L'analyse de corrélation** est une technique statistique qui **examine la force et la direction de la relation entre deux variables**. Elle aide à déterminer si les changements d'une variable sont associés aux changements d'une autre. La **corrélation est indiquée par le coefficient de corrélation (r), qui varie de -1 à +1**.") 

    st.markdown("")
    
    
    st.markdown("- **Corrélation positive** : **Lorsque deux variables évoluent dans le même sens**, on dit qu'elles ont une **corrélation positive**.") 
    
    st.markdown("Par exemple, il pourrait y avoir une corrélation positive entre la satisfaction des employés et la productivité. Si le coefficient de corrélation est proche de **+1**, cela indique une **forte corrélation positive**.") 

    st.markdown("**🏀Application 19** :")                
    
    st.markdown("Le contrôleur de gestion sociale d'un service public de *Ploucs-lès-Landes* souhaite analyser la relation entre « Productivité des agents » et « Satisfaction au travail ».")

    st.markdown("Ci-dessous un échantillon des données collectées :")

    # Import necessary libraries
    import streamlit as st
    import pandas as pd
    import plotly.express as px

# Sample HR data
    data = {
        'Agent': list(range(1, 11)),
        'Productivité de l\'agent': [80, 75, 90, 70, 85, 65, 95, 75, 85, 70],
        'Satisfaction au travail': [5, 4, 6, 3, 5, 2, 7, 4, 6, 3]
    }

# Create a DataFrame
    df = pd.DataFrame(data)

# Display the sample data
    st.dataframe(df)

# Introduction
    st.write("Dans cet exercice, nous analyserons la corrélation entre la productivité des agents et leur satisfaction au travail.")

# Calculate and display the correlation coefficient
    correlation_coefficient = df['Productivité de l\'agent'].corr(df['Satisfaction au travail'])
    st.write(f"Coefficient de correlation (r): {correlation_coefficient}")

# Determine the type of correlation
    if correlation_coefficient > 0:
        correlation_type = "correlation positive"
    elif correlation_coefficient < 0:
        correlation_type = "correlation negative"
    else:
        correlation_type = "non correlation"

# Create a scatter plot with a trendline
    fig = px.scatter(df, x='Productivité de l\'agent', y='Satisfaction au travail', title='Productivité de l\'agent vs. Satisfaction au travail', trendline='ols')
    st.plotly_chart(fig)

# Display the correlation type with the coefficient
    st.write(f"Cela indique une {correlation_type} avec un coefficient de {correlation_coefficient:.2f}.")


    st.markdown("")
    
    st.markdown("")
    
    
    st.markdown("- **Corrélation négative** : **lorsque deux variables évoluent dans des directions opposées**, elles présentent une **corrélation négative**.") 

    st.markdown("**🏀Application 20** :")

# Import necessary libraries
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import numpy as np

# Sample HR data
    data = {
        'Employee': list(range(1, 11)),
        'Absenteeism (days)': [5, 2, 8, 1, 6, 4, 9, 3, 7, 2],
        'Job Satisfaction (scale 1-5)': [2, 4, 1, 5, 2, 3, 1, 4, 1, 3]
    }

# Create a DataFrame
    df = pd.DataFrame(data)

# Title for the Streamlit app
    st.title("Negative Correlation Analysis in HR")

# Introduction
    st.write("In this exercise, we will analyze the negative correlation between Absenteeism and Job Satisfaction.")

# Calculate and display the correlation coefficient
    correlation_coefficient = df['Absenteeism (days)'].corr(df['Job Satisfaction (scale 1-5)'])
    st.write(f"Correlation Coefficient (r): {correlation_coefficient:.2f}")

# Create a scatter plot with a trendline
    fig = px.scatter(df, x='Absenteeism (days)', y='Job Satisfaction (scale 1-5)', title='Absenteeism vs. Job Satisfaction')
    fig.update_traces(marker=dict(size=12, opacity=0.6), selector=dict(mode='markers'))
    fig.add_trace(
        px.scatter(df, x='Absenteeism (days)', y='Job Satisfaction (scale 1-5)', trendline="ols").data[1]
    )
    st.plotly_chart(fig)

# Interpretation
    st.write("The negative correlation coefficient (r) of approximately -0.69 indicates a strong negative correlation between Absenteeism and Job Satisfaction.")
    st.write("As Absenteeism increases (employees missing more days), Job Satisfaction tends to decrease (lower job satisfaction scores). This suggests that higher absenteeism is associated with lower job satisfaction among employees.")

    
    st.markdown("Par exemple, l'absentéisme et la satisfaction au travail pourraient avoir une corrélation négative. Un coefficient de corrélation proche de **-1** représente une **forte corrélation négative**.")

    st.markdown("")
    
    
    st.markdown("- **Aucune corrélation** : **S'il n'y a pas de relation perceptible entre deux variables, elles sont considérées comme n'ayant aucune corrélation**. Le coefficient de corrélation serait proche de **0** dans de tels cas.")

    st.markdown("- **🏀Application 21** :")
    
    st.markdown("")
    











if st.button("Continuer vers la suite du Chap.5 - **B/ Régression linéaire simple : prédire les résultats**"):
    
    st.subheader("📈Chap.5-B/ Régression linéaire simple📉")
    
    st.markdown("La **régression linéaire simple est** une méthode statistique **utilisée pour comprendre et prédire la relation entre une variable dépendante et une seule variable indépendante**.")
    
    st.markdown("**Elle suppose une relation linéaire entre les deux variables et estime la ligne la mieux ajustée qui minimise la différence entre les données observées et les valeurs prédites**.") 
    
    st.markdown("En **RH, une régression linéaire simple peut être appliquée pour prédire les performances des employés** en fonction de divers facteurs. Par exemple, une entreprise peut vouloir comprendre comment le nombre d'heures consacrées à la formation influe sur la performance ultérieure d'un employé.") 
    
    st.markdown("**En analysant les données à l'aide d'une régression linéaire simple**, le contrôleur de gestion sociale peut estimer le niveau de performance attendu en fonction du nombre d'heures de formation.")

if st.button("Continuer vers la suite du Chap.5 - **C/ Régression multiple : prise en compte de plusieurs facteurs**"):
    
    st.markdown("La **régression multiple étend le concept** de régression linéaire simple **en incorporant plus d'une variable indépendante pour prédire une variable dépendante**. **Elle permet d'examiner l'effet combiné de plusieurs facteurs** sur un résultat d'intérêt.")
    
    st.markdown("Dans le contexte des RH, **la régression multiple peut être utilisée pour prédire le turnover en fonction de plusieurs variables** telles que **la satisfaction au travail, le salaire, la distance domicile - travail, et l'équilibre travail-vie personnelle**.") 
    
    st.markdown("En analysant les données historiques et en utilisant la régression multiple, le contrôleur de gestion sociale peut identifier les facteurs les plus importants impliqués dans le turnover et aider les services RH à développer des stratégies pour l'atténuer.")
    
    
    st.markdown("")


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
    redirect_button("https://cours-stats-rh.streamlit.app/Quiz_5_-_Correlation_et_Regression📉","Quiz du chapitre 5")

    
    
    
    
    
    
    
