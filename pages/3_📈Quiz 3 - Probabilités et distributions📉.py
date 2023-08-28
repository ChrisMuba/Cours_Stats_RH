



import streamlit as st

st.markdown("# Quiz du chapitre 3")
st.sidebar.markdown("# Quiz du chapitre 3")

st.title("Probabilités et distributions")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours d'**introduction aux probabilités et distributions**.")

st.markdown("Cocher les bonnes réponses.")

st.header("A/ Concepts de base en **probabilités**")

st.subheader("1/ Que représente l'espace d'échantillonnage dans le contexte de l'analyse de données RH ?")

check = st.checkbox("a) L'ensemble de tous les résultats possibles d'une expérience RH")

if check:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_2 = st.checkbox("b) La moyenne de tous les indicateurs RH d'une entreprise")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) La plage de valeurs pour une variable RH")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) Le nombre d'employés dans un service RH")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


st.subheader("2/ À quoi peut servir le calcul des probabilités en analytique RH ?")

check = st.checkbox("a) À identifier les domaines potentiels d'amélioration dans les processus RH")

if check:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_2 = st.checkbox("b) À déterminer la valeur moyenne d'une métrique RH")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) À prédire les performances futures des salariés")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) À établir l'erreur maximale tolérée dans les données RH")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


########################################################################################################


st.header("B/ Distributions de probabilité discrète")

st.subheader("1/ Dans un pool de candidats, quelle distribution de probabilité convient pour modéliser le nombre de candidats retenus pour un emploi ?")

check = st.checkbox("a) Distribution normale")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Loi de Poisson")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Distribution binomiale")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Distribution exponentielle")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


st.subheader("2/ Quels sont les paramètres qui caractérisent une distribution binomiale dans le contexte de l'analytique RH ?")

check = st.checkbox("a) Moyenne et écart type")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Médiane et mode")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Nombre de candidats à l'emploi et taux d'embauche")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Type et niveau des qualifications des candidats à un emploi")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


########################################################################################################


st.header("C/ Distributions de probabilité continue")
st.subheader("1/ Quelle distribution de probabilité peut être utilisée pour analyser les notes de performance des employés ?")

check = st.checkbox("a) Distribution binomiale", key="checkbox_1")
if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Loi de Poisson", key="checkbox_2")
if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Distribution exponentielle", key="checkbox_3")
if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) Distribution normale", key="checkbox_4")
if check_4:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

st.subheader("2/ En Analytique RH, quels paramètres définissent la distribution normale lors de l'analyse des notes de performance des employés ?")

check_5 = st.checkbox("a) Médiane et mode", key="checkbox_5")
if check_5:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_6 = st.checkbox("b) Asymétrie et aplatissement", key="checkbox_6")
if check_6:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_7 = st.checkbox("c) Moyenne et écart type", key="checkbox_7")
if check_7:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_8 = st.checkbox("d) Variance et intervalle des notes de performance", key="checkbox_8")
if check_8:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")



