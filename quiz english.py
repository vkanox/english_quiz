# start
while True:  # Boucle pour rejouer
    game = input("Entraînons-nous à améliorer ton anglais ! Choisissons la difficulté du quiz : Facile, Medium, Difficile : ").strip().lower()

    # score finale
    bonne_réponse = 0

    # corrige est un placeholder
    def lost(corrige):
        print("Ce n'est pas grave, tout le monde fait des erreurs. La bonne réponse est : " + corrige)

    def won():
        print("La réponse est correcte bien joué !")

    # level facile
    if game == "facile":
        piano = input("Quelle phrase est correcte ?\n"
                      "a) She plays the piano.\n"
                      "b) She play the piano.\n"
                      "c) She playing the piano.\n"
                      "Réponse : ").strip().lower()
        if piano == "a":
            won()
            bonne_réponse += 1
            print("score : 1/5")
        else:
            lost("a")

        happy = input("Quelle phrase est correcte ?\n"
                      "a) I is happy.\n"
                      "b) I am happy.\n"
                      "c) I are happy.\n"
                      "Réponse : ").strip().lower()
        if happy == "b":
            won()
            bonne_réponse += 1
            print("score : 2/5")
        else:
            lost("b")

        school = input("Quelle phrase est correcte ?\n"
                       "a) He walk to school.\n"
                       "b) He walks to school.\n"
                       "c) He walking to school.\n"
                       "Réponse : ").strip().lower()
        if school == "b":
            won()
            bonne_réponse += 1
            print("score : 3/5")
        else:
            lost("b")

        apple = input("Quelle phrase est correcte ?\n"
                      "a) I have a apple in my bag.\n"
                      "b) I have an apple in my bag.\n"
                      "c) I have the apple in my bag.\n"
                      "Réponse : ").strip().lower()
        if apple == "b":
            won()
            bonne_réponse += 1
            print("score : 4/5")
        else:
            lost("b")

        color = input("Quelle phrase est correcte ?\n"
                      "a) The sky is blue.\n"
                      "b) The sky are blue.\n"
                      "c) The sky is blues.\n"
                      "Réponse : ").strip().lower()
        if color == "a":
            won()
            bonne_réponse += 1
            print("score : 5/5")
        else:
            lost("a")

        print(f"Ton score final est de : {bonne_réponse}/5")

    # level medium
    elif game == "medium":
        dog = input("Quelle phrase est correcte ?\n"
                    "a) The dog run fast.\n"
                    "b) The dog runs fast.\n"
                    "c) The dog running fast.\n"
                    "Réponse : ").strip().lower()
        if dog == "b":
            won()
            bonne_réponse += 1
            print("score : 1/5")
        else:
            lost("b")

        friend = input("Quelle phrase est correcte ?\n"
                       "a) My friend is a doctor.\n"
                       "b) My friend are a doctor.\n"
                       "c) My friend am a doctor.\n"
                       "Réponse : ").strip().lower()
        if friend == "a":
            won()
            bonne_réponse += 1
            print("score : 2/5")
        else:
            lost("a")

        play = input("Quelle phrase est correcte ?\n"
                     "a) We plays football on Sundays.\n"
                     "b) We play football on Sundays.\n"
                     "c) We playing football on Sundays.\n"
                     "Réponse : ").strip().lower()
        if play == "b":
            won()
            bonne_réponse += 1
            print("score : 3/5")
        else:
            lost("b")

        eat = input("Quelle phrase est correcte ?\n"
                    "a) I eats breakfast at 8 AM.\n"
                    "b) I eat breakfast at 8 AM.\n"
                    "c) I eating breakfast at 8 AM.\n"
                    "Réponse : ").strip().lower()
        if eat == "b":
            won()
            bonne_réponse += 1
            print("score : 4/5")
        else:
            lost("b")

        time = input("Quelle phrase est correcte ?\n"
                     "a) What time is it?\n"
                     "b) What time are it?\n"
                     "c) What time am it?\n"
                     "Réponse : ").strip().lower()
        if time == "a":
            won()
            bonne_réponse += 1
            print("score : 5/5")
        else:
            lost("a")

        print(f"Ton score final est de : {bonne_réponse}/5")

    # level difficile
    elif game == "difficile":
        who = input("Quelle phrase est correcte ?\n"
                    "a) Who is the best player in the team?\n"
                    "b) Who are the best player in the team?\n"
                    "c) Who am the best player in the team?\n"
                    "Réponse : ").strip().lower()
        if who == "a":
            won()
            bonne_réponse += 1
            print("score : 1/5")
        else:
            lost("a")

        have = input("Quelle phrase est correcte ?\n"
                     "a) They have been to Paris last year.\n"
                     "b) They has been to Paris last year.\n"
                     "c) They had been to Paris last year.\n"
                     "Réponse : ").strip().lower()
        if have == "c":
            won()
            bonne_réponse += 1
            print("score : 2/5")
        else:
            lost("c")

        will = input("Quelle phrase est correcte ?\n"
                     "a) I will go to the store tomorrow.\n"
                     "b) I goes to the store tomorrow.\n"
                     "c) I go to the store tomorrow.\n"
                     "Réponse : ").strip().lower()
        if will == "a":
            won()
            bonne_réponse += 1
            print("score : 3/5")
        else:
            lost("a")

        read = input("Quelle phrase est correcte ?\n"
                     "a) She readed the book last night.\n"
                     "b) She reads the book last night.\n"
                     "c) She read the book last night.\n"
                     "Réponse : ").strip().lower()
        if read == "c":
            won()
            bonne_réponse += 1
            print("score : 4/5")
        else:
            lost("c")

        complete = input("Quelle phrase est correcte ?\n"
                         "a) He completed the project on time.\n"
                         "b) He complete the project on time.\n"
                         "c) He completes the project on time.\n"
                         "Réponse : ").strip().lower()
        if complete == "a":
            won()
            bonne_réponse += 1
            print("score : 5/5")
        else:
            lost("a")

        print(f"Ton score final est de : {bonne_réponse}/5")

    else:
        print("Tu n'as pas choisi la bonne difficulté.")

    # Demande à l'utilisateur s'il veut rejouer
    rejouer = input("Veux-tu rejouer ? (oui/non) : ").strip().lower()
    if rejouer != "oui":
        print("Merci d'avoir joué ! À bientôt.")
        break