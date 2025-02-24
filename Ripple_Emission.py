import numpy as np
import matplotlib.pyplot as plt

# Axe du temps de 0 à 8 ms pour les données
t_data = np.linspace(0, 8e-3, 4000)  # De 0 à 8 ms

# Axe du temps complet de 0 à 10 ms pour l'axe des X
t_total = np.linspace(0, 10e-3, 5000)

# Paramètres de l'oscillation
f = 1e3  # Fréquence d'oscillation en Hz
omega = 2 * np.pi * f

# Informations des deux courbes
courbes = [
    {
        'nom': 'MIL-STD-1275-F',
        'couleur': 'blue',
        'V_haute': 31,
        'V_basse': 22,
        'oscillation': 2,  # Amplitude +/-2V
    },
    {
        'nom': 'MIL-STD-1275-F',
        'couleur': 'red',
        'V_haute': 30,
        'V_basse': 25,
        'oscillation': 2,
    },
]

# Création du graphique
plt.figure(figsize=(15, 8))

for courbe in courbes:
    # Calcul de la tension haute
    V_haute_centrale = courbe['V_haute']
    V_haute_amplitude = courbe['oscillation']
    V_haute = V_haute_centrale + V_haute_amplitude * np.sin(omega * t_data)
    
    # Calcul de la tension basse
    V_basse_centrale = courbe['V_basse']
    V_basse_amplitude = courbe['oscillation']
    V_basse = V_basse_centrale + V_basse_amplitude * np.sin(omega * t_data)
    
    # Tracé des tensions centrales en pointillé
    plt.hlines(V_haute_centrale, 0, 8e-3, colors=courbe['couleur'], linestyles='dashed')
    plt.hlines(V_basse_centrale, 0, 8e-3, colors=courbe['couleur'], linestyles='dashed')
    
    # Tracé des oscillations hautes et basses
    plt.plot(t_data, V_haute, color=courbe['couleur'], label=f"{courbe['nom']} - Tension haute")
    plt.plot(t_data, V_basse, color=courbe['couleur'], linestyle='--', label=f"{courbe['nom']} - Tension basse")

# Ajout des limites hautes et basses (si nécessaire)
limite_haute = max([courbe['V_haute'] + courbe['oscillation'] for courbe in courbes]) + 1
limite_basse = min([courbe['V_basse'] - courbe['oscillation'] for courbe in courbes]) - 1



# Ajustement des axes
plt.xlim(0, 10e-3)  # Axe des X de 0 à 10 ms
plt.ylim(limite_basse - 1, limite_haute + 1)  # Ajusté pour inclure toutes les tensions

# Légendes et titres
plt.xlabel('Temps (s)')
plt.ylabel('Tension (V)')
plt.title('Comparaison des exigences "émission d''oscillation" entre la 1275 F et D')
plt.legend(loc='center right')  # Placement de la légende entre 8 ms et 10 ms
plt.grid(True)

# Affichage du graphique
plt.show()
