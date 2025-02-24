import numpy as np
import matplotlib.pyplot as plt

"""
This version never exceeds 58 V at any point. We define the same original
piecewise shape (exponential rise from 28 to Us in 0..20 ms, then an
exponential drop from Us down to 28 in 20..350 ms) but apply a clamp:

    V_clamped(t) = min(V_original(t), 58)

Thus:
  - If the original formula is below 58 at time t, we follow it.
  - If it tries to go above 58, we stay at 58.
  - If the original formula dips back below 58 later, we resume that shape.
"""

t = np.linspace(0, 350e-3, 2000)
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

# Define the original wave:

def original_wave(tt, Us):
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

# Generate two example curves
V_clamped_upper = load_dump_profile_never_exceed_58(t, Us=202.0, clamp=U_clamp)
V_clamped_lower = load_dump_profile_never_exceed_58(t, Us=151.0, clamp=U_clamp)

# Plot
plt.figure(figsize=(8,6))
plt.plot(t*1e3, V_clamped_upper, label="Clamped <58V, Us=202V")
plt.plot(t*1e3, V_clamped_lower, label="Clamped <58V, Us=151V")
plt.axhline(U_clamp, color='r', linestyle='--', label=f"Clamp={U_clamp}V")
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [V]")
plt.title("Load Dump: Never Exceed 58V, Resuming Original Shape Below 58V")
plt.grid(True)
plt.legend()
plt.show()
