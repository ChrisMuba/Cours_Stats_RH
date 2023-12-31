


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Chapitre 4")
st.sidebar.markdown("# Chapitre 4")

st.title("Statistiques inférentielles : estimation et tests d'hypothèses")

st.markdown("Dans ce chapitre, nous explorerons deux concepts fondamentaux des statistiques inférentielles : **l'estimation et les tests d'hypothèses**.") 
st.markdown("Nous aborderons également certains tests couramment utilisés tels que les **test t, test du chi carré et l'ANOVA**.")

if st.button("Cliquez pour acceder au Chap.4 - **A/ Estimation**"):
    
    st.subheader("📈Chap.4-A/ Estimation📉")
    
    st.markdown("Les **statistiques inférentielles** sont un outil puissant qui permet de **faire des déductions et de tirer des conclusions sur une population à partir d'un échantillon de données**.")

    st.markdown("")

    st.markdown("Définissons **Population** et **Échantillon** :")

    st.markdown("")

    st.markdown("💡En statistiques inférentielles, une **population fait référence à l'ensemble du groupe d'individus (ou de points de donnée) sur lequel nous voulons faire des déductions.**.") 
    st.markdown("Dans le contexte des RH, la population peut être constituée de tous les employés d'une entreprise, d'un service spécifique, d'une fonction particulière, etc...")

    st.markdown("")
    
    st.markdown("💡**Un échantillon, en revanche, est un sous-ensemble plus petit et gérable de la population que nous sélectionnons pour analyser et tirer des conclusions**.") 
    st.markdown("Il s'agit d'un sous-ensemble représentatif d'un groupe plus large, soigneusement choisi pour garantir qu'il reflète fidèlement la population.")
    st.markdown("En RH, un échantillon peut être un groupe d'employés qui ont été sélectionnés pour une enquête, un programme de formation, une évaluation des performances, etc...")

    # Explanation
    with st.expander("📢 Illustration des notions **Population** et **Échantillon**"):
        st.write("""Disons que nous souhaitons comprendre l’ancienneté moyenne des salariés au sein d’une entreprise. La population serait constituée de tous les salariés qui travaillent pour l’entreprise, passés et présents. 
        Cependant, il n'est pas possible de collecter des données sur chaque employé, c'est pourquoi nous sélectionnons un échantillon de 100 employés issus de différents services et niveaux de responsabilités.
        En analysant les échantillons de données, nous pouvons faire des déductions sur la population, telles que l'ancienneté moyenne des employés au sein de l'entreprise, la répartition de l'ancienneté entre les différents services ou la relation entre l'ancienneté et la performance des employés.
        🚨L'échantillon doit être représentatif de la population, ce qui signifie qu'il doit refléter les caractéristiques de la population, telles que l'âge, le sexe, la fonction professionnelle et l'ancienneté. 
        Cela garantit que les conclusions que nous tirons de l’échantillon sont exactes et fiables pour la population dans son ensemble.
        """)


    st.markdown("")
    
    
    st.markdown("- **L'estimation** est le processus qui permet d'estimer un paramètre de la population sur la base d'un échantillon.")
    st.markdown("Le *paramètre* à estimer peut-être par exemple, la moyenne, la proportion, etc...")
    
    st.markdown("- **L'estimation ponctuelle** consiste à estimer une valeur unique pour un paramètre de population sur la base d'un échantillon de données.") 
    st.markdown("")
    
    st.markdown("🏀**Application 14** : Le service RH souhaite estimer le nombre moyen d'années d'expérience des employés dans leur entreprise, sur la base d'un échantillon de données.")
    st.markdown("Ci-dessous l'histogramme des données représentant les années d'expérience pour un échantillon aléatoire de 50 employés.")


    st.markdown("")
    

#Example 1: Point Estimation
# Step 1: Sample Data. We'll start by generating some sample data representing years of experience for a random sample of 50 employees.

    import numpy as np
    import plotly.express as px
    import streamlit as st
    from scipy.stats import t
    
# For reproducibility
    np.random.seed(42)  
    
# Mean: 8 years, Standard Deviation: 2 years
    sample_experience = np.random.normal(8, 2, 50) 
    
#Step 2: Calculate Point Estimate. We'll calculate the point estimate, which is simply the sample mean.
    point_estimate = np.mean(sample_experience)

#Step 3: Visualization. Let's create a histogram to visualize the distribution of years of experience in the sample and mark the point estimate on the plot.
    fig = px.histogram(sample_experience, title="Répartition des années d\'expérience dans l'échantillon")
    fig.update_layout(xaxis_title="Années d\'experience", yaxis_title="Frequence")
    fig.add_vline(x=point_estimate, line_dash="dash", line_color="red", annotation_text=f"Estimation ponctuelle: {point_estimate:.2f}", annotation_position="top left")

# Display the figure in Streamlit
    st.plotly_chart(fig)


# Explanation
    with st.expander("🔮Interpretation de l'histogramme SANS intervalle de confiance"):
        st.write("""
        Dans cet exemple, nous avons utilisé l'estimation ponctuelle pour estimer le nombre d'années d'expérience en moyenne dans l'entreprise. Notre estimation ponctuelle, basée sur un échantillon de 50 employés, est d'environ 7,55 ans (ligne rouge sur l'histogramme). 
        
        Cela signifie que nous estimons qu'en moyenne, les employés de l'entreprise ont environ 7,55 années d'expérience. Cependant, il ne s’agit que d’une valeur unique et elle ne nous fournit pas d’informations sur l’incertitude associée à cette estimation.
        """)


    st.markdown("")
    

    st.markdown("- **L'estimation par intervalle**, d'autre part, fournit une une plage de valeurs plausibles à l'intérieur de laquelle le paramètre de population est susceptible de se situer ; ainsi qu'un niveau de confiance (par exemple 95 %).") 
    st.markdown("Cette plage de valeurs plausibles est appelée **intervalle de confiance**. L'estimation par intervalles est plus informative que l'estimation ponctuelle, car elle tient compte de l'incertitude associée à l'utilisation d'un échantillon pour estimer un paramètre de population.")
    st.markdown("")

    st.markdown("🏀**Application 15** : Dans la continuité de l'exemple précédent, le service RH souhaite calculer un intervalle de confiance de 95 % pour les années d'expérience moyennes dans l'entreprise.")  
    st.markdown("Nous pouvons visualiser l'intervalle de confiance sur l'histogramme ci-dessous.")

    
    st.markdown("")

    
#Example 2: Interval Estimation
# Scenario: Continuing from the previous example, HR professionals want to calculate a 95% confidence interval for the average years of experience in the organization.

#Step 1: Calculate Confidence Interval
    
    confidence_level = 0.95
    sample_size = len(sample_experience)
    standard_error = np.std(sample_experience, ddof=1) / np.sqrt(sample_size)
    margin_of_error = t.ppf((1 + confidence_level) / 2, sample_size - 1) * standard_error
    confidence_interval = (point_estimate - margin_of_error, point_estimate + margin_of_error)

#Step 2: Visualization

    fig = px.histogram(sample_experience, title="Répartition des années d\'expérience dans l'échantillon avec intervalle de confiance à 95%")
    fig.update_layout(xaxis_title="Années d\'experience", yaxis_title="Frequence")
    fig.add_vline(x=point_estimate, line_dash="dash", line_color="red", annotation_text=f"Point Estimate: {point_estimate:.2f}", annotation_position="top left")
    fig.add_shape(
        type="line",
        x0=confidence_interval[0],
        x1=confidence_interval[1],
        y0=0,
        y1=1,
        line=dict(color="green", width=3),
        opacity=0.7,
        layer="below"
   )
    fig.add_annotation(
        x=confidence_interval[0] + 0.2,
        y=0.05,
        text=f"{confidence_level*100}% Intervalle de confiance\n({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})",
        showarrow=False,
        bgcolor="green",
        font=dict(color="white"),
   )
    
# Display the figure in Streamlit
    st.plotly_chart(fig)


# Explanation
    with st.expander("🔮Interpretation de l'histogramme AVEC intervalle de confiance"):
        st.write("""
        Dans cet exemple, nous avons utilisé l'estimation par intervalle pour calculer un intervalle de confiance de 95 % pour les années d'expérience moyennes dans l'entreprise.

        L'intervalle de confiance (surlignage vert), basé sur notre échantillon, est d'environ [7.02 ; 8.08] ans. Cela signifie que nous sommes sûrs à 95 % que le nombre moyen d'années d'expérience dans l'entreprise situe dans cette fourchette.
        """)

    # Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/GIF_Chap1B.gif')
    

if st.button("Continuer vers la suite du Chap.4 - **B/ Tests d'hypothèses**"):
    
    st.subheader("📈Chap.4-B/ Test d'hypothèse : concepts et étapes📉")
    
    st.markdown("Le test d'hypothèse est un une **méthode statistique utilisée pour tester la validité d'une affirmation ou d'une hypothèse concernant une population** sur la base d'un échantillon de données.")
    
    st.markdown("En RH, les tests d'hypothèses peuvent être utilisés pour évaluer l'efficacité des interventions, comparer différents groupes ou évaluer les relations entre les variables.")
    
    st.markdown("")
    
    st.markdown("Étapes du test d'hypothèse :")

    st.markdown("")
    
    st.markdown("a. Formuler **l\'hypothèse nulle (H0)** et **l\'hypothèse alternative (H1)**")
    
    st.markdown("b. **Choisissez un niveau de significativité (α : alpha)**, qui représente la **probabilité de rejeter** l'hypothèse nulle lorsqu'elle est vraie (seuil de rejet de l'hypothèse nulle).")
    
    st.markdown("c. **Recueillir des échantillons de données** et **calculer** la statistique de test appropriée")
    
    st.markdown("d. Déterminer la valeur critique (**p-value**) pour prendre une décision concernant l'hypothèse nulle")
    
    st.markdown("e. Comparez la statistique du test à la **p-value** et **prenez la décision d'accepter ou de rejeter** l'hypothèse nulle **H0**.")
    
    st.markdown("f. **Tirer des conclusions basées sur la décision** et interpréter les résultats")
    
    st.markdown("")
    
    st.markdown("🏀**Application 16** : Supposons qu'un contrôleur de gestion sociale souhaite déterminer s'il existe un écart de rémunération entre les 👦🏾 et 👧 dans l'entreprise (l'écart de rémunération fait partie des indicateurs qui composent **l’index de l’égalité femmes-hommes**).") 


    st.markdown("")

    
    st.markdown("- **L'hypothèse nulle (H0)** serait : **Il n'y a pas de différence significative dans les salaires moyens** entre les 👦🏾 et 👧") 
    
    st.markdown("tandis que : ")
    
    st.markdown("- **l'hypothèse alternative (H1)** serait : **Il y a une différence significative dans les salaires moyens** entre les 👦🏾 et 👧")


    st.markdown("")


if st.button("Continuer vers la suite du Chap.4 - **C/ Tests statistiques communs**"):
    

    st.markdown("")

    st.markdown("Tests statistiques courants (test t, test du chi carré, ANOVA) : ")

    st.markdown("")
    
    st.markdown("- **Test t : il est utilisé pour comparer les moyennes entre deux groupes** afin de déterminer s’il existe une différence significative entre eux.")
    
    st.markdown("En RH, **les tests t** peuvent être utilisés pour comparer les performances de deux programmes de formation différents, les niveaux de satisfaction au travail des employés de différents services ; pour évaluer s'il existe une différence significative dans les salaires moyens entre les différents postes, services ou effectifs 👦🏾 et 👧.")
                
    st.markdown("")
    
    st.markdown("🏀**Application 17** : Un contrôleur de gestion RH est chargé de mener une étude pour comparer les niveaux de satisfaction au travail dans deux services de l'hôpital communal de *Trifouilly-les-Oies* : Anesthésie & Gériatrie.")
    
    st.markdown("Les notes de satisfaction au travail des 100 agents des deux services sont consignées dans le tableau suivant : ")


    st.markdown("")


    import streamlit as st
    import pandas as pd
    import numpy as np
    import scipy.stats as stats
    import plotly.express as px

# Create sample data
    np.random.seed(42)
    data = pd.DataFrame({
         'Service': np.random.choice(['Anesthésie', 'Gériatrie'], size=100),
         'Satisfaction au travail (sur 10)': np.random.randint(1, 11, size=100)
    })

# Display the data
    st.write("Données brutes :")
    st.write(data)

# Conduct a t-test
    st.subheader("Test d'hypothèse :")
    department_a = data[data['Service'] == 'Anesthésie']['Satisfaction au travail (sur 10)']
    department_b = data[data['Service'] == 'Gériatrie']['Satisfaction au travail (sur 10)']

# Formulate the null and alternative hypotheses
    st.write("Hypothèse nulle (H0) : Il n'y a pas de différence significative dans les niveaux de satisfaction au travail entre le Service Anesthésie et le Service Gériatrie.")
    st.write("AHypothèse alternative (H1) : Il existe une différence significative dans les niveaux de satisfaction au travail entre le Service Anesthésie et le Service Gériatrie.")


# Calculate the test statistic and p-value
    t_statistic, p_value = stats.ttest_ind(department_a, department_b)

# Choose a significance level (α)
    alpha = 0.05

# Compare p-value to α
    st.write(f"Niveau de significativité (α): {alpha}")
    st.write(f"Statistique du test: {t_statistic:.3f}") # Display t_statistic with 3 decimal places
    st.write(f"P-Value: {p_value:.3f}")  # Display p-value with 3 decimal places

    if p_value < alpha:
        st.write("Résultat : Rejeter l'hypothèse nulle")
    else:
        st.write("Resultat: Ne pas rejeter l'hypothèse nulle")

# Visualize the data
    fig = px.box(data, x='Service', y='Satisfaction au travail (sur 10)', points="all")
    fig.update_layout(title="Box Plot des niveaux de satisfaction au travail dans les services Anesthésie et Gériatrie")
    st.plotly_chart(fig)


    # Explanation
    with st.expander("🔮Explication"):
        st.write("""
        Nous commençons par generer un exemple d'ensemble de données avec des notes de satisfaction au travail pour deux services (Anesthésie et Gériatrie).

        Nous formulons les hypothèses nulles et alternatives.

        Nous calculons la statistique t et la p-value à l'aide de stats.ttest_ind (scipy.stats) pour comparer les niveaux de satisfaction au travail dans les deux services.
        
        Nous choisissons un niveau de significativité (α) de 0,05.

        Nous comparons la p-value à α pour décider d'accepter ou de rejeter l'hypothèse nulle. 
        
        Enfin, nous visualisons les données à l'aide d'un box plot.
        """)


    st.markdown("")


    st.markdown("")

    
    st.markdown("- **Test du chi carré (Test du χ²) : ce test est utilisé pour déterminer s'il existe une association significative entre deux variables catégorielles**.") 

    st.markdown("En RH, les tests du chi carré peuvent être utilisés pour évaluer la relation entre les données démographiques des employés (par exemple, le sexe, l'âge) et divers résultats, tels que le taux de promotion, le taux de turnover, etc...")

    st.markdown("")
    
    st.markdown("🏀**Application 18** : Le contrôleur de gestion sociale de la communauté de communes de *Teuf-les-Bretagne* doit rendre son rapport sur l'évaluation de la relation entre le genre (H/F) et les taux de promotion au sein de l'administration.") 
    st.markdown("Les données recueillies pour 200 agents (H/F) cat.B sont consignées dans le tableau ci-après : ")

    import streamlit as st
    import pandas as pd
    import numpy as np
    import scipy.stats as stats
    import plotly.express as px

# Create sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'Genre': np.random.choice(['Homme', 'Femme'], size=200),
        'Promotion': np.random.choice(['Promu', 'Non Promu'], size=200)
    })

# Display the data
    st.write("Données brutes:")
    st.write(data)

# Create a contingency table
    contingency_table = pd.crosstab(data['Genre'], data['Promotion'])

# Conduct a chi-square test
    st.subheader("Test d'hypothèse:")
    st.write("Hypothèse nulle (H0) : Il n'y a pas d'association significative entre le genre et les taux de promotion.")
    st.write("Hypothèse alternative (H1) : Il existe une association significative entre le genre et les taux de promotion.")

# Calculate the chi-square statistic and p-value
    chi2, p_value, _, _ = stats.chi2_contingency(contingency_table)

# Choose a significance level (α)
    alpha = 0.05

# Compare p-value to α
    st.write(f"Niveau de significativité (α): {alpha}")
    st.write(f"Statistique du chi carré: {chi2:.3f}")  # Display chi-square statistic with 3 decimal places}")
    st.write(f"P-Value: {p_value:.3f}")  # Display p-value with 3 decimal places}")

    if p_value < alpha:
        st.write("Résultat : Rejeter l'hypothèse nulle")
    else:
        st.write("Résultat : On ne peut pas rejeter l'hypothèse nulle")

# Visualize the contingency table
    st.subheader("Table de contingence:")
    st.write(contingency_table)

# Visualize the association between gender and promotion
    fig = px.bar(data, x='Genre', color='Promotion', barmode='group')
    fig.update_layout(title="Relation entre le Genre et les taux de Promotion")
    st.plotly_chart(fig)


     # Explanation
    with st.expander("🔮Explication"):
        st.write("""
        Nous commençons par generer un exemple d'ensemble de données avec deux variables catégorielles : le genre (H/F) et la promotion.

        Nous formulons les hypothèses nulles et alternatives.

        Nous créons un tableau de contingence pour résumer les données et calculer les fréquences observées.

        Nous calculons la statistique du chi carré et la p-value à l'aide de stats.chi2_contingency (scipy.stats) pour évaluer l'association entre le genre et la promotion.
        
        Nous choisissons un niveau de significativité (α) de 0,05.

        Nous comparons la p-value à α pour décider d'accepter ou de rejeter l'hypothèse nulle. 
        
        Enfin, nous visualisons le tableau de contingence et la relation entre le sexe et les taux de promotion à l'aide d'un graphique à barres groupées.
        """)

    
    st.markdown("")

    
    st.markdown("")
    
    st.markdown("- **ANOVA (Analyse de la Variance) : L'ANOVA est utilisée pour comparer les moyennes entre trois groupes ou plus** afin de déterminer s'il existe une différence significative entre eux.") 
    
    st.markdown("En RH, l'ANOVA peut être utilisée pour analyser s'il existe des différences significatives dans la comparaison de l'absentéisme moyen entre les employés de différents services, à différentes catégories de postes, ou à différents niveaux d'expérience.") 
    st.markdown("Ou encore pour comparer l'efficacité de différentes initiatives pour améliorer l'engagement des employés, ou comparer les performances des employés dans plusieurs services, etc... ") 
    
    st.markdown("")
    
    st.markdown("")


    st.markdown("🏀**Application 19** : La Mairie de *Mont-Crack-en-Parisis* souhaite développer des stratégies ciblées pour améliorer l'engagement et le climat social des équipes. Elle demande à son contrôleur de gestion RH de rechercher s'il existe des différences significatives dans les heures d'absences des agents des différents groupes d'âge (par exemple, 20-30, 31-40, 41-50, 51+).") 
    st.markdown("Cette analyse pourra soutenir des stratégies ciblées pour améliorer l'engagement et le climat social en fonction des différentes tranches d'âge.")

    import streamlit as st
    import pandas as pd
    import numpy as np
    import scipy.stats as stats
    import plotly.express as px

# Create sample data
    np.random.seed(42)

# Generate hours of absence for different age groups
    age_20_30 = np.random.normal(8, 2, 50)
    age_31_40 = np.random.normal(10, 2, 50)
    age_41_50 = np.random.normal(12, 2, 50)
    age_51_plus = np.random.normal(15, 2, 50)

    data = pd.DataFrame({
         'Groupe_Age': np.repeat(['20-30', '31-40', '41-50', '51+'], 50),
         'Heures_Absences': np.concatenate([age_20_30, age_31_40, age_41_50, age_51_plus])
    })

# Format the 'Heures_Absences' column to display only two digits after the decimal point
    data['Heures_Absences'] = data['Heures_Absences'].round(2)

# Display the data
    st.write("Sample Data:")
    st.write(data)

# Conduct one-way ANOVA
    st.subheader("Test d'hypothèse:")
    st.write("Hypothèse nulle (H0) : Il n'y a pas de différence significative dans les heures d'absence entre les différents groupes d'âge.")
    st.write("Hypothèse alternative (H1) : Il existe une différence significative dans les heures d'absence selon les différents groupes d'âge.")

# Perform one-way ANOVA
    f_statistic, p_value = stats.f_oneway(age_20_30, age_31_40, age_41_50, age_51_plus)

# Choose a significance level (α)
    alpha = 0.05

# Compare p-value to α
    st.write(f"Niveau de significativité (α) :{alpha}")
    st.write(f"Statistique F : {f_statistic:.3f}")  # Display F-statistic with 3 decimal places
    st.write(f"P-Value: {p_value:.3f}")  # Display p-value with 3 decimal places

    if p_value < alpha:
        st.write("Résultat : Rejeter l'hypothèse nulle")
    else:
        st.write("Result: Résultat : ne pas rejeter l'hypothèse nulle")

# Visualize the data
    fig = px.box(data, x='Groupe_Age', y='Heures_Absences')
    fig.update_layout(title="Heures d'absence selon les groupes d'âge")
    st.plotly_chart(fig)


    # Explanation
    with st.expander("🔮Explication"):
        st.write("""
        Nous commençons par generer un exemple d'ensemble de données avec des heures d'absence pour les agents de différentes tranches d'âge (20-30, 31-40, 41-50, 51+).

        Nous formulons les hypothèses nulles et alternatives pour tester s'il existe des différences significatives dans les heures d'absence entre ces groupes d'âge..

        Nous effectuons une ANOVA unidirectionnelle pour comparer les moyennes d'heures d'absence selon les groupes d'âge.

        Nous choisissons un niveau de significativité (α) de 0,05 et comparons la p-value à α pour prendre une décision concernant l'hypothèse nulle.
        
        nfin, nous visualisons les données à l'aide d'un diagramme en boîte pour aider à interpréter les différences d'heures d'absence selon les groupes d'âge.
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
    redirect_button("https://cours-stats-rh.streamlit.app/Quiz_4_-_Statistiques_inférentielles📉","Quiz du chapitre 4")
    
 

    
