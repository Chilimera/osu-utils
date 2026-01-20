from time import sleep
from sys import stdin, stdout
from subprocess import run
from pynput import keyboard
import os

path = 'D:\games\osu!' #osu! path
delay = 100           #delay between f2 and action, ms

def logic() -> None:
    game_path = path + '\osu!.exe'
    replays_path = path + '\Replays'

    if not os.path.exists(game_path):
        stdout.write('ERROR: File osu!.exe not found.\n')
        return 404
    elif not os.path.exists(replays_path):
        stdout.write('ERROR: Replay directory not found.\n')
        return 404

    files = os.listdir(replays_path)

    if files:
        files = [os.path.join(replays_path, file) for file in files]
        files = [file for file in files if os.path.isfile(file)]

        latest = max(files, key=os.path.getctime)

        stdout.write(f"Latest Replay: {latest}\n")

        os.startfile(latest)
        stdout.write(f"Replay succesfully injected: {latest}\n{('-' * 10)}\n")

def main() -> None:
    stdout.write(f"osu!utils dy chilimera\nF2 - Inject Replay | PageDown - Quit\n{('-' * 10)}\n")

    def on_press(key):
        if key == keyboard.Key.f2:
            sleep(delay / 1000)
            logic()
    
    def on_release(key):
        if key == keyboard.Key.page_down:
            return False
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()