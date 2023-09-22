


import streamlit as st

st.markdown("# Chapitre 3")
st.sidebar.markdown("# Chapitre 3")

st.title("Introductions aux probabilités et distributions")

st.markdown("Ce chapitre sert d'**introduction** en fournissant un **aperçu des concepts de base en probabilités et distributions, et leurs applications possibles dans le domaine des RH**.")

st.markdown("La **théorie des probabilités** est la branche des mathématiques qui **quantifie la possibilité qu'un événement particulier se produise** (événement aléatoire). Cette possibilité est exprimée sous la forme d'un nombre compris entre 0 et 1.")

st.markdown("En termes simples, la probabilité quantifie le degré de certitude ou d'incertitude associé à un résultat spécifique. Elle est calculée en divisant le nombre de résultats favorables par le nombre total de résultats possibles dans une situation donnée.")


st.markdown("")


if st.button("Cliquez pour acceder au Chap.3 - **A/ Concepts de clés**"):
    
    st.subheader("📈Chap.3-A/ Concepts de clés📉")

    st.markdown("Quelques définitionns :")

    st.markdown("")

    st.markdown("💡**Variable aléatoire** : c'est une quantité qui prend différentes valeurs à la suite d'événements aléatoires. Une variable aléatoire peut être **discrete ou continue**.") 
    
    st.markdown("")

    st.markdown("💡**Variable aléatoire discrète** : C'est une variable qui ne peut prendre que certaines valeurs distinctes. Par exemple, le nombre d'employés d'un service ne peut prendre que des valeurs entières.")

    st.markdown("")
                
    st.markdown("💡**Variable aléatoire continue** : C'est une variable qui peut prendre n'importe quelle valeur dans une plage. Par exemple, le salaire d’un employé peut prendre n’importe quelle valeur dans une certaine fourchette.")

    
    st.markdown("") 

    
    st.markdown("**Les concepts clés en probabilités comprennent les notions suivantes** :")

    st.markdown("")

    st.markdown("- **Espace d'échantillonnage et événements** : l'espace d'échantillonnage **représente l'ensemble de tous les résultats possibles d'une expérience**. Les **événements sont des sous-ensembles** de l'espace d'échantillonnage, représentant des résultats spécifiques ou des combinaisons de résultats.")

    
    st.markdown("")


    st.markdown("**🏀Application 15**")

    st.markdown("Illustrons les concepts d'espace d'échantillonnage et d'événements dans le contexte RH par un scénario hypothétique dans lequel nous analysons les qualifications des candidats à un poste vacant.")

    st.markdown("Ci-dessous un échantillon des données de 5 candidats :")
    
    
    import streamlit as st
    import plotly.express as px
    import pandas as pd

# Sample Data
    data = {
        "Candidate": ["Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4", "Candidate 5"],
        "Experience (Years)": [2, 4, 3, 5, 1],
        "Education": ["Bachelor's", "Master's", "Bachelor's", "Ph.D.", "Master's"],
    }

    df = pd.DataFrame(data)

# Display the sample data
    st.subheader("Échantillon des données :")
    st.dataframe(df)

# Calculate the sample space for education levels
    sample_space_education = df["Education"].unique()

# Calculate the sample space for experience
    sample_space_experience = df["Experience (Years)"].unique()

# Explain Sample Space and Events
    st.subheader("Explanation:")
    st.markdown(
        """
    - **Sample Space for Education Levels:** The sample space for education levels includes all possible education levels in our dataset. In this case, it consists of three categories: "Bachelor's," "Master's," and "Ph.D."

    - **Sample Space for Experience (Years):** The sample space for experience includes all unique years of experience in our dataset. In this case, it consists of the values [2, 4, 3, 5, 1].

    Now, let's define some events based on this sample space:
    - Event A: Candidates with a Master's degree
    - Event B: Candidates with more than 3 years of experience

    We'll use Plotly to visualize these events on the sample data.
    """
    )

# Define Events
    event_A = df[df["Education"] == "Master's"]
    event_B = df[df["Experience (Years)"] > 3]

# Visualize Event A (Master's Degree)
    st.subheader("Event A: Candidates with a Master's Degree")
    fig_A = px.scatter(event_A, x="Experience (Years)", y="Candidate", color="Education", title="Event A")
    st.plotly_chart(fig_A)

# Visualize Event B (More than 3 Years of Experience)
    st.subheader("Event B: Candidates with More than 3 Years of Experience")
    fig_B = px.scatter(event_B, x="Experience (Years)", y="Candidate", color="Education", title="Event B")
    st.plotly_chart(fig_B)


    


    st.markdown("- **Règles de probabilité** : La **probabilité d'un événement varie de 0** (événement impossible) à **1** (événement certain). La somme des probabilités de tous les résultats possibles dans l'espace échantillon est toujours **1**. De plus, la règle de complément, la règle d'addition et la règle de multiplication aident à calculer les probabilités dans différents scénarios.")
    
    st.markdown("- **Exemple 1 - Application possible en RH** : Supposons qu'un chargé d'études RH veuille déterminer la probabilité qu'un employé soit absent un jour particulier. Il peut collecter des données historiques sur les absences des employés et calculer la proportion d'absences par rapport au nombre total de jours de travail pour estimer la probabilité.")

if st.button("Continuer vers la suite du Chap.3 - **B/ Distributions de probabilité discrète**"):
    
    st.subheader("📈Chap.2-B/ Distributions de probabilité discrète📉")
    
    st.markdown("Des **distributions de probabilité discrètes sont utilisées lorsque la variable aléatoire ne peut prendre que des valeurs distinctes et séparées**.") 
    
    st.markdown("Deux exemples courants sont la **distribution binomiale** et la **distribution de Poisson**.")
    
    st.markdown("- **Distribution binomiale** : La distribution binomiale modélise le **nombre de succès (x)** dans un nombre fixe d'essais indépendants, chacun avec la **même probabilité de succès (p)**. Il est caractérisé par deux paramètres, **n (nombre d'essais) et p (probabilité de succès)**.")
    
    st.markdown("- **Exemple 2 - Application possible en RH** : Considérez un chargé d'études RH à qui l'on demande de déterminer la probabilité de sélectionner trois candidats parmi un groupe de 10 pour un entretien d'embauche. En utilisant la distribution binomiale, le chargé d'études RH peut calculer la probabilité d'exactement trois sélections réussies, compte tenu d'un certain taux de réussite (par exemple, la proportion des candidats qualifiés dans le bassin.")
    
    st.markdown("- **Distribution de Poisson** : La distribution de Poisson modélise le **nombre d'événements se produisant dans un intervalle de temps ou d'espace fixe**. Il est **souvent utilisé pour analyser des événements rares** qui se produisent indépendamment à un **taux moyen constant (λ)**.")
    
    st.markdown("- **Exemple 3 - Application possible en RH** : Un chargé d'études RH dans le secteur industriel peut devoir analyser mensuellement le nombre d'accidents du travail pour identifier les problèmes de sécurité. **En ajustant les données historiques d'accidents du travail à une distribution de Poisson**, le chargé d'études RH peut estimer la probabilité qu'un nombre spécifique d'accidents du travail se produisent au cours d'un mois donné.")

if st.button("Continuer vers la suite du Chap.3 - **C/ Distributions de probabilité continue**"):
    
    st.subheader("📈Chap.3-C/ Distributions de probabilité continue📉")
    
    st.markdown("**Les distributions de probabilité continues sont utilisées lorsque la variable aléatoire peut prendre n'importe quelle valeur dans une plage.**") 
    
    st.markdown("La distribution continue la plus utilisée est la **distribution normale**.")
    
    st.markdown("- **La distribution normale**, également connue sous le nom de **distribution gaussienne ou courbe en cloche**, se caractérise par sa **courbe symétrique en forme de cloche**. Elle est définie par deux paramètres : la **moyenne** (μ) et **l'écart type** (σ). De nombreux phénomènes naturels suivent une distribution normale, y compris dans le domaine des RH.")
    
    st.markdown("- **Exemple 3 - Application possible en RH** : Un chargé d'études RH doit analyser les notes de performance des employés pour attribuer une prime de rendement individuelle (prime non obligatoire). Si les notes sont distribuées normalement, le chargé d'études RH peut utiliser les propriétés de la distribution normale pour déterminer la proportion d'employés appartenant à des catégories de performance spécifiques (par exemple, les plus performants, ceux qui affichent une performance moyenne, et les moins performants.)")


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
    redirect_button("https://cours-stats-rh.streamlit.app/Quiz_3_-_Probabilités_et_distributions📉","Quiz du chapitre 3")
    

    
    
    
    

            
