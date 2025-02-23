import pyautogui
import keyboard
import time

def bienvenue():
    print(r"""
    ----------------------------------------------------------------------------
    _____                                 _             _ _      _
    /  ___|                               | |           | (_)    | |
    \ `--. _ __   __ _ _ __     __ _ _   _| |_ ___   ___| |_  ___| | _____ _ __
    `--. \ '_ \ / _` | '_ \   / _` | | | | __/ _ \ / __| | |/ __| |/ / _ \ '__|
    /\__/ / | | | (_| | |_) | | (_| | |_| | || (_) | (__| | | (__|   <  __/ |
    \____/|_| |_|\__,_| .__/   \__,_|\__,_|\__\___/ \___|_|_|\___|_|\_\___|_|
                    | |
                    |_|
    """)
    
    print("Autoclicker pour boost son score SnapChat fait par Kosmos !")
    print("")
    print("Ce programme permet d'automatiser l'envoi de snaps afin d'augmenter votre score Snapchat facilement.")
    print("")
    print("Comment ça marche ?")
    print("1/ Initialisation : Vous devez enregistrer les positions des boutons Snapchat (prise de photo, envoi, sélection du raccourcis pour l'envoi...).")
    print("2/ Lancement : Une fois les positions enregistrées, le programme enverra automatiquement des snaps, l'utilisateur peut chosisir de mettre pause avec n ou arrêter avec ECHAP")
    print("3️/ Arrêt : Appuyez sur la touche ESC pour arrêter l’autoclicker à tout moment.")
    print("")
    print("Fonctionnel sur snapchat Web et sur émulateur (BlueStack...)")
    print("-----------------------------------------------------------------")
    print("Commandes :\n- N pour mettre en pause\n- ECHAP pour quitter le programme\n- R pour reprendre si programme en pause\n- P pour les coordonnées si demandé")
    print("-----------------------------------------------------------------")
    print("Conseils : Ajoutez des utilisateurs à un raccourcis snap pour l'envoi de snap, nécéssaire au bon fonctionnement du programme, plus il y a de monde dans votre raccourcis plus le score augmentera plus vite.")
    print("-----------------------------------------------------------------")

def position():
    pos = []
    print('Récupération des positions pour prise de la photo, Appuyez sur la touche p pour commencer')
    
    while True:
        if keyboard.is_pressed('p'):
            x, y = pyautogui.position()
            pos.append({"X":x, "Y":y})
            print('Position récupérée avec succès !')
            print('-------------------------------------------')
            break

    time.sleep(1)
    print('Récupération des positions pour envoyer snap. Appuyez sur la touche p pour commencer')
    
    while True:
        if keyboard.is_pressed('p'):
            x, y = pyautogui.position()
            pos.append({"X": x, "Y": y})
            print('Position récupérée avec succès !')
            print('-------------------------------------------')
            break
    
    time.sleep(1)
    print('Récupération position pour séléctionner le raccourcis. Appuyez sur la touche p pour commencer')

    while True:
        if keyboard.is_pressed('p'):
            x, y = pyautogui.position()
            pos.append({"X": x, "Y": y})
            print('Position récupérée avec succès !')
            print('-------------------------------------------')
            break
    
    time.sleep(1)
    print('Récupération position pour séléctionner tous les utilisateurs du raccourcis. Appuyez sur la touche p pour commencer')
    
    while True:
            if keyboard.is_pressed('p'):
                x, y = pyautogui.position()
                pos.append({"X": x, "Y": y})
                print('Position récupérée avec succès !')
                print('-------------------------------------------')
                break
            
    time.sleep(1)
    print('Récupération position pour envoyer à tous les utilisateurs du raccourcis. Appuyez sur la touche p pour commencer')
    
    while True:
            if keyboard.is_pressed('p'):
                x, y = pyautogui.position()
                pos.append({"X": x, "Y": y})
                print('Position récupérée avec succès !')
                print('-------------------------------------------')
                break
    return pos


def autoclicker(positions, delais=1):
    paused = False
    pos = 0
    print("Préparez vous, l'autoclicker va démarrer ! Appuyez sur N pour le mettre en pause, R pour reprendre, et ECHAP pour l'arrêter")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
        
    while True:
        if keyboard.is_pressed("esc"):
            print("Autoclicker arrêté.")
            break
            
        if keyboard.is_pressed("n") and not paused:
            paused = True
            print('Le programme est mit en pause, appuyez sur R pour reprendre.')
    
        if not paused:
            time.sleep(delais)
            pyautogui.click(positions[pos]['X'], positions[pos]['Y'])
            pos += 1
            if pos == len(positions):
                pos = 0
        else:
            if keyboard.is_pressed("r"):
                paused = False
                print("Reprise")
                
            if keyboard.is_pressed("esc"):
                print("Autoclicker arrêté.")
                break
    
def main():
    bienvenue()
    delais = float(input("Veuillez entrer le délais entre chaque click (en secondes). Le délais par défaut est de 1 seconde : "))
    autoclicker(position(), delais=delais)
    

if __name__ == '__main__':
    main()