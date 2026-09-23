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
    guide_sections = [
        {
            "title": "🚀 Commencer en 60 secondes",
            "summary": "Le chemin le plus simple pour obtenir une comparaison utile.",
            "keywords": "démarrer debut commencer rapide première utilisation",
            "content": """
1. Choisissez le phénomène à étudier dans **Catégorie de courbe** à gauche.
2. Lisez les axes : le temps est en **µs**, **ms** ou **s** selon le phénomène ; la tension est en **V**.
3. Survolez une ligne pour obtenir une valeur précise.
4. Cliquez sur une entrée de légende pour ne conserver que les courbes qui vous intéressent.

**Objectif :** identifier rapidement l'enveloppe MIL et le niveau ISO à comparer, sans perdre le contexte du graphique.
""",
            "tip": "Commencez toujours par vérifier l'unité de temps avant de comparer deux amplitudes.",
        },
        {
            "title": "🧭 Choisir la bonne catégorie",
            "summary": "Comprendre en un coup d'œil ce que chaque menu affiche.",
            "keywords": "catégorie categorie spike surge ripple startup émission emission immunité immunity menu",
            "content": """
| Catégorie | À utiliser lorsque vous étudiez… |
| --- | --- |
| **Spike Emission** | les pics brefs que le système peut générer sur son alimentation. |
| **Spike Immunity** | les impulsions rapides que le système doit supporter. |
| **Surge Emission** | les transitoires de plus forte énergie générés par le système. |
| **Surge Immunity** | les transitoires à supporter, notamment les cas de *load dump*. |
| **Ripple Emission** | l'ondulation produite par le système. |
| **Ripple Immunity** | l'ondulation que le système doit tolérer. |
| **Startup** | les variations de tension pendant le démarrage. |

**Repère simple :** *Emission* = ce que le système peut injecter ; *Immunity* = ce qu'il doit encaisser.
""",
            "tip": "Si votre question commence par « que doit supporter mon équipement ? », choisissez généralement une catégorie Immunity.",
        },
        {
            "title": "📈 Lire les courbes sans ambiguïté",
            "summary": "Axes, couleurs, enveloppes et zones : les repères essentiels.",
            "keywords": "lire courbe graphique axe temps tension volt microseconde milliseconde couleur enveloppe zone grise",
            "content": """
- L'axe horizontal indique le **temps** ; l'unité est toujours écrite sous le graphique.
- L'axe vertical indique la **tension** en volts.
- La légende identifie l'édition MIL, la norme ISO ou le niveau de sévérité.
- Deux lignes de la même couleur peuvent être les bornes haute et basse d'une même **enveloppe** ; une seule entrée de légende représente alors les deux limites.
- Les zones grisées rendent certaines limites plus faciles à visualiser. Elles ne constituent pas, à elles seules, une règle de conformité.

Pour conclure, comparez toujours **la tension et la durée** : deux valeurs de tension identiques peuvent correspondre à des contraintes très différentes si leurs durées ne sont pas les mêmes.
""",
            "tip": "Une courbe haute n'est pas automatiquement « pire » : regardez aussi la borne basse, la durée et la sévérité ISO.",
        },
        {
            "title": "🖱️ Interagir avec le graphique",
            "summary": "Zoomer, isoler une courbe, restaurer la vue et exporter une image.",
            "keywords": "zoom légende masquer afficher double cliquer survoler souris molette déplacer reset accueil télécharger exporter image",
            "content": """
| Action | Résultat |
| --- | --- |
| **Survoler une courbe** | Affiche le temps et la tension au point visé. |
| **Cliquer dans la légende** | Masque ou affiche une famille de courbes. |
| **Double-cliquer dans la légende** | Isole généralement la courbe choisie ; recommencez pour tout réafficher. |
| **Faire glisser dans le graphique** | Zoome sur une zone ou déplace la vue selon l'outil sélectionné. |
| **Utiliser la barre d'outils** | Zoom, déplacement, sélection de zone, téléchargement d'image et retour à la vue initiale. |

La barre d'outils Plotly apparaît au survol, en haut à droite du graphique. Après une exploration, utilisez l'icône **Accueil / Reset axes** pour revenir immédiatement à l'affichage de départ.
""",
            "tip": "Pour comparer deux normes, masquez d'abord les courbes secondaires : le graphique devient beaucoup plus lisible.",
        },
        {
            "title": "🔎 Méthode de comparaison recommandée",
            "summary": "Une mini-checklist fiable avant de tirer une conclusion.",
            "keywords": "comparer comparaison mil iso sévérité severity edition F E D méthode conformité essai",
            "content": """
**Checklist en 5 gestes :**

1. Sélectionnez la catégorie correspondant au phénomène étudié.
2. Repérez l'édition MIL utile, par exemple F/E ou D.
3. Gardez uniquement le ou les niveaux ISO pertinents à l'aide de la légende.
4. Comparez les amplitudes, les bornes haute/basse et la durée du phénomène.
5. Notez la catégorie, l'édition et la sévérité avant d'exporter une image ou de rédiger une conclusion.

Cette application est une aide à la lecture. Pour une exigence contractuelle, un plan d'essai ou une décision de conformité, consultez toujours l'édition officielle de la norme applicable.
""",
            "tip": "Une capture de graphique doit toujours être accompagnée de la catégorie, de la norme et de la sévérité étudiées.",
        },
        {
            "title": "📘 Statut fonctionnel A à E",
            "summary": "Retrouver la signification des classes de fonctionnement pendant et après l'essai.",
            "keywords": "statut fonctionnel classification classe A B C D E DUT english french langue",
            "content": """
Sous le graphique, ouvrez **« 📘 Functional Status Classification »**. Cette section rappelle les classes de fonctionnement A à E utilisées pour qualifier le comportement du DUT (*Device Under Test*) pendant et après l'essai.

- Utilisez le sélecteur **English / French** pour choisir la langue de lecture.
- La classe A correspond au fonctionnement nominal ; les classes suivantes décrivent des dégradations ou des retours au fonctionnement normal selon des conditions différentes.

Cette référence est particulièrement utile lorsque vous reliez une courbe de contrainte à un critère d'acceptation de l'équipement.
""",
            "tip": "Lisez la classe attendue avant l'essai : elle définit le niveau de comportement acceptable, pas seulement la tension appliquée.",
        },
    ]

    st.markdown("## Votre guide, à votre rythme")
    st.caption(
        "Une aide visuelle pour trouver la bonne courbe, lire le graphique et comparer les normes en confiance."
    )

    first_step, second_step, third_step = st.columns(3)
    with first_step:
        st.info("**1 · Choisir**\n\nSélectionnez le phénomène à étudier.")
    with second_step:
        st.info("**2 · Explorer**\n\nSurvolez, masquez et zoomez sur les courbes.")
    with third_step:
        st.info("**3 · Comparer**\n\nVérifiez amplitudes, durées et sévérités.")

    st.divider()
    search_column, navigation_column = st.columns([3, 2])
    with search_column:
        search = st.text_input(
            "🔎 Rechercher dans le guide",
            placeholder="Ex. zoom, spike, export, classe A, load dump…",
        ).strip().lower()
    with navigation_column:
        destination = st.selectbox(
            "🧭 Aller directement à",
            ["✨ Voir tout le guide"] + [section["title"] for section in guide_sections],
        )

    def render_section(section, expanded=False):
        with st.expander(section["title"], expanded=expanded):
            st.caption(section["summary"])
            st.markdown(section["content"])
            st.success(f"💡 Conseil : {section['tip']}")

    if search:
        matching_sections = [
            section for section in guide_sections
            if search in " ".join(
                (section["title"], section["summary"], section["keywords"], section["content"])
            ).lower()
        ]
        if matching_sections:
            st.success(f"{len(matching_sections)} rubrique(s) trouvée(s) pour « {search} ».")
            for section in matching_sections:
                render_section(section, expanded=True)
        else:
            st.warning(
                "Aucune rubrique ne correspond exactement à cette recherche. "
                "Essayez par exemple : zoom, légende, émission, immunité, ISO ou classe A."
            )
    elif destination != "✨ Voir tout le guide":
        selected_section = next(
            section for section in guide_sections if section["title"] == destination
        )
        render_section(selected_section, expanded=True)
    else:
        st.markdown("### Les rubriques du guide")
        for index, section in enumerate(guide_sections):
            render_section(section, expanded=index == 0)


if st.sidebar.button("📖 Ouvrir le guide d'utilisation", use_container_width=True):
    st.switch_page("pages/Guide_utilisation.py")

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
