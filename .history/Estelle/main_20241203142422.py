def afficher_plateau(plateau):
    print("Plateau de jeu:")
    for i in range(3):
        print(" | ".join(plateau[i]))
        if i < 2:
            print("---------")
    print()

def check_victoire(plateau):
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != " ":
            return True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != " ":
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != " ":
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != " ":
        return True
    return False

def check_match_nul(plateau):
    for row in plateau:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur = "X"  

    while True:
        afficher_plateau(plateau)
        case = int(input(f"Joueur {joueur}, entrez un numéro de case (1-9): ")) - 1

        if case < 0 or case >= 9:
            print("Numéro de case invalide. Veuillez entrer un numéro entre 1 et 9.")
            continue

        x, y = divmod(case, 3)

        if plateau[x][y] != " ":
            print("Cette case est déjà occupée. Veuillez choisir une autre case.")
            continue

        plateau[x][y] = joueur

        if check_victoire(plateau):
            afficher_plateau(plateau)
            print(f"Joueur {joueur} a gagné !")
            break

        if check_match_nul(plateau):
            afficher_plateau(plateau)
            print("Match nul !")
            break

        joueur = "O" if joueur == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe() 