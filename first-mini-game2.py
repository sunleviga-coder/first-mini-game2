# first-mini-game2

import random

def spannendes_zahlenraten():
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    
    print("\n" + "="*40)
    print("🎮 WELTKREIS DER ZAHLEN - THE ARCADE EDITION 🎮")
    print("="*40)
    print(f"Ich denke an eine Zahl zwischen 1 und 100.")
    print(f"⚠️ ACHTUNG: Du hast genau {max_attempts} Leben. Nutze sie weise!\n")

    while attempts < max_attempts:
        try:
            remaining_lives = max_attempts - attempts
            print(f"❤️ Verbleibende Leben: {remaining_lives}")
            guess = int(input("🔢 Dein Tipp: "))
            attempts += 1
            
            # Abstand zur geheimen Zahl berechnen
            abstand = abs(secret_number - guess)
            
            if guess == secret_number:
                score = (max_attempts - attempts + 1) * 100
                print("\n" + "🎉"*15)
                print(f"WARHNSINN! Du hast die Zahl {secret_number} geknackt!")
                print(f"Du hast nur {attempts} Versuche gebraucht.")
                print(f"🏆 Dein Highscore: {score} Punkte!")
                print("🎉"*15 + "\n")
                return
            
            elif guess < secret_number:
                if abstand > 20:
                    print("📉 Viel zu niedrig! Du bist meilenweit entfernt.\n")
                else:
                    print("📉 Zu niedrig! Aber du spürst schon die Wärme...\n")
                    
            elif guess > secret_number:
                if abstand > 20:
                    print("📈 Viel zu hoch! Schieß nicht über das Ziel hinaus.\n")
                else:
                    print("📈 Zu hoch! Aber du bist verdammt nah dran...\n")
                    
        except ValueError:
            print("❌ He, kein Schummeln! Gib eine echte Zahl ein.\n")

    # Wenn alle Leben aufgebraucht sind:
    print("💀 GAME OVER 💀")
    print(f"Die gesuchte Zahl war übrigens: {secret_number}")
    print("Versuch es gleich noch einmal und knack den Highscore!\n")

if __name__ == "__main__":
    spannendes_zahlenraten()
