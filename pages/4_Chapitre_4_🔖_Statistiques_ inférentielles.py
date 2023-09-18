


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
    with st.expander("💡illustration des notions **Population** et **Échantillon**"):
        st.write("""Disons que nous souhaitons comprendre l’ancienneté moyenne des salariés au sein d’une entreprise. La population serait constituée de tous les salariés qui travaillent pour l’entreprise, passés et présents. 
        Cependant, il n'est pas possible de collecter des données sur chaque employé, c'est pourquoi nous sélectionnons un échantillon de 100 employés issus de différents services et niveaux de responsabilités.

        En analysant les échantillons de données, nous pouvons faire des déductions sur la population, telles que l'ancienneté moyenne des employés au sein de l'entreprise, la répartition de l'ancienneté entre les différents services ou la relation entre l'ancienneté et la performance des employés.

        📢L'échantillon doit être représentatif de la population, ce qui signifie qu'il doit refléter les caractéristiques de la population, telles que l'âge, le sexe, la fonction professionnelle et l'ancienneté. 
        Cela garantit que les conclusions que nous tirons de l’échantillon sont exactes et fiables pour la population dans son ensemble.
        """)


    st.markdown("")
    
    
    st.markdown("- **L'estimation** est le processus qui permet d'estimer un paramètre de la population sur la base d'un échantillon.")
    st.markdown("Le paramètre à estimer peut-être par exemple, la moyenne, la proportion, etc...")
    
    st.markdown("- **L'estimation ponctuelle** consiste à utiliser une seule valeur pour estimer le paramètre de la population. Par exemple, si nous voulons estimer le salaire moyen d'une population, nous pouvons calculer le salaire moyen des employés d'une entreprise (échantillon) et l'utiliser comme estimation de la moyenne de la population (la population peut être toutes les entreprises de la branche d'activité).")
    
    st.markdown("- **Exemple 4 - Application possible en RH** : Supposons que nous sélectionnions au hasard 100 employés d'une grande entreprise et constations que leur salaire moyen est de 50 000 €. Nous pouvons utiliser cette moyenne d'échantillon comme estimation ponctuelle du salaire moyen de la population.")
    
    st.markdown("- **L'estimation par intervalle**, d'autre part, fournit une gamme de valeurs plausibles pour le paramètre de population. Cette plage est appelée **intervalle de confiance**. **Les intervalles de confiance** nous **aident à comprendre l'incertitude associée à notre estimation**.")
                
    st.markdown("- **Exemple 4 - Application possible en RH** : En utilisant le même exemple que ci-dessus, si nous calculons un intervalle de confiance à 95 % pour le salaire moyen et que nous trouvons qu'il est de 48 000 € à 52 000 €, cela signifie que nous sommes sûrs à 95 % que le salaire moyen réel de la population se situe dans cette fourchette.")           


if st.button("Continuer vers la suite du Chap.4 - **B/ Tests d'hypothèses**"):
    
    st.subheader("📈Chap.4-B/ Tests d'hypothèses📉")
    
    st.markdown("Le test d'hypothèse est un **cadre permettant de prendre des décisions** ou de **tirer des conclusions** sur une population **sur la base de données** d'échantillon. Il s'agit de mettre en place une **hypothèse nulle (H0)** et une **hypothèse alternative (H1)**.") 
    
    st.markdown("**L'hypothèse nulle** représente le statut quo : **c'est l'hypothèse que nous voulons tester**, tandis que **l'hypothèse alternative suggère une explication ou un effet alternatif**.")
    
    st.markdown("Étapes du test d'hypothèse :")
    
    st.markdown("a. **Énoncez les hypothèses nulle** et **alternative**")
    
    st.markdown("b. **Définissez le niveau de signification souhaité** (α : alpha) **qui détermine le seuil de rejet** de l'hypothèse nulle")
    
    st.markdown("c. **Recueillir des échantillons de données** et **calculer** la statistique de test appropriée")
    
    st.markdown("d. **Déterminez la région critique ou la région de rejet** en fonction de la statistique de test et de l'alpha")
    
    st.markdown("e. **Comparez la statistique de test à la région critique** et **décidez de rejeter ou non** l'hypothèse nulle")
    
    st.markdown("f. **Tirer des conclusions basées sur la décision et interpréter les résultats**")
    
    st.markdown("- **Exemple 4 - Application possible en RH** : Supposons qu'un contrôleur de gestion sociale souhaite déterminer s'il existe un écart de rémunération entre les 👦🏾 et 👧 dans l'entreprise (l'écart de rémunération fait partie des indicateurs qui composent **l’index de l’égalité femmes-hommes**).") 
    
    st.markdown("- **L'hypothèse nulle (H0)** serait : **Il n'y a pas de différence significative dans les salaires moyens** entre les 👦🏾 et 👧") 
    
    st.markdown("tandis que : ")
    
    st.markdown("- **l'hypothèse alternative (H1)** serait : **Il y a une différence significative dans les salaires moyens** entre les 👦🏾 et 👧")

if st.button("Continuer vers la suite du Chap.4 - **C/ Tests statistiques communs**"):
    
    st.markdown("- **Test t : il est utilisé pour comparer les moyennes entre deux groupes**. En RH, il peut être utilisé pour évaluer s'il existe une différence significative dans les salaires moyens entre les différents postes, services ou effectifs 👦🏾 et 👧.")

    st.markdown("- **Exemple 4 - Application possible en RH** : Un contrôleur de gestion sociale peut aussi effectuer un **test t** pour déterminer s'il existe une différence significative dans les notes de performance moyennes entre les employés qui ont suivi un programme de formation interne et ceux qui ne l'ont pas fait.")
    
    st.markdown("- **Test du chi carré (Test du χ²) : ce test est utilisé pour déterminer s'il existe une association entre deux variables catégorielles**.") 
    
    st.markdown("- **Exemple 4 - Application possible en RH** : Un contrôleur de gestion sociale peut utiliser le **test du χ²** pour examiner s'il existe une relation significative entre les niveaux de satisfaction des employés (variable catégorielle) et leur engagement dans des programmes de développement professionnel (une autre variable catégorielle).") 
    
    st.markdown("Grâce au résultat du test, le contrôleur de gestion sociale pourra aider les autres professionnels RH à comprendre s'il existe un lien entre ces variables, et à décider si des interventions ciblées sont nécessaires pour améliorer la satisfaction des employés.")
    
    st.markdown("- **ANOVA (Analyse de la Variance): L'ANOVA est utilisée pour comparer les moyennes entre trois groupes ou plus**. En RH, elle peut être utilisée pour analyser s'il existe des différences significatives dans la comparaison de l'absentéisme moyen entre les employés de différents services, à différentes catégories de postes, ou à différents niveaux d'expérience.")
    
    st.markdown("- **Exemple 4 - Application possible en RH** : Un contrôleur de gestion sociale peut utiliser **l'ANOVA** pour rechercher s'il existe des variations significatives dans les heures d'absences des employés entre les différents groupes d'âge (par exemple, 20-30, 31-40, 41-50, 51+). Cette analyse peut donner un aperçu de la nécessité de stratégies ciblées pour améliorer l'engagement et le climat social en fonction des différentes tranches d'âge.")
    
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
    
 

    
