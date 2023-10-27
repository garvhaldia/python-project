import numpy as np
from tensorflow.keras.models import load_model
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk as ik
import cv2
import random
import time as t


def getChoice():
    val = ""
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    model10 = load_model(r"C:\Users\wrong\Desktop\RPS\model10.h5")
    bl, x = cap.read()
    x = cv2.resize(x, (100, 100))
    x = x / 255
    img_arr = np.array(x)
    img = np.array([img_arr])
    y = model10.predict(img)
    if np.argmax(y, axis=1) == [1]:
        val = "rock"
    elif np.argmax(y, axis=1) == [0]:
        val = "paper"
    elif np.argmax(y, axis=1) == [2]:
        val = "scissor"
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    val = ""
    bl, img = cap.read()
    palm_data = cv2.CascadeClassifier(cv2.haarcascades + "palm.xml")
    fist_data = cv2.CascadeClassifier(cv2.haarcascades + "closed_palm.xml")
    foundPaper = palm_data.detectMultiScale(img, minSize=(20, 20))
    foundRock = fist_data.detectMultiScale(img, minSize=(20, 20))
    for (x, y, height, width) in foundRock:
        cv2.rectangle(img, (x, y), (x + height, y + width), color=(0, 0, 255), thickness=5)
    for (x, y, height, width) in foundPaper:
        cv2.rectangle(img, (x, y), (x + height, y + width), color=(255, 0, 0), thickness=5)
    img1 = cv2.flip(img, 1)
    #cv2.imshow("Eye Tracker", img1)
    #cv2.waitKey(1)
    if len(foundPaper) > 0:
        val = "paper"
    elif len(foundRock) > 0:
        val = "rock"
    return val


def randomChoice():
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    return computer_action


def play(user_action, computer_action,c1,c2,play_window):
    t = ""
    if user_action == computer_action:
        t = 'Both players selected '+user_action+". It's a tie!"
    elif user_action == "rock":
        if computer_action == "scissors":
            t = "Rock smashes scissors! You win!"
            c1 += 1
        else:
            t = "Paper covers rock! You lose."
            c2 += 1
    elif user_action == "paper":
        if computer_action == "rock":
            t = "Paper covers rock! You win!"
            c1 += 1
        else:
            t = "Scissors cuts paper! You lose."
            c2 += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            t = "Scissors cuts paper! You win!"
            c1 += 1
        else:
            t = "Rock smashes scissors! You lose."
            c2 += 1
    r = tk.Label(play_window, text=t)
    r.pack()
    play_window.update()
    return c1,c2

def submit(user_name):
    name = user_name.get()

    print("The name is : " + name)
    user_name.set("")

def countdown(play_window):
    countdown3 = tk.Label(play_window, text=1, bg='black', fg='yellow', font=("Broadway", 90))
    countdown3.place(x=660, y=590)
    countdown2 = tk.Label(play_window, text=2, bg='black', fg='yellow', font=("Broadway", 90))
    countdown2.place(x=660, y=590)
    countdown1 = tk.Label(play_window, text=3, bg='black', fg='yellow', font=("Broadway", 90))
    countdown1.place(x=660, y=590)
    countdown4 = tk.Label(play_window, text=1, bg='black', fg='yellow', font=("Broadway", 90))
    countdown4.place(x=1000, y=590)
    countdown5 = tk.Label(play_window, text=2, bg='black', fg='yellow', font=("Broadway", 90))
    countdown5.place(x=1000, y=590)
    countdown6 = tk.Label(play_window, text=3, bg='black', fg='yellow', font=("Broadway", 90))
    countdown6.place(x=1000, y=590)
    countdown3.after(3000, countdown3.destroy)
    countdown4.after(3000, countdown4.destroy)
    countdown5.after(2000, countdown5.destroy)
    countdown2.after(2000, countdown2.destroy)
    countdown1.after(1000, countdown1.destroy)
    countdown6.after(1000, countdown6.destroy)
    play_window.update()

def score(player_score,computer_score,play_window):
    plabel = tk.Label(play_window, text=player_score, bg='yellow', fg='black', font=("Broadway", 50))
    clabel = tk.Label(play_window, text=computer_score, bg='yellow', fg='black', font=("Broadway", 50))
    plabel.place(x=700, y=375)
    clabel.place(x=1000, y=375)
    plabel.after(2000,plabel.destroy)
    clabel.after(2000, clabel.destroy)

def createMain():
    main_window = tk.Tk()
    main_window.geometry("1800x1000")
    filename = ik.PhotoImage(file=r"C:\Users\wrong\Desktop\RPS\bg.png")
    bg = tk.Label(main_window, image=filename)
    bg.place(x=0, y=0)
    start_game = tk.Button(main_window, text="Start Game", fg='white',
                           bg='orange', bd=15, height=2, width=20,
                           command=playGame, font=("Broadway", 15))
    options = tk.Button(main_window, text="Options", fg='white',
                        bg='orange', bd=15, height=2, width=20,
                        font=("Broadway", 15))

    user_name = tk.StringVar()
    user = tk.Entry(main_window, textvariable=user_name, font=("Broadway", 20), bd=10)
    sub = tk.Button(main_window, text="Submit", height=2, width=10,
                    bg='orange', fg='white',
                    activeforeground='blue', activebackground='white',
                    command=submit(user_name), font=("Broadway", 15), bd=10)
    start_game.pack(pady=60)
    options.pack(pady=30)
    user.pack(pady=30)
    sub.pack(pady=30)
    main_window.mainloop()

def playGame():
    while True:
        play_window = tk.Toplevel()
        play_window.title("Rock Paper Scissors")
        play_window.geometry("1800x1000")
        filename2 = ik.PhotoImage(file=r"C:\Users\wrong\Desktop\RPS\playbg.png")
        playbg = tk.Label(play_window, image=filename2)
        playbg.place(x=0, y=0)
        c1 = 0
        c2 = 0
        while c1 < 3 and c2 < 3:
            countdown(play_window)
            score(c1, c2, play_window)
            play_window.update()
            t.sleep(3)
            c1, c2 = play(getChoice(), randomChoice(), c1, c2,play_window)


        if c1 > c2:
            print("YOU WIN")
        elif c1 < c2:
            print("YOU LOSE")
        elif c1 == c2:
            print("ITS A TIE")
        play_again = messagebox.askyesno(message = "Do You want to play another game")
        play_window.update()
        if not play_again:
            break


createMain()