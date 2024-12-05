import random

def afficher_plateau(plateau):
    # Affiche le plateau de jeu
    print("Plateau de jeu:")
    for i in range(3):
        # Affiche chaque ligne du plateau, en joignant les cases avec " | "
        print(" | ".join(plateau[i]))
        if i < 2:
            # Affiche une ligne de séparation entre les lignes du plateau
            print("---------")
    print()

def check_victoire(plateau):
    # Vérifie si un joueur a gagné
    for i in range(3):
        # Vérifie les lignes
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != " ":
            return True
        # Vérifie les colonnes
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != " ":
            return True
    # Vérifie les diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != " ":
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != " ":
        return True
    return False

def check_match_nul(plateau):
    # Vérifie si le match est nul (aucune case vide)
    for row in plateau:
        if " " in row:
            return False
    return True


def ia_joue(plateau):
    # L'IA joue en suivant une stratégie
    # Vérifier si l'IA peut gagner
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == " ":
                plateau[i][j] = "O"  # L'IA joue "O"
                if check_victoire(plateau):
                    return  # L'IA a gagné, donc elle ne fait rien d'autre
                plateau[i][j] = " "  # Annule le coup

    # Vérifier si le joueur peut gagner et bloquer
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == " ":
                plateau[i][j] = "X"  # Le joueur joue "X"
                if check_victoire(plateau):
                    plateau[i][j] = "O"  # Bloque le coup du joueur
                    return
                plateau[i][j] = " "  # Annule le coup

    # Jouer au hasard si aucune victoire ou blocage n'est nécessaire
    while True:
        case = random.randint(0, 8)  # Choisit un numéro de case aléatoire
        x, y = divmod(case, 3)  # Convertit le numéro de case en coordonnées (x, y)
        if plateau[x][y] == " ":  # Vérifie si la case est vide
            plateau[x][y] = "O"  # L'IA joue "O"
            return
def tic_tac_toe():
    # Initialise le plateau de jeu
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur = "X"  # Le joueur commence avec "X"

    while True:
        afficher_plateau(plateau)  # Affiche le plateau actuel
        
        if joueur == "X":
            # Tour du joueur
            case = int(input(f"Joueur {joueur}, entrez un numéro de case (1-9): ")) - 1

            # Vérifie si le numéro de case est valide
            if case < 0 or case >= 9:
                print("Numéro de case invalide. Veuillez entrer un numéro entre 1 et 9.")
                continue

            x, y = divmod(case, 3)  # Convertit le numéro de case en coordonnées (x, y)

            # Vérifie si la case est déjà occupée
            if plateau[x][y] != " ":
                print("Cette case est déjà occupée. Veuillez choisir une autre case.")
                continue

            plateau[x][y] = joueur  # Le joueur joue
        else:
            # Tour de l'IA
            print("C'est le tour de l'IA.")
            ia_joue(plateau)  # L'IA joue

        # Vérifie si un joueur a gagné
        if check_victoire(plateau):
            afficher_plateau(plateau)  # Affiche le plateau final
            print(f"Joueur {joueur} a gagné !")  # Annonce le gagnant
            break

        # Vérifie si le match est nul
        if check_match 