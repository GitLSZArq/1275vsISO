import streamlit as st

# Streamlit App Configuration
st.set_page_config(page_title="Voltage Standard Curve Viewer", layout="wide")

# Inject meta viewport and CSS to force full height
st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes, shrink-to-fit=no">
    <style>
        html, body {
            height: 100vh;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }
        /* This targets the main Streamlit container; the test id may change in future versions */
        [data-testid="stAppViewContainer"] {
            height: 100vh !important;
            min-height: 100vh !important;
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
else:
    st.write("Please select a valid curve type and understanding option.")
