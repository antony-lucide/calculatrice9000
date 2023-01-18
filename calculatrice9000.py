from tkinter import *
import tkinter as tk 

equation = ""

def show(value): # Permet l'affichage des valeurs
    global equation #sélectionne la variable à l'exterieur de la fonction afin de l'utiliser
    equation+=value
    label_result.config(text=equation)
    
def clear(): #Permet d'éffacer les charactère de l'HUD
    global equation
    equation=""
    label_result.config(text=equation)



def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result = eval(equation) #évalue l'équation
        except:
            result = "error"
            equation = ""
    label_result.config(text=result) #Affiche le résultat de ma fonction et creer une instance dans mon interface
    
    
    


gui = tk.Tk() #créer une nouvelle fenêtre sur linux ou window/mac
gui.configure (background="dark blue")
gui.title("Calculateur9000")
gui.geometry("680x650+100+200")
label_result = Label(gui,width=80,height="3", text=(""),font="arial") #Affiche le résultat de mon calcule
label_result.pack() #Appelle mon résultat dans mon affichage
Button(gui, text="1",command=lambda: show(value=("1")), height=1, width=7, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=8,y=90) 
Button(gui, text="2",command=lambda: show(value=("2")), height=1, width=7, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=200,y=90)
Button(gui, text="3",command=lambda: show("3"), height=1, width=7, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=200,y=200)
Button(gui, text="4",command=lambda: show("4"), height=1, width=7, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=8,y=200)
Button(gui, text="5",command=lambda: show("5"), height=1, width=7, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=8,y=300)
Button(gui, text="6",command=lambda: show("6"), height=1, width=7, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=200,y=300)
Button(gui, text="7",command=lambda: show("7"), height=1, width=7, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=200,y=400)
Button(gui, text="8",command=lambda: show("8"), height=1, width=7, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=8,y=400)
Button(gui, text="9",command=lambda: show("9"), height=1, width=7, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=8,y=500)
Button(gui, text="0",command=lambda: show("0"), height=1, width=7, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=200,y=500)
Button(gui, text="+",command=lambda: show("+"), height=1, width=3, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=450,y=90)
Button(gui, text="-",command=lambda: show("-"), height=1, width=3, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=450,y=200)
Button(gui, text="*",command=lambda: show("*"), height=1, width=3, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=450,y=300)
Button(gui, text="/",command=lambda: show("/"), height=1, width=3, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=450,y=400)
Button(gui, text="=",command=lambda: calculate(), height=1, width=3, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=450,y=500)
Button(gui, text="c",command=lambda: clear(), height=1, width=3, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=570,y=500)
Button(gui, text="%",command=lambda: show("%"), height=1, width=3, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=570,y=400)
Button(gui, text="√",command=lambda: show("**0.5"), height=1, width=3, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=570,y=300)
Button(gui, text="π",command=lambda: show("3,14"), height=1, width=3, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=570,y=200)
Button(gui, text="a²",command=lambda: show("**2"), height=1, width=3, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=570,y=90)
Button(gui, text=".",command=lambda: show("."), height=1, width=3, font=("arial",30,"bold"), bd=1, fg="#0059b3", bg="#ff0000").place(x=570,y=580)
gui.mainloop()

