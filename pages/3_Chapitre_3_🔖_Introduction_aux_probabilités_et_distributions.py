


import streamlit as st

st.markdown("# Chapitre 3")
st.sidebar.markdown("# Chapitre 3")

st.title("Introductions aux probabilités et distributions")

st.markdown("Ce chapitre sert d'**introduction** en fournissant un **aperçu des concepts de base en probabilités et distributions, et leurs applications possibles dans le domaine des RH**.")

st.markdown("La **probabilité** est la branche des mathématiques qui **quantifie la possibilité qu'un événement se produise**.")

if st.button("Cliquez pour acceder au Chap.3 - **A/ Concepts de clés**"):
    
    st.subheader("📈Chap.3-A/ Concepts de clés📉")
    
    st.markdown("**Les concepts clés en probabilités comprennent les notions suivantes** :")
    
    st.markdown("- **Espace d'échantillonnage et événements** : l'espace d'échantillonnage **représente l'ensemble de tous les résultats possibles d'une expérience**. Les **événements sont des sous-ensembles** de l'espace d'échantillonnage, représentant des résultats spécifiques ou des combinaisons de résultats.")
    
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
    

    
    
    
    

            