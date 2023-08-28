



import streamlit as st

st.markdown("# Quiz du chapitre 5")
st.sidebar.markdown("# Quiz du chapitre 5")

st.title("Correlation et Regression")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours de **correlation et regression**.")

st.markdown("Cocher les bonnes réponses.")


##########


st.header("A/ Analyse de corrélation")

st.subheader("1/ Que détermine l'analyse de corrélation ?")

check = st.checkbox("a) Causalité entre les variables")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Intensité et sens de la relation entre les variables")

if check_2:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_3 = st.checkbox("c) La différence entre les variables indépendantes et dépendantes")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) Signification statistique des variables")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


############


st.subheader("2/ Deux variables présentent une corrélation positive lorsque :")

check = st.checkbox("a) Elles évoluent dans des directions opposées")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Elles ont une relation faible")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Les changements d'une variable sont associés aux changements de l'autre dans la même direction")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Elles ont un coefficient de corrélation proche de **-1**")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


###########


st.subheader("3/ Si le coefficient de corrélation est proche de 0, cela suggère :")

check = st.checkbox("a) Une forte corrélation positive")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Une forte corrélation négative")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Aucune relation perceptible entre les variables")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Une relation linéaire entre les variables")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


########################################################################################################


st.header("B/ Régression linéaire simple")

st.subheader("1/ À quoi sert la régression linéaire simple ?")

check = st.checkbox("a) À déterminer la causalité entre les variables")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) À estimer la ligne la mieux ajustée qui minimise la différence entre les données observées et les valeurs prédites")

if check_2:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_3 = st.checkbox("c) À prédire plusieurs variables dépendantes")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) À examiner la relation entre plusieurs variables indépendantes")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


##########


st.subheader("2/ En RH, la régression linéaire simple peut être utilisée pour prédire ?")

check = st.checkbox("a) Le sens de la relation entre les variables")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) La force de la relation entre les variables")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) La performance des employés basée sur une seule variable indépendante")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Plusieurs variables indépendantes basées sur une seule variable dépendante")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


##########


st.subheader("3/ Quelle hypothèse la régression linéaire simple fait-elle ?")

check = st.checkbox("a) La relation entre les variables est non linéaire")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Il n'y a pas de relation entre les variables")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Il existe une relation linéaire entre les variables")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Le coefficient de corrélation est proche de 1")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


########################################################################################################


st.header("C/ Régression multiple")

st.subheader("1/ En quoi la régression multiple diffère-t-elle de la régression linéaire simple ?")

check = st.checkbox("a) La régression multiple ne considère qu'une seule variable indépendante")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Prise en compte de plusieurs régressions pour plusieurs variables indépendantes")

if check_2:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_3 = st.checkbox("c) La régression multiple ne peut prédire que des résultats binaires")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) La régression multiple ne peut pas être utilisée dans les études RH")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


##########


st.subheader("2/ En RH, la régression multiple peut être utilisée pour prédire : ?")

check = st.checkbox("a) Le turnover du personnel basé sur de multiples facteurs")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) La force de la corrélation entre les variables")

if check_2:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_3 = st.checkbox("c) La performance des employés basée sur un seul facteur")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d)Le sens de la relation entre les variables")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


##########


st.subheader("3/ le chargé d'études RH peut utiliser la regression multiple pour :")


check = st.checkbox("a) Déterminer la causalité entre les variables")

if check:
  st.write("👏🏾**Bonne réponse !** 👍🏾")


check_2 = st.checkbox("b) Prédire les résultats en fonction de plusieurs variables indépendantes")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


check_3 = st.checkbox("c) Identifier le coefficient de corrélation entre les variables")

if check_3:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) Évaluer la significativité d'une seule variable")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


