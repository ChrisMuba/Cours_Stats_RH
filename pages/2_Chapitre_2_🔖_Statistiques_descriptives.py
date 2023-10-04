


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

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
    st.markdown("**Salaires (€) : [55000, 60000, 65000, 58000, 70000, 62000, 56000, 59000, 75000, 60000]**")

    

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

# Explanation
    with st.expander("🔮Interpretation de l'histogramme de la distribution des salaires"):
        st.write("""
        L'histogramme de répartition des salaires représente la **fréquence des différentes échelles** de salaire au sein de l'ensemble de données.
        
        La plupart des salaires se situent dans les fourchettes de **[55 k€ - 59 k€]** et **[60 k€ - 64 k€]**, ces 2 catégories ayant les fréquences les plus élevées.
        
        Dans cet échantillon de données, les salaires minimum et maximum sont respectivement 55 000 € et 75 000 €.
        
        La répartition est **légèrement asymétrique vers la gauche**, ce qui indique qu'il y a relativement plus d'employés dont le salaire est inférieur au salaire médian.
        """)
    

    st.markdown("")


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

# Explanation
    with st.expander("🔮Interpretation du box plot de la distribution des salaires"):
        st.write("""
        Le **box plot** fournit un résumé de la répartition des salaires, y compris des mesures de tendance centrale et de variabilité.
        
        La boite représente l'intervalle interquartile (IQR), les bords inférieur (à gauche) et supérieur (à droite) de la case marquant respectivement le premier quartile (Q1) et le troisième quartile (Q3).
        
        Intervalle interquartile (IQR) : la moitié moyenne des salaires (de Q1 à Q3) se situe entre environ 58 000 € et 65 000 €.
        
        La ligne verticale à l’intérieur de la boite représente le salaire médian (Q2) : environ 60 500 €.
        
        Les « moustaches » s'étendent des bords de la boîte jusqu'aux salaires minimum (55 000 €) et maximum (75 000 €) dans une fourchette raisonnable : **il n'y a pas de valeurs aberrantes dans l'ensemble de données**, car tous les salaires se situent dans la fourchette raisonnable des « moustaches ».
        """)


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

# Explanation
    with st.expander("🔮Interpretation de l'histogramme des salaires sans valeurs aberrantes"):
        st.write("""
        L'histogramme est une distribution de fréquence qui montre le nombre d'observations dans des intervalles spécifiques. Dans notre cas, l'histogramme représente la répartition des salaires sans valeurs aberrantes.
        
        Cet histogramme montre une répartition relativement symétrique centrée autour des valeurs moyennes (entre 45 000 et 55 000 €), avec un pic autour de 50 000 €. Les données semblent être distribuées assez normalement, sans outliers significatifs.
    
        Il apparaît quelques observations en dessous de 45 000 et au-dessus de 60 000 €. Cela suggère que la majorité des employés ont des salaires similaires, et que seuls quelques-uns ont des salaires nettement inférieurs ou supérieurs.
        """)
        
    
    st.markdown("")


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
    with st.expander("🔮Interpretation de l'histogramme des salaires avec valeurs aberrantes"):
        st.write("""
    Dans cet exemple, nous avons un échantillon de données salariales qui inclut des valeurs aberrantes.  
    
    Il s'agit des valeurs extrêmes qui peuvent **fausser la distribution**. Lorsque des valeurs aberrantes sont présentes, le mode peut **ne pas représenter avec précision la tendance centrale**
    car il est fortement influencé par les valeurs aberrantes. 
    
    Dans de tels cas, d’autres mesures comme la moyenne ou la médiane peuvent permettre de mieux comprendre le niveau de salaire typique.
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

# Explanation
    with st.expander("🔮Interpretation du box plot de la distribution des salaires avec valeurs aberrantes"):
        st.write("""
    Le **box plot** nous confirme visuellement la présence de valeurs aberrantes dans les données, avec des salaires allant de 35 000 € à 120 000 €.  
    
    La ligne verticale à l’intérieur de la boite nous montre que le salaire médian est de 50 000 €, et les moustaches nous montrent l'écart des salaires dans une plage de 1,5 fois l'écart interquartile (IQR). 
    
    Les valeurs aberrantes, représentées par les deux points individuels en dehors des moustaches, sont les salaires de 100 000 € et 120 000 €.
    
    La présence de valeurs aberrantes dans les données suggère que certains employés ont des salaires nettement supérieurs à ceux de la majorité des employés.
    """)
        
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/GIF_Chap1B.gif')

if st.button("Continuer vers la suite du Chap.2 - **B/ Mesures de la variabilité**"):
    
    st.subheader("📈Chap.2-B/ Mesures de la variabilité📉")
    
    st.markdown("Les mesures de variabilité sont utilisées pour décrire la dispersion (propagation) des points de données dans un ensemble de données.") 
    st.markdown("**Il existe plusieurs mesures principales de la variabilité** :")
    
    st.markdown("- **Plage** : La plage (gamme, étendue) est la mesure de variabilité la plus simple, elle représente la différence entre les valeurs maximales et minimales dans un ensemble de données. Elle fournit une estimation approximative de la variabilité, mais est sensible aux valeurs aberrantes.")

    st.markdown("**Mathématiquement, on peut l'exprimer comme suit :**")

    st.subheader("Plage = Valeur maximale - Valeur minimale")


    st.markdown("")
    

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

# Explanation
    with st.expander("🔮Interpretation du box plot de lâge des employés de l'entreprise"):
        st.write("""
    Ce **box plot** affiche la répartition des âges dans l'échantillon de données, l'axe horizontal représentant les différentes tranches d'âge.

    L'intervalle interquartile **IQR** (représenté par la boite) nous montre que la majorité des employés (50 %) ont entre 30 et 55 ans.")
    
    L’âge médian, (représenté par la ligne verticale dans la boite) est de 42.5 ans, ce qui signifie que la moitié des employés de l'échantillon de données a plus de 42.5 ans et l'autre moitié moins : il s'agit d'une information utile à connaître, car elle peut aider à éclairer les politiques et les pratiques liées au développement et à la rétention des employés.

    Ce **box plot** montre également les quartiles inférieur (Q1 = 30 ans) et supérieur (Q3 = 55 ans), qui sont représentés respectivement par les côtés gauche et droit de la boîte. Les valeurs de **Q1 et Q3** signifient respectivement que 25 % des employés ont moins de 30 ans et 25 % plus de 55 ans.
    """)


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
    'Employé': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Score de satisfaction': [1, 3, 4, 7, 9, 2, 10, 5, 8, 6]
    }

    df = pd.DataFrame(data)

    # Display the dataset
    st.write("Voici leurs scores de satisfaction :")
    st.write(df)

    st.markdown("")
    

    st.markdown("Maintenant, calculons la variance pour cet ensemble de données étape par étape :")


    st.markdown("")


    st.markdown("Étape 1 : **Calculons la Moyenne (**μ**) des scores de satisfaction**")

    # Display the Mean
    st.latex(r'\text{Moyenne (μ)} = \frac{\sum_{i=1}^{n}X_i}{n} = \frac{1+3+4+7+9+2+10+5+8+6​}{10} = \frac{55​}{10} = 5.5')


    st.markdown("")

    

    st.markdown("Étape 2 : **Calculons les carrés des différences entre chaque point de données (Xᵢ) et la moyenne (μ) :**")


    st.write("""
    - Pour l'employé 1 : (1 − 5.5)² = 20.25")  
    - Pour l'employé 2 : (3 − 5.5)² = 6.25 
    - Pour l'employé 3 : (4 − 5.5)² = 2.25
    - Pour l'employé 4 : (7 − 5.5)² = 2.25
    - Pour l'employé 5 : (9 − 5.5)² = 12.25  
    - Pour l'employé 6 : (2 − 5.5)² = 12.25 
    - Pour l'employé 7 : (10 − 5.5)² = 20.25
    - Pour l'employé 8 : (5 − 5.5)² = 0.25
    - Pour l'employé 9 : (8 −5 .5)² = 6.25
    - Pour l'employé 10 : ( 6− 5.5)² = 0.25
    """)
    

    st.markdown("")

    
    st.markdown("Étape 3 : **Additionnons tous les carrés des différences**")
    
    # Display
    st.latex(r'{\sum_{i=1}^{n}(X_i - \mu)^2} = {20.25+6.25+2.25+2.25+12.25+12.25+20.25+0.25+6.25+0.25} = {82.25}')


    st.markdown("")


    st.markdown("Étape 4 : **Calculons la variance (σ²)**")
    
    # Display
    st.latex(r'Variance (\sigma^2) = \frac{\sum_{i=1}^{n}(X_i - \mu)^2}{N} = \frac{82.25​}{10} = 8.225')
    
# Explanation
    with st.expander("🔮Interpretation de la variance"):
        st.write("""
    En statistiques, il n'existe pas de valeurs seuil fixes et universellement applicables pour déterminer ce qui constitue une variance faible ou élevée, car cela dépend du contexte des données et des objectifs spécifiques. 
    
    **Cependant, il existe quelques lignes directrices et approches générales que nous pouvons utiliser pour prendre cette décision :** 
    
    1. Comparez la valeur de la variance aux variances d'ensembles de données RH similaires des années antérieures, ou au sein d'organisation ou de services similaires.
    
    2. Utiliser des tests statistiques pour déterminer si la variance est statistiquement significative. Par exemple, on peut effectuer un test d'hypothèse pour comparer la variance de notre ensemble de données à une valeur hypothétique ou à la variance d'un autre ensemble de données.
    
    3. Visualisez les données à l'aide d'un histogramme, d'un box plot ou d'autres méthodes graphiques : un ensemble de données avec une variance élevée affichera généralement une plus grande répartition des points de données, tandis qu'un ensemble de données à faible variance aura des points de données regroupés plus près les uns des autres.
""")
    

    st.markdown("")
    

    st.markdown("")

    
    st.markdown("- **Écart type** : L'écart type est une mesure de la dispersion des valeurs des données par rapport à la moyenne de l'ensemble de données. **C'est la racine carrée de la variance**. Il s'agit de la mesure de variabilité la plus couramment utilisée et fournit une mesure de la dispersion dans les mêmes unités que l'ensemble de données d'origine.")

    st.markdown("**Mathématiquement, on peut l'exprimer comme suit :**")

    st.subheader("Écart type (σ) = √Variance")


    st.markdown("")


    st.markdown("**🏀Application 7**")
    st.markdown("Supposons qu'une entreprise souhaite analyser les scores d'évaluation de performance de ses employés.")
    

    import streamlit as st
    import pandas as pd
    import plotly.express as px

# Create a high variance dataset
    data = {
    'Equipe A': [80, 85, 90, 95, 100],
    'Equipe B': [60, 70, 90, 110, 120]
    }

    df = pd.DataFrame(data)

    # Display the dataset
    st.markdown("Les scores de performance de deux équipes, l’équipe A et l’équipe B, sont les suivants :")
    st.write(df)
    

    st.markdown("")
    

    st.write("""Tout d’abord, nous calculons la **plage** pour les deux équipes : 
    
    Équipe A : Plage = 100 - 80 = 20

    Équipe B : Plage = 120 - 60 = 60
    
    💡La plage indique qu’il existe une plus grande répartition des scores 
    d'évaluation de performance pour l’équipe B par rapport à l’équipe A.
""")

    
    st.markdown("")


    st.markdown("")
    

    st.write("""Calculons la **moyenne** pour les deux équipes : 
    
    Équipe A : Moyenne = (80 + 85 + 90 + 95 + 100) / 5 = 450 / 5 = 90

    Équipe B : Moyenne = (60 + 70 + 90 + 110 + 120) / 5 = 450 / 5 = 90
    
""")

    
    st.markdown("")
    

    st.write("""Puis, nous calculons la **variance** pour les deux équipes : 
    
    Équipe A :

    Variance = [(80 - 90)² + (85 - 90)² + (90 - 90)² + (95 - 90)² + (100 - 90)²] / 5
    Variance = [100 + 25 + 0 + 25 + 100] / 5
    Variance = 250 / 5
    Variance = 50

    Équipe B :

    Variance = [(60 - 90)² + (70 - 90)² + (90 - 90)² + (110 - 90)² + (120 - 90)²] / 5
    Variance = [900 + 400 + 0 + 400 + 900] / 5
    Variance = 2600 / 5
    Variance = 520
    
""")


    st.markdown("")
    

    st.write("""Enfin, nous calculons **l’écart type** pour les deux équipes : 
    
    Équipe A : Écart type ≈ √50 ≈ 7,07

    Équipe B : Écart type ≈ √520 ≈ 22.80
    
""")


    st.markdown("")


# Explanation
    with st.expander("🔮Interpretation des résultats"):
        st.write("""
   La variance et l'écart type montrent que les scores d'évaluation de performance de l'équipe B sont plus dispersés que ceux de l'équipe A.

   Ces informations peuvent aider à identifier des problèmes potentiels au sein de l'équipe B et à mettre en œuvre des actions correctives ciblées pour améliorer les performances de certains employés.
   """)


    st.markdown("")


if st.button("Continuer vers la suite du Chap.2 - **C/ Techniques graphiques**"):
    
    st.subheader("📈Chap.2-C/ Techniques graphiques📉")
    
    st.markdown("Les techniques graphiques sont un moyen puissant de visualiser les données et de les rendre plus faciles à comprendre.") 
    st.markdown("Elles peuvent être utilisées pour communiquer aux parties prenantes des informations complexes de manière claire et concise ; et pour identifier des modèles et des tendances qui peuvent ne pas ressortir des données brutes.")
    st.markdown("Les techniques graphiques à utiliser vont dépendre du type de données : **qualitative** ou **quantitative**.") 


    st.markdown("")


    st.subheader("Données qualitatives")

     
    st.markdown("Les types de graphiques courants pour analyser des data RH **qualitatives** incluent :") 
    

    st.markdown("")
    
    
    st.markdown("- **Diagramme circulaire** : Un diagramme circulaire (Camembert) est un graphique qui représente des **données catégorielles** sous forme de tranches du diagramme. Chaque tranche représente une catégorie et la taille de la tranche est proportionnelle au pourcentage du total.")

    st.markdown("**Cas d’usage** des diagrammes circulaires : Ils peuvent être utilisés pour afficher la répartition des employés entre différents services d'une entreprise, fonctions professionnelles, catégories démographiques, etc...")


    st.markdown("")
    

    st.markdown("**🏀Application 8**")
    st.markdown("Une équipe RH souhaite analyser la répartition des employés dans chaque service. Les données sont présentées dans le diagramme circulaire suivant :")


    import pandas as pd
    
# sample dataset:
    data = {
    'Service': ['Marketing', 'Finance', 'IT', 'RH'],
    'Nombre d\'employés': [100, 75, 50, 25]
    }

    df = pd.DataFrame(data)

    import streamlit as st
    import plotly.express as px

# Load the HR data
    data = {
    'Service': ['Marketing', 'Finance', 'IT', 'RH'],
    'Nombre d\'employés': [100, 75, 50, 25]
    }

    df = pd.DataFrame(data)

# Create a Pie Chart using Plotly
    fig = px.pie(df, values='Nombre d\'employés', names='Service', title='Répartition des employés par service')
    st.plotly_chart(fig)

    # Explanation
    with st.expander("🔮Interpretation du diagramme circulaire"):
        st.write("""
    Le diagramme circulaire montre la répartition des employés dans les différents services de l'entreprise. Chaque tranche du diagramme circulaire correspond à un service, tel que Marketing, Finance, IT & RH.
    
    La taille de chaque tranche du diagramme est proportionnelle au pourcentage du nombre total d'employés de ce service par rapport à l'ensemble des salariés de tous les services.
    
    On observe enfin que le service Marketing compte la plus grande proportion d'employés (40 %), suivi du service Finance (30 %), du service IT (20 %) et enfin du service RH (10 %).
    """)


    st.markdown("")


    st.markdown("")


    st.markdown("- **Graphique à barres** : Un graphique à barres est un graphique vertical ou horizontal qui affiche des **données catégorielles**. Des barres sont utilisées pour montrer la fréquence ou l’ampleur de chaque catégorie.")

    st.markdown("**Cas d’usage** des graphiques à barres : Ils peuvent être utilisés pour comparer diverses mesures entre différents services, groupes d'employés ou périodes. Notamment taux d'absentéisme / turnover par services, échelles salariales, notes d'évaluations de performances, participation à la formation. etc...")

    st.markdown("")
    

    st.markdown("**🏀Application 9**")
    st.markdown("Supposons qu'un contrôleur de gestion sociale souhaite analyser les taux d'absentéisme du personnel dans différents services au cours de l'année écoulée. Un graphique à barres peut afficher le taux d'absentéisme (axe des y) pour chaque service (axe des x) afin d'identifier les tendances et les problèmes potentiels.")


    import streamlit as st
    import plotly.express as px

# Load the HR data with colors for each department
    data = {
    'Service': ['RH', 'Finance', 'IT', 'Marketing', 'Ventes'],
    'Taux Absentéisme (%)': [8.5, 5.2, 6.8, 9.3, 7.0],
    }

    df = pd.DataFrame(data)

# Define a color map with department names as keys and colors as values
    color_map = {
    'HR': '#1f77b4',
    'Finance': '#ff7f0e',
    'IT': '#2ca02c',
    'Marketing': '#d62728',
    'Ventes': '#9467bd'
    }

# Create a Bar Graph using Plotly with assigned colors and department names as legend
    fig = px.bar(df, x='Service', y='Taux Absentéisme (%)', title='Taux d\'absentéisme par service',
             color='Service', color_discrete_map=color_map)
    st.plotly_chart(fig)
    
# Explanation
    with st.expander("🔮Interpretation du graphique à barres"):
        st.write("""
    Le graphique à barres représente les taux d'absentéisme dans différents services d'une entreprise au cours de l'année écoulée. Chaque barre du graphique correspond à un service, tel que RH, Finance, IT, Marketing et Ventes.
    
    La hauteur de chaque barre représente le taux d'absentéisme de ce service : nous pouvons voir que le service Marketing a le taux d'absentéisme le plus élevé (9.3 %), suivi par le service RH (8.5), Ventes (7 %), IT (6.8 %) et enfin Finance (5.2 %).
    """)


    st.markdown("")


    st.markdown("")


    st.subheader("Données quantitatives")


    st.markdown("Les types de graphiques courants pour analyser des data RH **quantitatives** incluent :") 


    st.markdown("- **Histogrammes** : Un histogramme est une représentation graphique de la distribution d'un ensemble de **données quantitatives**, où les données sont divisées en un ensemble d'intervalles et le nombre de points de données appartenant à un intervalle est représenté par la hauteur d'une barre.")

    st.markdown("**Cas d’usage** des histogrammes : Ils peuvent être utilisés pour comprendre la distribution d'une seule variable, telle que les salaires des employés, les années d'expérience, etc...")


    st.markdown("")
    

    st.markdown("**🏀Application 10**")
    st.markdown("Imaginez que vous êtes un responsable RH chargé de comprendre la répartition des salaires au sein de votre entreprise. La plupart des employés gagnent-ils des salaires similaires ou disposez-vous d’un large éventail d’échelles salariales ?") 
    st.markdown("Un histogramme peut vous aider à répondre à ces questions et à obtenir des informations précieuses en fournissant une image claire des échelles et fourchettes salariales les plus courantes parmi vos employés.")


    import streamlit as st
    import numpy as np
    import plotly.express as px

# Generate random salary data for 100 employees (in thousands of dollars)
    np.random.seed(42)
    salaries = np.random.normal(50, 10, 100)

# Create a Plotly histogram figure with a custom legend label and no legend title
    fig = px.histogram(salaries, nbins=20, title='Répartition des salaires dans notre entreprise')
    fig.update_xaxes(title_text='Salaire (en milliers d\'€)')
    fig.update_yaxes(title_text='Nombre d\'employés')

# Remove the legend title
    fig.update_layout(legend_title_text='Salaire (€)')

# Displaying Chart
    st.plotly_chart(fig)

    # Explanation
    with st.expander("🔮Interpretation de l'histogramme"):
        st.write("""
    Cet histogramme est une représentation graphique de la répartition des salaires entre les salariés de notre entreprise. Chaque barre de l'histogramme correspond à une fourchette salariale spécifique (en milliers d'€), et la hauteur de chaque barre indique le nombre d'employés dans cette fourchette salariale.
    
    Échelles salariales courantes : les barres les plus hautes de l'histogramme se situent dans les échelles salariales [45 k€ - 49,99 k€] et [50 k€ - 54,99 k€]. Cela suggère que ces échelles salariales sont les plus courantes parmi nos employés, avec respectivement 23 et 22 employés.
    
    Répartition des salaires : l'histogramme montre que les salaires sont répartis sur une plage de valeurs relativement uniforme sans écarts ni regroupements significatifs.
    
    Asymétrie : l'histogramme semble être légèrement incliné vers la droite. Cela signifie qu'il y a relativement moins d'employés dans les échelles salariales inférieures ([20 k€ - 24,99 k€] à [40 k€ - 44,99 k€]) et plus d'employés dans les échelles salariales moyennes à supérieures ([45 k€ - 49,99 k€] à [65 k€ - 69.99 k€].
    """)

    st.markdown("")


    st.markdown("")


    st.markdown("- **Boîtes à moustaches** : Une boîte à moustache est un diagramme utilisé pour visualiser la répartition et l'asymétrie des **données quantitatives**. Elles sont particulièrement utiles pour détecter les valeurs aberrantes.")

    st.markdown("**Cas d’usage** des boîtes à moustaches : Elles peuvent être utilisés pour comparer différentes distributions d'une même **variable quantitative** (salaires, ancienneté, etc...)")

    st.markdown("")
    

    st.markdown("**🏀Application 11**")
    st.markdown("Disons que nous analysons les salaires des employés. Nous voulons voir comment les salaires sont répartis entre les différents services l'entreprise.")
    st.markdown("Nous pouvons créer un box plot pour visualiser la répartition des salaires pour chaque service. Le box plot nous montrera le salaire médian, l’écart interquartile et toutes les valeurs aberrantes.")


    import pandas as pd
    import numpy as np

# Create sample data
    np.random.seed(42)

# Simulate salaries for three departments: HR, Sales, and IT
    hr_salaries = np.random.normal(50000, 10000, 50)
    sales_salaries = np.random.normal(60000, 15000, 60)
    it_salaries = np.random.normal(65000, 12000, 45)

# Combine data into a DataFrame
    data = pd.DataFrame({
    'Service': ['RH'] * 50 + ['Ventes'] * 60 + ['IT'] * 45,
    'Salaire': np.concatenate([hr_salaries, sales_salaries, it_salaries])
    })

    import streamlit as st
    import plotly.express as px

# Create an interactive box plot using Plotly Express
    fig = px.box(data, x='Service', y='Salaire', title='Répartition des salaires au sein des services RH, Ventes & IT')
    fig.update_xaxes(title_text='Service')
    fig.update_yaxes(title_text='Salaire (k€)')

# Show the plot in Streamlit
    st.plotly_chart(fig)

    # Explanation
    with st.expander("🔮Interpretation des 3 box plot"):
        st.write("""
    La boîte représente l'écart interquartile (IQR) des salaires au sein de chaque service. Les bords inférieur (q1) et supérieur (q3) de la boîte correspondent respectivement aux 25e et 75e centiles. Cela nous indique où se situent 50% des salaires au sein de chaque service.
    
    La ligne à l'intérieur de la boîte représente le salaire médian pour chaque service. C'est la valeur salariale qui sépare les 50 % inférieurs des 50 % supérieurs.
    
    Les moustaches s'étendent de la boîte jusqu'aux valeurs minimales et maximales dans une plage de 1,5 fois l'IQR. Tous les points de données au-delà des moustaches sont considérés comme des valeurs aberrantes et sont affichés sous forme de points individuels.
    
    Comparaison des salaires : nous pouvons facilement comparer les répartitions salariales entre les 3 services RH, Ventes & IT. Par exemple, l'IT a le salaire médian le plus élevé (66.19 k€), suivi des Ventes (59.77 k€) et des RH (47.66 k€).
    
    Variabilité : La longueur de la boîte et des moustaches peuvent nous donner une idée de la variabilité salariale au sein de chaque service : une boîte ou des moustaches plus longues indiquent une plus grande variabilité.
    
    Valeurs aberrantes : le box plot du services Ventes nous aide à identifier des salaires individuels qui se situent bien en dehors de l'échelle salariale typique. Ils sont repésentés par 3 points individuels (20.70 k€, 30.19 k€ et 88.29 k€).
    """)


    st.markdown("")


    st.markdown("")


    st.markdown("- **Graphique linéaire** : Un graphique linéaire est un graphique qui affiche des **données quantitatives** au fil du temps. Il utilise des points connectés pour afficher les tendances et les modèles dans les données.")

    st.markdown("**Cas d’usage** des graphiques linéaires : Ils peuvent être utilisés pour suivre l'évolution des effectifs et de la masse salariale au fil du temps, pour visualiser l'absentéisme sur plusieurs mois, pour suivre les mesures de performance au fil du temps, etc...")


    st.markdown("")
    

    st.markdown("**🏀Application 12**")
    st.markdown("Supposons que nous disposions de données sur le total des salaires mensuels payés par l'entreprise au cours des trois dernières années (2020, 2021 et 2022). Nous pouvons utiliser un graphique linéaire comme outil de visualisation permettant de suivre l’évolution des salaires mensuels sur plusieurs années.") 
    st.markdown("Cette visualisation va nous permettre d'identifier les tendances, la saisonnalité et les valeurs aberrantes potentielles, permettant ainsi de prendre des décisions liées à la planification et à la budgétisation de la rémunération, fondées sur des données.") 
   

    import pandas as pd

# Create sample data for three years (in thousands of euros)
    data = pd.DataFrame({
    'Année': [2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020,
             2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021,
             2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022],
    'Mois': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre',
              'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre',
              'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
    'Salaire_Total': [120, 125, 122, 128, 162.5, 135, 138, 140, 145, 150, 152, 193.75,
                     160, 162, 165, 170, 215, 175, 178, 180, 182, 185, 190, 240,
                     195, 200, 202, 205, 260, 210, 212, 215, 220, 225, 230, 290]
    })

    import streamlit as st
    import plotly.express as px

# Create an interactive line chart using Plotly Express
    fig = px.line(data, x='Mois', y='Salaire_Total', color='Année', title='Suivi de la masse salariale sur 3 ans')
    fig.update_xaxes(title_text='Mois')
    fig.update_yaxes(title_text='Salaires totaux (en k€)')

# Show the plot in Streamlit
    st.plotly_chart(fig)

    # Explanation
    with st.expander("🔮Interpretation du graphique linéaire"):
        st.write("""
    Axe des x (Mois) : L'axe des X représente les mois de l'année, fournissant une dimension temporelle pour nos données.
    
    Axe des y (salaire total) : L'axe des y représente le total des salaires payés par l'entreprise en milliers d'euros pour chaque mois.
    
    Lignes par année : le graphique linéaire montre trois lignes, chacune d'une couleur différente, représentant les années 2020, 2021 et 2022. Ces lignes relient les points de données pour chaque mois, nous permettant d'observer les tendances au fil du temps.
    
    Tendances au fil du temps : nous pouvons voir comment les salaires mensuels totaux ont augmenté au cours des trois années. Ce qui peut être lié aux effectifs, à la structure de la masse salariale (effectifs par catégories de salariés), à l’ancienneté, à la législation, etc...
    
    Modèles saisonniers : On observons une saisonnalité car les salaires ont tendance à être bien plus élevés aux mois de mai et décembre, ce qui peut corrrespondre aux versements de primes (vacances, fin d'année, etc...)
    """)


    st.markdown("")


    st.markdown("")
    
    
    st.subheader("Données qualitatives et quantitatives")

    
    st.markdown("")


    st.markdown("")


    st.markdown("- **Nuage de points** : Un nuage de points est un type de visualisation de données qui montre la relation entre deux variables en plaçant des points de données sur les axes X et Y.")

    st.markdown("**Cas d’usage** des nuages de points : Ils peuvent être utilisés pour analyser la relation entre la satisfaction au travail et l'absentéisme, le niveau d'expérience et le salaire, les scores de performance des employés et les heures de formation suivies, etc...")


    st.markdown("")
    

    st.markdown("**🏀Application 13**")
    st.markdown("Nous souhaitons analyser la relation entre les scores de performance des collaborateurs et les heures de formation suivies. Nous pouvons utiliser un nuage de points avec droite ajustée et coefficient R².")


    import pandas as pd
    import numpy as np

# Create sample data for employee performance and training hours
    np.random.seed(42)

    employee_data = pd.DataFrame({
    'Score_de_Performance': np.random.randint(0, 100, 100),
    'Heures_de_formation_suivies': np.random.randint(0, 50, 100)
    })

    import streamlit as st
    import plotly.express as px

# Create an interactive scatter plot using Plotly Express
    fig = px.scatter(
    employee_data, x='Heures_de_formation_suivies', y='Score_de_Performance',
    title='Scatter Plot des Scores de performance vs. Heures de formation',
    trendline='ols'  # Add a linear regression line
    )
    fig.update_xaxes(title_text='Heures_de_formation_suivies')
    fig.update_yaxes(title_text='Score_de_Performance')

# Show the plot in Streamlit
    st.plotly_chart(fig)

    # Explanation
    with st.expander("🔮Interpretation du nuage de points"):
        st.write("""
    Axe des x : L'axe des x représente le nombre d'heures de formation suivies par chaque employé.
    
    Axe des y : L'axe des y représente les scores de performance des employés.
    
    Points de dispersion : chaque point de données sur le tracé représente un employé. La position du point indique leurs heures de formation et leur score de performance.
    
    Droite de régression linéaire : c'est la ligne la mieux adaptée qui décrit la relation entre les heures de formation et les scores de performance. Elle peut nous aider à identifier les tendances dans les données.
    
    Coefficient R² : Il quantifie dans quelle mesure la ligne de régression linéaire s'adapte aux données. Il mesure la force de la relation entre les deux variables.
    
    R² va de 0 à 1, où :

    1. R² = 0 : Le modèle n'explique aucune variabilité de la variable dépendante

    2. R² = 1 : Le modèle explique parfaitement la variabilité de la variable dépendante
 
    Dans notre cas, la valeur R² est de 0,018599, ce qui est assez faible. Cela suggère que seule une petite fraction (environ 1,86 %) de la variabilité des scores de performance peut être expliquée par le nombre d’heures de formation suivies.
    
    En d’autres termes, la relation linéaire entre les heures de formation et les scores de performance est faible. Cela indique que d'autres facteurs non inclus dans cette analyse peuvent avoir un impact plus important sur les scores de performance.
    """)
    

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
    redirect_button("https://cours-stats-rh.streamlit.app/Heatmap_en_bonus", "Suite : Heatmap")
    



        
        
        
        
        
        
