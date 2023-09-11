


import streamlit as st

st.markdown("# Chapitre 2")
st.sidebar.markdown("# Chapitre 2")

st.title("Statistiques descriptives")

st.markdown("Comme nous l'avons précédemment vu, **les statistiques descriptives traitent de la collecte, de l'analyse et de la présentation des données**. Elles vont fournir aux professionnels RH des outils pour décrire et résumer les données d'une manière facile à comprendre.")

if st.button("Cliquez pour acceder au Chap.2 - **A/ Mesures de tendance centrale**"):
    
    st.subheader("📈Chap.2-A/ Mesures de tendance centrale📉")
    
    st.markdown("Les **mesures de tendance centrale** sont utilisées pour définir le centre d'une distribution ou d'un ensemble de données. En statistique, une **distribution** fait référence au modèle de variation dans un ensemble de données numériques. Ce modèle de variation décrit comment les données sont réparties sur une plage de valeurs. On peut visualiser une distribution à l'aide d'un graphique, tel qu'un histogramme ou un diagramme de densité.")
    
    st.markdown("**Il existe trois principales mesures de tendance centrale** :")
    
    st.markdown("- **Moyenne** : il s'agit de la moyenne arithmétique d'un ensemble de valeurs. Elle est calculée en additionnant toutes les valeurs et en divisant par le nombre de valeurs. La moyenne est sensible aux valeurs aberrantes et aux valeurs extrêmes, et peut ne pas être représentative des données s'il existe des valeurs extrêmes.")


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


    st.markdown("**Application**")
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


    st.markdown("**Interpretation de l'histogramme de la distribution des salaires**")


    st.markdown("L'histogramme de répartition des salaires représente la **fréquence des différentes échelles** de salaire au sein de l'ensemble de données.")

    st.markdown("La plupart des salaires se situent dans la fourchette de **55 000 € à 65 000 €**, cette catégorie ayant la fréquence la plus élevée.")

    st.markdown("Il n'y a pas de salaires inférieurs à 55 000 € ou supérieurs à 75 000 dans cet ensemble de données.")

    st.markdown("La répartition est **légèrement asymétrique vers la gauche**, ce qui indique qu'il y a relativement plus d'employés dont le salaire est inférieur au salaire médian (environ 61 000 €).")

    


# Create a density plot
    fig_density = px.density_contour(df, x='Salaire (en milliers €)', title='Graphique de densité salariale')

# Display the density plot
    st.plotly_chart(fig_density)

    st.markdown(
    """
    In this HR context, we've explained the theoretical formula for calculating the mean salary 
    and the steps involved in the calculation. The presence of an outlier can significantly 
    affect the mean, as shown in the histogram and density plot.
    """
)







    





    
    
    st.markdown("- **Médiane** : la valeur médiane est le point milieu d'un ensemble de données numériques. Elle est calculée en organisant les données dans l'ordre croissant, de sorte que la moitié des valeurs soient inférieures ou égales à la médiane et l'autre moitié supérieures ou égales. Ainsi la médiane se trouve être le point milieu. Comparativement à la moyenne, la médiane est moins sensible aux valeurs aberrantes ou extrêmes ; et fournit une meilleure représentation de la⚡**valeur typique**⚡de l'ensemble de données.") 
    
    st.markdown("- **Mode** : c'est la valeur la plus courante dans un ensemble de données. Le mode est calculé en identifiant la valeur qui se produit le plus fréquemment. Il s'agit d'une mesure simple qui peut être utilisée pour résumer et décrire des données, en conjonction avec la moyenne et la médiane pour obtenir une image plus complète des données. ⚠️Cependant, le mode a certaines limites. Par exemple, ce n'est pas un bon indicateur de tendance centrale lorsque les données contiennent des valeurs aberrantes, car ces valeurs peuvent fausser la distribution et rendre le mode moins représentatif de la⚡**valeur typique**⚡dans les données. Dans de tels cas, d'autres mesures de tendance centrale, telles que la moyenne ou la médiane, peuvent être plus appropriées.")

if st.button("Continuer vers la suite du Chap.2 - **B/ Mesures de la variabilité**"):
    
    st.subheader("📈Chap.2-B/ Mesures de la variabilité📉")
    
    st.markdown("Les mesures de variabilité sont utilisées pour décrire la dispersion (propagation) d'une distribution ou d'un ensemble de données.") 
    st.markdown("**Il existe plusieurs mesures principales de la variabilité** :")
    
    st.markdown("- **Plage** : c'est la différence entre les valeurs maximales et minimales dans un ensemble de données. Elle fournit une estimation approximative de la variabilité, mais est sensible aux valeurs aberrantes.")
                
    st.markdown("- **Variance** : il s'agit de la moyenne des différences au carré entre chaque valeur et la moyenne. Elle fournit une mesure plus précise de la variabilité, mais est affecté par des valeurs extrêmes.")    
                
    st.markdown("- **Écart type** : C'est la racine carrée de la variance. Il s'agit de la mesure de variabilité la plus couramment utilisée et fournit une mesure de la dispersion dans les mêmes unités que l'ensemble de données d'origine.")            

if st.button("Continuer vers la suite du Chap.2 - **C/ Techniques graphiques**"):
    
    st.subheader("📈Chap.2-C/ Techniques graphiques📉")
    
    st.markdown("Des techniques graphiques peuvent être utilisées pour améliorer encore la compréhension d'un ensemble de données. Les représentations visuelles peuvent aider les professionnels RH à identifier facilement des modèles ou des tendances dans les données et à communiquer des informations aux parties prenantes.")
    
    st.markdown("**Certains types courants de graphiques incluent** :") 
    
    st.markdown("- **Histogramme** : c'est un graphique qui montre la distribution de fréquence des données numériques. Les données sont divisées en intervalles ou bacs, et la hauteur de la barre représente la fréquence de chaque intervalle.")
    
    st.markdown("- **Boîte à moustache** : ce graphique montre la distribution de données numériques à l'aide de quartiles. Il affiche le minimum, le maximum, la médiane et les premier et troisième quartiles des données.")
    
    st.markdown("- **Nuages de points** : un graphique qui montre la relation entre deux variables numériques. Chaque point représente une paire de valeurs et le modèle des points peut indiquer la force et la direction de la relation.")
    



        
        
        
        
        
        
