


import streamlit as st

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


    st.markdown("")
    

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

    st.markdown("Tests statistiques courants (test t, test du chi carré, ANOVA) : ")
    
    st.markdown("- **Test t : il est utilisé pour comparer les moyennes entre deux groupes**. En RH, il peut être utilisé pour évaluer s'il existe une différence significative dans les salaires moyens entre les différents postes, services ou effectifs 👦🏾 et 👧.")
    st.markdown("")
    
    st.markdown("🏀**Application 17** : Un contrôleur de gestion sociale peut aussi effectuer un **test t** pour déterminer s'il existe une différence significative dans les notes de performance moyennes entre les employés qui ont suivi un programme de formation interne et ceux qui ne l'ont pas fait.")


    st.markdown("")

    
    st.markdown("- **Test du chi carré (Test du χ²) : ce test est utilisé pour déterminer s'il existe une association entre deux variables catégorielles**.") 
    st.markdown("")
    
    st.markdown("🏀**Application 18** : Un contrôleur de gestion sociale peut utiliser le **test du χ²** pour examiner s'il existe une relation significative entre les niveaux de satisfaction des employés (variable catégorielle) et leur engagement dans des programmes de développement professionnel (une autre variable catégorielle).") 


    st.markdown("")

    
    st.markdown("Grâce au résultat du test, le contrôleur de gestion sociale pourra aider les autres professionnels RH à comprendre s'il existe un lien entre ces variables, et à décider si des interventions ciblées sont nécessaires pour améliorer la satisfaction des employés.")
    
    st.markdown("- **ANOVA (Analyse de la Variance): L'ANOVA est utilisée pour comparer les moyennes entre trois groupes ou plus**. En RH, elle peut être utilisée pour analyser s'il existe des différences significatives dans la comparaison de l'absentéisme moyen entre les employés de différents services, à différentes catégories de postes, ou à différents niveaux d'expérience.")
    st.markdown("")
    
    st.markdown("🏀**Application 19** : Un contrôleur de gestion sociale peut utiliser **l'ANOVA** pour rechercher s'il existe des variations significatives dans les heures d'absences des employés entre les différents groupes d'âge (par exemple, 20-30, 31-40, 41-50, 51+). Cette analyse peut donner un aperçu de la nécessité de stratégies ciblées pour améliorer l'engagement et le climat social en fonction des différentes tranches d'âge.")

    
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
    
 

    
