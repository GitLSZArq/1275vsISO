import streamlit as st

# Streamlit App Configuration
st.set_page_config(page_title="Voltage Standard Curve Viewer", layout="wide")

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
st.title("Voltage Standard Curve Viewer")

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
    "Select Curve Category:",
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

# Understanding Type Selection
understanding_type = st.sidebar.radio(
    "Choose Understanding Type:",
    ("Explication 1", "Explication 2")
)

# Initialize fig variable
fig = None

# Plotting Logic
if curve_category == "Spike Emission":
    if understanding_type == "Explication 2":
        fig = plot_spike_emission_explication_2()
    elif understanding_type == "Explication 1":
        fig = plot_spike_emission_explication_2()
elif curve_category == "Spike Immunity":
    if understanding_type == "Explication 2":
        fig = plot_spike_immunity_explication_2()
    elif understanding_type == "Explication 1":
        fig = plot_spike_immunity_explication_1()
elif curve_category == "Surge Emission":
    if understanding_type == "Explication 2":
        fig = plot_surge_emission_explication_2()
    elif understanding_type == "Explication 1":
        fig = plot_surge_emission_explication_2()
elif curve_category == "Surge Immunity":
    if understanding_type == "Explication 2":
        fig = plot_surge_immunity_explication_2()
    elif understanding_type == "Explication 1":
        fig = plot_surge_immunity_explication_1()
elif curve_category == "Ripple Emission":
    if understanding_type == "Explication 2":
        fig = plot_ripple_emission_explication_2()
    elif understanding_type == "Explication 1":
        fig = plot_ripple_emission_explication_2()
elif curve_category == "Ripple Immunity":
    if understanding_type == "Explication 2":
        fig = plot_ripple_immunity_explication_2()
    elif understanding_type == "Explication 1":
        fig = plot_ripple_immunity_explication_2()
elif curve_category == "Startup":
    if understanding_type == "Explication 2":
        fig = plot_startup_explication_2()
    elif understanding_type == "Explication 1":
        fig = plot_startup_explication_2()

# Display the Plot
if fig is not None:
    st.plotly_chart(fig, use_container_width=True)
    fig.update_layout(autosize=True)
else:
    st.write("Please select a valid curve type and understanding option.")


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
# with st.expander("📘 Functional Status Classification"):
#    language = st.radio("Choose language", options=["English", "French"], index=0, horizontal=True)
#    st.markdown(definitions["Functional Status Classification"][language])

if 'show_def' not in st.session_state:
    st.session_state.show_def = False

if st.button("Show Functional Status Classification"):
    st.session_state.show_def = not st.session_state.show_def

if st.session_state.show_def:
    language = st.radio("Choose language", options=["English", "French"], index=0, horizontal=True)
    st.markdown(definitions["Functional Status Classification"][language])
