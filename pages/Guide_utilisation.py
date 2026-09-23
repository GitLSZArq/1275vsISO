import streamlit as st


st.set_page_config(
    page_title="Guide d'utilisation | MIL-STD-1275 et ISO",
    page_icon="📖",
    layout="wide",
)

st.sidebar.page_link("main.py", label="← Retour aux courbes", icon="📈")

guide_sections = [
    {
        "title": "🚀 Commencer en 60 secondes",
        "summary": "Le chemin le plus simple pour obtenir une comparaison utile.",
        "keywords": "démarrer debut commencer rapide première utilisation",
        "content": """
1. Choisissez le phénomène à étudier dans **Catégorie de courbe** à gauche.
2. Lisez les axes : le temps est en **µs**, **ms** ou **s** selon le phénomène ; la tension est en **V**.
3. Survolez une ligne pour obtenir une valeur précise.
4. Cliquez sur une entrée de légende pour ne conserver que les courbes utiles.

**Objectif :** identifier l'enveloppe MIL et le niveau ISO à comparer, sans perdre le contexte du graphique.
""",
        "tip": "Vérifiez toujours l'unité de temps avant de comparer deux amplitudes.",
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
        "tip": "Si votre question est « que doit supporter mon équipement ? », choisissez généralement une catégorie Immunity.",
    },
    {
        "title": "📈 Lire les courbes sans ambiguïté",
        "summary": "Axes, couleurs, enveloppes et zones : les repères essentiels.",
        "keywords": "lire courbe graphique axe temps tension volt microseconde milliseconde couleur enveloppe zone grise",
        "content": """
- L'axe horizontal indique le **temps** ; l'unité est écrite sous le graphique.
- L'axe vertical indique la **tension** en volts.
- La légende identifie l'édition MIL, la norme ISO ou le niveau de sévérité.
- Deux lignes de la même couleur peuvent former une **enveloppe** : elles sont alors les bornes haute et basse d'une même exigence.
- Les zones grisées aident à visualiser des limites ; elles ne remplacent pas l'interprétation de la norme.

Comparez toujours **la tension et la durée** : deux tensions identiques peuvent représenter des contraintes très différentes si leurs durées changent.
""",
        "tip": "Une courbe plus haute n'est pas automatiquement la plus contraignante : regardez aussi la borne basse et la durée.",
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

La barre d'outils Plotly apparaît au survol, en haut à droite du graphique. Utilisez l'icône **Accueil / Reset axes** pour revenir à l'affichage de départ.
""",
        "tip": "Masquez les courbes secondaires avant de comparer deux normes : la lecture devient immédiatement plus claire.",
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
        "tip": "Une capture doit toujours être accompagnée de la catégorie, de la norme et de la sévérité étudiées.",
    },
    {
        "title": "📘 Statut fonctionnel A à E",
        "summary": "Retrouver la signification des classes de fonctionnement pendant et après l'essai.",
        "keywords": "statut fonctionnel classification classe A B C D E DUT english french langue",
        "content": """
Sur la page des courbes, ouvrez **« 📘 Functional Status Classification »** sous le graphique. Cette section rappelle les classes de fonctionnement A à E utilisées pour qualifier le comportement du DUT (*Device Under Test*) pendant et après l'essai.

- Utilisez le sélecteur **English / French** pour choisir la langue de lecture.
- La classe A correspond au fonctionnement nominal ; les classes suivantes décrivent des dégradations ou des retours au fonctionnement normal selon des conditions différentes.

Cette référence relie une courbe de contrainte à un critère d'acceptation de l'équipement.
""",
        "tip": "Lisez la classe attendue avant l'essai : elle définit le comportement acceptable, pas seulement la tension appliquée.",
    },
]


st.title("📖 Guide d'utilisation")
st.markdown(
    "### Comparer les normes avec confiance, sans chercher l'information dans une notice interminable."
)
st.info(
    "Utilisez la recherche ou la navigation express ci-dessous. Le guide affiche immédiatement la rubrique utile."
)

step_one, arrow_one, step_two, arrow_two, step_three = st.columns([3, 1, 3, 1, 3])
with step_one:
    st.markdown("#### 1 · Choisir")
    st.write("Sélectionnez le phénomène à étudier dans la page des courbes.")
with arrow_one:
    st.markdown("## →")
with step_two:
    st.markdown("#### 2 · Explorer")
    st.write("Survolez, masquez les courbes inutiles et zoomez sur la zone utile.")
with arrow_two:
    st.markdown("## →")
with step_three:
    st.markdown("#### 3 · Comparer")
    st.write("Vérifiez les amplitudes, les durées et les sévérités avant de conclure.")

st.divider()
search_column, navigation_column, return_column = st.columns([4, 3, 2])
with search_column:
    search = st.text_input(
        "🔎 Recherche rapide",
        placeholder="Ex. zoom, spike, export, classe A, load dump…",
    ).strip().lower()
with navigation_column:
    destination = st.selectbox(
        "🧭 Navigation express",
        ["✨ Voir tout le guide"] + [section["title"] for section in guide_sections],
    )
with return_column:
    st.write("")
    if st.button("← Retour aux courbes", use_container_width=True):
        st.switch_page("main.py")


def render_section(section, expanded=False):
    with st.expander(section["title"], expanded=expanded):
        st.caption(section["summary"])
        st.markdown(section["content"])
        st.success(f"💡 Conseil pratique : {section['tip']}")


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
            "Aucune rubrique ne correspond exactement. Essayez : zoom, légende, émission, immunité, ISO ou classe A."
        )
elif destination != "✨ Voir tout le guide":
    selected_section = next(section for section in guide_sections if section["title"] == destination)
    render_section(selected_section, expanded=True)
else:
    st.subheader("Toutes les rubriques")
    for index, section in enumerate(guide_sections):
        render_section(section, expanded=index == 0)
