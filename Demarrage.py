import numpy as np
import matplotlib.pyplot as plt

# --------------------
# MIL-STD-461-F/E
# --------------------

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

# --------------------
# Tracé du graphique avec deux ruptures d'axe
# --------------------

from matplotlib.patches import ConnectionPatch

# Augmentation de la taille de la figure pour plus d'espace
fig = plt.figure(figsize=(20, 8))

# Création des sous-graphiques avec plus d'espace entre eux
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1], wspace=0.15)
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1], sharey=ax1)
ax3 = fig.add_subplot(gs[2], sharey=ax1)

# Ajustement des limites des axes
ax1.set_xlim(-1, 2)
ax2.set_xlim(9, 11)
ax3.set_xlim(30, 32)
ax1.set_ylim(0, 26)  # Axe des Y commençant à 0 V

# Masquer les étiquettes de l'axe Y des sous-graphiques de droite
ax2.tick_params(labelleft=False)
ax3.tick_params(labelleft=False)

# Tracé des courbes sur chaque axe
# Axe 1 : de -1 s à 2 s
ax1.plot(t_MIL[(t_MIL >= -1) & (t_MIL <= 2)], V_MIL[(t_MIL >= -1) & (t_MIL <= 2)], drawstyle='steps-post', color='blue', label='MIL-STD-1275-F/E')
ax1.plot(t_ISO_I[(t_ISO_I >= -1) & (t_ISO_I <= 2)], V_ISO_I[(t_ISO_I >= -1) & (t_ISO_I <= 2)], color='red', label='ISO Cas I')
ax1.plot(t_ISO_II[(t_ISO_II >= -1) & (t_ISO_II <= 2)], V_ISO_II[(t_ISO_II >= -1) & (t_ISO_II <= 2)], color='green', label='ISO Cas II')
ax1.plot(t_ISO_III[(t_ISO_III >= -1) & (t_ISO_III <= 2)], V_ISO_III[(t_ISO_III >= -1) & (t_ISO_III <= 2)], color='purple', label='ISO Cas III')

# Axe 2 : de 9 s à 11 s
ax2.plot(t_MIL[(t_MIL >= 9) & (t_MIL <= 11)], V_MIL[(t_MIL >= 9) & (t_MIL <= 11)], drawstyle='steps-post', color='blue')
ax2.plot(t_ISO_I[(t_ISO_I >= 9) & (t_ISO_I <= 11)], V_ISO_I[(t_ISO_I >= 9) & (t_ISO_I <= 11)], color='red')
ax2.plot(t_ISO_II[(t_ISO_II >= 9) & (t_ISO_II <= 11)], V_ISO_II[(t_ISO_II >= 9) & (t_ISO_II <= 11)], color='green')
ax2.plot(t_ISO_III[(t_ISO_III >= 9) & (t_ISO_III <= 11)], V_ISO_III[(t_ISO_III >= 9) & (t_ISO_III <= 11)], color='purple')

# Axe 3 : de 30 s à 32 s
ax3.plot(t_MIL[(t_MIL >= 30) & (t_MIL <= 32)], V_MIL[(t_MIL >= 30) & (t_MIL <= 32)], drawstyle='steps-post', color='blue', label='MIL-STD-1275-F/E')
ax3.plot(t_ISO_I[(t_ISO_I >= 30) & (t_ISO_I <= 32)], V_ISO_I[(t_ISO_I >= 30) & (t_ISO_I <= 32)], color='red', label='ISO Cas I')
ax3.plot(t_ISO_II[(t_ISO_II >= 30) & (t_ISO_II <= 32)], V_ISO_II[(t_ISO_II >= 30) & (t_ISO_II <= 32)], color='green', label='ISO Cas II')
ax3.plot(t_ISO_III[(t_ISO_III >= 30) & (t_ISO_III <= 32)], V_ISO_III[(t_ISO_III >= 30) & (t_ISO_III <= 32)], color='purple', label='ISO Cas III')

# Ajout des ruptures d'axe
d = .015  # Taille des diagonales de rupture
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)

# Rupture entre ax1 et ax2
ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)
ax1.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)
kwargs.update(transform=ax2.transAxes)
ax2.plot((-d, +d), (-d, +d), **kwargs)
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)

# Rupture entre ax2 et ax3
kwargs.update(transform=ax2.transAxes)
ax2.plot((1 - d, 1 + d), (-d, +d), **kwargs)
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)
kwargs.update(transform=ax3.transAxes)
ax3.plot((-d, +d), (-d, +d), **kwargs)
ax3.plot((-d, +d), (1 - d, 1 + d), **kwargs)

# Annotations des temps clés
# Axe 1
ax1.axvline(x=0, color='gray', linestyle='dotted')
ax1.text(0, ax1.get_ylim()[1], '0 s', rotation=90, verticalalignment='bottom', fontsize=10)
ax1.axvline(x=1, color='gray', linestyle='dotted')
ax1.text(1, ax1.get_ylim()[1], '1 s', rotation=90, verticalalignment='bottom', fontsize=10)
ax1.axvline(x=2, color='gray', linestyle='dotted')
ax1.text(2, ax1.get_ylim()[1], '2 s', rotation=90, verticalalignment='bottom', fontsize=10)

# Axe 2
ax2.axvline(x=9, color='gray', linestyle='dotted')
ax2.text(9, ax2.get_ylim()[1], '9 s', rotation=90, verticalalignment='bottom', fontsize=10)
ax2.axvline(x=11, color='gray', linestyle='dotted')
ax2.text(11, ax2.get_ylim()[1], '11 s', rotation=90, verticalalignment='bottom', fontsize=10)

# Axe 3
ax3.axvline(x=30, color='gray', linestyle='dotted')
ax3.text(30, ax3.get_ylim()[1], '30 s', rotation=90, verticalalignment='bottom', fontsize=10)
ax3.axvline(x=31, color='gray', linestyle='dotted')
ax3.text(31, ax3.get_ylim()[1], '31 s', rotation=90, verticalalignment='bottom', fontsize=10)
ax3.axvline(x=32, color='gray', linestyle='dotted')
ax3.text(32, ax3.get_ylim()[1], '32 s', rotation=90, verticalalignment='bottom', fontsize=10)

# Étiquettes et titre
ax1.set_xlabel('Temps (s)')
ax1.set_ylabel('Tension (V)')
ax2.set_xlabel('Temps (s)')
ax3.set_xlabel('Temps (s)')
fig.suptitle('Variation de la tension avec deux ruptures d\'axe', fontsize=16)

# Placement de la légende en bas à droite sur le dernier sous-graphe
handles, labels = ax3.get_legend_handles_labels()
if not labels:
    handles, labels = ax1.get_legend_handles_labels()
ax3.legend(handles, labels, loc='lower right', fontsize=12)

# Ajout de la grille
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)

plt.show()