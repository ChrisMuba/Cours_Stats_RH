


import streamlit as st

st.markdown("# Chapitre 2")
st.sidebar.markdown("# Chapitre 2")

st.title("Statistiques descriptives")

st.markdown("Comme nous l'avons précédemment vu, **les statistiques descriptives traitent de la collecte, de l'analyse et de la présentation des données**.") 
st.markdown("Elles vont fournir aux professionnels RH des outils pour décrire et résumer les données d'une manière facile à comprendre.")

if st.button("Cliquez pour acceder au Chap.2 - **A/ Mesures de tendance centrale**"):
    
    st.subheader("📈Chap.2-A/ Mesures de tendance centrale📉")
    
    st.markdown("Les **mesures de tendance centrale** sont utilisées pour définir le centre d'une distribution ou d'un ensemble de données.") 
    st.markdown("En statistique, une **distribution** fait référence au modèle de variation dans un ensemble de données numériques.") 
    st.markdown("Ce modèle de variation décrit comment les données sont réparties sur une plage de valeurs. On peut visualiser une distribution à l'aide d'un graphique, tel qu'un histogramme ou un box plot.")
    
    st.markdown("**Il existe trois principales mesures de tendance centrale** :")
    
    st.markdown("- **Moyenne** : il s'agit de la moyenne arithmétique d'un ensemble de valeurs. Elle est calculée en additionnant toutes les valeurs et en divisant par le nombre de valeurs.") 
    st.markdown("La moyenne est sensible aux valeurs aberrantes et aux valeurs extrêmes, et peut ne pas être représentative des données s'il existe des valeurs extrêmes.")


    import streamlit as st
    import plotly.express as px
    import pandas as pd
    import numpy as np

# Sample employee salary data (in thousands of dollars)
    salaires = [55000, 60000, 65000, 58000, 70000, 62000, 56000, 59000, 75000, 61000] 

# Create a DataFrame
    df = pd.DataFrame({'Salaire (en milliers €)': salaires})

# Calculate the mean
    mean_salary = np.mean(df['Salaire (en milliers €)'])

# Display the theoretical formula for calculating the mean
    st.subheader("Formule théorique de la **moyenne**")
    st.latex(r'\text{Moyenne} = \frac{\sum_{i=1}^{n}X_i}{n}')


    st.markdown("")


    st.markdown("**🏀Application**")
    st.markdown("**Salaires (€) : [55000, 60000, 65000, 58000, 70000, 62000, 56000, 59000, 75000, 61000]**")

    

# Display the steps for calculating the mean
    st.subheader("Étapes pour calculer la moyenne")
    st.markdown(
    """
    1. **Sommez toutes les valeurs:** additionnez toutes les valeurs de salaire dans l’ensemble de données.
    2. **Comptez le nombre de valeurs (n) :** déterminez le nombre total de salaires dans l'ensemble de données.
    3. **Appliquez la formule:** Divisez la somme par le nombre de valeurs pour obtenir la moyenne.
    """
)

# Display the calculated mean
    st.write(f"**Salaire moyen: {mean_salary:.2f} (en €)**")

# Create a histogram
    fig_hist = px.histogram(df, x='Salaire (en milliers €)', title='Histogramme de la distribution des salaires')

# Display the histogram
    st.plotly_chart(fig_hist)
    

    st.markdown("")


    st.markdown("**🔮Interpretation de l'histogramme de la distribution des salaires**")


    st.markdown("L'histogramme de répartition des salaires représente la **fréquence des différentes échelles** de salaire au sein de l'ensemble de données.")

    st.markdown("La plupart des salaires se situent dans la fourchette de **55 000 € à 65 000 €**, cette catégorie ayant la fréquence la plus élevée.")

    st.markdown("Il n'y a pas de salaires inférieurs à 55 000 € ou supérieurs à 75 000 dans cet ensemble de données.")

    st.markdown("La répartition est **légèrement asymétrique vers la gauche**, ce qui indique qu'il y a relativement plus d'employés dont le salaire est inférieur au salaire médian (environ 60 500 €).")


    st.markdown("")


    st.markdown("")

    
    st.markdown("- **Médiane** : la valeur médiane est le point milieu d'un ensemble de données numériques. Elle est calculée en organisant les données dans l'ordre croissant, de sorte que la moitié des valeurs soient inférieures ou égales à la médiane et l'autre moitié supérieures ou égales. Ainsi la médiane se trouve être le point milieu.") 
    st.markdown("Comparativement à la moyenne, la médiane est moins sensible aux valeurs aberrantes ou extrêmes ; et fournit une meilleure représentation de la⚡**valeur typique**⚡de l'ensemble de données.") 



    import streamlit as st
    import pandas as pd

# Sample employee salary data (in dollars)
    salaries = [55000, 60000, 65000, 58000, 70000, 62000, 56000, 59000, 75000, 61000]


# Display the theoretical formula for calculating the median
    st.subheader("Formule théorique de la **mediane**")
    st.latex(r'\text{Mediane} = \frac{N+1}{2}^{ème}\ \text{valeur dans les données classées par ordre croissant}')

    st.markdown("")


    st.markdown("**🏀Application**")
    st.markdown("**Salaires (€) : [55000, 60000, 65000, 58000, 70000, 62000, 56000, 59000, 75000, 61000]**")

# Display the steps for calculating the median
    st.subheader("Étapes pour calculer la mediane")
    st.markdown(
    """
    1. **Classez les données :** Commencez par classer les données salariales par ordre croissant.
    2. **Trouver la valeur médiane :** si l'ensemble de données comporte un nombre **impair** de valeurs (N), la médiane est la valeur médiane. 
       Si le nombre de valeurs est **pair**, la médiane est la moyenne des deux valeurs médianes.
    """
)


    # Calculate the median
    sorted_salaries = sorted(salaries)
    n = len(sorted_salaries)

    if n % 2 == 1:
    # Odd number of values
        median = sorted_salaries[n // 2]
    else:
    # Even number of values
        middle1 = sorted_salaries[(n - 1) // 2]
        middle2 = sorted_salaries[n // 2]
        median = (middle1 + middle2) / 2
    
    # Display the calculated median
    st.write(f"**Salaire median : {median} (en €)**")
    

    # Import necessary libraries
    import streamlit as st
    import plotly.express as px

# Data: Salaries in dollars
    salaires = [55000, 60000, 65000, 58000, 70000, 62000, 56000, 59000, 75000, 61000]

# Create a box plot using Plotly Express
    fig = px.box(x=salaires, labels={'x': 'Salaires (k€)'}, title="Box Plot de la distribution des salaires")

# Display the plot in the Streamlit app
    st.plotly_chart(fig)


    st.markdown("")


    st.markdown("**🔮Interpretation du box plot (boite à moustaches) de la distribution des salaires**")


    st.markdown("Le **box plot** fournit un résumé de la répartition des salaires, y compris des mesures de tendance centrale et de variabilité.")

    st.markdown("La boite représente l'intervalle interquartile (IQR), les bords inférieur (à gauche) et supérieur (à droite) de la case marquant respectivement le premier quartile (Q1) et le troisième quartile (Q3).")

    st.markdown("Intervalle interquartile (IQR) : la moitié moyenne des salaires (de Q1 à Q3) se situe entre environ 58 000 € et 65 000 €.")

    st.markdown("La ligne verticale à l’intérieur de la boite représente le salaire médian (Q2) : environ 60 500 €.")

    st.markdown("Les « moustaches » s'étendent des bords de la boîte jusqu'aux salaires minimum (55 000 €) et maximum (75 000 €) dans une fourchette raisonnable : **il n'y a pas de valeurs aberrantes dans l'ensemble de données**, car tous les salaires se situent dans la fourchette raisonnable des « moustaches ».")

    st.markdown("")


    st.markdown("")

    
    st.markdown("- **Mode** : c'est la valeur la plus courante dans un ensemble de données. Le mode est calculé en identifiant la valeur qui se produit le plus fréquemment.") 
    st.markdown("Il s'agit d'une mesure simple qui peut être utilisée pour résumer et décrire des données, en conjonction avec la moyenne et la médiane pour obtenir une image plus complète des données.") 
    st.markdown("⚠️Cependant, le mode a certaines limites. Par exemple, ce n'est pas un bon indicateur de tendance centrale lorsque les données contiennent des valeurs aberrantes, car ces valeurs peuvent fausser la distribution et rendre le mode moins représentatif de la⚡**valeur typique**⚡dans les données.") 
    st.markdown("Dans de tels cas, d'autres mesures de tendance centrale, telles que la moyenne ou la médiane, peuvent être plus appropriées.")


# Import necessary libraries
    import streamlit as st
    import pandas as pd
    import plotly.express as px

# Display the formula for calculating the mode
    st.subheader("Comment trouver le **mode** ?")
    st.markdown("Le mode est la valeur qui apparaît **le plus fréquemment** dans l'ensemble de données.)")

    st.markdown("**🏀Application**")
    
    # Sample data without outliers
    data_without_outliers = [35000, 40000, 42000, 45000, 48000, 50000, 50000, 52000, 55000, 58000, 60000]

# Create a DataFrame
    df_without_outliers = pd.DataFrame(data_without_outliers, columns=['Salaires (€)'])

# Display the data table
    st.markdown("Ci-dessous un échantillon de données de **Salaires (en €)** :")
    st.dataframe(df_without_outliers)
    
    

    # Display the steps for calculating the mode
    st.subheader("Étapes pour déterminer le mode")
    st.markdown(
    """
    1. **Classez les données :** Commencez par classer les données salariales par ordre croissant.
    2. **Trouver la valeur médiane :** si l'ensemble de données comporte un nombre **impair** de valeurs (N), la médiane est la valeur médiane. 
       Si le nombre de valeurs est **pair**, la médiane est la moyenne des deux valeurs médianes.
    """
)






# Calculate the mode
    mode_without_outliers = df_without_outliers['Salaires (€)'].mode().values[0]

# Display the mode
    st.subheader(f"Mode (Without Outliers): {mode_without_outliers}")

# Explanation and calculation steps
    st.subheader("Calculation Steps (Without Outliers)")

    # Step 1: Frequency Distribution
    st.write("Step 1: Create a frequency distribution to count the occurrences of each value in the dataset.")
    frequency_table_without_outliers = df_without_outliers['Salaires (€)'].value_counts().reset_index()
    frequency_table_without_outliers.columns = ['Salaires (€)', 'Frequency']
    st.dataframe(frequency_table_without_outliers)

# Step 2: Find the Maximum Frequency
    st.write("Step 2: Identify the value(s) with the highest frequency (mode).")
    max_frequency_without_outliers = frequency_table_without_outliers['Frequency'].max()
    mode_values_without_outliers = frequency_table_without_outliers[frequency_table_without_outliers['Frequency'] == max_frequency_without_outliers]['Salaires (€)'].tolist()
    st.write(f"Mode Value(s): {mode_values_without_outliers}")

# Create a histogram
    fig_without_outliers = px.histogram(df_without_outliers, x='Salaires (€)', nbins=6, title='Salary Distribution (Without Outliers)')
    st.plotly_chart(fig_without_outliers)





    

# Sample data without outliers
    data_without_outliers = [35000, 40000, 42000, 45000, 48000, 50000, 50000, 52000, 55000, 58000, 60000]

# Create a DataFrame
    df_without_outliers = pd.DataFrame(data_without_outliers, columns=['Salary'])

# Display the data table
    st.subheader("Sample Salary Data (Without Outliers)")
    st.dataframe(df_without_outliers)

# Calculate the mode
    mode_without_outliers = df_without_outliers['Salary'].mode().values[0]

# Display the mode
    st.subheader(f"Mode (Without Outliers): {mode_without_outliers}")

# Create a histogram
    fig_without_outliers = px.histogram(df_without_outliers, x='Salary', nbins=6, title='Salary Distribution (Without Outliers)')
    st.plotly_chart(fig_without_outliers)

# Explanation
    st.write("""
    In this example, we have a sample of salary data without any outliers. The mode represents the most 
    common salary in the dataset, which is the value that occurs most frequently. In this case, 
    the mode is used to describe the central tendency of the salary distribution. The mode helps HR 
    professionals understand the most typical salary level within the organization.
""")

# Create a second Streamlit app for data with outliers
    st.header("Measures of Central Tendency - Mode (With Outliers)")

# Sample data with outliers
    data_with_outliers = [35000, 40000, 42000, 45000, 48000, 50000, 50000, 52000, 55000, 58000, 60000, 100000, 120000]

# Create a DataFrame
    df_with_outliers = pd.DataFrame(data_with_outliers, columns=['Salary'])

# Display the data table
    st.subheader("Sample Salary Data (With Outliers)")
    st.dataframe(df_with_outliers)

# Calculate the mode
    mode_with_outliers = df_with_outliers['Salary'].mode().values[0]

# Display the mode
    st.subheader(f"Mode (With Outliers): {mode_with_outliers}")

# Create a histogram
    fig_with_outliers = px.histogram(df_with_outliers, x='Salary', nbins=6, title='Salary Distribution (With Outliers)')
    st.plotly_chart(fig_with_outliers)

# Explanation
    st.write("""
    In this example, we have a sample of salary data that includes outliers. Outliers are extreme values 
    that can skew the distribution. When outliers are present, the mode may not accurately represent 
    the central tendency because it's heavily influenced by the outliers. In such cases, other measures 
    like the mean or median may provide a better understanding of the typical salary level.
""")



if st.button("Continuer vers la suite du Chap.2 - **B/ Mesures de la variabilité**"):
    
    st.subheader("📈Chap.2-B/ Mesures de la variabilité📉")
    
    st.markdown("Les mesures de variabilité sont utilisées pour décrire la dispersion (propagation) d'une distribution ou d'un ensemble de données.") 
    st.markdown("**Il existe plusieurs mesures principales de la variabilité** :")
    
    st.markdown("- **Plage** : c'est la différence entre les valeurs maximales et minimales dans un ensemble de données.") 
    st.markdown("Elle fournit une estimation approximative de la variabilité, mais est sensible aux valeurs aberrantes.")
                
    st.markdown("- **Variance** : il s'agit de la moyenne des différences au carré entre chaque valeur et la moyenne.") 
    st.markdown("Elle fournit une mesure plus précise de la variabilité, mais est affecté par des valeurs extrêmes.")    
                
    st.markdown("- **Écart type** : C'est la racine carrée de la variance. Il s'agit de la mesure de variabilité la plus couramment utilisée et fournit une mesure de la dispersion dans les mêmes unités que l'ensemble de données d'origine.")            

if st.button("Continuer vers la suite du Chap.2 - **C/ Techniques graphiques**"):
    
    st.subheader("📈Chap.2-C/ Techniques graphiques📉")
    
    st.markdown("Des techniques graphiques peuvent être utilisées pour améliorer encore la compréhension d'un ensemble de données.") 
    st.markdown("Les représentations visuelles peuvent aider les professionnels RH à identifier facilement des modèles ou des tendances dans les données et à communiquer des informations aux parties prenantes.")
    
    st.markdown("**Certains types courants de graphiques incluent** :") 
    
    st.markdown("- **Histogramme** : c'est un graphique qui montre la distribution de fréquence des données numériques. Les données sont divisées en intervalles ou bacs, et la hauteur de la barre représente la fréquence de chaque intervalle.")
    
    st.markdown("- **Boîte à moustache** : ce graphique montre la distribution de données numériques à l'aide de quartiles. Il affiche le minimum, le maximum, la médiane et les premier et troisième quartiles des données.")
    
    st.markdown("- **Nuages de points** : un graphique qui montre la relation entre deux variables numériques. Chaque point représente une paire de valeurs et le modèle des points peut indiquer la force et la direction de la relation.")
    



        
        
        
        
        
        
