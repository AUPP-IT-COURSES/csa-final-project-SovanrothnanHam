# from tkinter import*
# import tkinter as tk
# from tkinter import messagebox
# import random
# import pygame


# root=tk.Tk()
# root.title("Typing Master")      
# root.geometry("600x400+400-200")
# root.configure(bg="#001D3D")
# root.iconbitmap("typing.ico")
# root.maxsize(600, 400)
# root.minsize(600, 400)


# words=['apple','pear','pair','mango','car','bike','cat','dog','horse','fan','air','blue','red','black','grey',
#        'hair','sudden','karachi','for','today','that','yesterday','fork','door','color','floor','flour','grape',
#        'duck','horn','crown','fish','fly','plain','Rapid','python', 'programming', 'language', 'computer', 'keyboard',
#        'speed', 'challenge', 'practice', 'algorithm', 'development','coding', 'software', 'developer', 'learning', 'syntax',
#        'variable', 'function', 'iteration', 'conditional', 'debugging']
# def time():
#     global timeleft,matched
#     if(timeleft>0):
#         timeleft-=1                   #it will run the time counter and -1 from its value after each sec
#         timercount.configure(text=timeleft)     #it will display the change in counter value after each sec
#         timercount.after(1000,time)          #1000ms = 1 sec
#         if (timeleft<11):
#             timercount.configure(fg="red")
#             timer.configure(fg="red")
#         if timeleft==10:
#             pygame.mixer.music.load("countdown1.mp3")     #countdown sound
#             pygame.mixer.music.play(loops=0)
#     else:
#         scorecount.configure(text=matched)                #change in score count and show after time is up
#         scorelabel.configure(text="You enter\tWPM")
#         if matched>=35 and matched<=40:
#             feedback.configure(text="Your typing speed is average")            #feedback on last
#         elif matched>=65:
#             feedback.configure(text="Your typing speed is above average")
#         else:
#             feedback.configure(text="Your typing speed is below average")
            
#         retry=messagebox.askretrycancel('Notification','Do you want to retry?')
        
#         if retry==True:
#             timeleft=60                                                    #RETRY BOX coding
#             matched=0
#             feedback.configure(text='')
#             scorecount.configure(text='')
#             scorelabel.configure(text='')
#             timercount.configure(text=timeleft,fg="yellow")
#             timer.configure(fg="yellow")
#             wordentry.delete(0,END)



# def startGame(event):

#     global matched,not_matched

#     if timeleft==60:        #it will call the func time
#         time()
        
#     if(wordentry.get() == word["text"]):
#         matched+=1            #if you enter correct word then it will be count otherwise else loop will run
#     elif(wordentry.get() != word["text"]):
#         not_matched+=1
#         pygame.mixer.music.load("buzzer1.mp3")     
#         pygame.mixer.music.play(loops=0)           #it will play sound when you enter wrong word

#     random.shuffle(words)              #it will shuffle words in a list
#     word.configure(text=words[0])        #it will print those shuffled words one by one
#     wordentry.delete(0,END)         #after user typed the word and pressed enter key then entry box will automatically cleared 
#     label.configure(text="")         #After starting game instruction below entry will remove
         
    
# h1=Label(root, text="Typing Master", bg="#001D3D", fg="#FFC300" ,font="comicsanms 24 bold", anchor="center")
# h1.pack(pady=10)             #first heading

# word=Label(root, text=words[0], font="comicsanms 20 bold", fg="#FFD60A", bg="#001D3D",width=15,anchor="center")
# word.place(y=150,x=40)            #words that we have to enter

# wordentry=Entry(root,font="comicsanms 18 bold",fg="grey",bg="#001D3D", justify="center",bd=4)
# wordentry.place(x=40,y=200)#entry box where we will enter words


# timer=Label(root, text="Timer:",fg="green", bg="#001D3D", font="comicsanms 18 bold")
# timer.place(x=470, y=100)         #timer heading

# timercount=Label(root, text="60",fg="green", bg="#001D3D", font="comicsanms 16 bold")
# timercount.place(x=495, y=140)         #timer count below its heading

# label=Label(root, text="Type word and Hit enter to start the game", bg="#001D3D", fg="grey", font="comicsanms 10 italic")
# label.place(x=68,y=250) #instruction 1 for user below entry label at starting of game



# matched=0             #variables used in this program
# not_matched=0
# timeleft=60

# scorelabel=Label(root, text="", bg="#001D3D", fg="#FFC300", font="comicsanms 17 bold")
# scorelabel.place(x=50,y=310)                   #text which will appear after time is up

# scorecount=Label(root, text="", bg="#001D3D", fg="#FFC300", font="comicsanms 17 bold")
# scorecount.place(x=190,y=310)                #number of wpm score which will in between the text of scorelabel

# feedback=Label(root, text="",bg="#001D3D",fg="#FFC300",font="comicsanms 12 bold")
# feedback.place(x=53,y=350)        #it will display the text which will tell your typing speed is average or not 



# root.bind('<Return>', startGame)
# root.mainloop()
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
import pygame

root = tk.Tk()
root.title("Typing Master")
root.geometry("600x400+400-200")
# root.configure(bg="#001D3D")
root.configure(bg="chartreuse3")
root.iconbitmap("typing.ico")
root.maxsize(600, 400)
root.minsize(600, 400)

words = [
    'apple', 'pear', 'pair', 'mango', 'car', 'bike', 'cat', 'dog', 'horse', 'fan', 'air', 'blue', 'red', 'black', 'grey',
    'hair', 'sudden', 'karachi', 'for', 'today', 'that', 'yesterday', 'fork', 'door', 'color', 'floor', 'flour', 'grape',
    'duck', 'horn', 'crown', 'fish', 'fly', 'plain', 'Rapid', 'python', 'programming', 'language', 'computer', 'keyboard',
    'speed', 'challenge', 'practice', 'algorithm', 'development', 'coding', 'software', 'developer', 'learning', 'syntax',
    'variable', 'function', 'iteration', 'conditional', 'debugging'
]

# Difficulty Levels Configuration
difficulty_levels = {
    'easy': {'word_length': (3, 5), 'time_limit': 60},
    'medium': {'word_length': (6, 8), 'time_limit': 45},
    'hard': {'word_length': (9, 12), 'time_limit': 30}
}

current_difficulty = 'easy'  # Default difficulty

pygame.mixer.init()


def update_difficulty(difficulty):
    global current_difficulty
    current_difficulty = difficulty


def time():
    global timeleft, matched
    if timeleft > 0:
        timeleft -= 1
        timercount.configure(text=timeleft)
        timercount.after(1000, time)
        if timeleft < 11:
            timercount.configure(fg="red")
            timer.configure(fg="red")
        if timeleft == 10:
            pygame.mixer.music.load("countdown1.mp3")
            pygame.mixer.music.play(loops=0)
    else:
        scorecount.configure(text=matched)
        scorelabel.configure(text="You enter\tWPM")
        if 35 <= matched <= 40:
            feedback.configure(text="Your typing speed is average")
        elif matched >= 65:
            feedback.configure(text="Your typing speed is above average")
        else:
            feedback.configure(text="Your typing speed is below average")

        retry = messagebox.askretrycancel('Notification', 'Do you want to retry?')

        if retry:
            initialize_game()


def startGame(event):
    global matched, not_matched

    if timeleft == 60:
        time()

    if wordentry.get() == word["text"]:
        matched += 1
    elif wordentry.get() != word["text"]:
        not_matched += 1
        pygame.mixer.music.load("buzzer1.mp3")
        pygame.mixer.music.play(loops=0)

    update_word()
    wordentry.delete(0, END)
    label.configure(text="")


def update_word():
    global words
    random.shuffle(words)
    word.configure(text=words[0])


def initialize_game():
    global matched, not_matched, timeleft
    matched = 0
    not_matched = 0
    timeleft = difficulty_levels[current_difficulty]['time_limit']
    timercount.configure(text=timeleft, fg="yellow")
    timer.configure(fg="yellow")
    wordentry.delete(0, END)
    update_word()
    feedback.configure(text='')


h1 = Label(root, text="Typing Master", bg="chartreuse3", fg="#FFC300", font="comicsanms 24 bold", anchor="center")
h1.pack(pady=10)

word = Label(root, text=words[0], font="comicsanms 20 bold", fg="#FFD60A", bg="chartreuse3", width=15, anchor="center")
word.place(y=150, x=40)

wordentry = Entry(root, font="comicsanms 18 bold", fg="grey", bg="chartreuse3", justify="center", bd=4)
wordentry.place(x=40, y=200)

timer = Label(root, text="Timer:", fg="green", bg="chartreuse3", font="comicsanms 18 bold")
timer.place(x=470, y=100)

timercount = Label(root, text="60", fg="green", bg="chartreuse3", font="comicsanms 16 bold")
timercount.place(x=495, y=140)

label = Label(root, text="Type word and Hit enter to start the game", bg="chartreuse3", fg="grey",
              font="comicsanms 10 italic")
label.place(x=68, y=250)

scorelabel = Label(root, text="", bg="chartreuse3", fg="#FFC300", font="comicsanms 17 bold")
scorelabel.place(x=50, y=310)

scorecount = Label(root, text="", bg="chartreuse3", fg="#FFC300", font="comicsanms 17 bold")
scorecount.place(x=190, y=310)

feedback = Label(root, text="", bg="chartreuse3", fg="#FFC300", font="comicsanms 12 bold")
feedback.place(x=53, y=350)

# Difficulty Buttons
easy_button = Button(root, text="Easy", command=lambda: update_difficulty('easy'))
easy_button.place(x=50, y=50)

medium_button = Button(root, text="Medium", command=lambda: update_difficulty('medium'))
medium_button.place(x=150, y=50)

hard_button = Button(root, text="Hard", command=lambda: update_difficulty('hard'))
hard_button.place(x=250, y=50)

initialize_game()  # Initialize the game with default difficulty

root.bind('<Return>', startGame)
root.mainloop()
