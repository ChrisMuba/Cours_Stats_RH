


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
    
    st.markdown("Nous devons embaucher des candidats pour deux postes : « Analyste de données RH » et « Coordonnateur RH ». Supposons que nous ayons deux groupes de candidats : un pour le poste « Analyste de données RH » et un autre pour le poste de « Coordonnateur RH ».") 
    
    st.markdown("La qualification de chaque candidat est classée comme « Qualifié » ou « Non qualifié ».") 
    
    st.markdown("Ci-dessous l'échantillon de données :")


    import streamlit as st
    import pandas as pd
    import plotly.express as px

# Sample Data
    data = {
        "ID du candidat": [1, 2, 3, 4, 5],
        "Qualification d'analyste de données RH": ["Qualifié", "Non Qualifié", "Qualifié", "Non Qualifié", "Qualifié"],
        "Qualification de coordonnateur RH": ["Non Qualifié", "Qualifié", "Non Qualifié", "Qualifié", "Non Qualifié"],
    }

    df = pd.DataFrame(data)

# Display the sample data
    st.dataframe(df)


    st.markdown("")

# Rule 1: The Sum Rule
    st.subheader("Règle 1 : la règle de la somme")
    st.latex(r"P(A \cup B) = P(A) + P(B) - P(A \cap B)")
    st.markdown(
        """
    La règle de la somme stipule que la probabilité que l'un des deux événements exclusifs se produise 
    est égale à la somme de leurs probabilités individuelles moins leur probabilité conjointe.

    Dans ce contexte, calculons la probabilité d'embauche soit pour le poste d'analyste de données RH, 
    soit pour le poste de Coordonnateur RH.

    - Événement A : Être qualifié pour le poste d'analyste de données RH
    - Événement B : Être qualifié pour le poste de coordonnateur RH

    Nous allons calculer P(A), P(B) et P(A et B) et utiliser la formule de la règle de somme pour trouver P(A ou B).
    """
    )

# Calculate P(A): Probability of being Qualified for Data Analyst
    total_data_analyst = df["Qualification d'analyste de données RH"].count()
    qualified_data_analyst = df[df["Qualification d'analyste de données RH"] == "Qualifié"]["Qualification d'analyste de données RH"].count()
    p_A = qualified_data_analyst / total_data_analyst

# Calculate P(B): Probability of being Qualified for HR Coordinator
    total_hr_coordinator = df["Qualification de coordonnateur RH"].count()
    qualified_hr_coordinator = df[df["Qualification de coordonnateur RH"] == "Qualifié"]["Qualification de coordonnateur RH"].count()
    p_B = qualified_hr_coordinator / total_hr_coordinator

# Calculate P(A and B): Probability of being Qualified for both positions
    qualified_both = df[(df["Qualification d'analyste de données RH"] == "Qualifié") & (df["Qualification de coordonnateur RH"] == "Qualifié")]["ID du candidat"].count()
    p_A_and_B = qualified_both / total_data_analyst  # Using the data analyst total for joint probability

# Calculate P(A or B) using the Sum Rule formula
    p_A_or_B = p_A + p_B - p_A_and_B

    st.latex(f"P(A) = {p_A}")
    st.latex(f"P(B) = {p_B}")
    st.latex(f"P(A \cap B) = {p_A_and_B}")
    st.latex(f"P(A \cup B) = {p_A_or_B}")


    st.markdown("")

# Rule 2: The Product Rule
    st.subheader("Règle 2 : la règle du produit")
    st.latex(r"P(A \cap B) = P(A) \cdot P(B)")
    st.markdown(
        """
    La règle du produit stipule que la probabilité que deux événements se produisent tous deux est égale au produit de leurs probabilités individuelles.

    Dans ce contexte, calculons la probabilité d'embauche à la fois pour le poste d'analyste de données RH et pour le poste de Coordonnateur RH.

   - Événement A : Être qualifié pour le poste d'analyste de données RH
   - Événement B : Être qualifié pour le poste de coordonnateur RH

    Nous allons calculer P(A) et P(B) et utiliser la formule de la règle du produit pour trouver P(A et B).
    """
    )

# Calculate P(A and B) using the Product Rule formula
    p_A_and_B = p_A * p_B

    st.latex(f"P(A) = {p_A}")
    st.latex(f"P(B) = {p_B}")
    st.latex(f"P(A \cap B) = {p_A_and_B}")

    st.markdown("")

# Rule 3: The Complement Rule
    st.subheader("Règle 3 : la règle du complément")
    st.latex(r"P(\neg A) = 1 - P(A)")
    st.markdown(
        """
    La règle du complément stipule que la probabilité qu’un événement ne se produise pas est égale à un moins la probabilité que l’événement se produise.

    Dans ce contexte, calculons la probabilité de ne pas être qualifié pour le poste d'analyste de données RH.

    - Événement A : Être qualifié pour le poste d'analyste de données RH

    Nous allons calculer P(A) et utiliser la formule de la règle du complément pour trouver P(non A).
    """
    )

# Calculate P(not A) using the Complement Rule formula
    p_not_A = 1 - p_A

    st.latex(f"P(A) = {p_A}")
    st.latex(f"P(\neg A) = {p_not_A}")

    
    st.markdown("")
    

if st.button("Continuer vers la suite du Chap.3 - **B/ Distributions de probabilité discrète**"):
    
    st.subheader("📈Chap.2-B/ Distributions discrète / Loi de Poisson📉")


    st.markdown("")


    st.markdown("Les distributions de probabilité sont des fonctions mathématiques qui décrivent la probabilité de différents résultats dans un processus aléatoire.") 
    
    st.markdown("Il existe deux principaux types de distributions de probabilité : **discrète** et **continue**.")
    

    st.markdown("")


    st.markdown("- **Distributions de probabilité discrète** : Des distributions de probabilité discrètes sont utilisées lorsque la variable aléatoire ne peut prendre que des valeurs distinctes et séparées. Cette distribution fournit la probabilité de chaque valeur possible de la variable aléatoire.")

    st.markdown("")
    
    st.markdown("**Distribution de Poisson** : La distribution de Poisson est une distribution de probabilité discrète, qui modélise le **nombre d'événements se produisant dans un intervalle de temps ou d'espace fixe**, étant donné un taux moyen d'événements connu. Elle est **souvent utilisée pour analyser des événements rares** qui se produisent indépendamment à un **taux moyen constant**.")

    st.markdown("")

    st.markdown("**Distribution binomiale** : La distribution binomiale est une distribution de probabilité discrète utilisée pour modéliser le nombre de réussites dans un nombre fixe d'essais indépendants (essais de Bernoulli), , chacun avec la **même probabilité de succès (p)**. Elle est caractérisé par deux paramètres, **n (nombre d'essais) et p (probabilité de succès)**.").")

    st.markdown("")
    
    st.markdown("- **🏀Application 17** :")
    
    
    st.markdown("")
    

   

    
    st.markdown("") 
    
    
if st.button("Continuer vers la suite du Chap.3 - **C/ Distributions de probabilité continue**"):


    st.markdown("")


    st.markdown("- **Distributions de probabilité continues** : Les distributions de probabilité continues sont utilisées lorsque la variable aléatoire peut prendre n'importe quelle valeur dans une plage. Cette distribution fournit la probabilité qu’un résultat se situe dans une certaine plage de valeurs.")
    
    st.markdown("Deux exemples courants sont la **distribution binomiale** et la **distribution de Poisson**.")
    
    st.markdown("- **Distribution binomiale** : La distribution binomiale modélise le **nombre de succès (x)** dans un nombre fixe d'essais indépendants, chacun avec la **même probabilité de succès (p)**. Il est caractérisé par deux paramètres, **n (nombre d'essais) et p (probabilité de succès)**.")
    
    st.markdown("- **Exemple 2 - Application possible en RH** : Considérez un chargé d'études RH à qui l'on demande de déterminer la probabilité de sélectionner trois candidats parmi un groupe de 10 pour un entretien d'embauche. En utilisant la distribution binomiale, le chargé d'études RH peut calculer la probabilité d'exactement trois sélections réussies, compte tenu d'un certain taux de réussite (par exemple, la proportion des candidats qualifiés dans le bassin.")
    
    


    
    st.subheader("📈Chap.3-C/ Distributions de probabilité continue📉")
    
    st.markdown("") 
    
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
    

    
    
    
    

            
