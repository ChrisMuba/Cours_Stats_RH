


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
    st.write(f"Coefficient de correlation (r): {correlation_coefficient:.2f}")

# Determine the type of correlation
    if correlation_coefficient > 0:
        correlation_type = "correlation positive"
    elif correlation_coefficient < 0:
        correlation_type = "correlation negative"
    else:
        correlation_type = "non correlation"

# Create a scatter plot with a trendline
    fig = px.scatter(df, x='Productivité de l\'agent', y='Satisfaction au travail', title='DataViz : Productivité de l\'agent vs. Satisfaction au travail', trendline='ols')
    st.plotly_chart(fig)

    # Display the correlation type with the coefficient
    st.write(f"Cette dataviz indique une {correlation_type} avec un coefficient de {correlation_coefficient:.2f}.")

    # Explanation
    with st.expander("🔮Interpretation"):
        st.write("""
        Le coefficient de corrélation positive (r) d'environ 0,98 indique une forte corrélation positive entre la productivité des agents et la satisfaction au travail. 
        
        À mesure que la satisfaction au travail augmente (scores de satisfaction au travail plus élévés), la productivité des agents augmente aussi (les agents accomplissent plus de tâches dans un laps de temps donné). 
        Cela suggère qu’une productivité plus élevée est associée à une meilleure satisfaction au travail parmi les agents.
        """)


    st.markdown("")

    st.markdown("")
    
    st.markdown("")
    
    
    st.markdown("- **Corrélation négative** : **lorsque deux variables évoluent dans des directions opposées**, elles présentent une **corrélation négative**.") 

    st.markdown("**🏀Application 20** :")

    st.markdown("Notre contrôleur de gestion sociale à *Ploucs-lès-Landes* souhaite maintenant analyser la relation entre « Absentéisme (en jours) » et « Satisfaction au travail (échelle 1-5) ».")

    st.markdown("Ci-dessous un échantillon des données collectées :")


# Import necessary libraries
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px

# Sample HR data
    data = {
        'Agents': list(range(1, 11)),
        'Absentéisme (jours)': [5, 2, 8, 1, 6, 4, 9, 3, 7, 2],
        'Satisfaction au travail (échelle 1-5)': [2, 4, 1, 5, 2, 3, 1, 4, 1, 3]
    }

# Create a DataFrame
    df = pd.DataFrame(data)

# Display the sample data
    st.dataframe(df)

# Introduction
    st.write("Dans cet exercice, nous analyserons la corrélation négative entre le nombre de jours d'absence et la satisfaction au travail.")

# Calculate and display the correlation coefficient
    correlation_coefficient = df['Absentéisme (jours)'].corr(df['Satisfaction au travail (échelle 1-5)'])
    st.write(f"Coefficient de correlation (r): {correlation_coefficient:.2f}")

# Determine the type of correlation
    if correlation_coefficient > 0:
        correlation_type = "correlation positive"
    elif correlation_coefficient < 0:
        correlation_type = "correlation negative"
    else:
        correlation_type = "non correlation"

# Create a scatter plot with a trendline
    fig = px.scatter(df, x='Absentéisme (jours)', y='Satisfaction au travail (échelle 1-5)', title='DataViz : Absentéisme vs. Satisfaction au travail', trendline='ols')
    st.plotly_chart(fig)

    st.write(f"Cette dataviz indique une {correlation_type} avec un coefficient de {correlation_coefficient:.2f}.")

    # Explanation
    with st.expander("🔮Interpretation"):
        st.write("""
        Le coefficient de corrélation négative (r) d'environ -0,94 indique une forte corrélation négative entre l'absentéisme et la satisfaction au travail. 
        
        À mesure que l’absentéisme augmente (les agents manquent plus de jours), la satisfaction au travail a tendance à diminuer (scores de satisfaction au travail plus faibles). 
        Cela suggère qu’un absentéisme plus élevé est associé à une moindre satisfaction au travail parmi les agents.
        """)


    st.markdown("")


    st.markdown("")


    st.markdown("- **Aucune corrélation** : **S'il n'y a pas de relation perceptible entre deux variables**, elles sont considérées comme n'ayant **aucune corrélation**.") 
    
    st.markdown("Le coefficient de corrélation serait alors proche de **0**.")

    st.markdown("**🏀Application 21** :")

    st.markdown("Notre contrôleur de gestion sociale à *Ploucs-lès-Landes* souhaite analyser la relation entre les niveaux de salaires et les notes d'évaluations de performances des agents de sa commune. Il veut déterminer s'il n'y a pas de corrélation entre ces variables.")

    st.markdown("Ci-dessous un échantillon des données collectées :")


    st.markdown("")
    
    
    st.markdown("")
    
# Import necessary libraries
    import streamlit as st
    import pandas as pd
    import plotly.express as px

# Sample HR data
    data = {
       'Agents': list(range(1, 11)),
        'Salaire annuel (€)': [120000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000],
        'Évaluation des performances (échelle 1 à 5)': [4, 3, 5, 2, 5, 4, 3, 5, 4, 2]
    }

# Create a DataFrame
    df = pd.DataFrame(data)
    
# Display the sample data
    st.dataframe(df)

# Introduction
    st.write("Dans cet exercice, nous analyserons s'il existe une corrélation entre les salaires annuels et les notes d'évaluation des performances.")

# Calculate and display the correlation coefficient
    correlation_coefficient = df['Salaire annuel (€)'].corr(df['Évaluation des performances (échelle 1 à 5)'])
    st.write(f"Coefficient de correlation (r): {correlation_coefficient:.2f}")

# Create a scatter plot with a trendline
    fig = px.scatter(df, x='Salaire annuel (€)', y='Évaluation des performances (échelle 1 à 5)', title='DataViz : Salaire annuel (€) vs. Notes d\'évaluation des performances')
    fig.update_traces(marker=dict(size=12, opacity=0.6), selector=dict(mode='markers'))
    fig.add_trace(
        px.scatter(df, x='Salaire annuel (€)', y='Évaluation des performances (échelle 1 à 5)', trendline="ols").data[1]
    )
    st.plotly_chart(fig)

    # Explanation
    with st.expander("🔮Interpretation"):
        st.write("""
        Le coefficient de corrélation d'environ 0,03 est proche de 0, ce qui indique qu'il n'y a aucune relation perceptible entre le niveau de salaire annuel et les notes d'évaluation des performances. 
        
        En d’autres termes, le salaire annuel qu’un agent reçoit ne semble pas avoir un impact significatif sur sa performance.
        """)

    st.markdown("")


if st.button("Continuer vers la suite du Chap.5 - **B/ Régression linéaire simple : prédire les résultats**"):
    
    st.subheader("📈Chap.5-B/ Régression linéaire simple📉")
    
    st.markdown("- La **régression linéaire simple est** une méthode statistique **utilisée pour comprendre et prédire la relation entre une variable dépendante et une seule variable indépendante**.")
    
    st.markdown("**Elle suppose une relation linéaire entre les deux variables et estime la ligne la mieux ajustée qui minimise la différence entre les données observées et les valeurs prédites**.")

    st.markdown("**🏀Application 22** :")

    st.markdown("Illustrons le concept de la « Régression linéaire simple » à l'aide de données RH pour comprendre comment prédire la note de performance d'un employé en fonction de ses années d'expérience.")

    st.markdown("Supposons que nous avons un ensemble de données avec deux variables, « Années d'expérience (variable indépendante) » et « Notes d'évaluation des performances (variable dépendante) ».")
    
    st.markdown("Ci-dessous un échantillon de nos données :")


    st.markdown("")
    
    
    st.markdown("")


# Import necessary libraries
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    from sklearn.linear_model import LinearRegression

# Step 1: Generate Sample Data
    np.random.seed(0)
    years_of_experience = np.random.randint(1, 20, 50)  # Generate 50 random years of experience
    performance_rating = 3 + 0.5 * years_of_experience + np.random.normal(0, 2, 50)  # Simulate performance rating

# Create a DataFrame
    data = pd.DataFrame({'Années d\'expérience': years_of_experience, 'Notes de performance': performance_rating})

# Display the sample data
    st.dataframe(data)

# Introduction
    st.write("Dans cet exercice, nous effectuerons une régression linéaire simple afin de trouver la droite la mieux adaptée qui prédit l'évaluation des performances en fonction des années d'expérience ; et visualiserons la droite de régression et les points de données.")


# Step 2: Perform Simple Linear Regression
    X = data['Années d\'expérience'].values.reshape(-1, 1)
    y = data['Notes de performance'].values
    model = LinearRegression()
    model.fit(X, y)

# Scatter plot with the regression line
    scatter_fig = go.Figure()

# Add scatter plot
    scatter_fig.add_trace(go.Scatter(x=data['Années d\'expérience'], y=data['Notes de performance'],
                                     mode='markers', name='Data Points'))

# Add regression line
    y_pred = model.predict(X)
    scatter_fig.add_trace(go.Scatter(x=data['Années d\'expérience'], y=y_pred,
                                     mode='lines', name='Regression Line', line=dict(color='red')))

    scatter_fig.update_layout(title="DataViz : Notes de performance vs. Années d\'expérience",
                           xaxis_title="Années d\'expérience",
                           yaxis_title="Notes de performance")
    st.plotly_chart(scatter_fig)

# Step 4: Interpretation
    st.write("🔮Interpretation:")
    st.write("Une régression linéaire simple nous aide à comprendre la relation entre les années d'expérience et l'évaluation des performances.")
    st.write(f"L'équation de régression est: Notes de performance = {model.intercept_:.2f} + {model.coef_[0]:.2f} * Années d'expérience")
    st.write("Ici, l'intercept représente la note de performance attendue lorsqu'un employé a 0 année d'expérience.")
    st.write("Le coefficient représente la variation attendue de la note de performance pour une augmentation d'une unité du nombre d'années d'expérience.")
    st.write("Dans notre cas, pour chaque année d'expérience supplémentaire, la note de performance attendue augmente d'environ 0,50 point.")

     
    st.markdown("")



    st.markdown("") 
    
    st.markdown("")

if st.button("Continuer vers la suite du Chap.5 - **C/ Régression multiple : prise en compte de plusieurs facteurs**"):
    
    st.markdown("La **régression multiple étend le concept** de régression linéaire simple **en incorporant plus d'une variable indépendante pour prédire une variable dépendante**. **Elle permet d'examiner l'effet combiné de plusieurs facteurs** sur un résultat d'intérêt.")
    
    st.markdown("Dans le contexte des RH, **la régression multiple peut être utilisée pour prédire le turnover en fonction de plusieurs variables** telles que **la satisfaction au travail, le salaire, la distance domicile - travail, et l'équilibre travail-vie personnelle**.") 
    
    st.markdown("En analysant les données historiques et en utilisant la régression multiple, le contrôleur de gestion sociale peut identifier les facteurs les plus importants impliqués dans le turnover et aider les services RH à développer des stratégies pour l'atténuer.")


# Import necessary libraries
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import statsmodels.api as sm

# Step 1: Generate Sample Data
    np.random.seed(0)

# Simulate data for job satisfaction, salary, distance, work-life balance, and turnover
    n_samples = 100
    job_satisfaction = np.random.uniform(1, 5, n_samples)
    salary = np.random.uniform(30000, 80000, n_samples)
    distance_to_work = np.random.uniform(1, 30, n_samples)
    work_life_balance = np.random.uniform(1, 5, n_samples)
    turnover = 20 + 3 * job_satisfaction - 2 * salary + 1.5 * distance_to_work + 2 * work_life_balance + np.random.normal(0, 5, n_samples)

# Create a DataFrame
    data = pd.DataFrame({'Job Satisfaction': job_satisfaction, 'Salary': salary,
                         'Distance to Work': distance_to_work, 'Work-Life Balance': work_life_balance, 'Turnover': turnover})

# Step 2: Perform Multiple Regression
    X = data[['Job Satisfaction', 'Salary', 'Distance to Work', 'Work-Life Balance']]
    X = sm.add_constant(X)  # Add a constant (intercept) to the model
    y = data['Turnover']

    model = sm.OLS(y, X).fit()

# Step 3: Visualize the Results
    st.title("Multiple Regression in HR")
    st.write("Dataset - Predicting Turnover")

# Scatter plot of actual vs. predicted values
    fig = px.scatter(x=model.fittedvalues, y=data['Turnover'], labels={'x': 'Predicted Turnover', 'y': 'Actual Turnover'})
    st.plotly_chart(fig)

# Step 4: Interpretation
    st.write("Interpretation:")
    st.write("Multiple regression helps us understand how multiple factors (independent variables) collectively impact a dependent variable (turnover in this case).")

# Print regression coefficients
    st.write("Regression Coefficients:")
    st.write(model.params)

# Interpretation of coefficients
    st.write("Interpreting the coefficients:")
    st.write("1. Job Satisfaction: For every one-unit increase in job satisfaction, turnover is expected to increase by approximately 3 units.")
    st.write("2. Salary: For every one-unit increase in salary, turnover is expected to decrease by approximately 2 units.")
    st.write("3. Distance to Work: For every one-unit increase in distance to work, turnover is expected to increase by approximately 1.5 units.")
    st.write("4. Work-Life Balance: For every one-unit increase in work-life balance, turnover is expected to increase by approximately 2 units.")

    st.write("These coefficients help HR professionals identify which factors have the most significant impact on turnover. In this example, job satisfaction and work-life balance have the strongest influence on turnover.")



# Import necessary libraries
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import statsmodels.api as sm
    import plotly.graph_objects as go

# Step 1: Generate Sample Data
    np.random.seed(0)

# Simulate data for job satisfaction, salary, distance, work-life balance, and turnover
    n_samples = 100
    job_satisfaction = np.random.uniform(1, 5, n_samples)
    salary = np.random.uniform(30000, 80000, n_samples)
    distance_to_work = np.random.uniform(1, 30, n_samples)
    work_life_balance = np.random.uniform(1, 5, n_samples)
    turnover = 20 + 3 * job_satisfaction - 2 * salary + 1.5 * distance_to_work + 2 * work_life_balance + np.random.normal(0, 5, n_samples)

# Create a DataFrame
    data = pd.DataFrame({'Job Satisfaction': job_satisfaction, 'Salary': salary,
                         'Distance to Work': distance_to_work, 'Work-Life Balance': work_life_balance, 'Turnover': turnover})

# Step 2: Perform Multiple Regression
    X = data[['Job Satisfaction', 'Salary', 'Distance to Work', 'Work-Life Balance']]
    X = sm.add_constant(X)  # Add a constant (intercept) to the model
    y = data['Turnover']

    model = sm.OLS(y, X).fit()

# Step 3: Visualize the Results
    st.title("Multiple Regression in HR")
    st.write("Dataset - Predicting Turnover")

# Scatter plot with regression lines
    fig = go.Figure()

# Add scatter plot of actual vs. predicted values
    fig.add_trace(go.Scatter(x=model.fittedvalues, y=data['Turnover'], 
                             mode='markers', name='Actual vs. Predicted Turnover'))

# Add regression lines
    for idx, col in enumerate(X.columns):
        if col != 'const':  # Skip the constant (intercept) column
            line = model.params[col] * X[col]  # Calculate the regression line for each variable
            fig.add_trace(go.Scatter(x=X[col], y=line, mode='lines', 
                                     name=f'Regression Line ({col})', line=dict(color=f'rgb({idx*50},0,0)')))

    fig.update_layout(xaxis_title="Predicted Turnover",
                      yaxis_title="Actual Turnover",
                      title="Actual vs. Predicted Turnover and Regression Lines")
    st.plotly_chart(fig)

# Display the DataFrame
    st.write("Sample HR Data:")
    st.write(data)

# Step 4: Interpretation
    st.write("Interpretation:")
    st.write("Multiple regression helps us understand how multiple factors (independent variables) collectively impact a dependent variable (turnover in this case).")

# Print regression coefficients
    st.write("Regression Coefficients:")
    st.write(model.params)

# Interpretation of coefficients
    st.write("Interpreting the coefficients:")
    st.write("1. Job Satisfaction: For every one-unit increase in job satisfaction, turnover is expected to increase by approximately 3 units.")
    st.write("2. Salary: For every one-unit increase in salary, turnover is expected to decrease by approximately 2 units.")
    st.write("3. Distance to Work: For every one-unit increase in distance to work, turnover is expected to increase by approximately 1.5 units.")
    st.write("4. Work-Life Balance: For every one-unit increase in work-life balance, turnover is expected to increase by approximately 2 units.")

    st.write("These coefficients help HR professionals identify which factors have the most significant impact on turnover. In this example, job satisfaction and work-life balance have the strongest influence on turnover.")


    import pandas as pd

    data = {
        'YearsExperience': [2, 3, 5, 7, 8, 10, 12, 15, 20, 22],
        'TrainingHours': [10, 12, 15, 18, 20, 25, 30, 35, 40, 45],
        'EmployeeSatisfaction': [3, 4, 3, 5, 4, 4, 5, 3, 5, 4],
        'PerformanceRating': [60, 65, 68, 72, 70, 75, 80, 78, 85, 88]
    }

    df = pd.DataFrame(data)

    import streamlit as st
    import plotly.express as px
    import statsmodels.api as sm

# Title for the Streamlit app
    st.title("Multiple Regression Analysis in HR")

# Scatter plot to visualize the data
    scatter_fig = px.scatter(df, x='YearsExperience', y='PerformanceRating',
                             title='Performance Rating vs. Years of Experience',
                             labels={'YearsExperience': 'Years of Experience', 'PerformanceRating': 'Performance Rating'})

# Adding a regression line to the scatter plot
    scatter_fig.update_traces(
        mode='markers+lines',
        marker=dict(size=8),
        line=dict(color='red', width=2)
    )

# Display the scatter plot
    st.plotly_chart(scatter_fig)

# Multiple regression analysis
    X = df[['YearsExperience', 'TrainingHours', 'EmployeeSatisfaction']]
    X = sm.add_constant(X)  # Add a constant term (intercept)
    y = df['PerformanceRating']

# Fit the regression model
    model = sm.OLS(y, X).fit()

# Display regression results
    st.header("Multiple Regression Results")
    st.write(model.summary())




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

    
    
    
    
    
    
    
