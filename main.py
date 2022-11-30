import tkinter as tk
import win32api
import math
from tkinter import messagebox
from random import randint
from threading import Thread


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        width = 480
        height = 480

        #get screen size
        screen_w = win32api.GetSystemMetrics(0)
        screen_h = win32api.GetSystemMetrics(1)

        #center window
        x = int(screen_w/2 - width/2)
        y = int(screen_h/2 - height/2)

        #set window geometry
        self.geometry(f"{width}x{height}+{x}+{y}")

        #set window title
        self.title("TicTacToe")

        #set window not resizable
        self.resizable(False, False)

        #load images
        self.circle_img = tk.PhotoImage(file="img/circle.png")
        self.cross_img = tk.PhotoImage(file="img/cross.png")

        self.load()
        
        #draw a player
        self.player = randint(0,1)
    
    def load(self):
        #delete buttons if they exist
        try:
            for button in self.btns:
                button.pack_forget()
        except:
            pass
        #create buttons
        self.btns = []
        button_width = 160
        button_height = 160
        

        self.btns.append(tk.Button(command= lambda: self.move(0)))
        self.btns.append(tk.Button(command= lambda: self.move(1)))
        self.btns.append(tk.Button(command= lambda: self.move(2)))
        self.btns.append(tk.Button(command= lambda: self.move(3)))
        self.btns.append(tk.Button(command= lambda: self.move(4)))
        self.btns.append(tk.Button(command= lambda: self.move(5)))
        self.btns.append(tk.Button(command= lambda: self.move(6)))
        self.btns.append(tk.Button(command= lambda: self.move(7)))
        self.btns.append(tk.Button(command= lambda: self.move(8)))
        
        for i in range(3):
            for j in range(3):
                self.btns[i*3+j].place(x=j*button_width, y=i*button_height, width=button_width, height=button_height)

    def move(self, n):
        #check round
        if self.player == 0:
            img = self.cross_img
            sign = 'x'
            self.player = 1

        elif self.player == 1:
            img = self.circle_img
            sign = 'o'
            self.player = 0

        self.btns[n] = tk.Button(image=img, text=sign)

        x_pos = n%3*160
        y_pos = math.ceil((n+1)/3-1)*160

        self.btns[n].place(x=x_pos, y= y_pos , width=160, height=160)
        self.check_winner()

    def check_winner(self):
        boxes = [btn.cget('text') for btn in self.btns]
        winner = None
        
        #check rows
        if boxes[0] == boxes[1] == boxes[2] != '':
            winner = boxes[0]
        if boxes[3] == boxes[4] == boxes[5] != '':
            winner = boxes[3]
        if boxes[6] == boxes[7] == boxes[8] != '':
            winner = boxes[6]

        #check columns
        if boxes[0] == boxes[3] == boxes[6] != '':
            winner = boxes[0]
        if boxes[1] == boxes[4] == boxes[7] != '':
            winner = boxes[1]
        if boxes[2] == boxes[5] == boxes[8] != '':
            winner = boxes[2]

        #check diagonal
        if boxes[0] == boxes[4] == boxes[8] != '':
            winner = boxes[0]
        if boxes[6] == boxes[4] == boxes[2] != '':
            winner = boxes[6]

        def callback():
            messagebox.showinfo("End of the game", f"Player {winner} won the game!")
            self.load()
        
        if winner is not None:
            Thread(target=callback).start()

app = MainWindow()
app.mainloop()