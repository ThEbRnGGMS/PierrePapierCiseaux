import random
import getpass
import kivy
import time

print(" ")

print("BIENVENUE DANS PierrePapierCiseau")

print(" ")

print("(1 = Pierre) (2 = Papier) (3 = Ciseaux)")

print(" ")

Partie_Mod = int(input("1V1 contre bot(Tape 1) ou contre un ami(Tape 2) : "))

if Partie_Mod > 2:
    print("Choix incorrect")
    Partie_Mod = int(input("1V1 contre bot(Tape 1) ou contre un ami(Tape 2)"))
    

    
options = ("1", "2", "3")
nbr_de_partie_gagner = 0
nbr_de_partie_perdu = 0

def rec(pieces_V, recompense):
    
    if pieces_V >= 20:
        print("Tu as gagnés un cadeau (Tu peux voir le choix de ton adversaire)")
        recompense = str(input("Veut tu dépenser 20 pièces pour ton cadeau ( o = oui ; n = non ) ???"))
        
        if recompense != 'o' or 'n':
            print("choix incorrect")
            recompense = str(input("Veut tu dépenser 20 pièces pour ton cadeau ( o = oui ; n = non ) ???"))
    
    if recompense == 'o':
        pieces_V -= 20
        print("L'adversaire va choisir",choix_ordinateur)

if Partie_Mod == 2:
  
  def demander_nom_joueur(numero):
     return input(f"Joueur {numero}, veuillez entrer votre nom : ")
  
  def choisir_action():
    while True:
        choix = getpass.getpass("Choisissez une action - 'pierre = 1', 'papier = 2' ou 'ciseaux = 3' : ").lower()
        if choix in ['1', '2', '3']:
            return choix
        else:
            print("Choix invalide. Veuillez choisir entre 'pierre', 'papier' ou 'ciseaux'.")
  
  def determiner_gagnant(joueur1, joueur2):
    if joueur1 == joueur2:
        return "égalité"
    elif (joueur1 == 1 and joueur2 == 3) or \
         (joueur1 == 2 and joueur2 == 1) or \
         (joueur1 == 3 and joueur2 == 2):
        return "joueur 1"
    else:
        return "joueur 2"

  def main():
    nom_joueur1 = demander_nom_joueur(1)
    nom_joueur2 = demander_nom_joueur(2)

    while True:
        action_joueur1 = choisir_action()
        action_joueur2 = choisir_action()
        print(f"{nom_joueur1} a choisi : {action_joueur1}")
        print(f"{nom_joueur2} a choisi : {action_joueur2}")
        gagnant = determiner_gagnant(action_joueur1, action_joueur2)
        if gagnant == "égalité":
            print("Égalité !")
        else:
            print(f"{gagnant.capitalize()} gagne cette manche !")
        
        DMD = str(input("Voulez vous jouer une autre manche ? o/n "))
        
        if(DMD == 'n'):
            break
        
        if DMD != 'o' or 'n':
            print("choix incorrect")
            DMD = str(input("Voulez vous jouer une autre manche ? o/n "))     

    print("Merci d'avoir joué !")

  if __name__ == "__main__":
    main()

if Partie_Mod == 1:
    
    pieces_V = 0
    DMD = "o"
    recompense = 'n'

    while DMD != "n":
        
        time.sleep(1)
        
        nbr_de_partie = int(input("Combien de partie souhaitez-vous jouer ? "))
        
        time.sleep(1)
        
        for _ in range(nbr_de_partie):
            
            choix_ordinateur = random.choice(options)
            rec(pieces_V, recompense)
            choix_utilisateur = input("Choisissez pierre(1), papier(2) ou ciseaux(3) : ").lower()
            
            time.sleep(1)
            
            if choix_utilisateur > '3':
                print("choix incorrect")
                choix_utilisateur = input("Choisissez pierre(1), papier(2) ou ciseaux(3) : ").lower()
            
            if choix_utilisateur == choix_ordinateur:
                print("EGALITE")
                pieces_V += 5

            elif (choix_utilisateur == "1" and choix_ordinateur == "3")or\
                (choix_utilisateur == "3" and choix_ordinateur == "2")or\
                (choix_utilisateur == "2" and choix_ordinateur == "1"):
                print("GAGNE!!!")
                pieces_V += 10
                nbr_de_partie_gagner += 1
            else:
                print("PERDU!!!")
                pieces_V -= 3
                nbr_de_partie_perdu += 1
                    
            time.sleep(1)

            print("L'adversaire a choisi", choix_ordinateur)
                
            time.sleep(1)
            
            print(" ")
            
            print("Nombre de parties gagnées :", nbr_de_partie_gagner)
            print("Nombre de parties perdues :", nbr_de_partie_perdu)
            
            print(" ")
            
            time.sleep(1)
                
            print("Tu as gagné",pieces_V,"pièces")
            
            print("  ")
            
            time.sleep(1)

        DMD = str(input("Voulez vous jouer une autre manche ? o/n "))
        
        if DMD != 'o' or 'n':
            print("choix incorrect")
            DMD = str(input("Voulez vous jouer une autre manche ? o/n "))
        
        if DMD == 'o':
            print(" ")
        
        while DMD == 'n':
            if nbr_de_partie_gagner>nbr_de_partie_perdu:
                print("Tu as gagné !!!")
            elif nbr_de_partie_gagner<nbr_de_partie_perdu:
                print("Perdu !!!")
            else:
                print("Egalité !!!")
            
            print(" ")
            
            break
