


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
    
    st.subheader("📈Chap.2-B/ Distribution discrète📉")


    st.markdown("")


    st.markdown("Les distributions de probabilité sont des fonctions mathématiques qui décrivent la probabilité de différents résultats dans un processus aléatoire.") 
    
    st.markdown("Il existe deux principaux types de distributions de probabilité : **discrète** et **continue**.")
    

    st.markdown("")


    st.markdown("- **Distributions de probabilité discrète** : Des distributions de probabilité discrètes sont utilisées lorsque la variable aléatoire ne peut prendre que des valeurs distinctes et séparées. Cette distribution fournit la probabilité de chaque valeur possible de la variable aléatoire.")

    st.markdown("")
    
    st.markdown("**Distribution de Poisson** : La distribution de Poisson est une distribution de probabilité discrète, qui modélise le **nombre d'événements se produisant dans un intervalle de temps ou d'espace fixe**, étant donné un taux moyen d'événements connu. Elle est **souvent utilisée pour analyser des événements rares** qui se produisent indépendamment à un **taux moyen constant**.")

    st.markdown("")

    st.markdown("**Distribution binomiale** : La distribution binomiale est une distribution de probabilité discrète utilisée pour modéliser le nombre de réussites dans un nombre fixe d'essais indépendants (essais de Bernoulli), chacun avec la **même probabilité de succès (p)**. Elle est caractérisé par deux paramètres, **n (nombre d'essais) et p (probabilité de succès)**.")

    st.markdown("")
    
    st.markdown("- **🏀Application 17** :")

    st.markdown("Un chargé de recrutement de la municipalité de Culiacan-lès-Marseille doit de suivre le nombre de candidats qui visitent le site web carrière de la commune au cours d'une période donnée.") 
    
    st.markdown("Ci-dessous les data collectées sur le nombre de visites du site web par heure sur une semaine.")

    st.markdown("")


    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import numpy as np
    from scipy.stats import poisson, binom

# Sample Data
    data = {
        "Heure": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Visites": [8, 7, 9, 6, 10, 9, 11, 8, 7, 10],
    }

    df = pd.DataFrame(data)

# Display the sample data
    st.markdown("Echantillon de données (Visites du site web carrière par heure):")
    st.dataframe(df)

# Poisson Distribution
    st.subheader("Distribution de Poisson (Visites site web):")
    st.markdown(
        """
    La distribution de Poisson modélise le nombre d'événements se produisant dans un intervalle de temps ou d'espace fixe,
    étant donné un taux d’événements moyen connu. Dans ce contexte, elle peut être utilisée pour prédire le nombre de visites du site web
    carrière à une heure spécifique en fonction du nombre moyen de visites par heure.

    Supposons que le nombre moyen de visites du site Web par heure soit de 8. 
    
    Nous calculons les probabilités de Poisson pour différents nombres de visites par heure et en visualisons la répartition.
    """
    )

    st.markdown("")


# Define the average number of visits per hour
    average_visits = 8

# Calculate Poisson probabilities for different values
    x = np.arange(0, 16)  # Number of visits from 0 to 15
    poisson_probs = poisson.pmf(x, average_visits)

# Display the Poisson probabilities table
    poisson_table = pd.DataFrame({"Nombre de visites (x)": x, "P(X = x)": poisson_probs})
    st.markdown("**Table des probabilités de Poisson pour différentes valeurs de *Nombre de visites* (x).**")
    st.table(poisson_table)

# Visualize the Poisson Distribution
    fig_poisson = px.bar(x=x, y=poisson_probs, labels={"x": "Nombre de visites", "y": "Probabilité"}, title="DataViz: Distribution de Poisson ")
    st.plotly_chart(fig_poisson)


# Explanation
    with st.expander("🔮Interpretation"):
        st.write("""
        Dans le tableau, nous avons calculé les probabilités de Poisson pour différents scenarii, représentant le nombre de visites de sites Web par heure (Nombre de visites (x)) sur la base d'un taux d'événements moyen de 8 visites par heure. 
        Chaque ligne du tableau correspond à une valeur spécifique de « x », qui représente le nombre de visites qui nous intéressent.

        Distribution de probabilité : la distribution de Poisson nous aide à comprendre la probabilité d'observer un nombre spécifique de visites de sites Web (Nombre de visites (x)) au cours d'une heure donnée.
        
        Courbe en forme de cloche : comme nous pouvons le voir sur la visualisation, la distribution de Poisson forme une courbe en forme de cloche. 
        Cette courbe est centrée autour du taux moyen d’événements, qui est ici de 8 visites par heure.
        
        Variation de probabilité : La probabilité d’observer différents nombres de visites varie. Par exemple, la probabilité d’avoir exactement 8 visites par heure (la moyenne) est relativement élevée, soit environ 0,14. 
        Cependant, à mesure que l’on s’éloigne de la moyenne dans un sens ou dans l’autre, les probabilités diminuent.

        Événements rares : la distribution de Poisson est particulièrement utile pour modéliser des événements rares, où le taux d'événements moyen est faible et où les événements se produisent indépendamment.

        ⚠️La distribution de Poisson n'est qu'un des nombreux outils de la boîte à outils statistiques et elle peut s'avérer un atout précieux lorsque l'on traite des événements qui se produisent de manière aléatoire et peu fréquente.
        """)
    

    st.markdown("")

    

# Binomial Distribution
    st.subheader("Distribution Binomiale (Succès des candidats à un emploi):")
    st.markdown(
       """
    La distribution binomiale modélise le nombre de réussites dans un nombre fixe d'essais indépendants
    (essais de Bernoulli), chacun avec la même probabilité de succès (p). En RH, elle peut être utilisée pour modéliser
    le nombre de candidats retenus sur un nombre fixe d'entretiens (essais) avec un probabilité de succès.

    Supposons qu'il y ait 10 candidats à un emploi et que chacun ait 30 % de chances de succès. Nous calculerons les
    Probabilités binomiales pour différents nombres de candidats retenus et visualiserons la distribution.
    """
    )

    st.markdown("")
    

# Define the parameters for the Binomial distribution
    n_applicants = 10  # Number of job applicants
    p_success = 0.3   # Probability of success for each applicant

# Calculate Binomial probabilities for different values
    x_binom = np.arange(0, 11)  # Number of successful applicants from 0 to 10
    binom_probs = binom.pmf(x_binom, n_applicants, p_success)

# Create a DataFrame to display the calculation details
    calculation_details_binom = pd.DataFrame({"Number of Successful Applicants (x)": x_binom, "P(X = x)": binom_probs})
    calculation_details_binom = calculation_details_binom.round(4)  # Round to 4 decimal places for readability

# Display the calculation details table
    st.subheader("Calculation Details:")
    st.dataframe(calculation_details_binom)

# Visualize the Binomial Distribution
    fig_binomial = px.bar(x=x_binom, y=binom_probs, labels={"x": "Nombre de candidats retenus", "y": "Probabilité"}, title="Distribution Binomiale")
    st.plotly_chart(fig_binomial)

    
    st.markdown("")
    
    
    st.markdown("") 
    
    
if st.button("Continuer vers la suite du Chap.3 - **C/ Distributions de probabilité continue**"):

    st.subheader("📈Chap.2-B/ Distribution continue📉")


    st.markdown("")


    st.markdown("- **Distributions de probabilité continues** : Les distributions de probabilité continue décrivent la probabilité de résultats pour des variables aléatoires continues, qui peuvent prendre un nombre infini de valeurs dans une plage spécifiée.")
    
    st.markdown("La distribution continue la plus utilisée est la **distribution normale**.")
    
    st.markdown("**La distribution normale**, également connue sous le nom de **distribution gaussienne ou courbe en cloche**, se caractérise par sa **courbe symétrique en forme de cloche**. Elle est définie par deux paramètres : la **moyenne** (μ) et **l'écart type** (σ). La distribution normale est largement utilisée dans divers domaines, y compris RH, en raison de sa capacité à modéliser avec précision de nombreux phénomènes du monde réel.")

    st.markdown("")
    
    st.markdown("- **🏀Application 18** :")

    st.markdown("Le contrôleur de gestion sociale d'un service public de *Pluie-lès-Brest* a collecté des données sur les évaluations de performance de 100 agents. Il souhaite analyser la répartition de ces évaluations.")

    st.markdown("Ci-dessous les données collectées.")

    st.markdown("")


    import pandas as pd
    import numpy as np
    import streamlit as st
    import plotly.express as px

# Sample Data
    data = {
        "Employee ID": range(1, 101),
        "Performance Rating": np.random.normal(70, 10, 100)  # Mean = 70, Standard Deviation = 10
    }

    df = pd.DataFrame(data)


# Display the sample data with two digits after the decimal point

    df_display = df.copy()  # Create a copy of the DataFrame for display
    df_display["Performance Rating"] = df_display["Performance Rating"].apply(lambda x: round(x, 2))
 
# Display the sample data
    st.markdown("Échantillon de données (évaluations des performances):")
    #st.dataframe(df)
    st.dataframe(df_display)

# Normal Distribution
    st.subheader("Distribution Normale (Évaluation Performance):")
    st.markdown(
        """
    La distribution normale, également connue sous le nom de distribution gaussienne ou courbe en cloche, se caractérise par sa courbe symétrique en forme de cloche. 
    Elle est définie par deux paramètres : la moyenne (μ) et l'écart type (σ). En RH, la distribution normale peut être utilisée pour modéliser diverses mesures de performance des employés.

    Dans ce contexte, supposons que la note de performance moyenne du Service Public est de 70 et que l'écart type est de 10. 
    Nous calculerons les probabilités associées aux différentes notes de performance et visualiserons la distribution normale.
    """
    )

    st.markdown("")
    

# Define the mean and standard deviation for the normal distribution
    mean_rating = 70
    std_deviation = 10

# Calculate the probabilities for different performance ratings
    x_values = np.linspace(mean_rating - 3 * std_deviation, mean_rating + 3 * std_deviation, 100)
    pdf_values = (1 / (std_deviation * np.sqrt(2 * np.pi))) * np.exp(-((x_values - mean_rating) ** 2) / (2 * std_deviation ** 2))

# Create a DataFrame to display the calculation details
    calculation_details = pd.DataFrame({"Évaluation Performance (x)": x_values, "Densité de probabilité (P(X = x))": pdf_values})
    calculation_details = calculation_details.round(4)  # Round to 4 decimal places for readability

# Display the calculation details table
    st.markdown("Table des probabilités pour différentes valeurs des notes d'évaluation de performance (x).:")
    st.dataframe(calculation_details)

# Visualize the Normal Distribution
    fig_normal = px.line(x=x_values, y=pdf_values, labels={"x": "Évaluation Performance", "y": "Densité de probabilité"}, title="DataViz : Distribution Normale")
    st.plotly_chart(fig_normal)

    # Explanation
    with st.expander("🔮Interpretation"):
        st.write("""
        Dans le tableau, nous avons calculé les probabilités associées à différentes notes de performance (Évaluation Performance (x)) sur la base d'une distribution normale avec une moyenne (μ) de 70 et un écart type (σ) de 10. 
        Chaque ligne du Le tableau correspond à une note de performance spécifique, et la colonne « Densité de probabilité (P(X = x)) » représente la probabilité d'observer cette note particulière.

        Distribution de probabilité : La distribution normale est symétrique et caractérisée par deux paramètres : la moyenne (μ) et l'écart type (σ). Cela nous aide à modéliser la probabilité d’observer différentes notes de performance.
        
        Courbe en forme de cloche : Comme le montre la visualisation, la distribution normale forme une courbe en forme de cloche, avec le pic centré autour de la moyenne (μ). 
        Dans notre cas, la note moyenne de performance est de 70.
        
        Densité de probabilité : la densité de probabilité (P(X = x)) quantifie la probabilité d'observer des évaluations de performance spécifiques. 
        Les notes plus proches de la moyenne ont des probabilités plus élevées, tandis que les notes plus éloignées de la moyenne ont des probabilités plus faibles.

        Plage de valeurs : La distribution normale s'étend à l'infini dans les deux directions, couvrant une large gamme de performances possibles. 
        ⚠️Cependant, les notes qui s’éloignent de plus de quelques écarts-types de la moyenne deviennent de plus en plus rares.
    """)
    

    st.markdown("")


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
    

    
    
    
    

            
