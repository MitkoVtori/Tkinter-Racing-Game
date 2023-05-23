import tkinter as tk
import random

track_length = 800
player_position = 0
opponent_position = 0
game_started = False

def move_player(event):
    global player_position
    global game_started
    if not game_started:
        return
    player_position += random.randint(1, 5)
    canvas.coords(player, player_position, 50, player_position + 40, 100)
    if player_position >= track_length or opponent_position >= track_length:
        determine_winner()
        game_started = False
        play_again_button.pack()

def move_opponent(event):
    global opponent_position
    global game_started
    if not game_started:
        return
    opponent_position += random.randint(1, 5)
    canvas.coords(opponent, opponent_position, 150, opponent_position + 40, 200)
    if opponent_position >= track_length:
        determine_winner()
        game_started = False
        play_again_button.pack()

def determine_winner():
    if player_position >= track_length and opponent_position >= track_length:
        result_label.config(text="It's a Draw!")
    elif player_position >= track_length:
        result_label.config(text="Blue Won!")
    elif opponent_position >= track_length:
        result_label.config(text="Red Won!")

def start_game():
    global game_started
    game_started = True
    start_button.config(state=tk.DISABLED)
    window.bind("d", move_player)
    window.bind("<Right>", move_opponent)

def play_again():
    global player_position, opponent_position, game_started
    player_position = 0
    opponent_position = 0
    game_started = False
    canvas.coords(player, player_position, 50, player_position + 40, 100)
    canvas.coords(opponent, opponent_position, 150, opponent_position + 40, 200)
    result_label.config(text="")
    play_again_button.pack_forget()
    start_button.config(state=tk.NORMAL)
    window.unbind("d")
    window.unbind("<Right>")

window = tk.Tk()
window.title("Racing Game")

canvas = tk.Canvas(window, width=800, height=250)
canvas.pack()

canvas.create_line(20, 100, 820, 100, width=2)
canvas.create_line(20, 200, 820, 200, width=2)

player = canvas.create_rectangle(player_position, 50, player_position + 40, 100, fill="blue")
opponent = canvas.create_rectangle(opponent_position, 150, opponent_position + 40, 200, fill="red")

result_label = tk.Label(window, text="", font=("Arial", 24))
result_label.pack()

start_button = tk.Button(window, text="Play", command=start_game)
start_button.pack()

play_again_button = tk.Button(window, text="Play Again", command=play_again)

window.mainloop()
