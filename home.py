from tkinter import*
import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()
root.title("Typing Speed Game")
root.geometry("600x400+400-200")
root.configure(bg="chartreuse3")
root.iconbitmap("typing.ico")
root.maxsize(1920, 1080)
root.minsize(600, 400)

def play_game():
   root.destroy()
   import game

label1 = Label(root, text="Welcome to Typing Speed Game", font="comicsanms 25 bold", fg="#FFC300", bg="chartreuse3", anchor="center")
label1.pack(pady=7)
label2 = Label(root, text="Instruction: Enter the given words in the limited time and find your typing speed at the end of the game. Enjoy!!", font="comicsanms 10 italic", fg="black", bg="chartreuse3", anchor="center", wraplength=500)
label2.pack(pady=20)

play = Image.open("pla.jpg")
resize_image = play.resize((224, 87))
play = ImageTk.PhotoImage(resize_image)
play_button=Button(root, image=play, borderwidth=0, bg="#001D3D", command=play_game, bd=0, anchor="center")
play_button.pack(pady=70)
root.mainloop()

