import numpy as np
import matplotlib.pyplot as plt

# --------------------
# Données pour la MIL-STD-1275-F/E
# --------------------

# Définition de l'axe des temps de -10 µs à 1000 µs
t_pre = np.linspace(-10e-6, 0, 500)        # De -10 µs à 0 µs
t1 = np.linspace(0, 70e-6, 1000)           # De 0 à 70 µs
t2 = np.linspace(70e-6, 1e-3, 1000)        # De 70 µs à 1000 µs (1 ms)

# Limite supérieure
V_pre_upper = np.full_like(t_pre, 0)       # Zéro avant le début
V_upper1 = np.full_like(t1, 250)           # 250 V de 0 à 70 µs
V_upper2 = np.linspace(250, 100, len(t2))  # Descente linéaire de 250 V à 100 V de 70 µs à 1 ms

# Limite inférieure
V_pre_lower = np.full_like(t_pre, 0)       # Zéro avant le début
V_lower1 = np.full_like(t1, -250)          # -250 V de 0 à 70 µs
V_lower2 = np.linspace(-250, 18, len(t2))  # Montée linéaire de -250 V à 18 V de 70 µs à 1 ms

# Concatenation des tableaux de temps et de tension
t = np.concatenate((t_pre, t1, t2))
V_upper = np.concatenate((V_pre_upper, V_upper1, V_upper2))
V_lower = np.concatenate((V_pre_lower, V_lower1, V_lower2))

# --------------------
# Données pour les pulses ISO
# --------------------

# ISO Pulse 2a : Spike à 50 µs de 37 V à 112 V
t_pulse_2a = np.array([50e-6, 50e-6])
V_pulse_2a = np.array([37, 112])

# ISO Pulse 3a : Spike à 0.15 µs de -150 V à -300 V
t_pulse_3a = np.array([0.15e-6, 0.15e-6])
V_pulse_3a = np.array([-150, -300])

# ISO Pulse 3b : Spike à 0.15 µs de +150 V à +300 V
t_pulse_3b = np.array([0.15e-6, 0.15e-6])
V_pulse_3b = np.array([150, 300])

# --------------------
# Tracé du graphique
# --------------------

plt.figure(figsize=(12, 6))

# Tracé des limites supérieure et inférieure avec une seule légende
plt.plot(t * 1e6, V_upper, color='black')
plt.plot(t * 1e6, V_lower, color='black', label='MIL-STD-1275-F/E')

# Remplissage de la zone interdite en haut (au-dessus de V_upper)
plt.fill_between(t * 1e6, V_upper, plt.ylim()[1], where=(V_upper <= plt.ylim()[1]), color='gray', alpha=0.5)

# Remplissage de la zone interdite en bas (en-dessous de V_lower)
plt.fill_between(t * 1e6, V_lower, plt.ylim()[0], where=(V_lower >= plt.ylim()[0]), color='gray', alpha=0.5)

# Tracé des pulses ISO
plt.plot(t_pulse_2a * 1e6, V_pulse_2a, color='blue', marker='o', linestyle='-', label='ISO Pulse 2a')
plt.plot(t_pulse_3a * 1e6, V_pulse_3a, color='red', marker='o', linestyle='-', label='ISO Pulse 3a')
plt.plot(t_pulse_3b * 1e6, V_pulse_3b, color='green', marker='o', linestyle='-', label='ISO Pulse 3b')

# Ajustement des limites de l'axe des Y pour inclure les pulses
plt.ylim(-350, 350)  # Ajustez les valeurs si nécessaire pour inclure tous les pulses

# Ajustement des limites de l'axe des X
plt.xlim(-10, 1000)  # De -10 µs à 1000 µs

# Ajout des lignes pointillées horizontales avec annotations
y_values = [250, -250, 18]
for y in y_values:
    plt.axhline(y=y, color='gray', linestyle='dotted')
    # Ajouter l'annotation sur l'axe Y à gauche, légèrement décalée vers l'intérieur
    plt.text(plt.xlim()[0] + 5, y, f'{y} V', verticalalignment='bottom' if y > 0 else 'top', color='gray', fontsize=9)

# Ajout de la ligne pointillée verticale à 70 µs avec annotation
plt.axvline(x=70, color='gray', linestyle='dotted')
# Ajouter l'annotation sur l'axe X en bas, légèrement décalée vers le haut
plt.text(70, plt.ylim()[0] + 10, '70 µs', horizontalalignment='center', verticalalignment='bottom', rotation=0, color='gray', fontsize=9)

# Personnalisation du graphique
plt.xlabel('Temps (µs)')
plt.ylabel('Tension (V)')
plt.title('MIL-STD-1275-F/E avec ISO Pulses')
plt.grid(True)

# Affichage de la légende
plt.legend(loc='upper right')

# Affichage du graphique
plt.show()
