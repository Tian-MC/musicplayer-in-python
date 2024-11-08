import pygame
import os
import random

current_volume = 0.01

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(current_volume)
    pygame.mixer.music.play()

def play_next_music(music_files):
    next_music = random.choice(music_files)
    play_music(next_music)

def play_previous_music(music_files):
    next_music = random.choice(music_files)
    play_music(next_music)

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def set_music_volume(volume):
    global current_volume
    current_volume = volume
    pygame.mixer.music.set_volume(volume)

def main():
    pygame.init()
    pygame.mixer.init()

    music_folder = "./musica"

    try:
        music_files = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith('.mp3', '.flac', '.wav', '.m4v', '.mp4')]
        if not music_files:
            raise FileNotFoundError("Nessun file musicale trovato nella cartella 'musica'.")
    except FileNotFoundError as e:
        print(e)
        create_folder = input("Vuoi creare una cartella 'musica' ora? (sì/no): ").lower()
        if create_folder == "sì" or create_folder == "si":
            os.makedirs(music_folder, exist_ok=True)
            print("Cartella 'musica' creata. Aggiungi i tuoi file musicali e riavvia il programma.")
        return

    random.shuffle(music_files)
    play_music(random.choice(music_files))

    while True:
        command = input("Inserisci il comando (stop (1) pause (2) unpause (3) skip (4) prev (5) \"volume\" (0 == 1)): ").lower()
        if command == "1":
            stop_music()
            break
        elif command == "2":
            pause_music()
        elif command == "3":
            unpause_music()
        elif command == "4":
            play_next_music(music_files)
        elif command == "5":
            play_previous_music(music_files)
        elif command.startswith("volume"):
            parts = command.split(" ")
            if len(parts) >= 2:
                try:
                    new_volume = float(parts[1])
                    set_music_volume(new_volume)
                except ValueError:
                    print("Inserisci un valore numerico valido per il volume.")
            else:
                print("Inserisci un valore per il volume.")
        else:
            print("Comando non valido. Riprova.")

if __name__ == "__main__":
    main()
