from random import randint
from tkinter import *
from tkinter import simpledialog, messagebox
def win(p1choice, p2choice):
    global player1, names
    messagebox.askokcancel("Result", p1name + " chose " + names[p1choice] + " and " + p2name + " chose " + names[p2choice] + ". " + p1name + " wins")
    player1 += 1
def draw(p1choice, p2choice):
    global player1, player2, names
    messagebox.askokcancel("Result", p1name + " chose " + names[p1choice] + " and " + p2name + " chose " + names[p2choice] + ". A draw has occured")
    player1 += 0.5
    player2 += 0.5
def loss(p1choice, p2choice):
    global player2, names
    messagebox.askokcancel("Result", p1name + " chose " + names[p1choice] + " and " + p2name + " chose " + names[p2choice] + ". " + p2name + " wins")
    player2 += 1
patterns = {(1, 1):draw, (1, 2):loss, (1, 3):win, (2, 1):win, (2, 2):draw, (2, 3):loss, (3, 1):loss, (3, 2):win, (3, 3):draw}
names = {"1":"rock", "2":"paper", "3":"scissors"}

def game():
    global p1name, p2name, twoplayers
    if twoplayers == False:
        p2name = "Computer"
    score.config(text=f"{p1name}: {player1} | {p2name}: {player2}")
    play = True
    while play == True:
        p1 = simpledialog.askinteger(p1name + ": Choice", "Enter 1 for Rock, 2 for Paper, 3 for Scissors")
        if twoplayers == True:
            p2 = simpledialog.askinteger(p2name + ": Choice", "Enter 1 for Rock, 2 for Paper, 3 for Scissors")
        else:
            p2 = randint(1, 3)
        if p1 not in (1, 2, 3) or p2 not in (1, 2, 3):
            raise SystemExit("Game over. " + ("It's a draw! " if player1 == player2 else (p1name if player1 > player2 else p2name) + " wins!"))
        patterns[(p1, p2)](str(p1), str(p2))
        score.config(text=f"{p1name}: {player1} | {p2name}: {player2}")

win = Tk()
c = Canvas(win, width=400, height=200)
c.pack()
win.attributes("-topmost", True)
player1 = 0
player2 = 0
p2name = ""
win.attributes("-topmost", False)
score = Label(c, text="Click on the top to begin", anchor=CENTER, font=("Helvetica", 24), padx=50, pady=50)
score.pack()
twoplayers = simpledialog.askstring("Player", "Enter 1 for single-player and 2 for two-player") == "2"
p1name = simpledialog.askstring("Name", "What is the name of your first player?")
if twoplayers == True:
    p2name = simpledialog.askstring("Name", "What is the name of your second player?")
game()
