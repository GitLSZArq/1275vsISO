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

# Limite supérieure pour MIL-STD-1275-F/E
V_upper1_F = np.full_like(t1, 100)                       # 100 V de 1 ms à 50 ms
V_upper2_F = np.linspace(100, 33, len(t2))               # Descente linéaire de 100 V à 33 V de 50 ms à 500 ms
V_upper3_F = np.full_like(np.concatenate((t3, t4)), 33)  # 33 V de 500 ms à 1000 ms

# Limite inférieure pour MIL-STD-1275-F/E
V_lower1_F = np.full_like(np.concatenate((t1, t2)), 18)  # 18 V de 1 ms à 500 ms
V_lower2_F = np.linspace(18, 20, len(t3))                # Montée linéaire de 18 V à 20 V de 500 ms à 600 ms
V_lower3_F = np.full_like(t4, 20)                        # 20 V de 600 ms à 1000 ms

# Concatenation des tableaux de temps et de tension pour MIL-STD-1275-F/E
t_MIL = np.concatenate((t1, t2, t3, t4))
V_upper_MIL_F = np.concatenate((V_upper1_F, V_upper2_F, V_upper3_F))
V_lower_MIL_F = np.concatenate((V_lower1_F, V_lower2_F, V_lower3_F))

# --------------------
# Données pour la MIL-STD-1275-D
# --------------------

# Limite supérieure pour MIL-STD-1275-D
V_upper1_D = np.full_like(t1, 100)                       # 100 V de 1 ms à 50 ms
V_upper2_D = np.linspace(100, 40, len(t2))               # Descente linéaire de 100 V à 40 V de 50 ms à 500 ms
V_upper3_D = np.full_like(np.concatenate((t3, t4)), 40)  # 40 V de 500 ms à 1000 ms

# Limite inférieure pour MIL-STD-1275-D
V_lower1_D = np.full_like(np.concatenate((t1, t2)), 15)  # 15 V de 1 ms à 500 ms
V_lower2_D = np.linspace(15, 16, len(t3))                # Montée linéaire de 15 V à 16 V de 500 ms à 600 ms
V_lower3_D = np.full_like(t4, 16)                        # 16 V de 600 ms à 1000 ms

# Concatenation des tableaux de temps et de tension pour MIL-STD-1275-D
V_upper_MIL_D = np.concatenate((V_upper1_D, V_upper2_D, V_upper3_D))
V_lower_MIL_D = np.concatenate((V_lower1_D, V_lower2_D, V_lower3_D))

# --------------------
# Données pour ISO 7637-2
# --------------------

# Temps pour les ISO 7637-2 (on peut utiliser le même que pour MIL-STD)
t_ISO = np.linspace(1e-3, 1000e-3, 1000)

# ISO 7637-2 Sévérité I/II
V_ISO_I_II_upper = np.full_like(t_ISO, 25)    # Limite supérieure à +25 V
V_ISO_I_II_lower = np.full_like(t_ISO, -100)  # Limite inférieure à -100 V

# ISO 7637-2 Sévérité III
V_ISO_III_upper = np.full_like(t_ISO, 37)     # Limite supérieure à +37 V
V_ISO_III_lower = np.full_like(t_ISO, -150)   # Limite inférieure à -150 V

# ISO 7637-2 Sévérité IV
V_ISO_IV_upper = np.full_like(t_ISO, 75)      # Limite supérieure à +75 V
V_ISO_IV_lower = np.full_like(t_ISO, -200)    # Limite inférieure à -200 V

# --------------------
# Tracé du graphique
# --------------------

fig, ax = plt.subplots(figsize=(12, 6))

# Tracé des limites MIL-STD-1275-F/E
ax.plot(t_MIL * 1e3, V_upper_MIL_F, color='black', label='MIL-STD-1275-F/E')
ax.plot(t_MIL * 1e3, V_lower_MIL_F, color='black')

# Tracé des limites MIL-STD-1275-D
ax.plot(t_MIL * 1e3, V_upper_MIL_D, color='blue', linestyle='--', label='MIL-STD-1275-D')
ax.plot(t_MIL * 1e3, V_lower_MIL_D, color='blue', linestyle='--')

# Remplissage des zones interdites pour MIL-STD-1275-F/E
ax.fill_between(t_MIL * 1e3, V_upper_MIL_F, ax.get_ylim()[1], where=(V_upper_MIL_F <= ax.get_ylim()[1]), color='gray', alpha=0.5)
ax.fill_between(t_MIL * 1e3, V_lower_MIL_F, ax.get_ylim()[0], where=(V_lower_MIL_F >= ax.get_ylim()[0]), color='gray', alpha=0.5)

# Remplissage des zones entre MIL-STD-1275-F/E et D
ax.fill_between(t_MIL * 1e3, V_upper_MIL_D, V_upper_MIL_F, where=(V_upper_MIL_D <= V_upper_MIL_F), color='gray', alpha=0.3)
ax.fill_between(t_MIL * 1e3, V_lower_MIL_D, V_lower_MIL_F, where=(V_lower_MIL_D >= V_lower_MIL_F), color='gray', alpha=0.3)

# Tracé des ISO 7637-2 Sévérité I/II
ax.plot(t_ISO * 1e3, V_ISO_I_II_upper, color='green', linestyle='-', label='ISO 7637-2 Sévérité I/II')
ax.plot(t_ISO * 1e3, V_ISO_I_II_lower, color='green', linestyle='-')

# Tracé des ISO 7637-2 Sévérité III
ax.plot(t_ISO * 1e3, V_ISO_III_upper, color='orange', linestyle='-', label='ISO 7637-2 Sévérité III')
ax.plot(t_ISO * 1e3, V_ISO_III_lower, color='orange', linestyle='-')

# Tracé des ISO 7637-2 Sévérité IV
ax.plot(t_ISO * 1e3, V_ISO_IV_upper, color='red', linestyle='-', label='ISO 7637-2 Sévérité IV')
ax.plot(t_ISO * 1e3, V_ISO_IV_lower, color='red', linestyle='-')

# Personnalisation du graphique
ax.set_xlabel('Temps (ms)')
ax.set_ylabel('Tension (V)')
ax.set_title('Comparaison des normes MIL-STD-1275-F/E et D avec ISO 7637-2')
ax.grid(True)

# Affichage de la légende
ax.legend(loc='upper right')

# Ajustement des limites de l'axe des Y pour couvrir uniquement la partie utile
ax.set_ylim(-210, 110)

# Ajustement des limites de l'axe des X
ax.set_xlim(0, 1000)

# Affichage du graphique
plt.show()
