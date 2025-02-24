import numpy as np
import matplotlib.pyplot as plt

# --------------------
# Données pour la MIL-STD-1275-F/E
# --------------------

# Définition de l'axe des temps de -10 µs à 1000 µs
t_pre = np.linspace(-10e-6, 0, 500)        # De -10 µs à 0 µs
t1 = np.linspace(0, 70e-6, 1000)           # De 0 à 70 µs
t2 = np.linspace(70e-6, 1e-3, 1000)        # De 70 µs à 1000 µs

# Limite supérieure pour MIL-STD-1275-F/E
V_pre_upper = np.full_like(t_pre, 0)                # Zéro avant le début
V_upper1 = np.full_like(t1, 250)                    # 250 V de 0 à 70 µs
V_upper2 = np.linspace(250, 100, len(t2))           # Descente linéaire de 250 V à 100 V de 70 µs à 1000 µs

# Limite inférieure pour MIL-STD-1275-F/E
V_pre_lower = np.full_like(t_pre, 0)                # Zéro avant le début
V_lower1 = np.full_like(t1, -250)                   # -250 V de 0 à 70 µs
V_lower2 = np.linspace(-250, 18, len(t2))           # Montée linéaire de -250 V à 18 V de 70 µs à 1000 µs

# Concatenation des tableaux de temps et de tension pour MIL-STD-1275-F/E
t_F = np.concatenate((t_pre, t1, t2))
V_upper_F = np.concatenate((V_pre_upper, V_upper1, V_upper2))
V_lower_F = np.concatenate((V_pre_lower, V_lower1, V_lower2))

# --------------------
# Données pour la MIL-STD-1275-D
# --------------------

# Limite supérieure pour MIL-STD-1275-D
V_upper2_D = np.linspace(250, 40, len(t2))          # Descente linéaire de 250 V à 40 V de 70 µs à 1000 µs
V_upper_D = np.concatenate((V_pre_upper, V_upper1, V_upper2_D))

# Limite inférieure pour MIL-STD-1275-D
V_lower2_D = np.linspace(-250, -40, len(t2))        # Montée linéaire de -250 V à -40 V de 70 µs à 1000 µs
V_lower_D = np.concatenate((V_pre_lower, V_lower1, V_lower2_D))

# --------------------
# Données pour les ISO 7637-2
# --------------------

# Axe des temps pour les ISO 7637-2
t_ISO = np.linspace(0, 1e-3, 1000)  # De 0 à 1000 µs

# Sévérité I/II : +100 V et -100 V
V_ISO_I_II_upper = np.full_like(t_ISO, 100)
V_ISO_I_II_lower = np.full_like(t_ISO, -100)

# Sévérité III : +150 V et -150 V
V_ISO_III_upper = np.full_like(t_ISO, 150)
V_ISO_III_lower = np.full_like(t_ISO, -150)

# Sévérité IV : +200 V et -200 V
V_ISO_IV_upper = np.full_like(t_ISO, 200)
V_ISO_IV_lower = np.full_like(t_ISO, -200)

# --------------------
# Tracé du graphique
# --------------------

plt.figure(figsize=(12, 6))

# Tracé des limites MIL-STD-1275-F/E
plt.plot(t_F * 1e6, V_upper_F, color='black', label='MIL-STD-1275-F/E')
plt.plot(t_F * 1e6, V_lower_F, color='black')

# Tracé des limites MIL-STD-1275-D
plt.plot(t_F * 1e6, V_upper_D, color='blue', linestyle='--', label='MIL-STD-1275-D')
plt.plot(t_F * 1e6, V_lower_D, color='blue', linestyle='--')

# Remplissage des zones interdites pour MIL-STD-1275-F/E
plt.fill_between(t_F * 1e6, V_upper_F, plt.ylim()[1], where=(V_upper_F <= plt.ylim()[1]), color='gray', alpha=0.5)
plt.fill_between(t_F * 1e6, V_lower_F, plt.ylim()[0], where=(V_lower_F >= plt.ylim()[0]), color='gray', alpha=0.5)

# Remplissage des zones entre MIL-STD-1275-F/E et D
plt.fill_between(t_F * 1e6, V_upper_D, V_upper_F, where=(V_upper_D <= V_upper_F), color='gray', alpha=0.3)
plt.fill_between(t_F * 1e6, V_lower_D, V_lower_F, where=(V_lower_D >= V_lower_F), color='gray', alpha=0.3)

# Tracé des ISO 7637-2 Sévérité I/II
plt.plot(t_ISO * 1e6, V_ISO_I_II_upper, color='green', linestyle='-', label='ISO 7637-2 Sévérité I/II')
plt.plot(t_ISO * 1e6, V_ISO_I_II_lower, color='green', linestyle='-')

# Tracé des ISO 7637-2 Sévérité III
plt.plot(t_ISO * 1e6, V_ISO_III_upper, color='orange', linestyle='-', label='ISO 7637-2 Sévérité III')
plt.plot(t_ISO * 1e6, V_ISO_III_lower, color='orange', linestyle='-')

# Tracé des ISO 7637-2 Sévérité IV
plt.plot(t_ISO * 1e6, V_ISO_IV_upper, color='red', linestyle='-', label='ISO 7637-2 Sévérité IV')
plt.plot(t_ISO * 1e6, V_ISO_IV_lower, color='red', linestyle='-')

# Ajustement des limites de l'axe des Y pour inclure toutes les courbes
plt.ylim(-350, 350)

# Ajustement des limites de l'axe des X
plt.xlim(-10, 1000)

# Ajout des lignes pointillées horizontales avec annotations
# Mise à jour : suppression des lignes à 200 V, 100 V, -100 V et -200 V
y_values = [250, -250, 150, -150, 40, -40, 18]
for y in y_values:
    plt.axhline(y=y, color='gray', linestyle='dotted')
    # Déplacer les annotations un peu plus à droite
    plt.text(plt.xlim()[0] + 20, y, f'{y} V', verticalalignment='bottom' if y > 0 else 'top', color='gray', fontsize=9)

# Ajout de la ligne pointillée verticale à 70 µs avec annotation
plt.axvline(x=70, color='gray', linestyle='dotted')
plt.text(70, plt.ylim()[0] + 10, '70 µs', horizontalalignment='center', verticalalignment='bottom', rotation=0, color='gray', fontsize=9)

# Personnalisation du graphique
plt.xlabel('Temps (µs)')
plt.ylabel('Tension (V)')
plt.title('Comparaison des normes MIL-STD-1275-F/E et D avec ISO 7637-2')
plt.grid(True)

# Affichage de la légende
plt.legend(loc='upper right')

# Affichage du graphique
plt.show()
