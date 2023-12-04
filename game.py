from tkinter import*
import tkinter as tk
from tkinter import messagebox
import random
import pygame


root=tk.Tk()
root.title("Typing Speed Game")      
root.geometry("600x400+400-200")
root.configure(bg="chartreuse3")
root.iconbitmap("typing.ico")
root.maxsize(1920, 1080)
root.minsize(600, 400)


words=['keyboard','programming','challenge','elephant','python','excellent', 'magnificent','fascinating','opportunity','technology'
       ,'innovation','happiness','curiosity','incredible','determination','adventurous','perseverance','extraordinary','serendipity',
       'apple','cybersecurity','pair','mango','car','bike','cat','dog','horse','fan','air','blue','red','black','grey',
       'hair','sudden','karachi','for','today','that','yesterday','fork','door','color','floor','flour','grape',
       'duck','horn','crown','fish','fly','plain']

pygame.mixer.init()       

def time():
    global timeleft,matched
    if(timeleft>0):
        timeleft-=1                   
        timercount.configure(text=timeleft)     
        timercount.after(1000,time)          
        if (timeleft<11):
            timercount.configure(fg="red")
            timer.configure(fg="red")
        if timeleft==10:
            pygame.mixer.music.load("countdown.mp3")     
            pygame.mixer.music.play(loops=0)
    else:
        scorecount.configure(text=matched)                
        scorelabel.configure(text="You enter\tWPM")
        if matched>=30 and matched<=35:
            feedback.configure(text="Your typing speed is average")            
        elif matched>=36:
            feedback.configure(text="Your typing speed is above average")
        else:
            feedback.configure(text="Your typing speed is below average")
            
        retry=messagebox.askretrycancel('Notification','Do you want to retry?')
        
        if retry==True:
            timeleft=60                                                  
            matched=0
            feedback.configure(text='')
            scorecount.configure(text='')
            scorelabel.configure(text='')
            timercount.configure(text=timeleft,fg="yellow")
            timer.configure(fg="yellow")
            wordentry.delete(0,END)



def startGame(event):

    global matched,not_matched

    if timeleft==60:       
        time()
        
    if(wordentry.get() == word["text"]):
        matched+=1           
    elif(wordentry.get() != word["text"]):
        not_matched+=1
        pygame.mixer.music.load("buzzer.wav")     
        pygame.mixer.music.play(loops=0)          

    random.shuffle(words)              
    word.configure(text=words[0])        
    wordentry.delete(0,END)         
    label.configure(text="")      
         
    
h1=Label(root, text="Typing Speed Game", bg="chartreuse3", fg="#FFC300" ,font="comicsanms 25 bold", anchor="center")
h1.pack(pady=10)  

label=Label(root, text="Type word and Hit enter to start the game", bg="chartreuse3", fg="black", font="comicsanms 10 italic")
label.pack(pady=12)            

word=Label(root, text=words[0], font="comicsanms 20 bold", fg="#FFD60A", bg="chartreuse3",width=15,anchor="center")
word.pack(pady=30)

wordentry=Entry(root,font="comicsanms 18 bold",fg="grey",bg="chartreuse3", justify="center",bd=4)
wordentry.pack(pady=32)


timer=Label(root, text="Timer:",fg="black", bg="chartreuse3", font="comicsanms 18 bold")
timer.place(x=470, y=100)

timercount=Label(root, text="60",fg="black", bg="chartreuse3", font="comicsanms 16 bold")
timercount.place(x=495, y=140)         

matched=0             
not_matched=0
timeleft=60

scorelabel=Label(root, text="", bg="chartreuse3", fg="#FFC300", font="comicsanms 17 bold")
scorelabel.place(x=50,y=310)                   

scorecount=Label(root, text="", bg="chartreuse3", fg="#FFC300", font="comicsanms 17 bold")
scorecount.place(x=190,y=310)              

feedback=Label(root, text="",bg="chartreuse3",fg="#FFC300",font="comicsanms 12 bold")
feedback.place(x=53,y=350)      



root.bind('<Return>', startGame)
root.mainloop()
