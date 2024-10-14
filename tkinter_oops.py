import tkinter as tk
from random import randrange

# NAMING THE PACKAGES ###
window = tk.Tk()

# APPEARANCE OF NAME OF GAME ##
window.title("Can You Guess the Number??")

# --------------------------## CREATING ALL OF THE LABELS FOR THE WINDOW OF THE GAME ##----------------#

lblInst = tk.Label(window, text="Guess a number from 0 to 9", font=("Times", 14), bg="light blue")
lblLine0 = tk.Label(window, text="___________________________________________________________________")
lblNoGuess = tk.Label(window, text="Amount of Guesses: 0", font=("Times", 14), bg="violet")
lblMaxGuess = tk.Label(window, text="Max Guesses: 3", font=("Times", 14), bg="violet")
lblLine1 = tk.Label(window, text="___________________________________________________________________")
lblLogs = tk.Label(window, text="Ready?", font=("Times", 14), bg="yellow")
lblLine2 = tk.Label(window, text="___________________________________________________________________")

# ---------------------------## CREATION OF BUTTONS AND DEFINING THE NUMBER RANGE ##------------------------

buttons = []
for index in range(0, 10):
    button = tk.Button(window, text=index, command=lambda index=index: process(index), state=tk.DISABLED)
    buttons.append(button)

# CREATING THE START BUTTON ##

btnStartGameList = []
for index in range(0, 1):
    btnStartGame = tk.Button(window, text="START THE GAME", font=("Times", 14), bg="green",
                             command=lambda: startgame(index))
    btnStartGameList.append(btnStartGame)

# CREATING THE QUIT BUTTON ##

btnEndGameList = []
for index in range(0, 1):
    btnEndGame = tk.Button(window, text="QUIT", font=("Times", 14), bg="red", command=lambda: endgame(index))
    btnEndGameList.append(btnEndGame)

# ---------------DEFINING EACH OF THE ELEMENTS ON THE GRID-------------###

lblInst.grid(row=0, column=0, columnspan=5)  # GIVING THE INSTRUCTIONS
lblLine0.grid(row=1, column=0, columnspan=5)  # DEFINING THE BORDERS TO SEPARATE COLUMNS
lblNoGuess.grid(row=2, column=0, columnspan=3)  # NUMBER OF GUESSES USED
lblMaxGuess.grid(row=2, column=3, columnspan=2)  # NUMBER OF GUESSES LEFT
lblLine1.grid(row=3, column=0, columnspan=5)  # DEFINING THE BORDERS TO SEPARATE COLUMNS
lblLogs.grid(row=4, column=0, columnspan=5)  # UPDATED STATS OF GUESSES TAKEN
lblLine2.grid(row=9, column=0, columnspan=5)

# ASSIGNING THE NUMBERS TO ROWS AND COLUMNS##

for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col  # CREATING 5 COLUMNS FOR NUMBERS AND TWO ROWS
        buttons[i].grid(row=row + 10, column=col)

# CREATING THE FRAME FOR START AND QUIT BUTTONS ##

btnStartGameList[0].grid(row=13, column=0, columnspan=5)
btnEndGameList[0].grid(row=14, column=0, columnspan=5)

# --------------------------------------------------------------------------------###

# BEGINNING STATS FOR GUESSES TAKEN AND GUESSES LEFT ##

guess = 0
totalNumberOfGuesses = 0
maxNumberOfGuesses = 3
guessNumber = randrange(10)
print(guessNumber)
lblLogs = []
guess_row = 4


def init():  # DEFINING THE BEGINNING STATS OF EACH STARTING GAME###
    global buttons, guess, totalNumberOfGuesses, guessNumber, lblNoGuess, lblLogs, guess_row, maxNumberOfGuesses, lblMaxGuess
    guess = 0
    totalNumberOfGuesses = 0
    maxNumberOfGuesses = 3
    guessNumber = randrange(10)
    print(guessNumber)
    lblNoGuess["text"] = "Amount of Guesses: 0"
    lblMaxGuess["text"] = "Guesses left: 3"
    guess_row = 4


# REMOVING ALL LOGS FOR INIT###
for lblLog in lblLogs:
    lblLog.grid_forget()
lblLogs = []


# --------------DEFINING IN-GAME RUNNING STATISTICS------------------------###

def process(i):  # FUNCTION TO TRACK OF NUMBER OF GUESSES##
    global totalNumberOfGuesses, buttons, guess_row, maxNumberOfGuesses, buttons, guess_row
    guess = i

    totalNumberOfGuesses += 1  ###ADDING 1 GUESS ON SCREEN WHEN PLAYER MAKES A GUESS###
    lblNoGuess["text"] = "Amount of Guesses: " + str(totalNumberOfGuesses)

    maxNumberOfGuesses -= 1  ###SUBTRACTING ONE GUESS ATTEMPT WHEN PLAYER MAKES GUESS###
    lblMaxGuess["text"] = "Attempts Left: " + str(maxNumberOfGuesses)


# DEFINING OUTCOME IF PLAYER IS CORRECT##

if guess == guessNumber:  # CHECKING GUESSED NUMBER TO SEE IF IT IS CORRECT##
    lbl = tk.Label(window, text="Correct!! YOU WIN!! ", font=("Times", 14), fg="green")
    lbl.grid(row=guess_row, column=0, columnspan=5)
    lblLogs.append(lbl)
    guess_row += 1  # ADDING 1 GUESS ONTO STATISTIC###

for b in buttons:  # GAME IS OVER, BUTTONS DISABLED###
    b["state"] = tk.DISABLED
else:

    # DEFINING OUTCOME IF PLAYER IS INCORRECT##

    if guess > guessNumber:  # IF PLAYER IS INCORRECT, THE STAT IS GIVEN THAT THEY USED ONE GUESS AND GIVES HINT TO NEXT GUESS##
        lbl = tk.Label(window, text="You've used a guess. Hint: Guess lower!", font=("Times", 14), fg="red")
        lbl.grid(row=guess_row, column=0, columnspan=5)
        lblLogs.append(lbl)
        guess_row += 1  # ADDING 1 GUESS ONTO STATISTIC###
    else:
        lbl = tk.Label(window, text="You've used a guess. Hint: Guess higher!", font=("Times", 14), fg="red")
        lbl.grid(row=guess_row, column=0, columnspan=5)
        lblLogs.append(lbl)
        guess_row += 1  # ADDING 1 GUESS ONTO STATISTIC###

# DEFINFING OUTCOME WHEN ALL GUESSES ARE USED###
if totalNumberOfGuesses == 3:  # GAME IS OVER WHEN THREE GUESSES ARE USED ##
    if guess != guessNumber:
        lbl = tk.Label(window, text="NO MORE GUESSES! START THE GAME AGAIN!", font=("Times", 14), fg="red")
        lbl.grid(row=guess_row, column=0, columnspan=5)
        lblLogs.append(lbl)
        guess_row += 1  # ADDING 1 GUESS ONTO STATISTIC###

for b in buttons:  # GAME IS OVER, BUTTONS DISABLED###
    b["state"] = tk.DISABLED

buttons[i]["state"] = tk.DISABLED

status = "none"


# -------------------------DEFINING START AND QUIT FUNCTIONS----------------##

def startgame(i):  # START GAME FUNCTION ##
    global status
    for b in buttons:  # DEFINING BUTTON STATE TO NORMAL###
        b["state"] = tk.NORMAL

    if status == "none":
        status = "started"
        btnStartGameList[i]["text"] = "Restart Game"

    else:
        status = "restarted"
        init()
        print("Game started")


def endgame(i):  # END GAME FUNCTION ##
    btnEndGameList[i].destroy()  # CLOSING GAME##
    window.destroy()  # CLOSING WINDOW##


window.mainloop()
