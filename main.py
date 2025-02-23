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
    
    print("Bienvenue sur l'Autoclicker Snap fait par Kosmos !")
    print("")
    print("Ce programme permet d'automatiser l'envoi de snaps afin d'augmenter votre score Snapchat facilement.")
    print("")
    print("Comment ça marche ?")
    print("1/ Initialisation : Vous devez enregistrer les positions des boutons Snapchat (prise de photo, envoi, sélection des contacts…).")
    print("2/ Lancement : Une fois les positions enregistrées, le programme clique automatiquement sur ces boutons à intervalles réguliers.")
    print("3️/ Arrêt : Appuyez sur la touche ESC pour arrêter l’autoclicker à tout moment.")
    print("")
    print("Fonctionnel sur snapchat Web et sur émulateur (BlueStack...)")
    print("Commandes : n pour mettre en pause\n echap pour quitter le programme\n r pour reprendre si programme en pause\nAPPUYEZ SUR LA TOUCHE p POUR LES COORDONNEES SI DEMANDEE")



def position():
    pos = []
    print('Récupération des positions pour prise de la photo, Appuyez sur la touche p pour commencer')
    
    while True:
        if keyboard.is_pressed('p'):
            x, y = pyautogui.position()
            pos.append({"X":x, "Y":y})
            print('Position récupérée avec succès !')
            break

    time.sleep(0.1)
    print('Récupération des positions pour envoyer snap. Appuyez sur la touche p pour commencer')
    
    while True:
        if keyboard.is_pressed('p'):
            x, y = pyautogui.position()
            pos.append({"X": x, "Y": y})
            print('Position récupérée avec succès !')
            break
    
    time.sleep(0.1)
    print('Récupération position pour séléctionner le raccourcis. Appuyez sur la touche p pour commencer')

    while True:
        if keyboard.is_pressed('p'):
            x, y = pyautogui.position()
            pos.append({"X": x, "Y": y})
            print('Position récupérée avec succès !')
            break
    
    time.sleep(0.1)
    print('Récupération position pour séléctionner tous les utilisateurs du raccourcis. Appuyez sur la touche p pour commencer')
    
    while True:
            if keyboard.is_pressed('p'):
                x, y = pyautogui.position()
                pos.append({"X": x, "Y": y})
                print('Position récupérée avec succès !')
                break
            
    time.sleep(0.1)
    print('Récupération position pour envoyer à tous les utilisateurs du raccourcis. Appuyez sur la touche p pour commencer')
    
    while True:
            if keyboard.is_pressed('p'):
                x, y = pyautogui.position()
                pos.append({"X": x, "Y": y})
                print('Position récupérée avec succès !')
                break
    return pos


def autoclicker(delais):
    running = True
    paused = False
    positions = position()
    pos = 0
    print("Préparez vous, l'autoclicker va démarrer !")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
        
    while running:
        if keyboard.is_pressed("n"):
            paused = True
    
        if not paused:
            pyautogui.click(positions[pos]['X'], positions[pos]['Y'])
            pos += 1
            if pos == len(positions):
                pos = 0
            time.sleep(delais)
        else:
            keyboard.wait("r")
            paused = False 
            print("Reprise du programme")
            
        if keyboard.is_pressed("esc"):
            running = False
    
def main():
    bienvenue()
    delais = float(input("Veuillez entrer le délais entre chaque click (en secondes): "))
    print('Parfait !')
    
    autoclicker(delais)
    

if __name__ == '__main__':
    main()