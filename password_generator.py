from tkinter import *
from random import randint,choices
import os, string, pyperclip

def gnd():
    mdp = ""
    all_character = string.ascii_letters + string.punctuation + string.digits
    min_mdp = 6
    max_mdp = 12 
    for n in range(randint(min_mdp,max_mdp)):
        mdp += choices(all_character)[0]
    Mdp_entry.delete(0,END)
    Mdp_entry.insert(0,mdp)

def copyMdp():
    mdp = Mdp_entry.get()
    pyperclip.copy(mdp)  

window = Tk()
window.geometry("720x480")
window.title("Générateur de mot de passe")
window.config(background="#4068A4")
window.iconbitmap(os.path.join("icon.ico"))

principale_frame = Frame(window,bg="#4068A4",borderwidth=1)  # Frame principale
principale_frame.pack(expand=YES)

left_frame = Frame(principale_frame,bg="#4068A4")            # Frame de gauche
left_frame.grid(row=0,column=0,pady=YES)

right_frame = Frame(principale_frame,bg="#4068A4")           # Frame de droite
right_frame.grid(row=0,column=1)

# Contenu de la Frame de gauche

height = 300
width = 300
image = PhotoImage(file= os.path.join("password-code.png")).zoom(30).subsample(55)
canvas = Canvas(left_frame,width=width,height=height,bg="#4068A4",bd=0,highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.pack()

# Contenu de la Frame de droite

title_label = Label(right_frame,text="Mot de Passe",bg="#4068A4",font=("Sans serrif",30),fg="white",padx=YES,highlightthickness=0)
title_label.grid(row=0)

Mdp_entry = Entry(right_frame,font=("Helvetica,50"),bg="#4068A4",fg="white",highlightbackground="white",highlightthickness=1)
Mdp_entry.grid(row=1,column=0)

copy_button = Button(right_frame,text="Copier",bg="#4068A4",fg="white",highlightbackground="white",highlightthickness=2,command=copyMdp)
copy_button.grid(row = 1, column= 1)

generate_button = Button(right_frame,text="Générer",font=("Sans serrif",14),bg="white",fg="#4068A4",highlightbackground="#4068A4",highlightthickness=1,command=gnd )
generate_button.grid(row=2)

window.mainloop()
