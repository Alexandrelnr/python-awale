import random

# Plateau : 6 cases par joueur, 4 graines par case
plateau = [4] * 12
scores = [0, 0]

def afficher_plateau():
    print("\n")
    print("   ", plateau[11], plateau[10], plateau[9], plateau[8], plateau[7], plateau[6])
    print("   ", plateau[0], plateau[1], plateau[2], plateau[3], plateau[4], plateau[5])
    print(f"\nScore Joueur : {scores[0]} | Score IA : {scores[1]}\n")

def distribuer(case):
    graines = plateau[case]
    plateau[case] = 0

    i = case
    while graines > 0:
        i = (i + 1) % 12
        plateau[i] += 1
        graines -= 1

    return i

def capturer(dernier, joueur):
    captures = 0

    while True:
        if joueur == 0 and 6 <= dernier <= 11:
            pass
        elif joueur == 1 and 0 <= dernier <= 5:
            pass
        else:
            break

        if plateau[dernier] in [2, 3]:
            captures += plateau[dernier]
            plateau[dernier] = 0
            dernier = (dernier - 1) % 12
        else:
            break

    scores[joueur] += captures

def tour_joueur():
    while True:
        try:
            case = int(input("Choisis une case (1-6) : ")) - 1

            if 0 <= case <= 5 and plateau[case] > 0:
                dernier = distribuer(case)
                capturer(dernier, 0)
                break

            print("Case invalide.")
        except ValueError:
            print("Entre un nombre.")

def tour_ia():
    coups = [i for i in range(6, 12) if plateau[i] > 0]

    if not coups:
        return

    case = random.choice(coups)
    print(f"L'IA joue la case {12 - case}")

    dernier = distribuer(case)
    capturer(dernier, 1)

def partie_finie():
    return (
        scores[0] >= 25
        or scores[1] >= 25
        or all(x == 0 for x in plateau[:6])
        or all(x == 0 for x in plateau[6:])
    )

def gagnant():
    print("\nFin de partie !")
    print(f"Joueur : {scores[0]} points")
    print(f"IA : {scores[1]} points")

    if scores[0] > scores[1]:
        print("Tu as gagné !")
    elif scores[1] > scores[0]:
        print("L'IA a gagné !")
    else:
        print("Égalité !")

print("=== AWALE PYTHON ===")

while not partie_finie():
    afficher_plateau()
    tour_joueur()

    if partie_finie():
        break

    tour_ia()

afficher_plateau()
gagnant()
