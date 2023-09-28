#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

import pandas as pd

st.markdown("# Chapitre 1")
st.sidebar.markdown("# Chapitre 1")

st.title("Introduction aux statistiques")

st.markdown("**Les statistiques** sont une branche des mathématiques qui **traitent de la collecte, de l'analyse, de l'interprétation, de la présentation et de l'organisation des données**. Deux grandes branches des statistiques sont les **statistiques descriptives** et les **statistiques inférentielles**.")

if st.button("Cliquez pour acceder au Chap.1 - **A/ Statistiques descriptives vs inférentielles**"):
    st.subheader("📈Chap.1-A/ Statistiques descriptives vs inférentielles📉")
    
    st.markdown("- Les **statistiques descriptives traitent de la collecte, de l'analyse et de la présentation des données**. Elles comprennent le **calcul des mesures de tendance centrale** telles que la **moyenne**, la **médiane** et le **mode**. Ainsi que des **mesures de variabilité** telle que la **gamme** ou **l'écart-type** pour **décrire et résumer les données**.")
    
    st.markdown("- Les **statistiques inférentielles**, quant à elles, **consistent à tirer des inférences ou des conclusions sur une population à partir d'un échantillon de données**. Ils comprennent **l'estimation des paramètres de la population et des tests d'hypothèses pour évaluer la validité des affirmations statistiques**.")

if st.button("Continuer vers la suite du Chap.1 - **B/ Types de données et sources de données**"):
    
    st.subheader("📈Chap.1-B/ Types de données et sources de données📉")
    
    st.markdown("En GRH les données jouent un rôle crucial dans la prise de décision. Les données peuvent être classées en deux types principaux : **catégorielles** et **numériques**.")
    
    st.markdown("**a/ Les données catégorielles**")
                
    st.markdown("Les données **catégorielles** sont des données qui peuvent être **triées en catégories ou en groupes**.") 
    
    st.write("Ces catégories sont non numériques et peuvent être **qualitatives** ou **quantitatives** :")

    st.markdown(" - a1/ Les données **catégorielles qualitatives**")

    st.markdown("Les données catégorielles qualitatives font référence à des **catégories qui ne peuvent pas être mesurées ou comptées**. Ce type de données sont souvent descriptives et sont utilisées pour présenter des caractéristiques ou des propriétés qui ne peuvent pas être quantifiées.")

### Affichage tableau au format tabulaire    
    
    st.markdown("🚨Exemple de données **catégorielles qualitatives** dans un service RH :")
    
    data = [
        ["001", "👧🏾 F", "Leadership","CDI", "Bachelor"],
        ["002", "👦🏿 H", "Communication", "CDD", "Master"],
        ["003", "👧 F", "Résolution de problèmes", "Contrat de travail temporaire (intérim)", "BTS / Titre pro"],
        ["004", "👨‍🦰 H", "Créativité", "Contrat d\'apprentissage", "Master"],
        ["005", "👴 H", "Travail d\'équipe", "Contrat de professionnalisation", "Master"],
        ["...", "...", "...", "...", "..."]
]

    headers = ["Matricule RH","Genre H/F", "Qualités professionnelles", "Le type de contrat de travail", "Diplôme"]

    df = pd.DataFrame(data, columns=headers)

    st.table(df)

    st.markdown(" - a2/ Les données **catégorielles quantitatives**")

    
    st.markdown("")
    
    

    st.markdown("⚠️Des données **catégorielles** peuvent être **quantitatives** car elles peuvent être quantifiées ou décrites à l'aide de méthodes numériques : calculs de fréquences, pourcentages, tests du khi-deux, pour résumer et analyser les données ; l'analyse de clustering ou l'analyse factorielle pour identifier des modèles et des relations dans les données catégorielles.")  
    
    st.markdown("Des exemples de données catégorielles en Ressources Humaines incluent par exemple **le genre** : 👦🏾/👧 ; le **titre du poste**: **contrôleur de gestion sociale**, **responsable formation**, etc... ; le **rattachement du poste** : **administration des RH**, **développement des RH**, etc...") 
    
    st.markdown("Les données catégorielles peuvent ensuite être divisées en données **nominales** et **ordinales**. Les données nominales sont des **données qui ne peuvent pas être classées ou ordonnées**, telles que **le genre** : 👦🏾/👧 ou le **titre du poste**.") 
    
    st.markdown("Les données **ordinales**, en revanche, sont des **données qui peuvent être classées ou ordonnées**, telles que le niveau d'emploi (ex : cadre sup, cadre, agent de maîtrise, etc...) ou le niveau d'éducation (ex: Master, Licence/Bachelor, DUT/BTS, etc...)")
    
    st.markdown(" Les données **catégorielles** sont souvent présentées sous forme de **tableaux de fréquence** ou de **diagrammes à barres**. Par exemple, un tableau de fréquence peut montrer le nombre d'employés dans chaque service, tandis qu'un graphique à barres peut montrer la répartition des sexes dans l'organisation.)")
    
    st.markdown("") 

### Affichage tableau au format tabulaire    
    
    st.markdown("🚨Exemple de données **catégorielles** dans un service RH :")
    
    data = [
        ["001", "👧🏾 F", "Chargée de recrutement","Développement des RH", "Bachelor"],
        ["002", "👦🏿 H", "Directeur adjoint - Relations sociales", "Direction des RH", "Master"],
        ["003", "👧 F", "Gestionnaire paie", "Administration des RH", "BTS / Titre pro"],
        ["004", "👨‍🦰 H", "Juriste droit social", "Administration des RH", "Master"],
        ["005", "👴 H", "Responsable GPEC", "Développement des RH", "Master"],
        ["...", "...", "...", "...", "..."]
]

    headers = ["Matricule RH","Genre H/F", "Poste", "Rattachement", "Diplôme"]

    df = pd.DataFrame(data, columns=headers)

    st.table(df)
       

    st.markdown("Dans cet exemple, l'ensemble de données comprend **diverses variables catégorielles liées aux RH**.") 
    st.markdown("Chaque ligne représente un employé différent et les colonnes représentent différents attributs :")
    
    st.markdown("⚠️**Matricule RH**⚠️: identifiant unique pour chaque employé")
    st.markdown("Le **Matricule RH** (ou « identifiant du salarié ») est une **variable importante à prendre en compte lorsque l'on travaille avec des données RH, qu'elles soient catégorielles ou numériques**. Cet identifiant agit comme un **identifiant clé qui relie les variables catégorielles et numériques à des employés spécifiques**. Il aide à **maintenir l'intégrité des données**, **permet une analyse au niveau individuel** et **permet des comparaisons et des calculs** basés sur différents attributs au sein de l'ensemble de données RH.")
                             
    
    st.markdown("")
    
    
    st.markdown("🎯**Genre H/F**: Variable catégorielle nominale indiquant si le salarié est un homme ou une femme (par exemple **H** ou **F**)")
    st.markdown("🎯**Poste**: Variable catégorielle nominale indiquant le poste du salarié : par exemple **Responsable formation**, **contrôleur de gestion sociale**, **gestionnaire paie**, etc")
    st.markdown("🎯**Rattachement**: Variable catégorielle nominale indiquant le domaine d'activité auquel se rattache le poste : par exemple **Développement des RH**, **Administration des RH**, **Direction des RH**")
    st.markdown("🎯**Diplôme**: Variable catégorielle **ordinale** indiquant le diplôme du salarié : par exemple **BTS / DUT**, **Bachelor**, **Maîtrise**, **Master**")     

       
    st.markdown("")   


    import streamlit as st
    import plotly.express as px
    import pandas as pd

# Sample HR dataset
    data = {
        'Employee ID': ['001', '002', '003', '004', '005', '006'],
        'Service': ['Ventes', 'Finance', 'RH', 'IT', 'Marketing', 'Operations'],
        'Genre': ['Femme', 'Femme', 'Homme', 'Femme', 'Homme', 'Homme']
}

    df = pd.DataFrame(data)

# Frequency table: Number of employees in each department
    st.markdown("🚨Exemple de **tableau de fréquences** :")
    department_counts = df['Service'].value_counts().reset_index()
    department_counts.columns = ['Service', 'Effectif']
    st.table(department_counts)

# Bar chart: Gender distribution in the organization
    st.markdown("🚨Exemple de **diagramme à barres**:")
    gender_distribution = df['Genre'].value_counts().reset_index()
    gender_distribution.columns = ['Genre', 'Effectif']

# Color mapping
    colors = {'Homme': 'blue', 'Femme': 'orange'}
    gender_distribution['Color'] = gender_distribution['Genre'].map(colors)

    fig = px.bar(gender_distribution, x='Genre', y='Effectif', color='Genre',
             color_discrete_map=colors, title='Effectif selon le genre')
    st.plotly_chart(fig)

    
    
    st.markdown("") 
    
    st.markdown("**b/ Les données numériques**")
    
    st.markdown("Les données **numériques** sont des données qui peuvent être **mesurées** ou **comptées**. Les données numériques peuvent ensuite être classées en données **discrètes** et **continues**.") 
    
    st.markdown("Les données **discrètes** sont des données qui ne peuvent prendre que des valeurs spécifiques (sans virgule), par exemple : le nombre d'employés dans un service.")

    df = pd.DataFrame(data)

# Frequency table: Number of employees in each department
    st.markdown("🚨Exemple de **données numériques discrètes** :")
    department_counts = df['Service'].value_counts().reset_index()
    department_counts.columns = ['Service', 'Effectif']
    st.table(department_counts)
    
    st.markdown("")
    
    st.markdown("Les données **continues**, en revanche, sont des données qui peuvent prendre n'importe quelle valeur dans une plage, par exemple l'âge, le salaire, l'ancienneté, etc...")

### Affichage tableau au format tabulaire    
    
    st.markdown("🚨Exemple de **données numériques continues** dans un service RH :")    
    
    data_2 = [
        ["001", 32, 50.5, 5.5, 9.5],
        ["002", 43.5, 72.3, 12.25, 9.25],
        ["003", 35.5, 40.1, 7.5, 9.1],
        ["004", 41, 65.9, 12, 8.9],
        ["005", 39, 58, 6.5, 7.8]
]

    headers_2 = ["⚠️Matricule RH⚠️", "Âge", "Salaire annuel (k€)", "Ancienneté", "Note de performance"]

    df_2 = pd.DataFrame(data_2, columns=headers_2)
    
# Formater les colonnes pour afficher 2 chiffres après la virgule : "Âge", "Salaire annuel (k€)", "Ancienneté", "Note de performance"
    
    df_2["Âge"] = df_2["Âge"].map(lambda x: "{:.1f}".format(x))
    df_2["Salaire annuel (k€)"] = df_2["Salaire annuel (k€)"].map(lambda x: "{:.1f}".format(x))
    df_2["Ancienneté"] = df_2["Ancienneté"].map(lambda x: "{:.2f}".format(x))
    df_2["Note de performance"] = df_2["Note de performance"].map(lambda x: "{:.2f}".format(x))

    st.table(df_2)
    
    
    st.markdown("Comme pour l'exemple précédent concernant les variables catégorielles, le jeu de données suivant comprend **diverses variables numériques liées aux RH**.") 
    st.markdown("Chaque ligne représente également un employé différent ; les colonnes représentent différents attributs :")
    
    st.markdown("⚠️**Matricule RH**⚠️: idem **identifiant unique pour chaque employé**")
    st.markdown("🎯**Âge**: Variable numérique indiquant l'âge du salarié")
    st.markdown("🎯**Salaire annuel**: Variable numérique indiquant le salaire annuel du salarié")
    st.markdown("🎯**Ancienneté**: Variable numérique indiquant le nombre d'années d'expérience professionnelle")
    st.markdown("🎯**Note de performance**: Variable numérique indiquant le score d'évaluation (échelle de 1 à 10) du rendement du salarié")     
        
        
    st.markdown("")
    
    st.markdown("Les données **numériques** sont souvent présentées sous forme **d'histogrammes** ou de **nuages de points**. Par exemple, un histogramme peut montrer la répartition des salaires dans l'organisation, tandis qu'un nuage de points peut montrer la relation entre l'âge et la performance au travail.")
    
    st.markdown("")     
        
    import streamlit as st
    import plotly.express as px
    import pandas as pd
    import numpy as np

# Sample HR dataset
    data = {
    'Employee ID': ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
    'Âge': [30, 28, 35, 42, 29, 36, 27, 31, 40, 33],
    'Salaire (€)': [55000, 60000, 65000, 58000, 70000, 62000, 56000, 59000, 75000, 61000],
    'Note de performance': [3, 4, 3, 2, 4, 2, 3, 4, 2, 4]
}

    df = pd.DataFrame(data)

# Histogram: Distribution of Salaries
    st.markdown("🚨Exemple d' **histogramme** :")
    fig_histogram = px.histogram(df, x='Salaire (€)', title='Distribution (répartition) des salaires')
    st.plotly_chart(fig_histogram)

# Scatter plot: Age vs. Performance Rating with correlation line
    st.markdown("🚨Exemple de **nuage de points** avec droite de régression :")
    correlation_coefficient = np.corrcoef(df['Âge'], df['Note de performance'])[0, 1]
    fig_scatter = px.scatter(df, x='Âge', y='Note de performance', title='Âge vs. Note de performance')
    fig_scatter.add_traces(px.scatter(x=df['Âge'], y=df['Note de performance']).data)
    fig_scatter.add_traces(px.line(x=df['Âge'], y=np.polyval(np.polyfit(df['Âge'], df['Note de performance'], 1), df['Âge'])).data)
    fig_scatter.update_layout(annotations=[dict(x=35, y=3.2, text=f'Correlation: {correlation_coefficient:.2f}', showarrow=False)])
    st.plotly_chart(fig_scatter)

    
    st.markdown("")

    st.markdown("**c/ Les sources des données**")

    st.markdown("")


    st.markdown("Les données peuvent être collectées à partir de diverses sources, telles que :")
    
    st.markdown("- les **dossiers du personnel** en **version papier** et / **ou digitale** (dématérialisée)")
    
    st.markdown("- le système d'information de gestion des ressources humaines (**SIRH**).")
    

    st.markdown("")


    st.markdown("🚨Le droit du travail ne prévoit aucune information obligatoire à renseigner sur un salarié, en revanche les informations recueillies doivent présenter un lien direct et nécessaire avec l'emploi proposé ou avec l'évaluation des aptitudes professionnelles (**Art. L1221-6 du CT**)")

    st.markdown("Ainsi pour assurer la gestion du personnel les données collectées et traitées sont généralement :")

    st.markdown("- copie pièce d'identité pour renseigner nom, prénoms, sexe, date et lieu de naissance")

    st.markdown("- coordonnées : adresse et téléphone")

    st.markdown("- copie carte vitale pour le NIR et attestation de securité sociale pour vérifier l'ouverture des droits à une complémentaire santé (mutuelle)")

    st.markdown("- Dossier de candidature, contrat de travail, documents relatifs à la gestion des arrêts maladie, compte-rendus d'entretiens annuels et autres évaluations, dossier « disciplinaire », etc...")

    
    st.markdown("")


    st.markdown("🚨Pour certains agents de la fonction publique de l'État, la liste des données à recueillir par les RH est précisée dans l'annexe du **décret n° 2019-612 du 19 juin 2019** portant création d'un traitement automatisé de données à caractère personnel (**RenoiRH**)")

                
    st.markdown("")


    st.markdown("🚨Un **SIRH** est un système logiciel qui gère des données RH. Il peut fournir une **base de données centralisée** pour les informations sur les employés, y compris les informations personnelles, l'historique professionnel, etc...") 

   
    st.markdown("Le SIRH peut également fournir des outils d’analyse des données et de reporting : c'est une excellente source de données catégorielles et numériques.")
    

    st.markdown("")


    st.markdown("Bien que les dossiers des employés constituent une source précieuse de données RH, un SIRH offre plusieurs avantages par rapport aux dossiers traditionnels.") 
    
    st.markdown("Le SIRH fournit une base de données centralisée accessible simultanément à plusieurs utilisateurs, ce qui facilite le partage d'informations entre les utilisateurs autorisés.") 
    
    st.markdown("Le SIRH fournit également des données RH en temps réel, permettant de prendre rapidement des décisions éclairées.") 
    
    st.markdown("Un autre avantage du SIRH est qu’il peut automatiser de nombreux processus RH, ce qui peut permettre de gagner du temps et de réduire les erreurs, améliorant ainsi l'efficacité globale d'un service RH.")
    
    
    st.markdown("")
    
    
# Afficher les images

    from PIL import Image
    col1, col2 = st.columns(2)

    with col1:
       st.markdown("dossiers du personnel")
       image = Image.open('cartoon_of_personnel_files.png')
       st.image(image)

    with col2:
       st.markdown("quelques SIRH")
       image = Image.open('photos_sirh.jpg')
       st.image(image)

    

if st.button("Continuer vers la suite du Chap.1 - **C/ Rôle des statistiques dans les RH**"):
    
    st.subheader("📈Chap.1-C/ Rôle des statistiques dans les RH📉")
    
    st.markdown("**Le rôle principal des statistiques appliquées aux RH est d'aider professionnels RH à prendre des décisions éclairées, basées sur des données**.") 
    
    st.markdown("Pour y arriver ils peuvent : ") 
                
    st.markdown("- **Créer des indicateurs**, concernant par exemple le **suivi de la masse salariale**, le **turn-over**, **l'absentéisme**, la **qualité du recrutement** et le **climat interne**.") 

    st.markdown("")


    import streamlit as st
    import plotly.express as px

# Monthly payroll data (in thousands of dollars)
    forecast_months_2023 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    réalisé_months_2023 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août']

    forecast_2023 = [1154300, 1200010, 1235205, 1305008, 1778120, 1263150, 1208180, 1240000, 1275002, 1299250, 2356280, 1251300]
    réalisé_2023 = [1152003, 1185350, 1113880, 1205008, 1677420, 1121245, 1148000, 1165000]

# Create a DataFrame for plotting
    df = pd.DataFrame({'Mois': forecast_months_2023 + réalisé_months_2023,
                   'Forecast 2023 (Prévision)': forecast_2023 + [None] * len(réalisé_months_2023),
                   'Réalisé 2023': [None] * len(forecast_months_2023) + réalisé_2023})

# Create an interactive line plot
    #st.header('Payroll Budget Evolution (2021 vs. 2022)')
    fig_1 = px.line(df, x='Mois', y=['Forecast 2023 (Prévision)', 'Réalisé 2023'],
                labels={'value': 'Masse salariale brute (Millions €)'},
                title='Exemple de suivi de la masse salariale (Prévision 2023 vs. Réalisé 2023)')
    st.plotly_chart(fig_1)

    
    st.markdown("")

    
    st.markdown("- Ils peuvent aussi **créer des tableaux de bord mensuels sur plusieurs indicateurs sociaux** tels que les **effectifs**, la **pyramide des âges** et **l'ancienneté**.")


    st.markdown("")
    

    st.markdown("Ci-dessous un exemple de pyramide des âges en **pelote de laine**")

    import streamlit as st
    import plotly.graph_objs as go
    import numpy as np

# Define age intervals
    age_intervals = ['[ < 25]', '[25 - 29]', '[30 - 34]', '[35 - 39]', '[40 - 44]', '[45 - 49]', '[50 - 54]', '[55 - 59]', '[60 et +]']

# Corresponding y values for the intervals
    y = list(range(len(age_intervals)))

    women_bins = np.array([-1686, -3868, -3463, -2346, -2074, -3037, -3495, -4194, -228])
    men_bins = np.array([887, 2013, 2323, 1842, 1645, 2270, 3115, 3891, 493])

    layout = go.Layout(
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
        marker=dict(color='blue')
    ),
    go.Bar(
        y=y,
        x=women_bins,
        orientation='h',
        name='👩‍🦰 Femme',
        text=-1 * women_bins.astype('int'),
        hoverinfo='text',
        marker=dict(color='pink')
    )
]

    fig_2 = go.Figure(data=data, layout=layout)
    
    st.plotly_chart(fig_2)


    st.markdown("- **Et enfin remplir les obligations légales**, notamment construire le **bilan social**, préparer et mettre à dsposition les données necessaires à la **négociation annuelle obligatoire** (NAO) ; ") 
    
    st.markdown("- Calculer l'**index égalité** 👦🏾/👧 ; effectuer la **déclaration annuelle obligatoire d’emploi des travailleurs handicapés** (DOETH), etc...") 
    
    st.markdown("Tous ces éléments sont basés sur la **collecte et l'analyse de données sociales** issues de la GRH.")


    st.markdown("")
    
    
    st.markdown("Les statistiques appliquées aux RH permettent aussi la mise en place de plans d’action **en vue d’améliorer la gestion des ressources humaines**.")
    

    st.markdown("")
    
    
    st.markdown("Par exemple, si on souhaite analyser l'écart de rémunération entre les 👦🏾/👧 dans une entreprise, on peut utiliser des données **numériques** (salaire **€**) et des données **catégorielles** (genre 👦🏾/👧).")
    
    st.markdown("On pourrait utiliser un **boxplot** pour montrer la répartition des salaires selon le genre (**fig.1**) et un **graphique à barres** pour montrer le salaire moyen par genre (**fig.2**).")

    
    st.markdown("")

    
    import streamlit as st
    import plotly.express as px
    import pandas as pd

    # Sample dataset
    data = {
    'Employee ID': ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
    'Genre': ['Homme👦🏾', 'Femme👧', 'Homme👦🏾', 'Femme👧', 'Homme👦🏾', 'Homme👦🏾', 'Femme👧', 'Femme👧', 'Homme👦🏾', 'Femme👧'],
    'Salaire €': [55000, 60000, 65000, 58000, 70000, 62000, 56000, 59000, 75000, 61000]
    }

    df = pd.DataFrame(data)

    # Distribution of salaries by gender
    st.markdown('**fig.1: Répartition des salaires selon le genre**')
    fig_box = px.box(df, x='Genre', y='Salaire €', points="all", color='Genre',
                     color_discrete_map={'Homme👦🏾': 'blue', 'Femme👧': 'orange'})
    st.plotly_chart(fig_box)
    
    st.markdown("")

    # Average salary by gender
    st.markdown('**fig.2: Salaire moyen selon le genre**')
    avg_salary = df.groupby('Genre')['Salaire €'].mean().reset_index()

    fig_bar = px.bar(avg_salary, x='Genre', y='Salaire €', color='Genre',
                     color_discrete_map={'Homme👦🏾': 'blue', 'Femme👧': 'orange'})
    st.plotly_chart(fig_bar)
    

    st.markdown("")
    
    st.markdown("")
    
    st.markdown("**Autre exemple** : utiliser des **données catégorielles** (intitulé du poste, département) et des **données numériques** (durée de l'emploi) pour identifier les tendances dans le **turnover** (départ et entrée de personnel).") 
    st.markdown("On pourrait utiliser un **nuage de points** pour montrer la **relation entre la durée de l'emploi et le taux de renouvellement des effectifs** (**fig.3**).")
    
    import streamlit as st
    import plotly.express as px
    import pandas as pd
    import numpy as np

    # Sample HR dataset
    data = {
    'Employee ID': ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
    'Job Title': ['Manager', 'Analyst', 'Specialist', 'Technician', 'Associate', 'Manager', 'Analyst', 'Specialist', 'Technician', 'Associate'],
    'Service': ['Sales', 'Finance', 'HR', 'IT', 'Marketing', 'Operations', 'Finance', 'HR', 'IT', 'Marketing'],
    'Durée Emploi (Années)': [5, 3, 2, 1, 4, 6, 2, 3, 2, 3],
    'Taux de turnover (%)': [8, 4, 12, 16, 6, 10, 9, 7, 15, 5]
    }

    df = pd.DataFrame(data)

    # Calculate correlation coefficient
    correlation_coefficient = np.corrcoef(df['Durée Emploi (Années)'], df['Taux de turnover (%)'])[0, 1]

    st.markdown("")
    
    # Scatter plot: Length of Employment vs. Turnover Rate with correlation line
   
    fig_scatter = px.scatter(df, x='Durée Emploi (Années)', y='Taux de turnover (%)', hover_data=['Job Title', 'Service'],
                         title='fig.3 : Relation entre durée Emploi et taux de turnover')
    fig_scatter.add_traces(px.scatter(x=df['Durée Emploi (Années)'], y=df['Taux de turnover (%)']).data)
    fig_scatter.add_traces(px.line(x=df['Durée Emploi (Années)'], y=np.polyval(np.polyfit(df['Durée Emploi (Années)'], df['Taux de turnover (%)'], 1), df['Durée Emploi (Années)'])).data)
    fig_scatter.update_layout(annotations=[dict(x=4, y=14, text=f'Correlation: {correlation_coefficient:.2f}', showarrow=False)])
    st.plotly_chart(fig_scatter)




    # Create the tabs
    tabs = st.tabs(["Suivi de la masse salariale", "Pyramide des âges", "Tab 3", "Tab 4"])

# Tab 1 - Line Chart
    with tabs[0]:
        st.write("## Line Chart")
        st.plotly_chart(fig_1)

# Tab 2 - Bar Chart
    with tabs[1]:
        st.write("## Bar Chart")
        st.plotly_chart(fig_2)

# Tab 3 - Box Plot
    with tabs[2]:
        st.write("## Box Plot")
        st.plotly_chart(fig_box)

# Tab 4 - Bar Chart
    with tabs[3]:
        st.write("## Bar Chart")
        st.plotly_chart(fig_bar)


                
    #url = "https://cours-stats-rh.streamlit.app/Quiz_1_-_Introduction_aux_Statistiques📉"
    #st.write("Acceder au quiz du chapitre 1 [ici](%s)" % url)


    #st.markdown("**Une solide compréhension des statistiques va donc aider les professionnels RH à prendre des décisions impactantes fondées sur des données**.")


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


                
    



    
   




    



    



