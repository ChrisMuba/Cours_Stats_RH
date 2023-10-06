#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.title("Cours de Statistiques :blue[appliquées aux Ressources Humaines]")

st.subheader("Formateur : Christian MUBA.")

st.caption("*Ancien coordinateur apprentissage CFA académique / Académie de Dijon*")

st.caption("*Diplômé des Master Gestion & Master Sciences (IAE Dijon & UB Dijon)*")

st.caption("Vous souhaitez faire analyser vos data RH ? Parlons-en 👉🏾 https://www.linkedin.com/in/chris-muba-io 🌐")

# Explanation
with st.expander("✨:blue[Pourquoi ce cours ?]✨"):
    st.write("""
    Êtes-vous un professionnel RH cherchant à exploiter la puissance de l’analyse des données pour une meilleure prise de décision ? 
    
    Vous avez du mal à trouver des ressources pédagogiques adaptées au contexte RH ?

    *Bienvenue dans notre cours sur mesure en Statistiques appliquées aux RH !*

    📢:blue[**Conçu sur mesure pour les professionnels des RH**] : nous comprenons les défis uniques auxquels les RH sont confrontés en matière d'analyse de données. Bien qu'il existe de nombreux cours de statistiques en ligne, ils sont souvent trop généraux ou déconnectés du contexte RH. 
    Notre cours est conçu spécifiquement en pensant aux profils RH, vous garantissant d'acquérir les connaissances dont vous avez besoin sans complexité inutile.

    📢:blue[**Libérez le potentiel de vos données**] : avec notre cours, vous n'aurez pas à vous battre avec des formules mathématiques abstraites ou des exercices scientifiques sans rapport. Nous comblons le fossé entre les statistiques et les RH, rendant l'analyse des données accessible, pertinente et pratique pour vos tâches RH quotidiennes.

    📢:blue[**Prenez des décisions éclairées**] : ne vous fiez pas uniquement à votre intuition. Apprenez à fonder vos décisions RH sur des informations solides basées sur des données. Notre cours couvre tout, des statistiques descriptives aux statistiques inférentielles, en passant par les probabilités, les distributions, la corrélation et la régression. :blue[**Mais ce qui nous distingue, c'est que nous proposons des exemples d'applications en RH pour chaque sujet, garantissant ainsi que vous puissiez immédiatement appliquer vos nouvelles compétences à votre travail**]. 

    Notre cours est conçu pour être convivial, avec des exercices commentés et des quiz pour vous aider à renforcer votre compréhension des concepts statistiques utiles dans votre travail ! 
    

    Ne laissez pas l’analyse des données devenir un défi de taille. Dotez-vous des compétences nécessaires pour prendre des décisions RH éclairées qui profitent à votre organisation.
    

    **Prêt à vous lancer dans votre voyage vers l’excellence RH basée sur les données ?** :blue[Commencez le cours maintenant et améliorez vos compétences en analyse de données RH !]
    """)

st.subheader("Description du cours")

st.markdown("Ce cours offre une introduction aux statistiques pour les professionnels des ressources humaines. L'accent est mis sur la compréhension de la façon d'analyser et d'interpréter les données statistiques pour prendre des décisions éclairées. Les sujets couverts comprennent la collecte de données, les mesures de la tendance centrale et de la variabilité, la probabilité, les tests d'hypothèses, la corrélation et la régression.")

st.subheader("🚀Objectifs d'apprentissage🚀")

st.markdown("A la fin de ce cours, vous serez capable de :")

st.markdown("🎯Analyser des données RH à l'aide de statistiques descriptives et de techniques de visualisation")
st.markdown("🎯Saisir les bases de la probabilité et des distributions")
st.markdown("🎯Appliquer des statistiques inférentielles pour tirer des conclusions à partir de données RH")
st.markdown("🎯Utiliser la corrélation et régression pour identifier les tendances et modèles dans vos données RH")

with st.sidebar:
    st.image('GIF/GIF_loading_data.gif')


st.markdown("")


st.markdown("")


# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")


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
redirect_button("https://cours-stats-rh.streamlit.app/Chapitre_1_🔖_Introduction_aux_statistiques","Aller au chapitre 1")



# In[ ]:





# In[ ]:




