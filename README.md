# 110borwein

> **Avertissement :** Ce projet a été réalisé dans le cadre du cursus pédagogique d'**Epitech**. Il est strictement interdit de le copier, de le reproduire ou de le réutiliser (sous peine de sanctions pour triche / -42).

## Description

Le projet **110borwein** a pour objectif de calculer numériquement des intégrales spécifiques appelées "Intégrales de Borwein". L'une des particularités de ces intégrales est qu'elles valent exactement $\pi/2$ pour les premières valeurs de $n$, mais s'éloignent de cette valeur de façon inattendue à partir de $n = 15$.

Ce programme calcule la valeur de l'intégrale $I_n$ pour un $n$ donné (passé en argument) sur l'intervalle $[0, 5000]$ en découpant cet intervalle en 10 000 sous-intervalles.

La valeur de l'intégrale est évaluée à travers 3 méthodes de calcul numérique euclidien :
- La méthode des points médians (**Midpoint rule**)
- La méthode des trapèzes (**Trapezoidal rule**)
- La méthode de Simpson (**Simpson's rule**)

Le résultat de chaque méthode est affiché avec une précision à 10 décimales, suivi de la différence absolue par rapport à la constante $\pi/2$.

## Prérequis

- Python 3
- Make

## Compilation

Un `Makefile` est fourni pour générer l'exécutable :

```bash
make
```
Cela créera le script exécutable `110borwein` à la racine du dépôt.

Autres règles disponibles :
- `make clean` : Nettoie les fichiers temporaires.
- `make fclean` : Supprime les exécutables et effectue un nettoyage complet.
- `make re` : Recompile le projet.

## Utilisation

```bash
./110borwein n
```

### Paramètres
- `n` : Une constante (entier supérieur ou égal à 0) qui définit le rang de l'intégrale à calculer.

### Afficher l'aide
```bash
./110borwein -h
```

## Structure du programme

- [main.py](main.py) : Contient la logique principale du programme en Python (calcul de la fonction mathématique de Borwein $x$ et implémentation des 3 algorithmes d'intégration numérique).
- [Makefile](Makefile) : Script utilisé pour compiler le wrapper et le rendre exécutable sous la forme requise par le sujet.