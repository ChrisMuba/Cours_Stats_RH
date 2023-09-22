


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

    st.markdown("")

    st.markdown("**Les concepts clés en probabilités comprennent les notions suivantes** :")

    
    st.markdown("")
    

    st.markdown("💡**Variable aléatoire** : c'est une quantité qui prend différentes valeurs à la suite d'événements aléatoires. Une variable aléatoire peut être **discrete ou continue**.") 
    
    st.markdown("")

    st.markdown("💡**Variable aléatoire discrète** : C'est une variable qui ne peut prendre que certaines valeurs distinctes. Par exemple, le nombre d'employés d'un service ne peut prendre que des valeurs entières.")

    st.markdown("")
                
    st.markdown("💡**Variable aléatoire continue** : C'est une variable qui peut prendre n'importe quelle valeur dans une plage. Par exemple, le salaire d’un employé peut prendre n’importe quelle valeur dans une certaine fourchette.")

    
    st.markdown("") 

    
    st.markdown("")

    st.markdown("- **Espace d'échantillonnage et événements** : l'espace d'échantillonnage **représente l'ensemble de tous les résultats possibles d'une expérience**. Les **événements sont des sous-ensembles** de l'espace d'échantillonnage, représentant des résultats spécifiques ou des combinaisons de résultats.")

    
    st.markdown("")


    st.markdown("**🏀Application 15**")

    st.markdown("Illustrons les concepts d'espace d'échantillonnage et d'événements par un scénario hypothétique dans lequel nous analysons les qualifications des candidats à un poste vacant.")

    st.markdown("Ci-dessous un échantillon des données de 5 candidats :")
    
    
    import streamlit as st
    import plotly.express as px
    import pandas as pd

# Sample Data
    data = {
        "Candidat": ["Candidat 1", "Candidat 2", "Candidat 3", "Candidat 4", "Candidat 5"],
        "Expérience (Années)": [2, 4, 3, 5, 1],
        "Diplôme": ["Bachelor", "Master", "Bachelor", "Ph.D.", "Master"],
    }

    df = pd.DataFrame(data)

# Display the sample data
    st.dataframe(df)

# Calculate the sample space for education levels
    sample_space_education = df["Diplôme"].unique()

# Calculate the sample space for experience
    sample_space_experience = df["Expérience (Années)"].unique()

# Explain Sample Space and Events
    st.markdown("**Explication**:")
    st.markdown(
        """
    - **Espace échantillon pour les diplômes :** L'espace échantillon pour les diplômes comprend tous les diplômes possibles dans notre ensemble de données. Dans notre cas, il se compose de trois catégories : « Bachelor », « Master » et « Ph.D »

    - **Espace échantillon pour l'expérience (années):** L'espace échantillon pour l'expérience comprend toutes les années d'expérience uniques dans notre ensemble de données. Dans ce cas, il s'agit des valeurs [2, 4, 3, 5, 1].

    Maintenant, définissons quelques événements basés sur cet exemple d'espace :
    - Événement A : Candidats titulaires d'un Master
    - Événement B : Candidats ayant plus de 3 ans d'expérience

    Nous pouvouns visualiser ces événements ci-dessous.
    """
    )

# Define Events
    event_A = df[df["Diplôme"] == "Master"]
    event_B = df[df["Expérience (Années)"] > 3]

# Visualize Event A (Master's Degree)
    st.subheader("Événement A: Candidats avec un diplôme de Master")
    fig_A = px.scatter(event_A, x="Expérience (Années)", y="Candidat", color="Diplôme", title="Événement A")
    st.plotly_chart(fig_A)

# Visualize Event B (More than 3 Years of Experience)
    st.subheader("Événement B: Candidats avec plus de 3 ans d'expérience")
    fig_B = px.scatter(event_B, x="Expérience (Années)", y="Candidat", color="Diplôme", title="Événement B")
    st.plotly_chart(fig_B)


    st.markdown("")


    st.markdown("- **Règles de probabilité** : La **probabilité d'un événement varie de 0** (événement impossible) à **1** (événement certain). Il existe trois règles principales de probabilité :")

    st.markdown("")

    st.markdown("La règle de la somme : la probabilité que l'un des deux événements exclusifs se produise est égale à la somme de leurs probabilités individuelles.")

    st.markdown("")
    
    st.markdown("La règle du produit : la probabilité que deux événements se produisent tous deux est égale au produit de leurs probabilités individuelles.")

    st.markdown("")

    st.markdown("La règle du complément : La probabilité qu’un événement ne se produise pas est égale à un moins la probabilité que l’événement se produise.")


    st.markdown("")


    st.markdown("**🏀Application 16**")

    st.markdown("Illustrons les trois principales règles de probabilité par un scénario hypothétique dans lequel nous analysons les candidats et leurs qualifications pour deux postes différents.")
    
    st.markdown("Disons que nous devons embaucher des candidats pour deux postes : « Analyste de données RH » et « Coordonnateur RH ».

    st.markdown("Supposons que nous ayons deux groupes de candidats : un pour le poste « Analyste de données RH » et un autre pour le poste de « Coordonnateur RH ».) 
    
    st.markdown("La qualification de chaque candidat est classée comme « Qualifié » ou « Non qualifié ». Voici les exemples de données :")


    import streamlit as st
    import pandas as pd
    import plotly.express as px

# Sample Data
    data = {
        "Applicant ID": [1, 2, 3, 4, 5],
        "Data Analyst Qualification": ["Qualified", "Not Qualified", "Qualified", "Not Qualified", "Qualified"],
        "HR Coordinator Qualification": ["Not Qualified", "Qualified", "Not Qualified", "Qualified", "Not Qualified"],
    }

    df = pd.DataFrame(data)

# Streamlit App
    st.title("HR Data Analysis: Probability Rules")

# Display the sample data
    st.subheader("Sample Data:")
    st.dataframe(df)

# Rule 1: The Sum Rule
    st.subheader("Rule 1: The Sum Rule")
    st.latex(r"P(A \cup B) = P(A) + P(B) - P(A \cap B)")
    st.markdown(
        """
    The sum rule states that the probability of either one of two exclusive events occurring 
    is equal to the sum of their individual probabilities minus their joint probability.

    In this context, let's calculate the probability of hiring for either the Data Analyst position or 
    the HR Coordinator position.

    - Event A: Being Qualified for Data Analyst
    - Event B: Being Qualified for HR Coordinator

    We'll calculate P(A), P(B), and P(A and B) and use the sum rule formula to find P(A or B).
    """
    )

# Calculate P(A): Probability of being Qualified for Data Analyst
    total_data_analyst = df["Data Analyst Qualification"].count()
    qualified_data_analyst = df[df["Data Analyst Qualification"] == "Qualified"]["Data Analyst Qualification"].count()
    p_A = qualified_data_analyst / total_data_analyst

# Calculate P(B): Probability of being Qualified for HR Coordinator
    total_hr_coordinator = df["HR Coordinator Qualification"].count()
    qualified_hr_coordinator = df[df["HR Coordinator Qualification"] == "Qualified"]["HR Coordinator Qualification"].count()
    p_B = qualified_hr_coordinator / total_hr_coordinator

# Calculate P(A and B): Probability of being Qualified for both positions
    qualified_both = df[(df["Data Analyst Qualification"] == "Qualified") & (df["HR Coordinator Qualification"] == "Qualified")]["Applicant ID"].count()
    p_A_and_B = qualified_both / total_data_analyst  # Using the data analyst total for joint probability

# Calculate P(A or B) using the Sum Rule formula
    p_A_or_B = p_A + p_B - p_A_and_B

    st.latex(f"P(A) = {p_A}")
    st.latex(f"P(B) = {p_B}")
    st.latex(f"P(A \cap B) = {p_A_and_B}")
    st.latex(f"P(A \cup B) = {p_A_or_B}")

# Rule 2: The Product Rule
    st.subheader("Rule 2: The Product Rule")
    st.latex(r"P(A \cap B) = P(A) \cdot P(B)")
    st.markdown(
        """
    The product rule states that the probability of two events both occurring is equal 
    to the product of their individual probabilities.

    In this context, let's calculate the probability of hiring for both the Data Analyst position and 
    the HR Coordinator position.

    - Event A: Being Qualified for Data Analyst
    - Event B: Being Qualified for HR Coordinator

    We'll calculate P(A) and P(B) and use the product rule formula to find P(A and B).
    """
    )

# Calculate P(A and B) using the Product Rule formula
    p_A_and_B = p_A * p_B

    st.latex(f"P(A) = {p_A}")
    st.latex(f"P(B) = {p_B}")
    st.latex(f"P(A \cap B) = {p_A_and_B}")

# Rule 3: The Complement Rule
    st.subheader("Rule 3: The Complement Rule")
    st.latex(r"P(\neg A) = 1 - P(A)")
    st.markdown(
        """
    The complement rule states that the probability of an event not occurring is equal 
    to one minus the probability of the event occurring.

    In this context, let's calculate the probability of not being Qualified for the Data Analyst position.

    - Event A: Being Qualified for Data Analyst

    We'll calculate P(A) and use the complement rule formula to find P(not A).
    """
    )

# Calculate P(not A) using the Complement Rule formula
    p_not_A = 1 - p_A

    st.latex(f"P(A) = {p_A}")
    st.latex(f"P(\neg A) = {p_not_A}")
























    




    
    
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
    

    
    
    
    

            
