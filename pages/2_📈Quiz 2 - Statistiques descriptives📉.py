



import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Quiz du chapitre 2")
st.sidebar.markdown("# Quiz du chapitre 2")
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/analyze_this.gif')

st.title("Statistiques descriptives")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours de **Statistiques descriptives**.")

st.markdown("Cocher les bonnes réponses.")

st.header("A/ Mesures de tendance centrale")

st.subheader("1/ Laquelle des mesures de tendance centrale suivantes est la plus couramment utilisée pour résumer des montants de salaires ?")

check = st.checkbox("a) Mode", key="check1")
if check:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_2 = st.checkbox("b) Médiane", key="check2")
if check_2:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_3 = st.checkbox("c) Moyenne géométrique", key="check3")
if check_3:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_4 = st.checkbox("d) Moyenne arithmétique", key="check4")
if check_4:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
    

st.subheader("2/ Quelle mesure de tendance centrale est la plus appropriée à utiliser lorsque les données incluent des valeurs aberrantes fortement asymétriques")

check_5 = st.checkbox("a) Mode", key="check5")
if check_5:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_6 = st.checkbox("b) Médiane", key="check6")
if check_6:
    st.write("👏🏾**Bonne réponse !** 👍🏾")
    
check_7 = st.checkbox("c) Moyenne arithmétique", key="check7")
if check_7:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")
    
check_8 = st.checkbox("d) Moyenne géométrique", key="check8")
if check_8:
    st.write("💩💩pfff... **mauvaise réponse**🤪🤪")



########################################################################################################


st.header("B/ Mesures de la variabilité")

st.subheader("1/ Quelle est la formule pour calculer la variance d'un échantillon ?")

check_9 = st.checkbox("a) somme des écarts à la moyenne / taille de l'échantillon")

if check_9:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_10 = st.checkbox("b) somme des carrés des écarts à la moyenne / taille de l'échantillon")

if check_10:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_11 = st.checkbox("c) somme des carrés des écarts à la moyenne / (taille de l'échantillon - 1) ")

if check_11:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_12 = st.checkbox("d) somme des écarts à la moyenne / (taille de l'échantillon taille - 1)")

if check_12:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


st.subheader("2/ Quelle mesure de variabilité peut être utilisée pour synthétiser des données salariales ?")

check_13 = st.checkbox("a) Écart-type")

if check_13:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_14 = st.checkbox("b) Variance")

if check_14:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_15 = st.checkbox("c) Étendue")

if check_15:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_16 = st.checkbox("d) Coefficient de variation")

if check_16:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


########################################################################################################


st.header("C/ Techniques graphiques")

st.subheader("1/ Quel type de graphique serait le plus approprié pour afficher la répartition des salaires dans une entreprise ?")

check_17 = st.checkbox("a) Graphique à barres")

if check_17:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_18 = st.checkbox("b) Graphique linéaire")

if check_18:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_19 = st.checkbox("c) Graphique circulaire")

if check_19:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_20 = st.checkbox("d) Histogramme")

if check_20:
   st.write("👏🏾**Bonne réponse !** 👍🏾")


st.subheader("2/ Lequel des éléments suivants serait le moins utile pour afficher les données d'une manière qui permette une comparaison facile entre plusieurs groupes ou catégories ?")

check_21 = st.checkbox("a) Boîte à moustaches")

if check_21:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_22 = st.checkbox("a) Graphique à barres empilées")

if check_22:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_23 = st.checkbox("b) Nuage de points")

if check_23:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_24 = st.checkbox("c) Carte thermique")

if check_24:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_25 = st.checkbox("d) Analyse de régression")

if check_25:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


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
redirect_button("https://cours-stats-rh.streamlit.app/Chapitre_3_🔖_Introduction_aux_probabilités_et_distributions","Aller au chapitre 3")




