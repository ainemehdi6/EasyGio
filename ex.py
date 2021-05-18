from tkinter import *
from PIL import ImageTk,Image
import deff,time

def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.title("EasyGio")
root.geometry("800x550")
root.iconbitmap("img/logoOnly.ico")
root.config(background="#e0dad6")
root.resizable(False,False)
f1 = Frame(root,bg="#e0dad6")
f2 = Frame(root,bg="#e0dad6")
f3 = Frame(root,bg="#e0dad6")
f4 = Frame(root,bg="#e0dad6")
f5 = Frame(root,bg="#e0dad6")
f51 = Frame(root,bg="#e0dad6")
f52 = Frame(root,bg="#e0dad6")
f53 = Frame(root,bg="#e0dad6")
f54 = Frame(root,bg="#e0dad6")
f55 = Frame(root,bg="#e0dad6")
f6 = Frame(root,bg="#e0dad6")

for frame in (f1, f2, f3, f4, f5,f51, f52, f53, f54, f55, f6):
    frame.grid(row=0, column=0, sticky='news')


#first_page
#logo
image1 = Image.open("img/logo.png")
test = ImageTk.PhotoImage(image1)
label1 = Label(f1,image=test,bg="#e0dad6")
label1.image = test
label1.pack(side=TOP, anchor=NW)
#title
label_title = Label(f1, text="Bienvenue sur EasyGio",font=("Helvetica",42), bg='#e0dad6', fg='#001d26')
label_title.pack(padx=60,pady=70)
#main_button
main_button = Button(f1, text="Démarer", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:raise_frame(f2))
main_button.pack(padx=30)


#second_page
#logo
label1 = Label(f2,image=test,bg="#e0dad6")
label1.image = test
label1.pack(side=TOP, anchor=NW)
#title
label_title = Label(f2, text="Sélectionner votre partie ",font=("Helvetica",42), bg='#e0dad6', fg='#001d26')
label_title.pack(padx=60,pady=40)
#fonct_button
fonct_button = Button(f2, text="Les fonctions", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:raise_frame(f3))
fonct_button.pack(padx=30)
#plan_button
plan_button = Button(f2, text="L'espace", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:raise_frame(f4))
plan_button.pack(padx=30,pady=20)
#footer_buttons
left_button = Button(f2, text="Retourner", width='10', font=("Helvetica",16), bg="#64ffaa", fg="#FFFFFF",
                    command=lambda:raise_frame(f1))
left_button.pack(side=LEFT,padx=20,pady=100)
right_button = Button(f2, text="Annuler", width='10', font=("Helvetica",16), bg="#eb6b6b", fg="#FFFFFF",
                    command=lambda:raise_frame(f1))
right_button.pack(side=RIGHT,padx=10,pady=100)


#fonction_page
#logo
label1 = Label(f3,image=test,bg="#e0dad6")
label1.image = test
label1.pack(side=TOP, anchor=NW)
#label
f_label = Label(f3, text="Sélectionner le type du fonction",font=("Helvetica",35), bg='#e0dad6', fg='#001d26')
f_label.pack(padx=60,pady=40)
#buttons
first_button = Button(f3, text="Defnit", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:[raise_frame(f5)])
first_button.pack(pady=10)
second_button = Button(f3, text="Non definit", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:raise_frame(f51))
second_button.pack(pady=10)
#footer_buttons
left_button = Button(f3, text="Retourner", width='10', font=("Helvetica",16), bg="#64ffaa", fg="#FFFFFF",
                    command=lambda:raise_frame(f2))
left_button.pack(side=LEFT, padx=20, pady=20)
right_button = Button(f3, text="Annuler", width='10', font=("Helvetica",16), bg="#eb6b6b", fg="#FFFFFF",
                    command=lambda:raise_frame(f1))
right_button.pack(side=RIGHT, padx=20, pady=20)


#espace_page
#logo
label1 = Label(f4,image=test,bg="#e0dad6")
label1.image = test
label1.pack(side=TOP, anchor=NW)
#label
f_label = Label(f4, text="Sélectionner la figure géométrique",font=("Helvetica",35), bg='#e0dad6', fg='#001d26')
f_label.pack(padx=40,pady=40)
#buttons
first_button = Button(f4, text="Sphére", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:raise_frame(f52))
first_button.pack(pady=5)
second_button = Button(f4, text="Cube", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:raise_frame(f53))
second_button.pack(pady=5)
ther_button = Button(f4, text="Les vecteurs", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:raise_frame(f54))
ther_button.pack(pady=5)
#footer_buttons
left_button = Button(f4, text="Retourner", width='10', font=("Helvetica",16), bg="#64ffaa", fg="#FFFFFF",
                    command=lambda:raise_frame(f2))
left_button.pack(side=LEFT, padx=20, pady=20)
right_button = Button(f4, text="Annuler", width='10', font=("Helvetica",16), bg="#eb6b6b", fg="#FFFFFF",
                    command=lambda:raise_frame(f1))
right_button.pack(side=RIGHT, padx=20, pady=20)

#inpute_pages
#fct_def
#logo
label1 = Label(f5,image=test,bg="#e0dad6")
label1.image = test
label1.pack(side=TOP, anchor=NW)
#spc
spc = Label(f5, text="",bg='#e0dad6')
spc.pack(pady=40)
#label
f_label = Label(f5, text="Entrer la fonction x",font=("Helvetica",16), bg='#e0dad6', fg='#001d26')
f_label.pack()
#input
fct1_input = Entry(f5,width=30)
fct1_input.pack(pady=20,ipady=3)
#execute_button
exec_button = Button(f5, text="Executer", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:[raise_frame(f6),deff.Execute_fct1(fct1_input.get())])
exec_button.pack(padx=30,pady=20)
#footer_buttons
left_button = Button(f5, text="Retourner", width='10', font=("Helvetica",16), bg="#64ffaa", fg="#FFFFFF",
                    command=lambda:raise_frame(f3))
left_button.pack(side=LEFT, padx=20, pady=20)
right_button = Button(f5, text="Annuler", width='10', font=("Helvetica",16), bg="#eb6b6b", fg="#FFFFFF",
                    command=lambda:raise_frame(f1))
right_button.pack(side=RIGHT, padx=20, pady=20)

#fct_ind
#logo
label1 = Label(f51,image=test,bg="#e0dad6")
label1.image = test
label1.pack(side=TOP, anchor=NW)
#spc
spc = Label(f51, text="",bg='#e0dad6')
spc.pack(pady=5)
#label
f_label = Label(f51, text="Entrer la fonction (x,y)",font=("Helvetica",16), bg='#e0dad6', fg='#001d26')
f_label.pack()
#input
fct_input = Entry(f51,width=30)
fct_input.pack(pady=20,ipady=3)
#label
f_label = Label(f51, text="Entrer les sommets du diagonales (a et b)",font=("Helvetica",16), bg='#e0dad6', fg='#001d26')
f_label.pack()
#input
pts_inputs = Entry(f51,width=30)
pts_inputs.pack(pady=20,ipady=3)
#execute_button
exec_button = Button(f51, text="Executer", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:[raise_frame(f6),deff.Execute_fct2(fct_input.get(),pts_inputs.get())])
exec_button.pack(padx=30)
#footer_buttons
left_button = Button(f51, text="Retourner", width='10', font=("Helvetica",16), bg="#64ffaa", fg="#FFFFFF",
                    command=lambda:raise_frame(f3))
left_button.pack(side=LEFT, padx=20, pady=20)
right_button = Button(f51, text="Annuler", width='10', font=("Helvetica",16), bg="#eb6b6b", fg="#FFFFFF",
                    command=lambda:raise_frame(f1))
right_button.pack(side=RIGHT, padx=20, pady=20)

#sphere
#logo
label1 = Label(f52,image=test,bg="#e0dad6")
label1.image = test
label1.pack(side=TOP, anchor=NW)
#spc
spc = Label(f52, text="",bg='#e0dad6')
spc.pack(pady=30)
#label
f_label = Label(f52, text="Entrer la taille du sphére",font=("Helvetica",16), bg='#e0dad6', fg='#001d26')
f_label.pack()
#input
fct3_input = Entry(f52,width=30)
fct3_input.pack(pady=20,ipady=3)
#execute_button
exec_button = Button(f52, text="Executer", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:[raise_frame(f52),deff.Execute_fct3(fct3_input.get())])
exec_button.pack(padx=30)
#spc
spc = Label(f52, text="",bg='#e0dad6')
spc.pack(pady=28)
#footer_buttons
left_button = Button(f52, text="Retourner", width='10', font=("Helvetica",16), bg="#64ffaa", fg="#FFFFFF",
                    command=lambda:raise_frame(f4))
left_button.pack(side=LEFT, padx=20, pady=20)
right_button = Button(f52, text="Annuler", width='10', font=("Helvetica",16), bg="#eb6b6b", fg="#FFFFFF",
                    command=lambda:raise_frame(f1))
right_button.pack(side=RIGHT, padx=20, pady=20)

#cube
#logo
label1 = Label(f53,image=test,bg="#e0dad6")
label1.image = test
label1.pack(side=TOP, anchor=NW)
#spc
spc = Label(f53, text="",bg='#e0dad6')
spc.pack(pady=30)
#label
f_label = Label(f53, text="Entrer la taille du cube",font=("Helvetica",16), bg='#e0dad6', fg='#001d26')
f_label.pack()
#input
fct4_input = Entry(f53,width=30)
fct4_input.pack(pady=20,ipady=3)
#execute_button
exec_button = Button(f53, text="Executer", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:[raise_frame(f53),deff.Execute_fct4(fct4_input.get())])
exec_button.pack(padx=30)
#spc
spc = Label(f53, text="",bg='#e0dad6')
spc.pack(pady=28)
#footer_buttons
left_button = Button(f53, text="Retourner", width='10', font=("Helvetica",16), bg="#64ffaa", fg="#FFFFFF",
                    command=lambda:raise_frame(f4))
left_button.pack(side=LEFT, padx=20, pady=20)
right_button = Button(f53, text="Annuler", width='10', font=("Helvetica",16), bg="#eb6b6b", fg="#FFFFFF",
                    command=lambda:raise_frame(f1))
right_button.pack(side=RIGHT, padx=20, pady=20)

#Vecteur
#logo
label1 = Label(f54,image=test,bg="#e0dad6")
label1.image = test
label1.pack(side=TOP, anchor=NW)
#spc
spc = Label(f54, text="",bg='#e0dad6')
spc.pack(pady=30)
#spc
spc = Label(f53, text="",bg='#e0dad6')
spc.pack(pady=28)
#footer_buttons
left_button = Button(f54, text="Retourner", width='10', font=("Helvetica",16), bg="#64ffaa", fg="#FFFFFF",
                    command=lambda:raise_frame(f4))
left_button.pack(side=LEFT, padx=20, pady=20)
right_button = Button(f54, text="Annuler", width='10', font=("Helvetica",16), bg="#eb6b6b", fg="#FFFFFF",
                    command=lambda:raise_frame(f1))
right_button.pack(side=RIGHT, padx=20, pady=20)

#results_page
#logo
label1 = Label(f6,image=test,bg="#e0dad6")
label1.image = test
label1.pack(side=TOP, anchor=NW)
#result_image
res_img = Image.open("img/Dessin1.png")
img = ImageTk.PhotoImage(res_img)
label2 = Label(f6,image=img,bg="#ffffff")
label2.image = test
label2.pack()
#canvas = Canvas(f6, width = 300, height = 300,bg="#ffffff")
#canvas.pack()
#img = ImageTk.PhotoImage(Image.open("Dessin.png"))
#canvas.create_image(20, 20, anchor=NW, image=img)
#spc
spc = Label(f6, text="",bg='#e0dad6')
spc.pack()
#download_button
download_button = Button(f6, text="Télécharger", width='10', font=("Helvetica",16), bg="#c972ad", fg="#FFFFFF",
                    command=lambda:deff.Download_img())
download_button.pack(padx=30)
#footer_buttons
left_button = Button(f6, text="Retourner", width='10', font=("Helvetica",16), bg="#64ffaa", fg="#FFFFFF",
                    command=lambda:raise_frame(f2))
left_button.pack(side=LEFT, padx=20,pady=0)
right_button = Button(f6, text="Annuler", width='10', font=("Helvetica",16), bg="#eb6b6b", fg="#FFFFFF",
                    command=lambda:raise_frame(f1))
right_button.pack(side=RIGHT, padx=20,pady=0)