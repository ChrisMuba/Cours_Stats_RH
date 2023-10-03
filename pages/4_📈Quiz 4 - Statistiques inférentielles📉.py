



import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Quiz du chapitre 4")
st.sidebar.markdown("# Quiz du chapitre 4")
# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
   
st.title("Statistiques inférentielles")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours de **statistiques inférentielles**.")

st.markdown("Cocher les bonnes réponses.")

st.header("A/ Estimation ponctuelle et d'intervalle")

st.subheader("1/ Quel est le but de l'estimation en statistiques inférentielles ?")

check = st.checkbox("a) Calculer la moyenne de l'échantillon")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Estimer le paramètre de la population sur la base d'un échantillon")

if check_2:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_3 = st.checkbox("c) Déterminer l'intervalle de confiance")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) Effectuer des tests d'hypothèse")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


st.subheader("2/ Laquelle des affirmations suivantes est vraie concernant l'estimation d'intervalle ?")

check = st.checkbox("a) Elle fournit une estimation de valeur unique du paramètre de population")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Elle aide à déterminer le niveau de significativité")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Elle fournit une gamme de valeurs plausibles pour le paramètre de population")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Elle est utilisée pour calculer la valeur p")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


########################################################################################################


st.header("B/ Test d'hypothèse (concepts et étapes)")

st.subheader("1/  Quel est le but des tests d'hypothèses en statistiques inférentielles ?")

check = st.checkbox("a) Estimer le paramètre de population")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Calculer la moyenne de l'échantillon")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Tirer des conclusions sur une population à partir de données d'échantillon")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Déterminer l'intervalle de confiance")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


st.subheader("2/ Quelle est la première étape du test d'hypothèse ?")

check = st.checkbox("a) Collecte d'échantillons de données")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Définition du niveau de signification souhaité")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Énoncer les hypothèses nulle et alternative")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Calcul de la statistique de test appropriée")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


########################################################################################################


st.header("C/ Tests courants (test t, test du chi carré, ANOVA)")

st.subheader("1/  Quand un **test t** peut-il être utilisé en RH ?")

check = st.checkbox("a) Pour comparer les moyennes entre deux groupes")

if check:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_2 = st.checkbox("b) Pour déterminer l'association entre deux variables catégorielles")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Pour comparer les moyennes entre trois groupes ou plus")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) Pour analyser la relation entre les variables continues")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


st.subheader("2/  Quel test peut-être utilisé pour examiner l'association entre deux variables catégorielles en RH ?")

check_3 = st.checkbox("c) Comparer les moyennes entre trois groupes ou plus")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check = st.checkbox("a) Test t")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) ANOVA")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Test du chi carré")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Analyse de régression")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


st.subheader("3/ En RH, l'ANOVA peut-être utilisée pour :")


check = st.checkbox("a) Comparer les moyennes entre trois groupes ou plus")

if check:
  st.write("👏🏾**Bonne réponse !** 👍🏾")


check_2 = st.checkbox("b) Comparer les moyennes entre deux groupes")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


check_3 = st.checkbox("c) Estimer le paramètre de la population")

if check_3:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) Déterminer l'association entre deux variables catégorielles")

if check_4:
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
redirect_button("https://cours-stats-rh.streamlit.app/Chapitre_5_🔖_Correlation_et_Regression","Aller au chapitre 5")


