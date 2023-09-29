#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

st.title("Cours de Statistiques :blue[appliquées aux Ressources Humaines]")

st.subheader("Formateur : Christian MUBA - Data Analyst RH")

st.caption("*Master Sciences (UB Dijon)*")

st.caption("*Master Gestion (IAE Dijon)*")

st.caption("Vous souhaitez faire analyser vos data RH, prendre des décisions éclairées ou bénéficier d'un tutorat personnalisé ? contactez-moi 📧https://www.linkedin.com/in/chris-muba-io 🌍")

st.subheader("Description du cours")

st.markdown("Ce cours offre une introduction aux statistiques pour les professionnels des ressources humaines. L'accent est mis sur la compréhension de la façon d'analyser et d'interpréter les données statistiques pour prendre des décisions éclairées. Les sujets couverts comprennent la collecte de données, les mesures de la tendance centrale et de la variabilité, la probabilité, les tests d'hypothèses, la corrélation et la régression.")

st.subheader("🚀Objectifs d'apprentissage🚀")

st.markdown("A la fin de ce cours, les étudiants seront capables de :")

st.markdown("🎯Comprendre comment les données statistiques peuvent éclairer les décisions liées aux RH")
st.markdown("🎯Recueillir, résumer et analyser des données à l'aide de statistiques descriptives")
st.markdown("🎯Interpréter les données à l'aide de techniques statistiques inférentielles")
st.markdown("🎯Évaluer la validité des conclusions statistiques basées sur des données d'échantillon")
st.markdown("🎯Appliquer des techniques statistiques aux problèmes liés aux RH")


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




