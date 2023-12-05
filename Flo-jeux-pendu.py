import random

mots = ["python", "pendu", "molengeek", "belgique", "jeux", "pomme"]

mot_a_deviner = random.choice(mots)
lettres_trouvees = []
tentatives_restantes = 10

print(f"Le mot à deviner fait {len(mot_a_deviner)} lettres.")

while tentatives_restantes > 0:
    mot_cache = ""
    for lettre in mot_a_deviner:
        if lettre in lettres_trouvees:
            mot_cache += lettre + " "
        else:
            mot_cache += " _ "

    print(f"Mot caché : {mot_cache}")
    print(f"Il vous reste {tentatives_restantes} chances sur 10.")

    lettre = input("Devinez une lettre : ").lower()

    if len(lettre) == 1 :
        if lettre in mot_a_deviner:
            print(f"La lettre '{lettre}' est dans le mot.")
            if lettre not in lettres_trouvees:
                lettres_trouvees.append(lettre)
        else:
            print(f"La lettre : {lettre} est pas dans le mot.")
        
        if lettre in lettres_trouvees == lettre in mot_a_deviner :
            print("Bravo, vous avez réussi")
        
        tentatives_restantes -= 1


if tentatives_restantes <= 0:
    print(f"Dommage, vous avez épuisé vos chances. Le mot était : '{mot_a_deviner}'.")

