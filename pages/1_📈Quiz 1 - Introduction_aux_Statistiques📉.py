



import streamlit as st

st.sidebar.success("Cliquez sur un :blue[chapitre] ou un :blue[quiz]")

st.markdown("# Quiz du chapitre 1")
st.sidebar.markdown("# Quiz du chapitre 1")

# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")
with st.sidebar:
        st.image('GIF/analyze_this.gif')

st.title("Introduction aux statistiques")

st.markdown("Ces questions visent à évaluer la compréhension des concepts clés et des sujets abordés dans le cours d'introduction aux statistiques.")

st.markdown("Cocher les bonnes réponses.")

st.header("A/ Statistiques descriptives vs inférentielles")

st.subheader("1/ Lequel des énoncés suivants décrit le mieux les statistiques descriptives ?")

check = st.checkbox("a) Techniques pour tirer des conclusions sur une population à partir d'un échantillon de données")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Techniques de synthèse et de description des caractéristiques d'un échantillon de données")

if check_2:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_3 = st.checkbox("c) Techniques de test d'hypothèses sur une population à partir d'un échantillon de données")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) Techniques d'estimation des paramètres de la population avec un haut degré de précision")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


########################################################################################################


st.header("B/ Types de données et sources de données")

st.subheader("1/ Lequel des éléments suivants est un exemple de données quantitatives ?")

check = st.checkbox("a) L'intitulé du poste")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) Le genre : 👦🏾/👧")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) Le niveau de qualification")

if check_3:
  st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_4 = st.checkbox("d) Les années d'expérience")

if check_4:
   st.write("👏🏾**Bonne réponse !** 👍🏾")


st.subheader("2/ Lequel des éléments suivants est une source potentielle de données RH ?")

check = st.checkbox("a) Enquêtes clients")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b) États financiers")

if check_2:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_3 = st.checkbox("c) SIRH")

if check_3:
  st.write("👏🏾**Bonne réponse !** 👍🏾")

check_4 = st.checkbox("d) Réseaux sociaux")

if check_4:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")


########################################################################################################


st.header("C/ Le rôle des statistiques dans les RH")

st.subheader("1/ Quel est le rôle premier des statistiques en RH ?")

check = st.checkbox("a) Garantir la conformité légale des décisions d'embauche et de promotion")

if check:
   st.write("💩💩pfff... **mauvaise réponse**🤪🤪")

check_2 = st.checkbox("b)  Fournir une base pour évaluer l'efficacité des politiques RH")

if check_2:
   st.write("👏🏾**Bonne réponse !** 👍🏾")

check_3 = st.checkbox("c) Identifier les tendances et modèles dans les comportement des équipes pour aider à la prise de décision managériale")

if check_3:
  st.write("**mauvaise réponse**🤪🤪 car il s'agit ici de **modelisation statistique**, bien loin du rôle premier")

check_4 = st.checkbox("d) Fournir un moyen de surveiller la productivité et la performance des employés")

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
redirect_button("https://cours-stats-rh.streamlit.app/Chapitre_2_🔖_Statistiques_descriptives","Aller au chapitre 2")




