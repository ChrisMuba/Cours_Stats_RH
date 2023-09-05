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
                
    st.markdown("Les données **catégorielles** sont des données qui peuvent être **triées en catégories ou en groupes**. Ces catégories sont non numériques et peuvent être **qualitatives** ou **quantitatives**.")

    st.markdown("⚠️Des données **catégorielles** peuvent être **quantitatives** car elles peuvent être quantifiées ou décrites à l'aide de méthodes numériques : calculs de fréquences, pourcentages, tests du khi-deux, pour résumer et analyser les données ; l'analyse de clustering ou l'analyse factorielle pour identifier des modèles et des relations dans les données catégorielles.")  
    
    st.markdown("Des exemples de données catégorielles en Ressources Humaines incluent par exemple **le genre** : 👦🏾/👧 ; le **titre du poste**: **contrôleur de gestion sociale**, **responsable formation**, etc... ; le **rattachement du poste** : **administration des RH**, **développement des RH**, etc...") 
    
    st.markdown("Les données catégorielles peuvent ensuite être classées en données **nominales** et **ordinales**. Les données nominales sont des **données qui ne peuvent pas être classées ou ordonnées**, telles que **le genre** : 👦🏾/👧 ou le **titre du poste**.") 
    
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
        ["006", "👩‍🦰 F", "Assistante RH", "Administration des RH", "BTS"],
        ["007", "🧔🏽 H", "Responsable formation", "Développement des RH", "Master"],
        ["008", "👱🏽‍♀️ F", "Chargée de marketing RH", "Développement des RH", "DUT"],
        ["009", "👩🏼‍🦳 F", "Directrice RH", "Direction des RH", "Maîtrise"],
        ["010", "🧑🏻 H", "Contrôleur de gestion sociale", "Administration des RH", "Master"]
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
        'Employee ID': ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
        'Service': ['Ventes', 'Finance', 'RH', 'IT', 'Marketing', 'Operations', 'Finance', 'RH', 'IT', 'Marketing'],
        'Genre': ['Homme', 'Femme', 'Homme', 'Femme', 'Homme', 'Homme', 'Femme', 'Femme', 'Homme', 'Femme']
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
    
    st.markdown("Les données **discrètes** sont des données qui ne peuvent prendre que des valeurs spécifiques, par exemple : le nombre d'employés dans un service.")

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
        ["001", 32.5, 50000, 5, 9.5],
        ["002", 43, 72000, 12.5, 9.2],
        ["003", 35.5, 40000, 7, 9.1],
        ["004", 41, 65000, 12.5, 8.9],
        ["005", 39.5, 58000, 6, 7.8],
        ["006", 36, 40000, 8, 9.4],
        ["007", 38, 55000, 6, 8.7],
        ["008", 27.5, 36000, 3.5, 6.9],
        ["009", 49, 75000, 15, 8.7],
        ["010", 35, 45000, 5, 8.5],
]

    headers_2 = ["⚠️Matricule RH⚠️", "Âge", "Salaire annuel (€)", "Ancienneté", "Note de performance"]

    df_2 = pd.DataFrame(data_2, columns=headers_2)
    
# Format Performance Score column
    
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
    'Age': [30, 28, 35, 42, 29, 36, 27, 31, 40, 33],
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
    correlation_coefficient = np.corrcoef(df['Age'], df['Note de performance'])[0, 1]
    fig_scatter = px.scatter(df, x='Age', y='Note de performance', title='Age vs. Note de performance')
    fig_scatter.add_traces(px.scatter(x=df['Age'], y=df['Note de performance']).data)
    fig_scatter.add_traces(px.line(x=df['Age'], y=np.polyval(np.polyfit(df['Age'], df['Note de performance'], 1), df['Age'])).data)
    fig_scatter.update_layout(annotations=[dict(x=35, y=3.2, text=f'Correlation: {correlation_coefficient:.2f}', showarrow=False)])
    st.plotly_chart(fig_scatter)

    
    st.markdown("")
    
    
    st.markdown("Les données peuvent être collectées à partir de diverses sources, telles que :")
    
    st.markdown("- les **dossiers du personnel** en **version papier** et / **ou digitale**")
    
    st.markdown("- le système d'information de gestion des ressources humaines (**SIRH**).")
    
    
    st.markdown("")
    
    
# Afficher les images

    from PIL import Image
    col1, col2 = st.columns(2)

    with col1:
       st.markdown("dossiers du personnel")
       image = Image.open('dossiers_employes.jpg')
       st.image(image)

    with col2:
       st.markdown("quelques SIRH")
       image = Image.open('photos_sirh.jpg')
       st.image(image)

    

if st.button("Continuer vers la suite du Chap.1 - **C/ Rôle des statistiques dans les RH**"):
    
    st.subheader("📈Chap.1-C/ Rôle des statistiques dans les RH📉")
    
    st.markdown("**Le rôle principal des statistiques appliquées aux RH est d'aider professionnels RH à prendre des décisions éclairées, basées sur des données**.") 
    
    st.markdown("Pour y arriver ils peuvent : ") 
                
    st.markdown("- **Créer des indicateurs**, concernant par exemple la **masse salariale**, le **turn-over**, **l'absentéisme**, la **qualité du recrutement** et le **climat interne**.") 
    
    st.markdown("- Ils peuvent aussi **créer des tableaux de bord mensuels sur plusieurs indicateurs sociaux** tels que les **effectifs**, la **pyramide des âges** et **l'ancienneté**.")
    
    st.markdown("- **Et enfin remplir les obligations légales**, notamment : **bilan social, NAO, rapport social, index égalité 👦🏾/👧, déclaration annuelle obligatoire d’emploi des travailleurs handicapés** (DOETH).") 
    
    st.markdown("Tous ces éléments sont basés sur la **collecte et l'analyse de données sociales** et permettront la mise en place de plans d’action **en vue d’améliorer la gestion des ressources humaines**.")
    
    st.markdown("Par exemple, si on souhaite analyser l'écart de rémunération entre les 👦🏾/👧 dans une entreprise, on peut utiliser des données **numériques** (salaire **€**) et des données **catégorielles** (genre 👦🏾/👧).")
    
    st.markdown("On pourrait utiliser un **boxplot** pour montrer la répartition des salaires selon le genre (**fig.1**) et un **graphique à barres** pour montrer le salaire moyen par genre(**fig.2**).")
    
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
    
    st.markdown("**Autre exemple :** utiliser des données catégorielles (intitulé du poste, département) et des données numériques (durée de l'emploi) pour identifier les tendances du roulement.") 
    st.markdown("On pourrait utiliser un **nuage de points** pour montrer la relation entre la durée de l'emploi et le taux de roulement (**fig.3**).")
    
    import streamlit as st
    import plotly.express as px
    import pandas as pd
    import numpy as np

    # Sample HR dataset
    data = {
    'Employee ID': ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
    'Job Title': ['Manager', 'Analyst', 'Specialist', 'Technician', 'Associate', 'Manager', 'Analyst', 'Specialist', 'Technician', 'Associate'],
    'Department': ['Sales', 'Finance', 'HR', 'IT', 'Marketing', 'Operations', 'Finance', 'HR', 'IT', 'Marketing'],
    'Length of Employment (Years)': [5, 3, 2, 1, 4, 6, 2, 3, 2, 3],
    'Turnover Rate (%)': [8, 4, 12, 16, 6, 10, 9, 7, 15, 5]
    }

    df = pd.DataFrame(data)

    # Calculate correlation coefficient
    correlation_coefficient = np.corrcoef(df['Length of Employment (Years)'], df['Turnover Rate (%)'])[0, 1]

    st.markdown("")
    
    # Scatter plot: Length of Employment vs. Turnover Rate with correlation line
   
    fig_scatter = px.scatter(df, x='Length of Employment (Years)', y='Turnover Rate (%)', hover_data=['Job Title', 'Department'],
                         title='fig.3 : Relationship between Length of Employment and Turnover Rate')
    fig_scatter.add_traces(px.scatter(x=df['Length of Employment (Years)'], y=df['Turnover Rate (%)']).data)
    fig_scatter.add_traces(px.line(x=df['Length of Employment (Years)'], y=np.polyval(np.polyfit(df['Length of Employment (Years)'],         df['Turnover Rate (%)'], 1), df['Length of Employment (Years)'])).data)
    fig_scatter.update_layout(annotations=[dict(x=4, y=14, text=f'Correlation: {correlation_coefficient:.2f}', showarrow=False)])
    st.plotly_chart(fig_scatter)


                
    #st.markdown("Mais aussi de **mesurer et anticiper les coûts financiers de la gestion et de la politique RH** d'une entreprise.")
    
    st.markdown("")
                
    #st.markdown("**Une solide compréhension des statistiques va donc aider les professionnels RH à prendre des décisions impactantes fondées sur des données**.")
    
   




    



    



