import streamlit as st

# Streamlit App Configuration
st.set_page_config(
    page_title="Comparaison entre MIL-STD-1275 et ISO",
    layout="wide",
)

# Inject meta viewport and CSS to force full height
st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes, shrink-to-fit=no, viewport-fit=cover">
    <script>
      function setVh() {
        let vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty('--vh', `${vh}px`);
      }
      setVh();
      window.addEventListener('resize', setVh);
    </script>
    <style>
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }
        /* Use the custom property for height */
        [data-testid="stAppViewContainer"] {
            height: calc(var(--vh, 1vh) * 100) !important;
            min-height: calc(var(--vh, 1vh) * 100) !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Title
st.title("Comparaison entre MIL-STD-1275 et ISO")

from plot_functions import (
    plot_spike_emission_explication_2,
    plot_spike_immunity_explication_2,
    plot_surge_emission_explication_2,
    plot_surge_immunity_explication_2,
    plot_surge_immunity_explication_1,
    plot_ripple_emission_explication_2,
    plot_ripple_immunity_explication_2,
    plot_startup_explication_2,
    plot_spike_immunity_explication_1
)





# Sidebar for Curve Type Selection
curve_category = st.sidebar.selectbox(
    "Catégorie de courbe :",
    (
        "Spike Emission",
        "Spike Immunity",
        "Surge Emission",
        "Surge Immunity",
        "Ripple Emission",
        "Ripple Immunity",
        "Startup"
    )
)


@st.dialog("Guide d'utilisation")
def show_tutorial():
    st.markdown(
        """
        ## Bienvenue

        Cette application permet de **visualiser et comparer les enveloppes de tension**
        définies par les normes **MIL-STD-1275** et les normes **ISO** associées aux
        perturbations de l'alimentation électrique. Elle est conçue comme une aide à la
        lecture et à la comparaison : la norme applicable et son édition restent la
        référence à utiliser pour une exigence, un plan d'essai ou une décision de conformité.

        ---

        ## 1. Démarrage rapide

        1. Dans la barre latérale gauche, choisissez une **catégorie de courbe**.
        2. Lisez le titre, les axes et la légende du graphique qui s'affiche.
        3. Survolez une courbe pour obtenir la valeur de **temps** et de **tension** à
           l'endroit visé.
        4. Cliquez sur un élément de la **légende** pour masquer ou réafficher cette
           famille de courbes et faciliter la comparaison.
        5. Utilisez les outils du graphique pour zoomer, déplacer la vue ou revenir à la
           vue initiale.

        ## 2. Choisir la bonne catégorie

        | Catégorie | Ce que montre le graphique |
        | --- | --- |
        | **Spike Emission** | Les surtensions et sous-tensions brèves susceptibles d'être générées sur l'alimentation. |
        | **Spike Immunity** | Les impulsions rapides que l'équipement doit pouvoir supporter. |
        | **Surge Emission** | Les variations transitoires d'amplitude plus importante et de durée plus longue, incluant les limites MIL et les sévérités ISO. |
        | **Surge Immunity** | Les contraintes de type *load dump* à supporter, avec les profils ISO centralisé et non centralisé lorsque présents. |
        | **Ripple Emission** | Les exigences relatives à l'ondulation produite par l'équipement. |
        | **Ripple Immunity** | Les niveaux d'ondulation auxquels l'équipement doit résister. |
        | **Startup** | Les variations de tension associées au démarrage. |

        Les termes *Emission* et *Immunity* sont conservés volontairement :
        **Emission** décrit ce que le système peut injecter sur son alimentation ;
        **Immunity** décrit ce qu'il doit tolérer sans dégradation inacceptable.

        ## 3. Lire un graphique correctement

        - L'axe horizontal est le **temps**. Son unité est indiquée sous le graphique :
          microsecondes (µs), millisecondes (ms) ou secondes (s) selon le phénomène.
        - L'axe vertical est la **tension**, exprimée en volts (V).
        - Chaque couleur, style de trait ou zone correspond à une exigence, une édition
          de norme ou un niveau de sévérité identifié dans la légende.
        - Les deux lignes d'une même couleur peuvent former une **enveloppe** : elles
          représentent alors une limite haute et une limite basse, même si une seule
          entrée apparaît dans la légende.
        - Les zones grisées servent à rendre les limites visuellement plus lisibles ;
          elles ne remplacent pas l'interprétation de la norme.

        ## 4. Utiliser les interactions du graphique

        - **Survoler** : affiche les coordonnées précises de la courbe sous le pointeur.
        - **Cliquer dans la légende** : masque ou affiche une courbe ou un groupe de
          courbes. Cliquez de nouveau pour le réafficher.
        - **Double-cliquer dans la légende** : isole généralement la courbe sélectionnée ;
          double-cliquez à nouveau pour tout réafficher.
        - **Faire glisser dans le graphique** : zoome sur une zone ou déplace la vue,
          selon l'outil actif.
        - **Molette** : permet de zoomer lorsque le navigateur le prend en charge.
        - **Barre d'outils en haut à droite du graphique** : elle apparaît au survol et
          permet notamment de zoomer, dézoomer, déplacer la vue, sélectionner une zone,
          télécharger l'image et revenir à l'affichage initial. L'icône *Accueil* ou
          *Reset axes* annule les zooms et déplacements.

        ## 5. Comparer les normes sans se tromper

        1. Commencez par isoler l'édition MIL concernée (par exemple F/E ou D).
        2. Ajoutez ensuite la ou les courbes ISO correspondant à la sévérité étudiée.
        3. Comparez les amplitudes **et** les durées : une tension identique n'implique
           pas nécessairement une contrainte équivalente si la durée diffère.
        4. Vérifiez systématiquement l'unité de temps affichée avant toute conclusion.
        5. Consultez le texte officiel de la norme avant de retenir une limite pour un
           essai, une spécification ou une validation produit.

        ## 6. Classification du statut fonctionnel

        Sous le graphique, ouvrez **« 📘 Functional Status Classification »** pour
        consulter les classes de fonctionnement A à E. Sélectionnez **English** ou
        **French** pour changer la langue de cette référence. Cette section aide à
        qualifier le comportement du DUT (*Device Under Test*) pendant et après l'essai.

        ## 7. Bonnes pratiques

        - Notez la catégorie, l'édition de norme, la sévérité et la date de consultation
          lorsque vous capturez un graphique.
        - Utilisez le téléchargement d'image du graphique pour joindre une comparaison à
          une revue technique ; indiquez toujours la source normative dans votre document.
        - Si une courbe ou une valeur semble ambiguë, revenez à la vue initiale puis
          vérifiez la légende, les unités et l'édition de norme.
        """
    )


if st.sidebar.button("📖 Ouvrir le guide d'utilisation", use_container_width=True):
    show_tutorial()

# Initialize fig variable
fig = None

# Plotting Logic
if curve_category == "Spike Emission":
    fig = plot_spike_emission_explication_2()
elif curve_category == "Spike Immunity":
    fig = plot_spike_immunity_explication_1()
elif curve_category == "Surge Emission":
    fig = plot_surge_emission_explication_2()
elif curve_category == "Surge Immunity":
    fig = plot_surge_immunity_explication_1()
elif curve_category == "Ripple Emission":
    fig = plot_ripple_emission_explication_2()
elif curve_category == "Ripple Immunity":
    fig = plot_ripple_immunity_explication_2()
elif curve_category == "Startup":
    fig = plot_startup_explication_2()

# Display the Plot
if fig is not None:
    st.plotly_chart(fig, use_container_width=True)
    fig.update_layout(autosize=True)
else:
    st.write("Veuillez sélectionner une catégorie de courbe valide.")


# Define the bilingual definitions as a dictionary
definitions = {
    "Functional Status Classification": {
        "English": """
**6 Functional Status Classification**

**6.1 General**  
This element describes the functional status of a DUT during and after a test. The minimum functional status shall be given in each test. An additional test requirement may be agreed between device supplier and vehicle manufacturer. Vehicle manufacturer and device supplier shall specify operations that are not allowed.

**6.2 Class A**  
All functions of the device/system perform as designed during and after the test.

**6.3 Class B**  
All functions of the device/system perform as designed during the test. However, one or more may go beyond the specified tolerance. All functions return automatically to within normal limits after the test. Memory functions shall remain Class A.

**6.4 Class C**  
One or more functions of a device/system do not perform as designed during the test but return automatically to normal operation after the test.

**6.5 Class D**  
One or more functions of a device/system do not perform as designed during the test and do not return to normal operation after the test until the device/system is reset by a simple “operator/use” action.

**6.6 Class E**  
One or more functions of a device/system do not perform as designed during and after the test and cannot be returned to proper operation without repairing or replacing the device/system.
        """,
        "French": """
**6 Classification du Statut Fonctionnel**

**6.1 Général**  
Cet élément décrit le statut fonctionnel d’un DUT pendant et après un essai. Le statut fonctionnel minimum doit être indiqué pour chaque essai. Une exigence supplémentaire peut être convenue entre le fournisseur et le constructeur automobile. Le constructeur et le fournisseur doivent spécifier les opérations non autorisées.

**6.2 Classe A**  
Toutes les fonctions du dispositif/système fonctionnent comme prévu pendant et après l’essai.

**6.3 Classe B**  
Toutes les fonctions du dispositif/système fonctionnent comme prévu pendant l’essai. Cependant, une ou plusieurs peuvent dépasser la tolérance spécifiée. Toutes les fonctions reviennent automatiquement à la normale après l’essai. Les fonctions de mémoire doivent rester de classe A.

**6.4 Classe C**  
Une ou plusieurs fonctions d’un dispositif/système ne fonctionnent pas comme prévu pendant l’essai mais reviennent automatiquement à un fonctionnement normal après l’essai.

**6.5 Classe D**  
Une ou plusieurs fonctions d’un dispositif/système ne fonctionnent pas comme prévu pendant l’essai et ne reviennent pas à un fonctionnement normal après l’essai tant que le dispositif/système n’est pas réinitialisé par une simple action de l’opérateur.

**6.6 Classe E**  
Une ou plusieurs fonctions d’un dispositif/système ne fonctionnent pas comme prévu pendant et après l’essai et ne peuvent pas être ramenées à un fonctionnement correct sans réparer ou remplacer le dispositif/système.
        """
    }
}

# Create an expander for the definition
with st.expander("📘 Functional Status Classification"):
    language = st.radio("Choisis la langue", options=["English", "French"], index=0, horizontal=True)
    st.markdown(definitions["Functional Status Classification"][language])
