


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
    st.subheader("Formule théorique de la moyenne")
    st.latex(r'\text{Moyenne} = \frac{\sum_{i=1}^{n}X_i}{n}')


    st.markdown("")


    st.markdown("**🏀Application 1**")
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
    st.write(f"**💡Salaire moyen: {mean_salary:.2f} (en €)**")

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
    st.subheader("Formule théorique de la mediane")
    st.latex(r'\text{Mediane} = \frac{N+1}{2}^{ème}\ \text{valeur dans les données classées par ordre croissant}')

    st.markdown("")


    st.markdown("**🏀Application 2**")
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
    st.write(f"**💡Salaire median : {median} (en €)**")
    

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
    st.subheader("Comment trouver le mode ?")
    st.markdown("Le mode est la valeur qui apparaît **le plus fréquemment** dans l'ensemble de données.)")

    st.markdown("**🏀Application 3**")
    
# Sample data without outliers
    data_without_outliers = [35000, 40000, 42000, 45000, 48000, 50000, 50000, 52000, 55000, 58000, 60000]

# Create a DataFrame
    df_without_outliers = pd.DataFrame(data_without_outliers, columns=['Salaires (€)'])

# Display the data table
    st.subheader("Echantillon de données salariales SANS outliers (valeurs aberrantes)")
    st.dataframe(df_without_outliers)
    

# Calculate the mode
    mode_without_outliers = df_without_outliers['Salaires (€)'].mode().values[0]


# Explanation and calculation steps
    st.subheader("Étapes pour déterminer le mode")

    # Step 1: Frequency Distribution
    st.write("**Étape 1**: Créez une distribution de fréquence pour compter les occurrences de chaque valeur dans l'ensemble de données.")
    frequency_table_without_outliers = df_without_outliers['Salaires (€)'].value_counts().reset_index()
    frequency_table_without_outliers.columns = ['Salaires (€)', 'Frequence']
    st.dataframe(frequency_table_without_outliers)

# Step 2: Find the Maximum Frequency
    st.write("**Étape 2** : Identifiez la ou les valeurs avec la fréquence (mode) la plus élevée.")
    max_frequency_without_outliers = frequency_table_without_outliers['Frequence'].max()
    mode_values_without_outliers = frequency_table_without_outliers[frequency_table_without_outliers['Frequence'] == max_frequency_without_outliers]['Salaires (€)'].tolist()
    st.write(f"💡La valeur du **mode** est : {mode_values_without_outliers}")

# Create a histogram
    fig_without_outliers = px.histogram(df_without_outliers, x='Salaires (€)', nbins=6, title='Histogramme de la distribution des salaires')
    st.plotly_chart(fig_without_outliers)


    st.markdown("")


    st.markdown("**🔮Interpretation de l'histogramme des salaires sans valeurs aberrantes**")


    st.markdown("L'histogramme est une distribution de fréquence qui montre le nombre d'observations dans des intervalles spécifiques. Dans notre cas, l'histogramme représente la répartition des salaires sans valeurs aberrantes.") 
    
    st.markdown("Cet histogramme montre une répartition relativement symétrique centrée autour des valeurs moyennes (entre 45 000 et 55 000 €), avec un pic autour de 50 000 €. Les données semblent être distribuées assez normalement, sans outliers significatifs.")
    
    st.markdown("Il apparaît quelques observations en dessous de 45 000 et au-dessus de 60 000 €. Cela suggère que la majorité des employés ont des salaires similaires, et que seuls quelques-uns ont des salaires nettement inférieurs ou supérieurs.")

    
    st.markdown("")


    st.markdown("**🏀Application 4**")


# Sample data with outliers
    data_with_outliers = [35000, 40000, 42000, 45000, 48000, 50000, 50000, 52000, 55000, 58000, 60000, 100000, 120000]

# Create a DataFrame
    df_with_outliers = pd.DataFrame(data_with_outliers, columns=['Salaires (€)'])

# Display the data table
    st.subheader("Echantillon de données salariales AVEC outliers (valeurs aberrantes)")
    st.dataframe(df_with_outliers)

# Calculate the mode
    mode_with_outliers = df_with_outliers['Salaires (€)'].mode().values[0]

# Explanation and calculation steps
    st.subheader("Tableau de la distribution de fréquence")

    # Step 1: Frequency Distribution
    frequency_table_with_outliers = df_with_outliers['Salaires (€)'].value_counts().reset_index()
    frequency_table_with_outliers.columns = ['Salaires (€)', 'Frequence']
    st.dataframe(frequency_table_with_outliers)

# Step 2: Find the Maximum Frequency
    max_frequency_with_outliers = frequency_table_with_outliers['Frequence'].max()
    mode_values_with_outliers = frequency_table_with_outliers[frequency_table_with_outliers['Frequence'] == max_frequency_with_outliers]['Salaires (€)'].tolist()
    st.write(f"💡La valeur du **mode** est : {mode_values_with_outliers}")

# Create a histogram
    fig_with_outliers = px.histogram(df_with_outliers, x='Salaires (€)', nbins=6, title='Histogramme de la distribution des salaires (avec Outliers)')
    st.plotly_chart(fig_with_outliers)

# Explanation
    st.markdown("**🔮Interpretation de l'histogramme des salaires avec valeurs aberrantes**")
    st.write("""
    Dans cet exemple, nous avons un échantillon de données salariales qui inclut des valeurs aberrantes.  
    Il s'agit des valeurs extrêmes qui peuvent **fausser la distribution**. Lorsque des valeurs aberrantes sont présentes, 
    le mode peut **ne pas représenter avec précision la tendance centrale**
    car il est fortement influencé par les valeurs aberrantes. Dans de tels cas, d’autres mesures 
    comme la moyenne ou la médiane peuvent permettre de mieux comprendre le niveau de salaire typique.
""")


    st.markdown("")


# Import necessary libraries
    import streamlit as st
    import plotly.express as px

# Data: Salaries in dollars
    salaires = [35000, 40000, 42000, 45000, 48000, 50000, 50000, 52000, 55000, 58000, 60000, 100000, 120000]

# Create a box plot using Plotly Express
    fig = px.box(x=salaires, labels={'x': 'Salaires (k€)'}, title="Box Plot de la distribution des salaires avec outliers")

# Display the plot in the Streamlit app
    st.plotly_chart(fig)

    st.markdown("**🔮Interpretation du box plot de la distribution des salaires avec valeurs aberrantes**")
    st.write("""
    Le **box plot** nous confirme visuellement la présence de valeurs aberrantes dans les données, avec des salaires allant de 35 000 € à 120 000 €.  
    La ligne verticale à l’intérieur de la boite nous montre que le salaire médian est de 50 000 €, et les moustaches nous montrent l'écart des salaires dans une plage de 1,5 fois l'écart interquartile (IQR). 
    Les valeurs aberrantes, représentées par les deux points individuels en dehors des moustaches, sont les salaires de 100 000 € et 120 000 €.
    La présence de valeurs aberrantes dans les données suggère que certains employés ont des salaires nettement supérieurs à ceux de la majorité des employés.
""")


if st.button("Continuer vers la suite du Chap.2 - **B/ Mesures de la variabilité**"):
    
    st.subheader("📈Chap.2-B/ Mesures de la variabilité📉")
    
    st.markdown("Les mesures de variabilité sont utilisées pour décrire la dispersion (propagation) des points de données dans un ensemble de données.") 
    st.markdown("**Il existe plusieurs mesures principales de la variabilité** :")
    
    st.markdown("- **Plage** : La plage (gamme, étendue) est la mesure de variabilité la plus simple, elle représente la différence entre les valeurs maximales et minimales dans un ensemble de données. Elle fournit une estimation approximative de la variabilité, mais est sensible aux valeurs aberrantes.")

    st.markdown("**Mathématiquement, on peut l'exprimer comme suit :**")

    st.subheader("Plage = Valeur maximale - Valeur minimale")


    st.markdown("")

    

    st.markdown("**🏀Application 5**")

    st.write("""Supposons que nous disposions d'un échantillon de données sur l'âge des employés d'une entreprise. 
    
    âges = [22, 25, 30, 35, 40, 45, 50, 55, 60 et 65 ans] 
    
    💡La plage de cet échantillon de données est : 65 - 22 = 43 ans.
""")


    st.markdown("")


    st.markdown("Bien que cette plage puisse donner un aperçu de la répartition des âges au sein de l'entreprise, elle présente certaines limites :")

    st.markdown("1. Elle ne tient pas compte de la distance entre les points de données consécutifs.")
    st.markdown("2. Elle peut être affectée par des valeurs extrêmes ou des valeurs aberrantes.")
    

    st.markdown("Pour mieux **visualiser et comprendre** la répartition des âges dans notre échantillon de données, nous pouvons utiliser d'autres représentations en plus de la plage. Certaines techniques de visualisation populaires incluent : Histogramme et Box plot.") 
    
    
    st.markdown("")


     # Import necessary libraries
    import streamlit as st
    import plotly.express as px

# Data: Salaries in dollars
    âges = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]

# Create a box plot using Plotly Express
    fig = px.box(x=âges, labels={'x': 'âge des employés (ans)'}, title="Box Plot de lâge des employés de l'entreprise")

# Display the plot in the Streamlit app
    st.plotly_chart(fig)

    st.markdown("**🔮Interpretation du box plot de lâge des employés de l'entreprise**")


    st.markdown("Ce **box plot** affiche la répartition des âges dans l'échantillon de données, l'axe horizontal représentant les différentes tranches d'âge.")

    st.markdown("L'intervalle interquartile **IQR** (représenté par la boite) nous montre que la majorité des employés (50 %) ont entre 30 et 55 ans.")
    
    st.markdown("L’âge médian, (représenté par la ligne verticale dans la boite) est de 42.5 ans, ce qui signifie que la moitié des employés de l'échantillon de données a plus de 42.5 ans et l'autre moitié moins : il s'agit d'une information utile à connaître, car elle peut aider à éclairer les politiques et les pratiques liées au développement et à la rétention des employés.")

    st.markdown("Ce **box plot** montre également les quartiles inférieur (Q1 = 30 ans) et supérieur (Q3 = 55 ans), qui sont représentés respectivement par les côtés gauche et droit de la boîte. Les valeurs de **Q1 et Q3** signifient respectivement que 25 % des employés ont moins de 30 ans et 25 %de plus de 55 ans.")

    st.markdown("")


    st.markdown("")
    
    
    st.markdown("- **Variance** : La variance est une mesure de variabilité plus sophistiquée que la plage. C'est une mesure de **comment** les données d'un ensemble diffèrent de la moyenne de l'ensemble.") 

    # Display the theoretical formula for calculating the variance
    st.subheader("Formule théorique de la Variance")
    st.latex(r'Variance (\sigma^2) = \frac{\sum_{i=1}^{n}(X_i - \mu)^2}{N}')

    st.markdown("Où :")

    st.markdown("**σ²** représente la variance")

    st.markdown("**Xᵢ** représente chaque point de données individuel")

    st.markdown("**μ** représente la moyenne de l'échantillon de données")

    st.markdown("**N** est le nombre total de points de données")


    st.markdown("")


    st.markdown("**🏀Application 6**")
    st.markdown("❗Pour la suite nous pourrions exprimer nos **scores de satisfaction** en ESI (employee satisfaction index) mais cela n'a aucun intérêt pour illustrer le calcul de la variance, donc nous travaillerons avec les données brutes.")

    st.markdown("Supposons que vous ayez mené une enquête sur l'engagement des employés et que vous ayez collecté des scores de satisfaction sur une échelle de 1 à 10, où 1 représente très insatisfait et 10 représente très satisfait. Vous avez interrogé 10 employés.")
    

    import streamlit as st
    import pandas as pd
    import plotly.express as px

# Create a high variance dataset
    data = {
    'Matricule': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Score de satisfaction': [1, 3, 4, 7, 9, 2, 10, 5, 8, 6]
    }

    df = pd.DataFrame(data)

    # Display the dataset
    st.write("Voici leurs scores de satisfaction :")
    st.write(df)

    st.markdown("")
    

    st.markdown("Maintenant, calculons la variance pour cet ensemble de données étape par étape :")


    st.markdown("")


    st.markdown("Étape 1 : Calculons la Moyenne (**μ**) des scores de satisfaction")

    # Display the Mean
    st.latex(r'\text{Moyenne} = \frac{\sum_{i=1}^{n}X_i}{n} = \frac{1+3+4+7+9+2+10+5+8+6​}{10} = \frac{55​}{10} = 5.5')
    

    
    

# Sample data of Satisfaction Score
    scores_de_satisfaction = [10, 2, 8, 4, 6, 1, 9, 7, 3, 5]

# Sample data of Squared Difference
    squared_difference = [4.5, 3.5, 8, 4, 6, 1, 9, 7, 3, 5]

# Create a DataFrame
    df_without_outliers = pd.DataFrame(scores_de_satisfaction, columns=['Salaires (€)'])

# Display the data table
    st.subheader("Echantillon de données salariales SANS outliers (valeurs aberrantes)")
    st.dataframe(df_without_outliers)

    

    

    
    

    

# Display the steps for calculating the mean
    st.subheader("Étapes pour calculer la variance")
    st.markdown(
    """
    1. Déterminez la **moyenne** des données.
    2. **Soustrayez** la moyenne de chaque point de données pour trouver les différences.
    3. **Mettez au carré** chaque différence pour éliminer les valeurs négatives et souligner les écarts plus importants.
    4. **Calculez** la moyenne des précédents carrés.
    """
)

# Display the calculated mean
    st.write(f"**💡Salaire moyen: {mean_salary:.2f} (en €)**")
    

    st.markdown("")
    
                
    st.markdown("- **Écart type** : L'écart type est une mesure de la dispersion des valeurs des données par rapport à la moyenne de l'ensemble de données. C'est la racine carrée de la variance. Il s'agit de la mesure de variabilité la plus couramment utilisée et fournit une mesure de la dispersion dans les mêmes unités que l'ensemble de données d'origine.")            

if st.button("Continuer vers la suite du Chap.2 - **C/ Techniques graphiques**"):
    
    st.subheader("📈Chap.2-C/ Techniques graphiques📉")
    
    st.markdown("Des techniques graphiques peuvent être utilisées pour améliorer encore la compréhension d'un ensemble de données.") 
    st.markdown("Les représentations visuelles peuvent aider les professionnels RH à identifier facilement des modèles ou des tendances dans les données et à communiquer des informations aux parties prenantes.")
    
    st.markdown("**Certains types courants de graphiques incluent** :") 
    
    st.markdown("- **Histogramme** : c'est un graphique qui montre la distribution de fréquence des données numériques. Les données sont divisées en intervalles ou bacs, et la hauteur de la barre représente la fréquence de chaque intervalle.")
    
    st.markdown("- **Boîte à moustache** : ce graphique montre la distribution de données numériques à l'aide de quartiles. Il affiche le minimum, le maximum, la médiane et les premier et troisième quartiles des données.")
    
    st.markdown("- **Nuages de points** : un graphique qui montre la relation entre deux variables numériques. Chaque point représente une paire de valeurs et le modèle des points peut indiquer la force et la direction de la relation.")
    



        
        
        
        
        
        
