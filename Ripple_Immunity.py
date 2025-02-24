import numpy as np
import matplotlib.pyplot as plt

# Axe du temps de 0 à 8 ms pour les données
t_data = np.linspace(0, 8e-3, 4000)  # De 0 à 8 ms

# Axe du temps complet de 0 à 10 ms pour l'axe des X
t_total = np.linspace(0, 10e-3, 5000)

# Paramètres de l'oscillation
f = 1e3  # Fréquence d'oscillation en Hz
omega = 2 * np.pi * f

# Création d'une liste pour stocker les informations des courbes
courbes = [
    {
        'nom': 'MIL-STD-1275-F',
        'couleur': 'blue',
        'V_haute': 31,
        'V_basse': 22,
        'oscillation': 2,  # Amplitude +/-2V pour une oscillation crête à crête de 4V
    },
    {
        'nom': 'MIL-STD-1275-E',
        'couleur': 'green',
        'V_haute': 30,
        'V_basse': 23,
        'oscillation': 2,
    },
    {
        'nom': 'MIL-STD-1275-D',
        'couleur': 'red',
        'V_haute': 30,
        'V_basse': 25,
        'oscillation': 2,
    },
    {
        'nom': 'ISO-Code-E',
        'couleur': 'orange',
        'V_haute': 30.5,
        'V_basse': 11.5,
        'oscillation': 1.5,  # Amplitude +/-1.5V pour une oscillation crête à crête de 3V
    },
    {
        'nom': 'ISO-Code-F',
        'couleur': 'purple',
        'V_haute': 30.5,
        'V_basse': 17.5,
        'oscillation': 1.5,
    },
    {
        'nom': 'ISO-Code-G',
        'couleur': 'cyan',
        'V_haute': 30.5,
        'V_basse': 23.5,
        'oscillation': 1.5,
    },
    {
        'nom': 'ISO-Code-H',
        'couleur': 'magenta',
        'V_haute': 30.5,
        'V_basse': 19.5,
        'oscillation': 1.5,
    },
]

# Premier graphique : Tensions hautes
plt.figure(figsize=(15, 8))

for courbe in courbes:
    # Calcul de la tension haute
    V_haute_centrale = courbe['V_haute']
    V_haute_amplitude = courbe['oscillation']
    V_haute = V_haute_centrale + V_haute_amplitude * np.sin(omega * t_data)
    
    # Tracé de la tension centrale en pointillé
    plt.hlines(V_haute_centrale, 0, 8e-3, colors=courbe['couleur'], linestyles='dashed')
    
    # Tracé de l'oscillation haute
    plt.plot(t_data, V_haute, color=courbe['couleur'], label=courbe['nom'])
    
# Ajustement des axes
plt.xlim(0, 10e-3)  # Axe des X de 0 à 10 ms
plt.ylim(28, 34)    # Ajusté pour les tensions hautes

# Légendes et titres
plt.xlabel('Temps (s)')
plt.ylabel('Tension (V)')
plt.title('Comparaison des exigences d''oscillation de tension des normes MIL-STD et ISO - limite supérieure')
plt.legend(loc='center right')  # Placement de la légende entre 8 ms et 10 ms
plt.grid(True)

# Deuxième graphique : Tensions basses
plt.figure(figsize=(15, 8))

for courbe in courbes:
    # Calcul de la tension basse
    V_basse_centrale = courbe['V_basse']
    V_basse_amplitude = courbe['oscillation']
    V_basse = V_basse_centrale + V_basse_amplitude * np.sin(omega * t_data)
    
    # Tracé de la tension centrale en pointillé
    plt.hlines(V_basse_centrale, 0, 8e-3, colors=courbe['couleur'], linestyles='dashed')
    
    # Tracé de l'oscillation basse
    plt.plot(t_data, V_basse, color=courbe['couleur'], label=courbe['nom'])
    
# Ajustement des axes
plt.xlim(0, 10e-3)  # Axe des X de 0 à 10 ms
plt.ylim(10, 27)    # Ajusté pour inclure toutes les tensions basses

# Légendes et titres
plt.xlabel('Temps (s)')
plt.ylabel('Tension (V)')
plt.title('Comparaison des exigences d''oscillation de tension des normes MIL-STD et ISO - limite inférieure')
plt.legend(loc='center right')  # Placement de la légende entre 8 ms et 10 ms
plt.grid(True)

# Affichage des graphiques
plt.show()
