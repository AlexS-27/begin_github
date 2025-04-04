import tkinter as tk
import subprocess
import os
import webbrowser

#game's dictionnary (name and path)
games = {}

#function to start the game
def launch_game(game_name):
    path = games[game_name]
    if path.endswith(".html"):
        # start the html game in the web host
        abs_path = os.path.abspath(path)
        webbrowser.open(f"file://{abs_path}")
    elif path.endswith(".exe"):
        # start the pc game
        subprocess.Popen([os.path.abspath(path)])

#graphic
root = tk.Tk()
root.title("Game Launcher")
root.geometry("400x400")
root.configure(bg="#222")


