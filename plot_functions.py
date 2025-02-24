import numpy as np
import plotly.graph_objects as go
import streamlit as st

# Function to plot Spike Emission - How Jad understood it (with gray area)
def plot_spike_emission_explication_2():
    t_pre = np.linspace(-10e-6, 0, 500)
    t1 = np.linspace(0, 70e-6, 1000)
    t2 = np.linspace(70e-6, 1e-3, 1000)

    t_F = np.concatenate((t_pre, t1, t2))
    V_pre_upper = np.full_like(t_pre, 0)
    V_upper1 = np.full_like(t1, 250)
    V_upper2 = np.linspace(250, 100, len(t2))
    V_upper_F = np.concatenate((V_pre_upper, V_upper1, V_upper2))

    V_pre_lower = np.full_like(t_pre, 0)
    V_lower1 = np.full_like(t1, -250)
    V_lower2 = np.linspace(-250, 18, len(t2))
    V_lower_F = np.concatenate((V_pre_lower, V_lower1, V_lower2))

    V_upper2_D = np.linspace(250, 40, len(t2))
    V_upper_D = np.concatenate((V_pre_upper, V_upper1, V_upper2_D))
    V_lower2_D = np.linspace(-250, -40, len(t2))
    V_lower_D = np.concatenate((V_pre_lower, V_lower1, V_lower2_D))

    t_ISO = np.linspace(0, 1e-3, 1000)
    V_ISO_I_II_upper = np.full_like(t_ISO, 100)
    V_ISO_I_II_lower = np.full_like(t_ISO, -100)
    V_ISO_III_upper = np.full_like(t_ISO, 150)
    V_ISO_III_lower = np.full_like(t_ISO, -150)
    V_ISO_IV_upper = np.full_like(t_ISO, 200)
    V_ISO_IV_lower = np.full_like(t_ISO, -200)

    # Create Plotly figure with a white background
    fig = go.Figure()

    # MIL-STD-1275-F/E
    fig.add_trace(go.Scatter(x=t_F * 1e6, y=V_upper_F, mode='lines', name='MIL-STD-1275-F/E', line=dict(color='black'), legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_F * 1e6, y=V_lower_F, mode='lines', line=dict(color='black'), showlegend=False, legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))

    # MIL-STD-1275-D
    fig.add_trace(go.Scatter(x=t_F * 1e6, y=V_upper_D, mode='lines', name='MIL-STD-1275-D', line=dict(color='blue', dash='dash'), legendgroup='MIL-STD-1275-D',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_F * 1e6, y=V_lower_D, mode='lines', line=dict(color='blue', dash='dash'), showlegend=False, legendgroup='MIL-STD-1275-D',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))

    # ISO 7637-2 Severity I/II
    fig.add_trace(go.Scatter(x=t_ISO * 1e6, y=V_ISO_I_II_upper, mode='lines', name='ISO 7637-2 (2011)<br>Sévérité I/II', line=dict(color='green'), legendgroup='ISO I/II',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_ISO * 1e6, y=V_ISO_I_II_lower, mode='lines', line=dict(color='green'), showlegend=False, legendgroup='ISO I/II',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))

    # ISO 7637-2 Severity III
    fig.add_trace(go.Scatter(x=t_ISO * 1e6, y=V_ISO_III_upper, mode='lines', name='ISO 7637-2 (2011)<br>Sévérité III', line=dict(color='orange'), legendgroup='ISO III',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_ISO * 1e6, y=V_ISO_III_lower, mode='lines', line=dict(color='orange'), showlegend=False, legendgroup='ISO III',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))

    # ISO 7637-2 Severity IV
    fig.add_trace(go.Scatter(x=t_ISO * 1e6, y=V_ISO_IV_upper, mode='lines', name='ISO 7637-2 (2011)<br>Sévérité IV', line=dict(color='red'), legendgroup='ISO IV',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_ISO * 1e6, y=V_ISO_IV_lower, mode='lines', line=dict(color='red'), showlegend=False, legendgroup='ISO IV',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))

    # Adding the gray shaded area
    max_y = 350
    min_y = -350

    fig.add_trace(go.Scatter(
        x=np.concatenate((t_F * 1e6, t_F[::-1] * 1e6)),
        y=np.concatenate((V_upper_F, [max_y] * len(t_F))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False,
        legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    fig.add_trace(go.Scatter(
        x=np.concatenate((t_F * 1e6, t_F[::-1] * 1e6)),
        y=np.concatenate((V_lower_F, [min_y] * len(t_F))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False,
        legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    fig.add_trace(go.Scatter(
        x=np.concatenate((t_F * 1e6, t_F[::-1] * 1e6)),
        y=np.concatenate((V_upper_D, [max_y] * len(t_F))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False,
        legendgroup='MIL-STD-1275-D',
        hoverinfo='skip'
    ))

    fig.add_trace(go.Scatter(
        x=np.concatenate((t_F * 1e6, t_F[::-1] * 1e6)),
        y=np.concatenate((V_lower_D, [min_y] * len(t_F))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False,
        legendgroup='MIL-STD-1275-D',
        hoverinfo='skip'
    ))

    # Layout with enhanced styling
    fig.update_layout(
        title=dict(text="Comparaison des normes MIL-STD-1275-F/E et D avec ISO 7637-2", font=dict(size=24, color='black')),
        xaxis_title=dict(text="Temps (µs)", font=dict(size=18, color='black')),
        yaxis_title=dict(text="Tension (V)", font=dict(size=18, color='black')),
        legend_title=dict(text="Curves", font=dict(size=16, color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        hovermode='closest',
        legend=dict(font=dict(size=14, color='black')),
        yaxis_autorange=True,  # Automatically fit y-axis to the selected data
        width=1000,
        height=800
    )

    # adjust_plot_layout(
    #     fig,
    #     title=dict(text="Comparaison des normes MIL-STD-1275-F/E et D avec ISO 7637-2", font=dict(size=24, color='black')),
    #     xaxis_title=dict(text="Temps (µs)", font=dict(size=18, color='black')),
    #     yaxis_title=dict(text="Tension (V)", font=dict(size=18, color='black')),
        
    # )

    return fig



# Placeholder function for "Other understanding" (using Plotly)
def plot_spike_emission_explication_1():
    fig = go.Figure()
    fig.add_annotation(
        text="Other understanding - To be defined",
        xref="paper", yref="paper",
        showarrow=False,
        font=dict(size=20)
    )
    fig.update_layout(
        title="Spike Emission - Other Understanding",
        xaxis_title="Time (µs)",
        yaxis_title="Voltage (V)",
        template="plotly_dark"
    )
    return fig







 # Function for Spike Immunity - How Jad understood it (with gray area outside the limits)



def generate_iso_pulse_2a(Us, Ri=2, tr=1e-6, td=0.00e-3, t1=50e-6):
    """
    Generate a mathematical representation of ISO Pulse 2a.

    Parameters:
    Us (float): Peak voltage (37V or 112V).
    Ri (float): Internal resistance (default: 2 ohms).
    tr (float): Rise time (time to go from 10% to 90% of Us).
    td (float): Delay time before the pulse starts.
    t1 (float): Total duration of the pulse (time to drop to 10% of Us).

    Returns:
    t (np.ndarray): Time array.
    V (np.ndarray): Voltage array.
    """
    # Time resolution
    resolution = 1000

    # Total duration of the simulation
    t_total = (t1 + tr) * 3  # Extend to include full decay to 0

    # Define the time array
    t = np.linspace(0, t_total, resolution)

    # Initialize the voltage array
    V = np.zeros_like(t)

    # Calculate key points in time
    t_start_rise = td  # Pulse starts after the delay time
    t_end_rise = t_start_rise + tr  # Rise ends after rise time
    t_mid_fall = td + t1  # Time when voltage reaches 10% Us
    t_end_fall = t_mid_fall + tr * 5  # Extend decay for smoothness to 0

    # Define the rise section (smooth exponential from 0 to 100% Us)
    rise_mask = (t >= t_start_rise) & (t <= t_end_rise)
    normalized_t_rise = (t[rise_mask] - t_start_rise) / tr
    V[rise_mask] = Us * (1 - np.exp(-5 * normalized_t_rise))

    # Define the fall section (smooth exponential decay from Us to 0 through 10% Us at t1)
    fall_mask = (t > t_end_rise)
    decay_time_constant = -np.log(0.1) / (t_mid_fall - t_end_rise)  # Ensure 10% Us at t1
    normalized_t_fall = (t[fall_mask] - t_end_rise) / (t_end_fall - t_end_rise)
    V[fall_mask] = Us * np.exp(-decay_time_constant * (t[fall_mask] - t_end_rise))

    return t, V


def generate_iso_pulse_3a(Us, tr=5e-9, td=150e-9, pulse_duration=100e-6, repetitions=10):

    """
    Generate a mathematical representation of ISO Pulse 3a.

    Parameters:
    Us (float): Peak voltage (-Us represents the negative spike value).
    tr (float): Rise time (time between 10% and 90% of -Us).
    td (float): Duration between the 10% (fall) and 10% (rise).
    pulse_duration (float): Duration before the pulse repeats.
    repetitions (int): Number of pulse repetitions.

    Returns:
    t (np.ndarray): Time array.
    V (np.ndarray): Voltage array.
    """
    # Define resolution for each section
    points_fall = 10
    points_rise = 50
    points_zero = 2

    # Initialize arrays
    t = []
    V = []

    # Create one pulse
    for i in range(repetitions):
        # Spike fall to -Us
        t_fall = np.linspace(0, tr, points_fall, endpoint=False)
        V_fall = -Us * (1 - np.exp(-5 * (t_fall / tr)))

        # Rise back to 0
        t_rise = np.linspace(tr, tr + td, points_rise, endpoint=False)
        V_rise = -Us * np.exp(-5 * ((t_rise - tr) / td))

        # Hold at 0 until next pulse
        t_zero = np.linspace(tr + td, pulse_duration, points_zero, endpoint=True)
        V_zero = np.zeros_like(t_zero)

        # Combine time and voltage for this pulse
        t_pulse = np.concatenate([t_fall, t_rise, t_zero])
        V_pulse = np.concatenate([V_fall, V_rise, V_zero])

        # Append to full signal
        if len(t) > 0:
            t_pulse += t[-1] + (pulse_duration - t_pulse[-1])  # Adjust offset precisely to ensure proper spacing
        t.extend(t_pulse)
        V.extend(V_pulse)

    return np.array(t), np.array(V)

def plot_spike_immunity_explication_2():
    t_pre = np.linspace(-10e-6, 0, 500)
    t1 = np.linspace(0, 70e-6, 1000)
    t2 = np.linspace(70e-6, 1e-3, 1000)

    t_F = np.concatenate((t_pre, t1, t2))
    V_pre_upper = np.full_like(t_pre, 0)
    V_upper1 = np.full_like(t1, 250)
    V_upper2 = np.linspace(250, 100, len(t2))
    V_upper_F = np.concatenate((V_pre_upper, V_upper1, V_upper2))

    V_pre_lower = np.full_like(t_pre, 0)
    V_lower1 = np.full_like(t1, -250)
    V_lower2 = np.linspace(-250, 18, len(t2))
    V_lower_F = np.concatenate((V_pre_lower, V_lower1, V_lower2))

    t_pulse_2a = np.array([50e-6, 50e-6])
    V_pulse_2a = np.array([37, 112])
    t_pulse_3a = np.array([0.15e-6, 0.15e-6])
    V_pulse_3a = np.array([-150, -300])
    t_pulse_3b = np.array([0.15e-6, 0.15e-6])
    V_pulse_3b = np.array([150, 300])

    fig = go.Figure()

    # MIL-STD-1275-F/E
    fig.add_trace(go.Scatter(x=t_F * 1e6, y=V_upper_F, mode='lines', name='MIL-STD-1275-F/E', line=dict(color='black'), legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_F * 1e6, y=V_lower_F, mode='lines', line=dict(color='black'), showlegend=False, legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))

    # Adding the gray shaded area outside the limits
    max_y = 350
    min_y = -350

    # Area above the upper limit
    fig.add_trace(go.Scatter(
        x=np.concatenate((t_F * 1e6, t_F[::-1] * 1e6)),
        y=np.concatenate((V_upper_F, [max_y] * len(t_F))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False, legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    # Area below the lower limit
    fig.add_trace(go.Scatter(
        x=np.concatenate((t_F * 1e6, t_F[::-1] * 1e6)),
        y=np.concatenate((V_lower_F, [min_y] * len(t_F))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False, legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    # ISO Pulse 2a
    fig.add_trace(go.Scatter(x=t_pulse_2a * 1e6, y=V_pulse_2a, mode='lines+markers', name='ISO Pulse 2a (2011)', line=dict(color='blue'), legendgroup='ISO Pulse 2a',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))


    # ISO Pulse 3a
    fig.add_trace(go.Scatter(x=t_pulse_3a * 1e6, y=V_pulse_3a, mode='lines+markers', name='ISO Pulse 3a (2011)', line=dict(color='red'), legendgroup='ISO Pulse 3a',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))


    # ISO Pulse 3b
    fig.add_trace(go.Scatter(x=t_pulse_3b * 1e6, y=V_pulse_3b, mode='lines+markers', name='ISO Pulse 3b (2011)', line=dict(color='green'), legendgroup='ISO Pulse 3b',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))


    # Layout with enhanced styling
    fig.update_layout(
        title="Spike Immunity",
        xaxis_title=dict(text="Temps (µs)", font=dict(size=18, color='black')),
        yaxis_title=dict(text="Tension (V)", font=dict(size=18, color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(font=dict(size=14, color='black')),
        xaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        hovermode='closest',
        yaxis_autorange=True,  # Automatically fit y-axis to the selected data
        width=1000,
        height=800
    )

    return fig


 # Function for Surge Emission - How Jad understood it (with inside gray area and ISO curves)

def plot_spike_immunity_explication_1():
    t_pre = np.linspace(-10e-6, 0, 500)
    t1 = np.linspace(0, 70e-6, 1000)
    t2 = np.linspace(70e-6, 1e-3, 1000)

    t_F = np.concatenate((t_pre, t1, t2))
    V_pre_upper = np.full_like(t_pre, 0)
    V_upper1 = np.full_like(t1, 250)
    V_upper2 = np.linspace(250, 100, len(t2))
    V_upper_F = np.concatenate((V_pre_upper, V_upper1, V_upper2))

    V_pre_lower = np.full_like(t_pre, 0)
    V_lower1 = np.full_like(t1, -250)
    V_lower2 = np.linspace(-250, 18, len(t2))
    V_lower_F = np.concatenate((V_pre_lower, V_lower1, V_lower2))

    
    t_pulse_2a_SevI_II,V_pulse_2a_SevI_II = generate_iso_pulse_2a(37, Ri=2, tr=1e-6, td=0.00e-3, t1=50e-6)
    t_pulse_2a_SevIII,V_pulse_2a_SevIII = generate_iso_pulse_2a(55, Ri=2, tr=1e-6, td=0.00e-3, t1=50e-6)
    t_pulse_2a_SevIV,V_pulse_2a_SevIV = generate_iso_pulse_2a(112, Ri=2, tr=1e-6, td=0.00e-3, t1=50e-6)
    
    t_pulse_3a_SevI_II,V_pulse_3a_SevI_II =generate_iso_pulse_3a(150, tr=5e-9, td=150e-9, pulse_duration=100e-6, repetitions=10)
    t_pulse_3a_SevIII,V_pulse_3a_SevIII =generate_iso_pulse_3a(220, tr=5e-9, td=150e-9, pulse_duration=100e-6, repetitions=10)
    t_pulse_3a_SevIV,V_pulse_3a_SevIV =generate_iso_pulse_3a(300, tr=5e-9, td=150e-9, pulse_duration=100e-6, repetitions=10)
    
    t_pulse_3b_SevI_II,V_pulse_3b_SevI_II =generate_iso_pulse_3a(-150, tr=5e-9, td=150e-9, pulse_duration=100e-6, repetitions=10)
    t_pulse_3b_SevIII,V_pulse_3b_SevIII =generate_iso_pulse_3a(-220, tr=5e-9, td=150e-9, pulse_duration=100e-6, repetitions=10)
    t_pulse_3b_SevIV,V_pulse_3b_SevIV =generate_iso_pulse_3a(-300, tr=5e-9, td=150e-9, pulse_duration=100e-6, repetitions=10)

    fig = go.Figure()

    # MIL-STD-1275-F/E
    fig.add_trace(go.Scatter(x=t_F * 1e6, y=V_upper_F, mode='lines', name='MIL-STD-1275-F/E', line=dict(color='black'), legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_F * 1e6, y=V_lower_F, mode='lines', line=dict(color='black'), showlegend=False, legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))

    # Adding the gray shaded area outside the limits
    max_y = 350
    min_y = -350

    # Area above the upper limit
    fig.add_trace(go.Scatter(
        x=np.concatenate((t_F * 1e6, t_F[::-1] * 1e6)),
        y=np.concatenate((V_upper_F, [max_y] * len(t_F))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False, legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    # Area below the lower limit
    fig.add_trace(go.Scatter(
        x=np.concatenate((t_F * 1e6, t_F[::-1] * 1e6)),
        y=np.concatenate((V_lower_F, [min_y] * len(t_F))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False, legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    # ISO Pulse 2a
    fig.add_trace(go.Scatter(x=t_pulse_2a_SevI_II * 1e6, y=V_pulse_2a_SevI_II, mode='lines+markers', name='ISO Pulse 2a (2011)<br>Sévérité I/II', line=dict(color='blue'), legendgroup='ISO Pulse 2a Sévérité I/II',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_pulse_2a_SevIII * 1e6, y=V_pulse_2a_SevIII, mode='lines+markers', name='ISO Pulse 2a (2011)<br>Sévérité III', line=dict(color='orange'), legendgroup='ISO Pulse 2a Sévérité III',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_pulse_2a_SevIV * 1e6, y=V_pulse_2a_SevIV, mode='lines+markers', name='ISO Pulse 2a (2011)<br>Sévérité IV', line=dict(color='purple'), legendgroup='ISO Pulse 2a Sévérité IV',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))


    # ISO Pulse 3a
    fig.add_trace(go.Scatter(x=t_pulse_3a_SevI_II * 1e6, y=V_pulse_3a_SevI_II, mode='lines+markers', name='ISO Pulse 3a (2011)<br>Sévérité I/II', line=dict(color='brown'), legendgroup='ISO Pulse 3a Sévérité I/II',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_pulse_3a_SevIII * 1e6, y=V_pulse_3a_SevIII, mode='lines+markers', name='ISO Pulse 3a (2011)<br>Sévérité III', line=dict(color='pink'), legendgroup='ISO Pulse 3a Sévérité III',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_pulse_3a_SevIV * 1e6, y=V_pulse_3a_SevIV, mode='lines+markers', name='ISO Pulse 3a (2011)<br>Sévérité IV', line=dict(color='navy'), legendgroup='ISO Pulse 3a Sévérité IV',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))


    # ISO Pulse 3b
    fig.add_trace(go.Scatter(x=t_pulse_3b_SevI_II * 1e6, y=V_pulse_3b_SevI_II, mode='lines+markers', name='ISO Pulse 3b (2011)<br>Sévérité I/II', line=dict(color='peachpuff'), legendgroup='ISO Pulse 3b Sévérité I/II',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_pulse_3b_SevIII * 1e6, y=V_pulse_3b_SevIII, mode='lines+markers', name='ISO Pulse 3b (2011)<br>Sévérité III', line=dict(color='turquoise'), legendgroup='ISO Pulse 3b Sévérité III',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_pulse_3b_SevIV * 1e6, y=V_pulse_3b_SevIV, mode='lines+markers', name='ISO Pulse 3b (2011)<br>Sévérité IV', line=dict(color='indigo'), legendgroup='ISO Pulse 3b Sévérité IV',hovertemplate='Time: %{x:.2f} µs<br>Voltage: %{y:.2f} V<extra></extra>'))


    # Layout with enhanced styling
    fig.update_layout(
        title="Spike Immunity",
        xaxis_title=dict(text="Temps (µs)", font=dict(size=18, color='black')),
        yaxis_title=dict(text="Tension (V)", font=dict(size=18, color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(font=dict(size=14, color='black')),
        xaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        hovermode='closest',
        yaxis_autorange=True,  # Automatically fit y-axis to the selected data
        width=1000,
        height=800
    )

    return fig


 # Function for Surge Emission - How Jad understood it (with inside gray area and ISO curves)

# Function for Surge Emission - How Jad understood it (with fixed ISO curve linking)
def plot_surge_emission_explication_2():
    # Time intervals
    t1 = np.linspace(1e-3, 50e-3, 1000)
    t2 = np.linspace(50e-3, 500e-3, 1000)
    t3 = np.linspace(500e-3, 600e-3, 500)
    t4 = np.linspace(600e-3, 1, 800)

    t_MIL = np.concatenate((t1, t2, t3, t4))

    # MIL-STD-1275-F/E limits
    V_upper1_F = np.full_like(t1, 100)
    V_upper2_F = np.linspace(100, 33, len(t2))
    V_upper3_F = np.full_like(np.concatenate((t3, t4)), 33)
    V_upper_MIL_F = np.concatenate((V_upper1_F, V_upper2_F, V_upper3_F))

    V_lower1_F = np.full_like(np.concatenate((t1, t2)), 18)
    V_lower2_F = np.linspace(18, 20, len(t3))
    V_lower3_F = np.full_like(t4, 20)
    V_lower_MIL_F = np.concatenate((V_lower1_F, V_lower2_F, V_lower3_F))

    # MIL-STD-1275-D limits
    V_upper1_D = np.full_like(t1, 40)
    V_upper2_D = np.linspace(40, 32, len(t2))
    V_upper3_D = np.full_like(np.concatenate((t3, t4)), 32)
    V_upper_MIL_D = np.concatenate((V_upper1_D, V_upper2_D, V_upper3_D))

    V_lower1_D = np.full_like(np.concatenate((t1, t2)), 18)
    V_lower2_D = np.linspace(18, 23, len(t3))
    V_lower3_D = np.full_like(t4, 23)
    V_lower_MIL_D = np.concatenate((V_lower1_D, V_lower2_D, V_lower3_D))

    # ISO 7637-2 severity levels
    t_ISO = np.linspace(1e-3, 1000e-3, 1000)
    V_ISO_I_II_upper = np.full_like(t_ISO, 25)
    V_ISO_I_II_lower = np.full_like(t_ISO, -100)
    V_ISO_III_upper = np.full_like(t_ISO, 37)
    V_ISO_III_lower = np.full_like(t_ISO, -150)
    V_ISO_IV_upper = np.full_like(t_ISO, 75)
    V_ISO_IV_lower = np.full_like(t_ISO, -200)

    fig = go.Figure()

    # MIL-STD-1275-F/E with gray shaded area outside
    fig.add_trace(go.Scatter(x=t_MIL * 1e3, y=V_upper_MIL_F, mode='lines', name='MIL-STD-1275-F/E', line=dict(color='black'), legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_MIL * 1e3, y=V_lower_MIL_F, mode='lines', line=dict(color='black'), showlegend=False, legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))

    # Area above the upper limit
    max_y = 110
    min_y = -210
    fig.add_trace(go.Scatter(
        x=np.concatenate((t_MIL * 1e3, t_MIL[::-1] * 1e3)),
        y=np.concatenate((V_upper_MIL_F, [max_y] * len(t_MIL))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False, legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    # Area below the lower limit
    fig.add_trace(go.Scatter(
        x=np.concatenate((t_MIL * 1e3, t_MIL[::-1] * 1e3)),
        y=np.concatenate((V_lower_MIL_F, [0] * len(t_MIL))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False, legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    # MIL-STD-1275-D
    fig.add_trace(go.Scatter(x=t_MIL * 1e3, y=V_upper_MIL_D, mode='lines', name='MIL-STD-1275-D', line=dict(color='blue', dash='dash'), legendgroup='MIL-STD-1275-D',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_MIL * 1e3, y=V_lower_MIL_D, mode='lines', line=dict(color='blue', dash='dash'), showlegend=False, legendgroup='MIL-STD-1275-D',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))

    # ISO 7637-2 Severity I/II (Linked upper and lower)
    fig.add_trace(go.Scatter(x=t_ISO * 1e3, y=V_ISO_I_II_upper, mode='lines', name='ISO 7637-2 (2011) <br>Sévérité I/II', line=dict(color='green'), legendgroup='ISO I/II',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_ISO * 1e3, y=V_ISO_I_II_lower, mode='lines', line=dict(color='green'), showlegend=False, legendgroup='ISO I/II',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))

    # ISO 7637-2 Severity III (Linked upper and lower)
    fig.add_trace(go.Scatter(x=t_ISO * 1e3, y=V_ISO_III_upper, mode='lines', name='ISO 7637-2 (2011) <br>Sévérité III', line=dict(color='orange'), legendgroup='ISO III',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_ISO * 1e3, y=V_ISO_III_lower, mode='lines', line=dict(color='orange'), showlegend=False, legendgroup='ISO III',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))

    # ISO 7637-2 Severity IV (Linked upper and lower)
    fig.add_trace(go.Scatter(x=t_ISO * 1e3, y=V_ISO_IV_upper, mode='lines', name='ISO 7637-2 (2011) <br>Sévérité IV', line=dict(color='red'), legendgroup='ISO IV',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_ISO * 1e3, y=V_ISO_IV_lower, mode='lines', line=dict(color='red'), showlegend=False, legendgroup='ISO IV',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))

    # Layout with Enhanced Styling
    fig.update_layout(
        title=dict(text="Comparaison des normes MIL-STD-1275-F/E et D avec ISO 7637-2", font=dict(size=24, color='black')),
        xaxis_title=dict(text="Temps (ms)", font=dict(size=18, color='black')),
        yaxis_title=dict(text="Tension (V)", font=dict(size=18, color='black')),
        legend_title=dict(text="Curves", font=dict(size=16, color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        hovermode='closest',
        legend=dict(font=dict(size=14, color='black')),
        yaxis_autorange=True,  # Automatically fit y-axis to the selected data
        width=1200,
        height=800
    )

    return fig


def load_dump_profile_no_centralized(t_array, Us=202.0):
    # For clarity define a piecewise function:
    # Segment A (0 <= t < 20 ms): Exponential rise
    # Segment B (>= 20 ms): Exponential drop
    
    # Exponential rise: we want 99% coverage by 20 ms.
    #  => exp(-kA*0.02) = 0.01 => -kA*0.02 = ln(0.01) => kA ~ 230.26

    kA = 230.26

    # For the drop, we want: at t=225 ms => 28 + 0.1*(Us-28)
    # Let t_drop = t - 20 ms. Then at t=20 ms => we have exactly Us.
    # Our drop formula:
    #   V_B(t) = 28 + (Us - 28)*exp(-kB*(t - 20e-3))
    # We want V_B(225 ms) = 28 + 0.1*(Us - 28)
    #   => 28 + (Us-28)*exp(-kB*(0.225-0.02)) = 28 + 0.1*(Us-28)
    #   => exp(-kB*0.205) = 0.1 => kB = -ln(0.1)/0.205 ~ 11.23
    kB = 11.23


    U_start = 28.0
    tA_end = 20e-3  # boundary between rise and drop

    def segmentA(tt):
        return Us - (Us - U_start)*np.exp(-kA * tt)

    def segmentB(tt):
        # If t < tA_end, we don't want to evaluate segment B.
        # But the main loop won't call segmentB below 20 ms anyway.
        return U_start + (Us - U_start)*np.exp(-kB*(tt - tA_end))

    V_out = np.zeros_like(t_array)

    for i, tt in enumerate(t_array):
        if tt < tA_end:
            # Exponential rise
            V_out[i] = segmentA(tt)
        else:
            # Exponential drop
            V_out[i] = segmentB(tt)

    return V_out

def original_wave(tt, Us):
    U_start = 28.0
    U_clamp = 58.0

    # Key times for the original shape
    tA_end = 20e-3  # end of rise

    t_total = 350e-3

    # Exponential constants:
    # We'll do a typical approach: we want ~99% rise by 20 ms => kA ~ 230.26.
    # For the drop, let's pick k_drop so that at 225 ms we are near 28+0.1*(Us-28):
    #   28 + (Us-28)*exp(-k_drop*(225e-3 - 20e-3)) = 28 + 0.1*(Us-28)
    #   => exp(-k_drop*0.205) = 0.1 => k_drop= -ln(0.1)/0.205 ~ 11.23

    kA = 230.26
    k_drop = -np.log(0.1)/0.205  # ~ 11.23
    
    # Segment A: 0..20 ms, exponential rise 28->Us
    if 0 <= tt < tA_end:
        return Us - (Us - U_start)*np.exp(-kA * tt)
    elif tt >= tA_end:
        # Segment B: 20..350 ms, single exponential drop from Us->28
        #   V_drop(t) = 28 + (Us - 28)*exp(-k_drop*(t - 0.02))
        return U_start + (Us - U_start)*np.exp(-k_drop*(tt - tA_end))
    else:
        # For negative t, just define 28
        return U_start
    

def load_dump_profile_never_exceed_58(t_array, Us=202.0, clamp=58.0):
    """
    Returns a piecewise array that follows the original shape (rise then drop),
    but is clamped so that it never exceeds `clamp`.
    """
    V_out = np.zeros_like(t_array)
    for i, tt in enumerate(t_array):
        V_orig = original_wave(tt, Us)
        V_out[i] = min(V_orig, clamp)
    return V_out


# Function for Surge Immunity - How DGA wants it
def plot_surge_immunity_explication_1():
    # Time intervals
    t1 = np.linspace(1e-3, 50e-3, 1000)
    t2 = np.linspace(50e-3, 500e-3, 1000)
    t3 = np.linspace(500e-3, 600e-3, 500)
    t4 = np.linspace(600e-3, 1000e-3, 800)

    t_MIL = np.concatenate((t1, t2, t3, t4))

    # MIL-STD-1275-F/E limits
    V_upper_MIL = np.concatenate((np.full_like(t1, 100), np.linspace(100, 33, len(t2)), np.full_like(np.concatenate((t3, t4)), 33)))
    V_lower_MIL = np.concatenate((np.full_like(np.concatenate((t1, t2)), 18), np.linspace(18, 20, len(t3)), np.full_like(t4, 20)))

    # ISO No Centralized Load Dump (Orange zone)
    t_ISO_zone_No_Centralized_Load_Dump = np.linspace(0e-3, 1000e-3, 2000)
    V_upper_No_Centralized_Load_Dump = load_dump_profile_no_centralized(t_ISO_zone_No_Centralized_Load_Dump, Us=202.0)
    V_lower_No_Centralized_Load_Dump = load_dump_profile_no_centralized(t_ISO_zone_No_Centralized_Load_Dump, Us=151.0)
    
    # ISO Centralized Load Dump (Dashed blue line)
    U_clamp = 58.0
    t_ISO_zone_Centralized_Load_Dump = np.linspace(0e-3, 1000e-3, 2000)
    V_clamped_upper = load_dump_profile_never_exceed_58(t_ISO_zone_Centralized_Load_Dump, Us=202.0, clamp=U_clamp)
    V_clamped_lower = load_dump_profile_never_exceed_58(t_ISO_zone_Centralized_Load_Dump, Us=151.0, clamp=U_clamp)

    # Create Plotly figure
    fig = go.Figure()

    # MIL-STD-1275-F/E with gray shaded area outside
    fig.add_trace(go.Scatter(x=t_MIL * 1e3, y=V_upper_MIL, mode='lines', name='MIL-STD-1275-F/E', line=dict(color='black'), legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_MIL * 1e3, y=V_lower_MIL, mode='lines', line=dict(color='black'), showlegend=False, legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))

    # Gray shaded area outside MIL-STD-1275-F/E limits
    max_y = 220
    min_y = 0

    # Area above the upper limit
    fig.add_trace(go.Scatter(
        x=np.concatenate((t_MIL * 1e3, t_MIL[::-1] * 1e3)),
        y=np.concatenate((V_upper_MIL, [max_y] * len(t_MIL))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False, legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    # Area below the lower limit
    fig.add_trace(go.Scatter(
        x=np.concatenate((t_MIL * 1e3, t_MIL[::-1] * 1e3)),
        y=np.concatenate((V_lower_MIL, [min_y] * len(t_MIL))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False, legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    # ISO No Centralized Load Dump (Orange shaded area)
    fig.add_trace(go.Scatter(
        x=t_ISO_zone_No_Centralized_Load_Dump * 1e3, y=V_upper_No_Centralized_Load_Dump,
        mode='lines',line=dict(color='Green'),
        name='ISO No Centralized Load Dump <br>ISO 16750-2 (2023)', legendgroup='ISO No Load Dump',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'
    ))

    fig.add_trace(go.Scatter(
        x=t_ISO_zone_No_Centralized_Load_Dump * 1e3, y=V_lower_No_Centralized_Load_Dump,
        mode='lines',line=dict(color='Green'), legendgroup='ISO No Load Dump',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>', showlegend=False
    ))

    # ISO Centralized Load Dump (Dashed blue line)
    fig.add_trace(go.Scatter(x=t_ISO_zone_Centralized_Load_Dump * 1e3, y=V_clamped_upper, mode='lines', name='ISO Centralized Load Dump <br>ISO 16750-2 (2023)', line=dict(color='blue', dash='dash'), legendgroup='ISO Centralized Load Dump',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_ISO_zone_Centralized_Load_Dump * 1e3, y=V_clamped_upper, mode='lines', showlegend=False, line=dict(color='blue', dash='dash'), legendgroup='ISO Centralized Load Dump',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))

    # Dotted lines for key voltage levels
    voltage_levels = [58, 33, 20, 18, 151, 202]
    for level in voltage_levels:
        fig.add_hline(y=level, line=dict(color='gray', dash='dot'), annotation_text=f"{level} V", annotation_position="top left")

    # Dotted vertical lines for key time markers
    time_markers = [1, 50, 100, 350, 500, 600, 1000]
    for marker in time_markers:
        fig.add_vline(x=marker, line=dict(color='gray', dash='dot'), annotation_text=f"{marker} ms", annotation_position="bottom right")

    # Enhanced layout styling
    fig.update_layout(
        title=dict(text="MIL-STD-1275-F/E avec ISO Load Dump", font=dict(size=24, color='black')),
        xaxis_title=dict(text="Temps (ms)", font=dict(size=18, color='black')),
        yaxis_title=dict(text="Tension (V)", font=dict(size=18, color='black')),
        legend_title=dict(text="Curves", font=dict(size=16, color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        hovermode='closest',
        legend=dict(font=dict(size=14, color='black')),
        yaxis_autorange=True,  # Automatically fit y-axis to the selected data
        width=1200,
        height=1200
    )

    return fig


# Function for Surge Immunity - How Jad understood it
def plot_surge_immunity_explication_2():
    # Time intervals
    t1 = np.linspace(1e-3, 50e-3, 1000)
    t2 = np.linspace(50e-3, 500e-3, 1000)
    t3 = np.linspace(500e-3, 600e-3, 500)
    t4 = np.linspace(600e-3, 1000e-3, 800)

    t_MIL = np.concatenate((t1, t2, t3, t4))

    # MIL-STD-1275-F/E limits
    V_upper_MIL = np.concatenate((np.full_like(t1, 100), np.linspace(100, 33, len(t2)), np.full_like(np.concatenate((t3, t4)), 33)))
    V_lower_MIL = np.concatenate((np.full_like(np.concatenate((t1, t2)), 18), np.linspace(18, 20, len(t3)), np.full_like(t4, 20)))

    # ISO No Centralized Load Dump (Orange zone)
    t_ISO_zone = np.linspace(100e-3, 350e-3, 1000)
    V_ISO_zone_upper = np.full_like(t_ISO_zone, 202)
    V_ISO_zone_lower = np.full_like(t_ISO_zone, 151)

    # ISO Centralized Load Dump (Dashed blue line)
    t_ISO_line = np.linspace(100e-3, 350e-3, 1000)
    V_ISO_line = np.full_like(t_ISO_line, 58)

    # Create Plotly figure
    fig = go.Figure()

    # MIL-STD-1275-F/E with gray shaded area outside
    fig.add_trace(go.Scatter(x=t_MIL * 1e3, y=V_upper_MIL, mode='lines', name='MIL-STD-1275-F/E', line=dict(color='black'), legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))
    fig.add_trace(go.Scatter(x=t_MIL * 1e3, y=V_lower_MIL, mode='lines', line=dict(color='black'), showlegend=False, legendgroup='MIL-STD-1275-F/E',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))

    # Gray shaded area outside MIL-STD-1275-F/E limits
    max_y = 220
    min_y = 0

    # Area above the upper limit
    fig.add_trace(go.Scatter(
        x=np.concatenate((t_MIL * 1e3, t_MIL[::-1] * 1e3)),
        y=np.concatenate((V_upper_MIL, [max_y] * len(t_MIL))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False, legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    # Area below the lower limit
    fig.add_trace(go.Scatter(
        x=np.concatenate((t_MIL * 1e3, t_MIL[::-1] * 1e3)),
        y=np.concatenate((V_lower_MIL, [min_y] * len(t_MIL))),
        fill='toself', fillcolor='lightgray', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        showlegend=False, legendgroup='MIL-STD-1275-F/E',
        hoverinfo='skip'
    ))

    # ISO No Centralized Load Dump (Orange shaded area)
    fig.add_trace(go.Scatter(
        x=np.concatenate((t_ISO_zone * 1e3, t_ISO_zone[::-1] * 1e3)),
        y=np.concatenate((V_ISO_zone_upper, V_ISO_zone_lower[::-1])),
        fill='toself', fillcolor='orange', opacity=0.5, line=dict(color='rgba(0,0,0,0)'),
        name='ISO No Centralized Load Dump <br>ISO 16750-2 (2023)', legendgroup='ISO No Load Dump',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'
    ))

    # ISO Centralized Load Dump (Dashed blue line)
    fig.add_trace(go.Scatter(x=t_ISO_line * 1e3, y=V_ISO_line, mode='lines', name='ISO Centralized Load Dump <br>ISO 16750-2 (2023)', line=dict(color='blue', dash='dash'), legendgroup='ISO Centralized Load Dump',hovertemplate='Time: %{x:.2f} ms<br>Voltage: %{y:.2f} V<extra></extra>'))

    # Dotted lines for key voltage levels
    voltage_levels = [58, 33, 20, 18, 151, 202]
    for level in voltage_levels:
        fig.add_hline(y=level, line=dict(color='gray', dash='dot'), annotation_text=f"{level} V", annotation_position="top left")

    # Dotted vertical lines for key time markers
    time_markers = [1, 50, 100, 350, 500, 600, 1000]
    for marker in time_markers:
        fig.add_vline(x=marker, line=dict(color='gray', dash='dot'), annotation_text=f"{marker} ms", annotation_position="bottom right")

    # Enhanced layout styling
    fig.update_layout(
        title=dict(text="MIL-STD-1275-F/E avec ISO Load Dump", font=dict(size=24, color='black')),
        xaxis_title=dict(text="Temps (ms)", font=dict(size=18, color='black')),
        yaxis_title=dict(text="Tension (V)", font=dict(size=18, color='black')),
        legend_title=dict(text="Curves", font=dict(size=16, color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='darkgray',
            color='black',
            tickfont=dict(size=14, color='black'),
            showspikes=True,
            spikemode='across+marker',
            spikesnap='cursor',
            spikedash='dot',
            spikecolor='gray',
            spikethickness=1.5
        ),
        hovermode='closest',
        legend=dict(font=dict(size=14, color='black')),
        yaxis_autorange=True,  # Automatically fit y-axis to the selected data
        width=1200,
        height=1200
    )

    return fig




# Function for Ripple Emission - How Jad understood it
def plot_ripple_emission_explication_2():
    # Time axis for the data (0 to 8 ms)
    t_data = np.linspace(0, 8e-3, 4000)

    # Frequency of oscillation
    f = 1e3  # Frequency in Hz
    omega = 2 * np.pi * f

    # Curve information
    courbes = [
        {
            'nom': 'MIL-STD-1275-F (Bleue)',
            'couleur': 'blue',
            'V_haute': 31,
            'V_basse': 22,
            'oscillation': 2
        },
        {
            'nom': 'MIL-STD-1275-D (Rouge)',
            'couleur': 'red',
            'V_haute': 30,
            'V_basse': 25,
            'oscillation': 2
        },
    ]

    fig = go.Figure()

    # Maximum and minimum y-values for shading
    max_y = max([courbe['V_haute'] + courbe['oscillation'] for courbe in courbes]) + 5
    min_y = min([courbe['V_basse'] - courbe['oscillation'] for courbe in courbes]) - 5

    # Plot each curve
    for courbe in courbes:
        V_haute_centrale = courbe['V_haute']
        V_basse_centrale = courbe['V_basse']
        amplitude = courbe['oscillation']

        # Upper and lower oscillation calculations
        V_haute = V_haute_centrale + amplitude * np.sin(omega * t_data)
        V_basse = V_basse_centrale + amplitude * np.sin(omega * t_data)

        # Dashed central lines linked to the legend
        fig.add_trace(go.Scatter(
            x=[t_data[0] * 1e3, t_data[-1] * 1e3], y=[V_haute_centrale, V_haute_centrale],
            mode='lines', name=f"{courbe['nom']} <br>Ligne Centrale Haute", line=dict(color=courbe['couleur'], dash='dash'),
            legendgroup=courbe['nom'], showlegend=True
        ))
        fig.add_trace(go.Scatter(
            x=[t_data[0] * 1e3, t_data[-1] * 1e3], y=[V_basse_centrale, V_basse_centrale],
            mode='lines', name=f"{courbe['nom']} <br>Ligne Centrale Basse", line=dict(color=courbe['couleur'], dash='dash'),
            legendgroup=courbe['nom'], showlegend=True
        ))

        # Upper and lower oscillating lines
        fig.add_trace(go.Scatter(
            x=t_data * 1e3, y=V_haute, mode='lines', name=f"{courbe['nom']} <br>Oscillation Haute",
            line=dict(color=courbe['couleur']), legendgroup=courbe['nom']
        ))
        fig.add_trace(go.Scatter(
            x=t_data * 1e3, y=V_basse, mode='lines', name=f"{courbe['nom']} <br>Oscillation Basse",
            line=dict(color=courbe['couleur'], dash='dot'), showlegend=True, legendgroup=courbe['nom']
        ))

    

    # Layout adjustments with French text
    fig.update_layout(
        title=dict(text="Comparaison des exigences d'émission d'ondulation (Ripple Emission)", font=dict(size=24, color='black')),
        xaxis_title=dict(text="Temps (ms)", font=dict(size=18, color='black')),
        yaxis_title=dict(text="Tension (V)", font=dict(size=18, color='black')),
        legend_title=dict(text="Courbes", font=dict(size=16, color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(showgrid=True, gridcolor='darkgray', color='black', tickfont=dict(size=14, color='black')),
        yaxis=dict(showgrid=True, gridcolor='darkgray', color='black', tickfont=dict(size=14, color='black')),
        legend=dict(font=dict(size=14, color='black')),
        yaxis_autorange=True,  # Automatically fit y-axis to the selected data
        width=1200,
        height=1200
    )

    return fig


# Function for Ripple Immunity - How Jad understood it (with combined upper and lower limits)
def plot_ripple_immunity_explication_2():
    # Time axis for the data (0 to 8 ms)
    t_data = np.linspace(0, 8e-3, 4000)

    # Frequency of oscillation
    f = 1e3  # Frequency in Hz
    omega = 2 * np.pi * f

    # Curve information
    courbes = [
        {'nom': 'MIL-STD-1275-F', 'couleur': 'blue', 'V_haute': 31, 'V_basse': 22, 'oscillation': 2},
        {'nom': 'MIL-STD-1275-E', 'couleur': 'green', 'V_haute': 30, 'V_basse': 23, 'oscillation': 2},
        {'nom': 'MIL-STD-1275-D', 'couleur': 'red', 'V_haute': 30, 'V_basse': 25, 'oscillation': 2},
        {'nom': 'ISO-Code-E - ISO 16750-2 (2023)', 'couleur': 'orange', 'V_haute': 30.5, 'V_basse': 11.5, 'oscillation': 1.5},
        {'nom': 'ISO-Code-F - ISO 16750-2 (2023)', 'couleur': 'purple', 'V_haute': 30.5, 'V_basse': 17.5, 'oscillation': 1.5},
        {'nom': 'ISO-Code-G - ISO 16750-2 (2023)', 'couleur': 'cyan', 'V_haute': 30.5, 'V_basse': 23.5, 'oscillation': 1.5},
        {'nom': 'ISO-Code-H - ISO 16750-2 (2023)', 'couleur': 'magenta', 'V_haute': 30.5, 'V_basse': 19.5, 'oscillation': 1.5},
    ]

    fig = go.Figure()

    # Maximum and minimum y-values for shading
    max_y = 35
    min_y = 10

    # Plot each curve
    for courbe in courbes:
        V_haute_centrale = courbe['V_haute']
        V_basse_centrale = courbe['V_basse']
        amplitude = courbe['oscillation']

        # Upper and lower oscillation calculations
        V_haute = V_haute_centrale + amplitude * np.sin(omega * t_data)
        V_basse = V_basse_centrale + amplitude * np.sin(omega * t_data)

        # Dashed central lines linked to the legend
        fig.add_trace(go.Scatter(
            x=[t_data[0] * 1e3, t_data[-1] * 1e3], y=[V_haute_centrale, V_haute_centrale],
            mode='lines', name=f"{courbe['nom']} <br>Ligne Centrale Haute", line=dict(color=courbe['couleur'], dash='dash'),
            legendgroup=courbe['nom'], showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=[t_data[0] * 1e3, t_data[-1] * 1e3], y=[V_basse_centrale, V_basse_centrale],
            mode='lines', name=f"{courbe['nom']} <br>Ligne Centrale Basse", line=dict(color=courbe['couleur'], dash='dash'),
            legendgroup=courbe['nom'], showlegend=False
        ))

        # Upper and lower oscillating lines
        fig.add_trace(go.Scatter(
            x=t_data * 1e3, y=V_haute, mode='lines', name=f"{courbe['nom']} <br>Oscillation Haute",
            line=dict(color=courbe['couleur']), legendgroup=courbe['nom']
        ))
        fig.add_trace(go.Scatter(
            x=t_data * 1e3, y=V_basse, mode='lines', name=f"{courbe['nom']} <br>Oscillation Basse",
            line=dict(color=courbe['couleur'], dash='dot'), showlegend=False, legendgroup=courbe['nom']
        ))

  
    # Layout adjustments with French text
    fig.update_layout(
        title=dict(text="Comparaison des exigences d'immunité d'ondulation (Ripple Immunity)", font=dict(size=24, color='black')),
        xaxis_title=dict(text="Temps (ms)", font=dict(size=18, color='black')),
        yaxis_title=dict(text="Tension (V)", font=dict(size=18, color='black')),
        legend_title=dict(text="Courbes", font=dict(size=16, color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(showgrid=True, gridcolor='darkgray', color='black', tickfont=dict(size=14, color='black')),
        yaxis=dict(showgrid=True, gridcolor='darkgray', color='black', tickfont=dict(size=14, color='black')),
        legend=dict(font=dict(size=14, color='black')),
        yaxis_autorange=True,  # Automatically fit y-axis to the selected data
        width=1200,
        height=1200
    )

    return fig



# Function for Démarrage (Startup) - Unified Plot
def plot_startup_explication_2():
    # MIL-STD-1275-F/E Data
    # Définition des intervalles de temps
    t1_MIL = np.linspace(-1, 0, 1000)    # De -1 s à 0 s
    t2_MIL = np.linspace(0, 1, 1000)     # De 0 s à 1 s
    t3_MIL = np.linspace(1, 2, 1000)     # De 1 s à 2 s
    t4_MIL = np.linspace(9, 11, 1000)    # De 9 s à 11 s
    t5_MIL = np.linspace(30, 31, 1000)   # De 30 s à 31 s
    t6_MIL = np.linspace(31, 32, 1000)   # De 31 s à 32 s

    # Correspondance des tensions
    V1_MIL = np.full_like(t1_MIL, 20)    # 20 V
    V2_MIL = np.full_like(t2_MIL, 12)    # 12 V
    V3_MIL = np.full_like(t3_MIL, 16)    # 16 V
    V4_MIL = np.full_like(t4_MIL, 16)    # 16 V
    V5_MIL = np.full_like(t5_MIL, 16)    # 20 V
    V6_MIL = np.full_like(t6_MIL, 20)    # 20 V

    # Concatenation des intervalles de temps et des tensions
    t_MIL = np.concatenate((t1_MIL, t2_MIL, t3_MIL, t4_MIL, t5_MIL, t6_MIL))
    V_MIL = np.concatenate((V1_MIL, V2_MIL, V3_MIL, V4_MIL, V5_MIL, V6_MIL))

    # --------------------
    # ISO Cas I
    # --------------------

    # Définition des intervalles de temps
    t_iso1 = np.linspace(-1, 0, 1000)          # De -1 s à 0 s
    t_iso2 = np.linspace(0, 0.01, 1000)        # De 0 s à 10 ms (descente)
    t_iso3 = np.linspace(0.01, 0.06, 1000)     # De 10 ms à 60 ms (tension constante)
    t_iso4 = np.linspace(0.06, 0.11, 1000)     # De 60 ms à 110 ms (montée)
    t_iso5 = np.linspace(0.11, 1.11, 2000)     # De 110 ms à 1.11 s (oscillation)
    t_iso6 = np.linspace(1.11, 1.15, 1000)     # De 1.11 s à 1.15 s (montée finale)
    t_iso7 = np.linspace(1.15, 2, 1000)        # De 1.15 s à 2 s (tension constante)
    t_iso8 = np.linspace(9, 11, 1000)          # De 9 s à 11 s (tension constante)
    t_iso9 = np.linspace(30, 32, 1000)         # De 30 s à 32 s (tension constante)

    # Tensions correspondantes
    V_iso1 = np.full_like(t_iso1, 24)                          # 24 V
    V_iso2 = np.linspace(24, 10, len(t_iso2))                  # Descente de 24 V à 10 V
    V_iso3 = np.full_like(t_iso3, 10)                          # 10 V constant
    V_iso4 = np.linspace(10, 21, len(t_iso4))                  # Montée de 10 V à 21 V
    # Oscillation autour de 21 V
    f_osc_I = 2                                                # Fréquence de 2 Hz
    omega_osc_I = 2 * np.pi * f_osc_I
    V_iso5 = 21 + 1 * np.sin(omega_osc_I * (t_iso5 - t_iso5[0]))
    V_iso6 = np.linspace(21, 24, len(t_iso6))                  # Montée de 21 V à 24 V
    V_iso7 = np.full_like(t_iso7, 24)                          # 24 V constant
    V_iso8 = np.full_like(t_iso8, 24)                          # 24 V constant
    V_iso9 = np.full_like(t_iso9, 24)                          # 24 V constant

    # Concatenation
    t_ISO_I = np.concatenate((t_iso1, t_iso2, t_iso3, t_iso4, t_iso5, t_iso6, t_iso7, t_iso8, t_iso9))
    V_ISO_I = np.concatenate((V_iso1, V_iso2, V_iso3, V_iso4, V_iso5, V_iso6, V_iso7, V_iso8, V_iso9))

    # --------------------
    # ISO Cas II
    # --------------------

    # Ajustements spécifiques pour l'ISO Cas II
    t_iso5_II = np.linspace(0.11, 10.11, 2000)  # Oscillation sur 10 s
    t_iso6_II = np.linspace(10.11, 10.21, 1000) # Montée finale sur 100 ms
    t_iso7_II = np.linspace(10.21, 11, 1000)    # Tension constante jusqu'à 11 s

    # Tensions correspondantes
    V_iso2_II = np.linspace(24, 8, len(t_iso2))                 # Descente à 8 V
    V_iso3_II = np.full_like(t_iso3, 8)                         # 8 V constant
    V_iso4_II = np.linspace(8, 15, len(t_iso4))                 # Montée à 15 V
    V_iso5_II = 15 + 1 * np.sin(omega_osc_I * (t_iso5_II - t_iso5_II[0]))  # Oscillation autour de 15 V
    V_iso6_II = np.linspace(15, 24, len(t_iso6_II))             # Montée finale
    V_iso7_II = np.full_like(t_iso7_II, 24)                     # 24 V constant
    V_iso8_II = np.full_like(t_iso8, 24)                        # 24 V constant
    V_iso9_II = np.full_like(t_iso9, 24)                        # 24 V constant

    # Concatenation
    t_ISO_II = np.concatenate((t_iso1, t_iso2, t_iso3, t_iso4, t_iso5_II, t_iso6_II, t_iso7_II, t_iso8, t_iso9))
    V_ISO_II = np.concatenate((V_iso1, V_iso2_II, V_iso3_II, V_iso4_II, V_iso5_II, V_iso6_II, V_iso7_II, V_iso8_II, V_iso9_II))

    # --------------------
    # ISO Cas III
    # --------------------

    # Ajustements spécifiques pour l'ISO Cas III
    V_iso2_III = np.linspace(24, 6, len(t_iso2))                # Descente à 6 V
    V_iso3_III = np.full_like(t_iso3, 6)                        # 6 V constant
    V_iso4_III = np.linspace(6, 11, len(t_iso4))                # Montée à 11 V
    V_iso5_III = 11 + 1 * np.sin(omega_osc_I * (t_iso5 - t_iso5[0]))  # Oscillation autour de 11 V
    V_iso6_III = np.linspace(11, 24, len(t_iso6))               # Montée finale
    V_iso7_III = np.full_like(t_iso7, 24)                       # 24 V constant
    V_iso8_III = np.full_like(t_iso8, 24)                       # 24 V constant
    V_iso9_III = np.full_like(t_iso9, 24)                       # 24 V constant

    # Concatenation
    t_ISO_III = np.concatenate((t_iso1, t_iso2, t_iso3, t_iso4, t_iso5, t_iso6, t_iso7, t_iso8, t_iso9))
    V_ISO_III = np.concatenate((V_iso1, V_iso2_III, V_iso3_III, V_iso4_III, V_iso5_III, V_iso6_III, V_iso7_III, V_iso8_III, V_iso9_III))

    # Create the Plotly figure
    fig = go.Figure()

    # MIL-STD-1275-F/E
    fig.add_trace(go.Scatter(x=t_MIL, y=V_MIL, mode='lines', name='MIL-STD-1275-F/E', line=dict(color='blue')))

    # ISO Cas I
    fig.add_trace(go.Scatter(x=t_ISO_I, y=V_ISO_I, mode='lines', name='ISO Cas I <br>ISO 16750-2 (2023)', line=dict(color='red')))

    # ISO Cas II
    fig.add_trace(go.Scatter(x=t_ISO_II, y=V_ISO_II, mode='lines', name='ISO Cas II <br>ISO 16750-2 (2023)', line=dict(color='green')))

    # ISO Cas III
    fig.add_trace(go.Scatter(x=t_ISO_III, y=V_ISO_III, mode='lines', name='ISO Cas III <br>ISO 16750-2 (2023)', line=dict(color='purple')))

    # Layout configuration
    fig.update_layout(
        title="Démarrage - Variation de la tension (Courbes combinées)",
        xaxis_title=dict(text="Temps (s)", font=dict(size=18, color='black')),
        yaxis_title=dict(text="Tension (V)", font=dict(size=18, color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(showgrid=True, gridcolor='darkgray', color='black', tickfont=dict(size=14, color='black')),
        yaxis=dict(showgrid=True, gridcolor='darkgray', color='black', tickfont=dict(size=14, color='black')),
        legend=dict(font=dict(size=14, color='black')),
        width=1200,
        height=1200
    )

    return fig


# def adjust_plot_layout(fig, title, xaxis_title, yaxis_title):
#     fig.update_layout(
#         title=dict(text=title, font=dict(size=24, color='black')),
#         xaxis_title=dict(text=xaxis_title, font=dict(size=18, color='black')),
#         yaxis_title=dict(text=yaxis_title, font=dict(size=18, color='black')),
#         legend_title=dict(text="Legend", font=dict(size=16, color='black')),
#         plot_bgcolor='white',
#         paper_bgcolor='white',
#         xaxis=dict(showgrid=True, gridcolor='darkgray', color='black', tickfont=dict(size=14, color='black')),
#         yaxis=dict(showgrid=True, gridcolor='darkgray', color='black', tickfont=dict(size=14, color='black')),
#         autosize=True,  # Allow dynamic resizing
#         margin=dict(l=50, r=50, t=50, b=50)  # Adjust margins to ensure proportional spacing
#     )
