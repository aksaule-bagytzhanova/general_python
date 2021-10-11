from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import sqlite3 as sq
import msvcrt
import keyboard
from time import *
while True:
    if keyboard.is_pressed('q'):  
        print('You Pressed A Key!')
        break  
    # with sq.connect("shop.db") as db:
    #     cursor = db.cursor()
        # cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
        #                     id INTEGER PRIMARY KEY,
        #                     username TEXT NOT NULL,
        #                     password TEXT NOT NULL);
        #     """)
        # cursor.execute("INSERT INTO users(username, password) VALUES(?,?)", ("Aksi", "aksi"))
        # db.commit()

        # cursor.execute("INSERT INTO users(username, password) VALUES(?,?)", ("Sula", "sula"))
        # db.commit()

    def click():
        username1 = ent2.get()
        password2 = ent3.get()
        with sq.connect("shop.db") as db:
            cursor = db.cursor()

            cursor.execute("SELECT password FROM users WHERE username= '"+ username1 +"' ")
            pas = cursor.fetchone()
            pas = list(pas)
            global io 
            io = False
            if pas[0] == password2:
                labMes.config(text="You are in")
                io= True
                if io:
                    sleep(5)
                    main_root.destroy()

                    root = Tk()

                    root.geometry("500x500")
                    root.title("Lesson 2 tk")
                    root.config(bg="white")


                    label = Label(root, text="Hello, to our market!", font=('Times', 25), bg="white").pack()


                    canvas = Canvas(root, bg="white")
                    image = Image.open("C:/Users/aksau/Desktop/cap.jpg")
                    photo = ImageTk.PhotoImage(image)
                    image = canvas.create_image(60, 30, anchor='nw',image=photo)
                    canvas.pack()

                    but = Button(root, text="Купить").pack()

                    root.mainloop()
            else:
                labMes.config(text="Invalid password or login")






    main_root = Tk()
    main_root.geometry("500x500")
    main_root.title("Lesson 2 tk")

    lab1 = Label(main_root, text="First login please!", font=("Times", 20))
    lab1.place(x=150,y=20)

    lab2 = Label(main_root, text="Login", font=("Times", 20))
    lab2.place(x=150,y=50)

    ent2 = Entry(main_root, text ="")
    ent2.place(x=150,y=90)

    lab3 = Label(main_root, text="Password", font=("Times", 20))
    lab3.place(x=150,y=120)

    ent3 = Entry(main_root, text="")
    ent3.place(x=150,y=150)

    but = Button(main_root, text="Login", command=click)
    but.place(x=150,y=220)

    labMes = Label(main_root, text="ugyyhujiok", font=("Times", 20))
    labMes.place(x=150,y=400)

    main_root.mainloop()

    


