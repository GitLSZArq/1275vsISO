import numpy as np
import matplotlib.pyplot as plt

# --------------------
# Données pour la MIL-STD-1275-F/E
# --------------------

# Définition des intervalles de temps en secondes
t1 = np.linspace(1e-3, 50e-3, 1000)       # De 1 ms à 50 ms
t2 = np.linspace(50e-3, 500e-3, 1000)     # De 50 ms à 500 ms
t3 = np.linspace(500e-3, 600e-3, 500)     # De 500 ms à 600 ms
t4 = np.linspace(600e-3, 1000e-3, 800)    # De 600 ms à 1000 ms

# Limite supérieure
V_upper1 = np.full_like(t1, 100)                       # 100 V de 1 ms à 50 ms
V_upper2 = np.linspace(100, 33, len(t2))               # Descente linéaire de 100 V à 33 V de 50 ms à 500 ms
V_upper3 = np.full_like(np.concatenate((t3, t4)), 33)  # 33 V de 500 ms à 1000 ms

# Limite inférieure
V_lower1 = np.full_like(np.concatenate((t1, t2)), 18)  # 18 V de 1 ms à 500 ms
V_lower2 = np.linspace(18, 20, len(t3))                # Montée linéaire de 18 V à 20 V de 500 ms à 600 ms
V_lower3 = np.full_like(t4, 20)                        # 20 V de 600 ms à 1000 ms

# Concatenation des tableaux de temps et de tension pour MIL-STD-1275-F/E
t_MIL = np.concatenate((t1, t2, t3, t4))
V_upper_MIL = np.concatenate((V_upper1, V_upper2, V_upper3))
V_lower_MIL = np.concatenate((V_lower1, V_lower2, V_lower3))

# --------------------
# Données pour ISO No Centralized Load Dump
# --------------------

t_ISO_zone = np.linspace(100e-3, 350e-3, 1000)  # De 100 ms à 350 ms
V_ISO_zone_upper = np.full_like(t_ISO_zone, 202)  # Limite supérieure à 202 V
V_ISO_zone_lower = np.full_like(t_ISO_zone, 151)  # Limite inférieure à 151 V

# --------------------
# Données pour ISO Centralized Load Dump
# --------------------

t_ISO_line = np.linspace(100e-3, 350e-3, 1000)  # De 100 ms à 350 ms
V_ISO_line = np.full_like(t_ISO_line, 58)       # Tension constante à 58 V

# --------------------
# Tracé du graphique
# --------------------

fig, ax = plt.subplots(figsize=(12, 6))

# Tracé des limites MIL-STD-1275-F/E
ax.plot(t_MIL * 1e3, V_upper_MIL, color='black', label='MIL-STD-1275-F/E')
ax.plot(t_MIL * 1e3, V_lower_MIL, color='black')

# Remplissage des zones interdites pour MIL-STD-1275-F/E
ax.fill_between(t_MIL * 1e3, V_upper_MIL, ax.get_ylim()[1], where=(V_upper_MIL <= ax.get_ylim()[1]), color='gray', alpha=0.5)
ax.fill_between(t_MIL * 1e3, V_lower_MIL, ax.get_ylim()[0], where=(V_lower_MIL >= ax.get_ylim()[0]), color='gray', alpha=0.5)

# Tracé de la zone ISO No Centralized Load Dump
ax.fill_between(t_ISO_zone * 1e3, V_ISO_zone_lower, V_ISO_zone_upper, color='orange', alpha=0.5, label='ISO No Centralized Load Dump')

# Tracé de la ligne ISO Centralized Load Dump
ax.plot(t_ISO_line * 1e3, V_ISO_line, color='blue', linestyle='--', label='ISO Centralized Load Dump')

# Ajout des lignes pointillées horizontales aux tensions clés
tension_values = [58, 33, 20, 18, 151, 202]
for v in tension_values:
    ax.axhline(y=v, color='gray', linestyle='dotted')
    # Déplacer les annotations à droite de l'axe Y
    ax.text(0.02, (v - ax.get_ylim()[0]) / (ax.get_ylim()[1] - ax.get_ylim()[0]), f'{v} V',
            transform=ax.transAxes,
            verticalalignment='center',
            color='gray',
            fontsize=10)

# Ajout des lignes pointillées verticales aux temps clés
time_values = [1, 50, 100, 350, 500, 600, 1000]
for t_val in time_values:
    ax.axvline(x=t_val, color='gray', linestyle='dotted')
    ax.text((t_val - ax.get_xlim()[0]) / (ax.get_xlim()[1] - ax.get_xlim()[0]), 0.02, f'{t_val} ms',
            transform=ax.transAxes,
            horizontalalignment='center',
            verticalalignment='bottom',
            color='gray',
            fontsize=10)

# Personnalisation du graphique
ax.set_xlabel('Temps (ms)')
ax.set_ylabel('Tension (V)')
ax.set_title('MIL-STD-1275-F/E avec ISO Load Dump')
ax.grid(True)

# Affichage de la légende
ax.legend(loc='upper right')

# Ajustement des limites de l'axe des Y pour inclure toutes les courbes
ax.set_ylim(0, 220)

# Ajustement des limites de l'axe des X
ax.set_xlim(0, 1000)

# Affichage du graphique
plt.show()
