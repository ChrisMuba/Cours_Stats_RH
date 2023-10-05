#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

import pandas as pd

st.markdown("# Chapitre 1")
st.sidebar.markdown("# Chapitre 1")

st.title("Introduction aux statistiques")

st.markdown("**Les statistiques** sont une branche des mathématiques qui **traitent de la collecte, de l'analyse, de l'interprétation, de la présentation et de l'organisation des données**. Deux grandes branches des statistiques sont les **statistiques descriptives** et les **statistiques inférentielles**.")

st.markdown("")

if st.button("Cliquez pour acceder au Chap.1 - **A/ Statistiques descriptives vs inférentielles**"):
    st.subheader("📈Chap.1-A/ Statistiques descriptives vs inférentielles📉")
    
    st.markdown("- Les **statistiques descriptives traitent de la collecte, de l'analyse et de la présentation des données**. Elles comprennent le **calcul des mesures de tendance centrale** telles que la **moyenne**, la **médiane** et le **mode**. Ainsi que des **mesures de variabilité** telle que la **gamme** ou **l'écart-type** pour **décrire et résumer les données**.")
    
    st.markdown("- Les **statistiques inférentielles**, quant à elles, **consistent à tirer des inférences ou des conclusions sur une population à partir d'un échantillon de données**. Ils comprennent **l'estimation des paramètres de la population et des tests d'hypothèses pour évaluer la validité des affirmations statistiques**.")
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/GIF_Chap1B.gif')

if st.button("Continuer vers la suite du Chap.1 - **B/ Types de données et sources de données**"):
    
    st.subheader("📈Chap.1-B/ Types de données et sources de données📉")
    
    st.markdown("En GRH les données jouent un rôle crucial dans la prise de décision. Les données peuvent être classées en deux types principaux : **catégorielles** et **numériques**.")

    st.markdown("")
    
    st.markdown("**A/ Les données catégorielles** (ou données qualitatives)")
                
    st.markdown("Les données **catégorielles** sont des données qui peuvent être **triées en catégories ou en groupes**.") 
    
    st.write("Ces catégories sont non numériques et peuvent être **nominales** ou **ordinales** :")

    st.markdown(" - 1/ Les données **catégorielles nominales**")

    st.markdown("Les données catégorielles nominales font référence à des **catégories qui ne peuvent pas être mesurées, comptées, classées ou ordonnées**. Ce type de données sont souvent descriptives et sont utilisées pour présenter des caractéristiques ou des propriétés qui ne peuvent pas être quantifiées.")

    st.markdown("")
### Affichage tableau au format tabulaire    
    
    st.markdown("🚨**Tableau 1** : Exemple de données **catégorielles nominales**")
    
    data_1 = [
        ["Femme", "Leadership", "CDI", "Rupture conventionnelle", "Comptabilité-Finances"],
        ["Homme", "Communication", "CDD", "fin de CDD", "Marketing-Ventes"],
        ["Femme", "Résolution de problèmes", "Contrat de travail temporaire (intérim)", "Fin de mission", "RH"],
        ["Homme", "Créativité", "Contrat d\'apprentissage", "Démission", "Informatique"],
        ["Homme", "Travail d\'équipe", "Contrat de professionnalisation", "Fin de période d’essai", "Administration générale"],
        ["...", "...", "...", "...", "..."]
]

    headers = ["Genre H/F", "Qualités professionnelles", "Type de contrat de travail", "Motif de fin de contrat", "Service"]

    df = pd.DataFrame(data_1, columns=headers)

    st.table(df)
#####
    st.markdown(" - 2/ Les données **catégorielles ordinales**")

    st.markdown("Les données catégorielles ordinales impliquent des **catégories basées sur des caractéristiques qui peuvent traduire une chronologie, un classement, une échelle. ; Souvent elles peuvent être comptées** par des valeurs discrètes.")

    ### Affichage tableau au format tabulaire    
    
    st.markdown("🚨**Tableau 2** : Exemple de données **catégorielles ordinales**")
    
    data = [
        ["18 - 24", "0 à 2 ans", "Employé","BTS / Titre pro"],
        ["25 - 34", "3 à 5 ans", "Agent de maîtrise", "Bachelor"],
        ["35 - 44", "6 à 10 ans", "Cadre", "Master"],
        ["45 - 54", "11 à 15 ans", "Cadre sup.", "Master"],
        ["55 et plus", "plus de 15 ans", "Cadre sup.", "BTS / Titre pro"],
        ["...", "...", "...", "..."]
]

    headers = ["Tranche d'âge des employés","Ancienneté", "Catégorie de l'emploi", "Diplôme"]

    df = pd.DataFrame(data, columns=headers)

    st.table(df)

    
    st.markdown("")
    
    
    st.markdown("⚠️Bien que non numériques les données **catégorielles**, aussi appelées données **qualitatives**, peuvent être **quantifiées** ou décrites à l'aide de méthodes numériques :") 
    
    st.markdown(" 🌶️ calculs de fréquences, pourcentages, tests du khi-deux, pour résumer et analyser ce type de données ;") 
    
    st.markdown(" 🌶️ l'analyse de clustering ou l'analyse factorielle pour identifier des modèles et des relations dans ces données.")  
    
    st.markdown("") 
    
    st.markdown("") 
#####
    st.markdown("**3/ Visualisation des données catégorielles**")
    
    st.markdown("Les données catégorielles sont souvent présentées sous forme de *graphique en barres*📊 ou de *diagramme circulaire*🥧 ( « camembert »). Par exemple si nous reprenons notre **Tableau 1**, nous pouvons tracer un diagramme circulaire à partir de données catégorielles nominales : ici les données de la colonne **Genre H/F**.")


    import streamlit as st
    import plotly.graph_objects as go

    data = ["Femme", "Homme", "Femme", "Homme", "Homme"]
    colors = ['#e377c2', '#1f77b4']

    def plot_pie_chart(data, colors, title):
        gender_counts = {gender: data.count(gender) for gender in set(data)}
        labels = list(gender_counts.keys())
        values = list(gender_counts.values())

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
        fig.update_layout(title=title)
        st.plotly_chart(fig)

    plot_pie_chart(data, colors, "DataViz : Genre H/F - Tableau 1")

    st.markdown("")
    
    st.markdown("") 
       
    st.markdown("")   
    
    st.markdown("") 
#####
    st.markdown("**B/ Les données quantitatives**")
    
    st.markdown("Les données **quantitatives** sont des données qui peuvent être **mesurées** ou **comptées**. Ces données peuvent ensuite être classées en données **discrètes** ou **continues**.") 

    st.markdown("") 
#####
    st.markdown(" - 1/ Les données **quantitatives discrètes**")
    
    st.markdown("Les données **quantitatives discrètes** sont des données qui ne peuvent prendre que des valeurs entières, c'est à dire sans virgule. Les données discrètes sont souvent représentées à l'aide de chiffres entiers ou de nombres entiers.")

    st.markdown("") 

    
    import streamlit as st
    import plotly.express as px
    import pandas as pd

# Sample HR dataset
    data = {
        'Effectif du service': ['Ventes : 12', 'Finance : 5', 'RH : 5', 'IT : 3', 'Marketing : 8', 'Operations : 21'],
        'Nombre d\'évaluations de performances': ['9', '4', '4', '1', '3', '8'],
        'Candidatures reçues': ['6', '3', '3', '2', '4', '11'],
        'Effectifs recrutés': ['2', '1', '1', '0', '1', '4']
}

# Affichage tableau au format tabulaire   
    st.markdown("🚨**Tableau 3** : Exemple de données **quantitatives discrètes**")
    df = pd.DataFrame(data)
    st.write(df)

    
    st.markdown("")
#####
    st.markdown(" - 2/ Les données **quantitatives continues**")
    
    st.markdown("Les données **quantitatives continues**, quant à elles, font référence à sont des données qui peuvent prendre n'importe quelle valeur dans une certaine plage.") 
    st.markdown("Il n'y a pas d'intervalles ni de ruptures entre les valeurs de données continues et il existe un nombre infini de valeurs possibles qui peuvent être prises ; même si par convention on admet seulement un certain nombre de chiffres après la virgule.")

    st.markdown("")
    
### Affichage tableau au format tabulaire    
    
    st.markdown("🚨**Tableau 4** : Exemple de données **quantitatives continues**")    
    
    data_2 = [
        [32, 50.5, 5.5, 7.5],
        [43.5, 72.3, 12.25, 7.25],
        [35.5, 40.1, 7.5, 7.1],
        [41, 65.9, 12, 8.9],
        [39, 58, 6.5, 7.8]
    ]

    headers_2 = ["Âge", "Salaire annuel (k€)", "Ancienneté", "Note de performance"]

    df_2 = pd.DataFrame(data_2, columns=headers_2)
    
# Formater les colonnes pour afficher 2 chiffres après la virgule : "Âge", "Salaire annuel (k€)", "Ancienneté", "Note de performance"
    
    df_2["Âge"] = df_2["Âge"].map(lambda x: "{:.1f}".format(x))
    df_2["Salaire annuel (k€)"] = df_2["Salaire annuel (k€)"].map(lambda x: "{:.1f}".format(x))
    df_2["Ancienneté"] = df_2["Ancienneté"].map(lambda x: "{:.2f}".format(x))
    df_2["Note de performance"] = df_2["Note de performance"].map(lambda x: "{:.2f}".format(x))

    st.table(df_2)

    st.markdown("") 
    
    st.markdown("") 
#####
    st.markdown("**3/ Visualisation des données quantitatives**")
        
    st.markdown("")
    
    st.markdown("Les données **quantitatives** sont souvent présentées sous forme **d'histogrammes**, de **boîtes à moustaches**, de **graphiques linéaires** ou de **nuages de points**. Par exemple si nous reprenons notre **Tableau 4**, nous pouvons tracer un nuages de point avec droite de régression à partir de données quantitatives continues : ici les données des colonnes **Âge** et **Note de performance**.")
   
    
    st.markdown("")     
        
    import streamlit as st
    import plotly.express as px
    import pandas as pd
    import numpy as np

    data_2 = [
        [32, 50.5, 5.5, 7.5],
        [43.5, 72.3, 12.25, 7.25],
        [35.5, 40.1, 7.5, 7.1],
        [41, 65.9, 12, 8.9],
        [39, 58, 6.5, 7.8]
    ]

    headers_2 = ["Âge", "Salaire annuel (k€)", "Ancienneté", "Note de performance"]

    df_2 = pd.DataFrame(data_2, columns=headers_2)

# Scatter plot: Age vs. Performance Rating with correlation line
    
    correlation_coefficient = np.corrcoef(df_2['Âge'], df_2['Note de performance'])[0, 1]
    fig_scatter = px.scatter(df_2, x='Âge', y='Note de performance', title='DataViz : Relation entre l\'âge et la performance au travail - Tableau 4')
    fig_scatter.add_trace(px.scatter(x=df_2['Âge'], y=df_2['Note de performance']).data[0])
    fig_scatter.add_trace(px.line(x=df_2['Âge'], y=np.polyval(np.polyfit(df_2['Âge'], df_2['Note de performance'], 1), df_2['Âge'])).data[0])
    fig_scatter.update_layout(annotations=[dict(x=35, y=3.2, text=f'Correlation: {correlation_coefficient:.2f}', showarrow=False)])
    st.plotly_chart(fig_scatter)

    
    st.markdown("")

    st.markdown("**C/ Les sources des données**")

    st.markdown("")


    st.markdown("Les données peuvent être collectées à partir de diverses sources, telles que :")

    st.markdown("- le système d'information de gestion des ressources humaines (**SIRH**)")
    
    st.markdown("- les **dossiers du personnel** en **version papier** et / **ou digitale** (dématérialisée).")

    st.markdown("")

    # Afficher les images

    from PIL import Image
    col1, col2 = st.columns(2)

    with col1:
       st.markdown("dossiers du personnel")
       image = Image.open('GIF/dossiers_du personnel_giphy.gif')
    # Display a GIF
       st.image('GIF/dossiers_du personnel_giphy.gif')

    with col2:
       st.markdown("quelques SIRH")
       image = Image.open('GIF/photos_sirh.jpg')
       st.image(image)

    
    
    st.markdown("")


    st.markdown("⚠️Le droit du travail ne prévoit aucune information obligatoire à renseigner sur un salarié, en revanche les informations recueillies doivent présenter un lien direct et nécessaire avec l'emploi proposé ou avec l'évaluation des aptitudes professionnelles (**Art. L1221-6 du CT**)")

    
    st.markdown("")


    st.markdown("⚠️Pour certains agents de la fonction publique de l'État, la liste des données à recueillir par les RH est précisée dans l'annexe du **décret n° 2019-612 du 19 juin 2019** portant création d'un traitement automatisé de données à caractère personnel (**RenoiRH**)")

                
    st.markdown("")


    st.markdown("🚨Un **SIRH** est un système logiciel qui gère des données RH. Il peut fournir une **base de données centralisée** pour les informations sur les employés, y compris les informations personnelles, l'historique professionnel, etc...") 

   
    st.markdown("Le SIRH peut également fournir des outils d’analyse des données et de reporting : c'est une excellente source de données catégorielles et numériques.")
    

    st.markdown("")


    st.markdown("Bien que les dossiers des employés constituent une source précieuse de données RH, un SIRH offre plusieurs avantages par rapport aux dossiers traditionnels.") 
    
    st.markdown("Le SIRH fournit une base de données centralisée accessible simultanément à plusieurs utilisateurs, ce qui facilite le partage d'informations entre les utilisateurs autorisés.") 
    
    st.markdown("Le SIRH fournit également des données RH en temps réel, permettant de prendre rapidement des décisions éclairées.") 
    
    st.markdown("Un autre avantage du SIRH est qu’il peut automatiser de nombreux processus RH, ce qui peut permettre de gagner du temps et de réduire les erreurs, améliorant ainsi l'efficacité globale d'un service RH.")

    st.markdown("")

    st.markdown("")


    
if st.button("Continuer vers la suite du Chap.1 - **C/ Rôle des statistiques dans les RH**"):
    
    st.subheader("📈Chap.1-C/ Rôle des statistiques dans les RH📉")
    
    st.markdown("**Le rôle principal des statistiques appliquées aux RH est d'aider professionnels RH à prendre des décisions éclairées, basées sur des données pertinentes**.") 
    
    st.markdown("Pour y arriver ils peuvent : ") 
                
    st.markdown("- **Créer des indicateurs** : concernant par exemple le **suivi des effectifs**, la **pyramide des âges**, la **pyramide des anciennetés**, le **suivi de la masse salariale**, le **suivi du turn-over**, le **suivi de l'absentéisme**, la **qualité du recrutement**, le **climat interne**, etc...") 

    st.markdown("*📌Les possibilités de création d'indicateurs RH sont nombreuses et dépendent des objectifs suivis par l'entreprise et des données à disposition.*")

    st.markdown("")

    st.markdown("- **Créer des tableaux de bord** : après avoir défini les indicateurs RH à suivre et collecté les données appropriées, nous pouvons créer un tableau de bord automatisé qui rassemblera et facilitera le suivi en temps réel de nos indicateurs.")

    st.markdown("📌*Les outils pour créer des tableaux de bords RH sont nombreux : parmi les solutions « presse-bouton » mais peu flexibles certaines bien rodées sont Power BI, Tableau, Qlik ou Looker Studio ; en revanche si on sait écrire du code, les possibilités sont presque sans limites avec Streamlit (framework Python🐍), Flexdashboard (framework R), Shiny (R / Python🐍), etc... .*")


    st.markdown("")


    st.markdown("Ci-dessous un :blue[exemple de **tableau de bord RH**] à 4 onglets :") 
    
    st.markdown("- Suivi de la masse salariale") 
    st.markdown("- Pyramide des âges") 
    st.markdown("- Répartition H/F")
    st.markdown("- Salaire moyen H/F")

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objs as go
    import plotly.express as px
   

# Line Plot
    # Monthly payroll data (in thousands of dollars)
    forecast_months_2023 = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    réalisé_months_2023 = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août']

    forecast_2023 = [1154300, 1200010, 1235205, 1305008, 1778120, 1263150, 1208180, 1240000, 1275002, 1299250, 2356280, 1251300]
    réalisé_2023 = [1152003, 1185350, 1113880, 1205008, 1677420, 1121245, 1148000, 1165000]

# Create a dataframe for plotting
    df = pd.DataFrame({'mois': forecast_months_2023 + réalisé_months_2023,
                       'forecast 2023 (prévision)': forecast_2023 + [None] * len(réalisé_months_2023),
                       'réalisé 2023': [None] * len(forecast_months_2023) + réalisé_2023})

# Create an interactive line plot
    fig_1 = px.line(df, x='mois', y=['forecast 2023 (prévision)', 'réalisé 2023'],
                    labels={'value': 'masse salariale brute (millions €)'},
                    title='suivi de la masse salariale (prévision 2023 vs. réalisé 2023)')

# Customize line colors
    fig_1.update_traces(line_color='red', selector=dict(name='forecast 2023 (prévision)'))
    fig_1.update_traces(line_color='blue', selector=dict(name='réalisé 2023'))

# Display the line plot
  #st.plotly_chart(fig_1)
    

    st.markdown("")


# Age Pyramid
# Define age intervals
    age_intervals = ['[ < 25]', '[25 - 29]', '[30 - 34]', '[35 - 39]', '[40 - 44]', '[45 - 49]', '[50 - 54]', '[55 - 59]', '[60 et +]']

# Corresponding y values for the intervals
    y = list(range(len(age_intervals)))

    women_bins = np.array([-1686, -3868, -3463, -2346, -2074, -3037, -3495, -4194, -228])
    men_bins = np.array([887, 2013, 2323, 1842, 1645, 2270, 3115, 3891, 493])

    layout = go.Layout(
    title='Pyramide des âges en pelote de laine',
    yaxis=go.layout.YAxis(title='Âge', tickvals=y, ticktext=age_intervals),
    xaxis=go.layout.XAxis(
        range=[-5000, 5000],
        tickvals=[-4000, -2000, 0, 2000, 4000],
        ticktext=[4000, 2000, 0, 2000, 4000],
        title='Effectif'
    ),
    barmode='overlay',
    bargap=0.1
)

    data = [
    go.Bar(
        y=y,
        x=men_bins,
        orientation='h',
        name='👦🏿 Homme',
        hoverinfo='x',
        marker=dict(color='#1f77b4')
    ),
    go.Bar(
        y=y,
        x=women_bins,
        orientation='h',
        name='👩‍🦰 Femme',
        text=-1 * women_bins.astype('int'),
        hoverinfo='text',
        marker=dict(color='#e377c2')
    )
]

    fig_2 = go.Figure(data=data, layout=layout)
    
    #st.plotly_chart(fig_2)


    st.markdown("")
    

# Pie Chart
    # Répartition 👦🏿/👩‍🦰

    data = ["femme", "homme", "femme", "homme", "homme"]
    colors = ['#e377c2', '#1f77b4']

    def fig_3(data, colors, title):
        gender_counts = {gender: data.count(gender) for gender in set(data)}
        labels = list(gender_counts.keys())
        values = list(gender_counts.values())

        fig_3 = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
        fig_3.update_layout(title=title)
        return fig_3

    fig_3 = fig_3(data, colors, "Répartition H/F")
    #st.plotly_chart(fig_3)


# Bar Chart
    # Sample dataset
    data = {
    'Employee ID': ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
    'Genre': ['Homme👦🏾', 'Femme👧', 'Homme👦🏾', 'Femme👧', 'Homme👦🏾', 'Homme👦🏾', 'Femme👧', 'Femme👧', 'Homme👦🏾', 'Femme👧'],
    'Salaire €': [55000, 60000, 65000, 58000, 70000, 62000, 56000, 59000, 75000, 61000]
    }

    df = pd.DataFrame(data)

    # Average salary by gender
    #st.markdown('**fig.2: Salaire moyen selon le genre**')
    avg_salary = df.groupby('Genre')['Salaire €'].mean().reset_index()

    fig_4 = px.bar(avg_salary, x='Genre', y='Salaire €', title='Comparaison du salaire moyen entre H/F', color='Genre',
                     color_discrete_map={'Homme👦🏾': '#1f77b4', 'Femme👧': '#e377c2'})
    #st.plotly_chart(fig_4)

    st.markdown("")


    st.markdown("")
    
    
    # Create the tabs
    tabs = st.tabs(["Suivi de la masse salariale", "Pyramide des âges", "Répartition H/F", "Salaire moyen H/F"])

# Tab 1 - Line Chart
    with tabs[0]:
        #st.write("## Line Chart")
        st.plotly_chart(fig_1)

# Tab 2 - Histogram
    with tabs[1]:
        #st.write("## Histogram")
        st.plotly_chart(fig_2)

# Tab 3 - Pie Chart
    with tabs[2]:
        #st.write("## Pie Chart")
        st.plotly_chart(fig_3)

# Tab 4 - Bar Chart
    with tabs[3]:
        #st.write("## Bar Chart")
        st.plotly_chart(fig_4)

    
    st.markdown("")


    st.markdown("")
    

    st.markdown("- **Remplir les obligations légales** : notamment construire le **bilan social**, préparer et mettre à dsposition les **données necessaires à la négociation annuelle obligatoire** (NAO) ; ") 
    
    st.markdown("- Calculer l'**index égalité** H/F ; effectuer la **déclaration annuelle obligatoire d’emploi des travailleurs handicapés** (DOETH), etc...") 
    
    st.markdown("🚀**Tous ces éléments sont basés sur la collecte et l'analyse de données sociales, et requièrent donc une excellente compréhension des concepts et méthodes statistiques**.🚀")


    st.markdown("")
    
    
    st.markdown("Les statistiques appliquées aux RH permettent aussi la **réalisation d'études ponctuelles**, sur des sujets précis, pouvant conduire à la mise en place de diverses actions correctives.")
    

    st.markdown("")


    st.markdown("")


    st.markdown("**🏀Application 1**")

    st.markdown("Nous menons une étude dans laquelle nous souhaitons comparer le nombre de jours d'absence au sein de différents services sur une période donnée ; et ainsi déceler d'éventuels problèmes de climat social au sein de certaines équipes.")
    
    st.markdown("Ci-dessous un échantillon données : ")
    

    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    from statsmodels.stats.multicomp import pairwise_tukeyhsd

     # Sample dataset
    data = pd.read_csv('csv_files/employee_absence_data.csv')

    # Remove leading/trailing spaces from column names
    data.columns = data.columns.str.strip()

    st.markdown("**Tableau de suivi des absences des employés**")

# Display the data
    st.write(data)

    st.markdown("")

    st.markdown("Nous visualisons la répartition des jours d'absence à l'aide de Box Plot, qui montrent des variations d'absence selon les différents services.")

    
    fig = px.box(data, x='Department', y='Days_of_Absence', title='Box Plot : Jours d\'absence par service')
    st.plotly_chart(fig)


    # Explanation
    with st.expander("🔮Interpretation"):
        st.write("""
        **Tableau ANOVA** : La statistique F (F) est d'environ 4.8257 et la p-value (PR(>F)) associée est de 0.011, ce qui est inférieur au seuil typique de significativité de *0.05*.
        **Cela indique qu’il existe une différence statistiquement significative dans les jours d’absence entre au moins certains services**.

        ⚠️ Dans notre cas il faut compléter l'analyse à l'aide d'un **test HSD de Tukey** pour identifier quelles paires de services spécifiques ont des jours d'absence moyens significativement différents,
        ce qui permettra d'orientier de façon efficiente la mise en place d'actions correctives.

        """)

    st.markdown("")

    anova_model = ols('Days_of_Absence ~ Department', data=data).fit()
    anova_table = sm.stats.anova_lm(anova_model, typ=2)

    st.markdown("Nous effectuons un test d'ANOVA unidirectionnel pour vérifier s'il existe des différences significatives dans les jours d'absence entre les départements. Si la valeur p est inférieure à 0.05, on peut conclure qu’au moins un service est significativement différent des autres.")
    
    st.write("Table d\'ANOVA:")
    st.write(anova_table)

    st.markdown("")

    st.markdown("")

    st.markdown("📌 *Les possibilités de sujets d'études statistiques sont très nombreuses en RH et dépendent des problématiques et objectifs propres à chaque entreprises* :")

    st.markdown("1. :blue[**Engagement des employés** :] Mesurer et analyser les niveaux d'engagement des employés peut aider les entreprises à identifier les domaines dans lesquels elles peuvent **améliorer la satisfaction et la productivité des employés**.")

    st.markdown("2. :blue[**Acquisition de talents** :] Aider les entreprises à comprendre leur processus d'embauche et à identifier les domaines dans lesquels il peut être amélioré. Cela peut inclure des études sur l'efficacité des différents canaux de recrutement, le temps qu'il faut pour embaucher pour différents postes, le coût de l'embauche de nouveaux employés, etc...")
                
    st.markdown("3. :blue[**Fidélisation des employés** :] Aider les entreprises à comprendre pourquoi les employés quittent leur emploi et à **identifier des moyens pour réduire le turnover**. Cela peut inclure des études sur les différentes raisons de départ, **le coût du turnover, l'impact du turnover sur les résultats financiers de l'entreprise**, etc...")

    st.markdown("4. :blue[**Rémunération et avantages sociaux** :] S'assurer que les entreprises offrent des packages de rémunération et avantages sociaux compétitifs. Cela peut inclure des études sur les salaires et les avantages sociaux du marché, la satisfaction des employés à l'égard de la rémunération et des avantages sociaux, et **l'impact de la rémunération et des avantages sociaux sur la fidélisation des employés**, etc...")

    st.markdown("5. :blue[**Formation et développement des compétences** :] Aider les entreprises à évaluer l'efficacité de leurs programmes de formation et de développement des compétences. Cela peut inclure des études sur la satisfaction des employés à l'égard des programmes de formation et de développement des compétences, **l'impact de ces programmes sur les performances des employés et le retour sur investissement des programmes de formation et de développement**.")

    st.markdown("6. :blue[**Commentaires et communication des employés** :] Examiner l'efficacité des canaux de rétroaction et de communication au sein de l'entreprise et identifier les opportunités d'amélioration en favorisant un environnement de travail transparent et collaboratif.")

    st.markdown("7. :blue[etc...]")

    st.markdown("")

    st.markdown("Ce ne sont là que quelques exemples d’études RH qui peuvent être menées en entreprise. Les études spécifiques les plus pertinentes dépendront des besoins de l’entreprise.")

    st.markdown("")

    #url = "https://cours-stats-rh.streamlit.app/Quiz_1_-_Introduction_aux_Statistiques📉"
    #st.write("Acceder au quiz du chapitre 1 [ici](%s)" % url)

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
    redirect_button("https://cours-stats-rh.streamlit.app/Quiz_1_-_Introduction_aux_Statistiques📉","Quiz du chapitre 1")


                
    



    
   




    



    



