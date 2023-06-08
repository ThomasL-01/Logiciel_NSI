from tkinter import *
from tkinter import ttk
from import_csv import get_all_chapters, add_lesson, get_name_exercices, get_name_lessons, delete_lesson, add_chapter, delete_chapter, add_exercice, delete_exo, add_hint, delete_hint, get_hint, get_user, delete_user,modif_mdp_admin
from pdf_opener import recup_path, copy_file, delete_file, recup_path_py
from sauvegarde_ import add_user
import platform

if platform.system() == "Darwin":
    font = 17
    big_font = 20
else:
    font = 14
    big_font = 17

def set_background(image_path: str, root) -> None:
    """Définit l'image de fond de la fenêtre principale"""
    background_image = PhotoImage(file=image_path)
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

def menu_compte(master):
    window = Toplevel(master=master, bg="black")
    window.geometry("1000x600")
    window.minsize(1000,600)
    window.maxsize(1000,600)
    window.title("Compte")
    window.attributes("-topmost", True)
    set_background("graphics/bg.png", window)

    def add_user_window():
        window.attributes("-topmost", False)
        window_2 = Toplevel(window)
        window_2.minsize(1000,600)
        window_2.maxsize(1000,600)
        window_2.attributes("-topmost", True)
        set_background("graphics/bg.png", window_2)

        label_title = Label(window_2, bg="black", fg="White", font=("Cascadia Code", big_font), text="Ajouter un utilisateur")
        user_txt = Label(window_2, bg="black", fg="White", font=("Cascadia Code", big_font), text="Ajouter le nom de l'utilisateur:")
        error_txt = Label(window_2, bg="black", fg="black", font=("Cascadia Code", big_font), text="")
        mdp_txt = Label(window_2, bg="black", fg="white", font=("Cascadia Code", big_font), text="Renseigner son mot de passe:")
        selected_mdp = Label(window_2, bg="black", fg="black", font=("Cascadia Code", big_font))
        res_txt = Label(window_2, bg="black", fg="White", font=("Cascadia Code", big_font), text="L'utilisateur a été ajouter avec succès' !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
        
        user_entry = Entry(window_2, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")
        mdp_entry = Entry(window_2, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")

        def enter():
            if user_entry.get() == "" or mdp_entry.get() == "":
                error_txt.config(fg="red", text="Il faut rentrer des valeurs correctes")
                error_txt.pack()
            else:
                add_user(user_entry.get(), mdp_entry.get())
                res_txt.pack()
        
        
        enter_img = PhotoImage(master = window_2, file="graphics/enter.png").subsample(2)
        enter_btn = Button(window_2, image=enter_img, command=enter)

        quit_img = PhotoImage(master = window, file="graphics/quitter.png")
        quit_btn = Button(master = window_2, image= quit_img, command=window_2.destroy)

        label_title.pack(pady = big_font)
        user_txt.pack()
        user_entry.pack()
        mdp_txt.pack(pady = big_font)
        mdp_entry.pack()
        selected_mdp.pack()
        error_txt.pack()
        enter_btn.pack(pady = big_font)
        quit_btn.pack(side=BOTTOM, fill=X)

        window_2.mainloop()

    def suppr_user_window():
        window.attributes("-topmost", False)
        window_2 = Toplevel(window)
        window_2.minsize(1000,600)
        window_2.maxsize(1000,600)
        window_2.attributes("-topmost", True)
        set_background("graphics/bg.png", window_2)

        label_title = Label(window_2, bg="black", fg="White", font=("Cascadia Code", big_font), text="Supprimer un utilisateur")
        user_txt = Label(window_2, bg="black", fg="White", font=("Cascadia Code", big_font), text="Ajouter le nom de l'utilisateur: que vous voulez supprimer")
        error_txt = Label(window_2, bg="black", fg="black", font=("Cascadia Code", big_font), text="")
        res_txt = Label(window_2, bg="black", fg="White", font=("Cascadia Code", big_font), text="L'utilisateur a été supprimer avec succès' !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
        
        user_entry = Entry(window_2, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")

        def enter():
            if user_entry.get() == "" or user_entry.get() not in get_user():
                error_txt.config(fg="red", text="Il faut rentrer des valeurs correctes")
                error_txt.pack()
            else:
                delete_user(user_entry.get())
                res_txt.pack()
        
        
        enter_img = PhotoImage(master = window_2, file="graphics/enter.png").subsample(2)
        enter_btn = Button(window_2, image=enter_img, command=enter)

        quit_img = PhotoImage(master = window, file="graphics/quitter.png")
        quit_btn = Button(master = window_2, image= quit_img, command=window_2.destroy)
        
        label_title.pack()
        user_txt.pack()
        user_entry.pack()
        error_txt.pack()
        enter_btn.pack()
        quit_btn.pack(side=BOTTOM, fill=X)

        window_2.mainloop()
    
    def modifier_mdp():
        window.attributes("-topmost", False)
        window_2 = Toplevel(window)
        window_2.minsize(1000,600)
        window_2.maxsize(1000,600)
        window_2.attributes("-topmost", True)
        set_background("graphics/bg.png", window_2)

        label_title = Label(window_2, bg="black", fg="White", font=("Cascadia Code", big_font), text="Modifier mot de passe")
        user_txt = Label(window_2, bg="black", fg="White", font=("Cascadia Code", big_font), text="Veuillez mettre votre nouveau mot de passe")
        error_txt = Label(window_2, bg="black", fg="black", font=("Cascadia Code", big_font), text="")
        user2_txt = Label(window_2, bg="black", fg="white", font=("Cascadia Code", big_font), text="Veuillez de nouveau mettre votre nouveau mot de passe")
        selected_user2 = Label(window_2, bg="black", fg="black", font=("Cascadia Code", big_font))
        res_txt = Label(window_2, bg="black", fg="White", font=("Cascadia Code", big_font), text="Le mot de passe a été modifier avec succès' !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
        
        user_entry = Entry(window_2, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")
        user2_entry = Entry(window_2, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")

        def enter():
            if user_entry.get() != user2_entry.get():
                error_txt.config(fg="red", text="Il faut rentrer des valeurs correctes")
                error_txt.pack()
            else:
                error_txt.config(fg="black", text = "")
                modif_mdp_admin(user_entry.get())
                res_txt.pack()
        
        
        enter_img = PhotoImage(master = window_2, file="graphics/enter.png").subsample(2)
        enter_btn = Button(window_2, image=enter_img, command=enter)

        quit_img = PhotoImage(master = window, file="graphics/quitter.png")
        quit_btn = Button(master = window_2, image= quit_img, command=window_2.destroy)
        
        label_title.pack()
        user_txt.pack()
        user_entry.pack()
        user2_txt.pack()
        user2_entry.pack()
        selected_user2.pack()
        error_txt.pack()
        enter_btn.pack()
        quit_btn.pack(side=BOTTOM, fill=X)

        window_2.mainloop()
    
    useradd = Button(window,text='Ajouter un utilisateur', font=("Cascadia Code", big_font), command = add_user_window, pady = big_font)
    usersuppr = Button(window,text='Supprimer un utilisateur', font=("Cascadia Code", big_font), command = suppr_user_window, pady = big_font)
    usermodif = Button(window,text='Modifier mot de passe', font=("Cascadia Code", big_font), command = modifier_mdp, pady = big_font)
    #On crée le bouton de séléction des users
    users_lst : list = ["Voici la liste des users :"]
    for user in get_user():
        users_lst.append(user)
    user_btn = ttk.Combobox(window,values=users_lst, width = 40)
    user_btn.current(0)
    user_btn.bind("<<ComboboxSelected>>",None)
    
    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window, image= quit_img, command=window.destroy)

    useradd.pack(pady=big_font)
    usersuppr.pack(pady=big_font)
    usermodif.pack(pady=big_font)
    user_btn.pack(pady=30)
    quit_btn.pack(side=BOTTOM, fill=X)

    window.mainloop()

def add_lesson_menu(master, combobox, chapter_selected):
    global path
    window = Toplevel(master=master, bg="black")
    window.geometry("1000x600")
    window.minsize(1000,600)
    window.maxsize(1000,600)
    window.title("Ajouter une leçon")
    window.attributes("-topmost", True)
    path = ""
    set_background("graphics/bg.png", window)

    label_title = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Ajouter une leçon")
    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Insérer le nom du chapitre")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", big_font), text="")
    path_txt = Label(window, bg="black", fg="white", font=("Cascadia Code", big_font), text="Veuillez rensigner le fichier PDF")
    selected_path = Label(window, bg="black", fg="black", font=("Cascadia Code", big_font))
    lesson_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Insérer le nom de votre nouvelle leçon")
    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="La leçon a été ajoutée avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=chapter_selected), highlightbackground="white")
    lesson_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")

    def recup_path_bis():
        global path
        window.attributes("-topmost", False)
        path = recup_path()
        window.attributes("-topmost", True)
        selected_path.config(fg="white", text=path)
        select_path_btn.config(text="changer le chemin du fichier")

    def enter():
        global path
        if chapter_entry.get() not in get_all_chapters():
            error_txt.config(text="Ce chapitre n'existe pas !", fg="red")
        elif lesson_entry.get() in get_name_lessons(chapter_entry.get()) or lesson_entry.get() == "":
            error_txt.config(text="Cette leçon existe déjà ou ne convient pas!", fg = "red")
        elif path == "":
            error_txt.config(text="Votre chemin de fichier ne convient pas", fg = "red")
        else:
            path = copy_file(path)
            res = add_lesson(chapter_entry.get(), f"'{path}'", f" '{lesson_entry.get()}'")
            if res is False:
                delete_file(path)
                error_txt.config(text="Il y'a eu un problème... Il faut recommencer", fg = "red")
            else:
                error_txt.config(fg="black")
                res_txt.pack(pady=15)
                lst_chapters = ["Veuillez choisir un chapitre"]
                for lesson in get_name_lessons(chapter_entry.get()):
                        lst_chapters.append(lesson)
                lst_chapters.append(" + Ajouter un chapitre + ")
                lst_chapters.append(" - Supprimer un chapitre - ")  
                combobox.config(values = lst_chapters) 
                window.after(5000, window.destroy)

    select_img = PhotoImage(master = window, file="graphics/select_file.png").subsample(2)
    select_path_btn = Button(window,image=select_img, command=recup_path_bis)
    enter_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    enter_btn = Button(window, image=enter_img, command=enter)
    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window, image= quit_img, command=window.destroy)

    label_title.pack(pady=50)
    chapter_txt.pack()
    chapter_entry.pack(pady=big_font)
    path_txt.pack()
    select_path_btn.pack(pady=10)
    selected_path.pack()
    lesson_txt.pack(pady=5)
    lesson_entry.pack()
    error_txt.pack(pady=10)
    enter_btn.pack(pady=0)
    quit_btn.pack(side=BOTTOM, fill=X)

    window.mainloop()

def del_lesson_menu(master, combobox, chapter_selected):
    window = Toplevel(master=master, bg="black")
    window.geometry("1000x600")
    window.minsize(1000,600)
    window.maxsize(1000,600)
    window.title("Supprimer une leçon")
    window.attributes("-topmost", True)
    set_background("graphics/bg.png", window)

    label_title = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Supprmier une leçon")
    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Insérer le nom du chapitre")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", big_font), text="")

    lesson_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Insérer le nom de la leçon à supprimer")
    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="La leçon a été supprimée avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=chapter_selected), highlightbackground="white")
    lesson_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")

    def enter():
        global path
        if chapter_entry.get() not in get_all_chapters():
            error_txt.config(text="Ce chapitre n'existe pas !", fg="red")
        elif lesson_entry.get() not in get_name_lessons(chapter_entry.get()) or lesson_entry.get() == "":
            error_txt.config(text="Cette leçon n'existe pas", fg = "red")
        else:
            sure = Toplevel(master=window, bg="black")
            sure.geometry("1000x600")
            sure.minsize(1000,300)
            sure.maxsize(1000,300)
            sure.title("En êtes vous sûr ?")
            sure.attributes("-topmost",True)

            label_title_ = Label(sure, bg="black", fg="White", font=("Cascadia Code", big_font), text=f"Voulez vous vraiment supprimer la leçon: {lesson_entry.get()} ?\n cela entraînera la suppression de tous les exercices")

            def answer(x):
                if not x :
                    sure.destroy()
                else:
                    sure.destroy()

                    res = delete_lesson(chapter_entry.get(),lesson_entry.get())
                    if res is False:
                        error_txt.config(text="Il y'a eu un problème... Il faut recommencer", fg = "red")
                    else:
                        error_txt.config(fg="black")
                        res_txt.pack(pady=15)
                        lst_chapters = ["Veuillez choisir un chapitre"]
                        for lesson in get_name_lessons(chapter_entry.get()):
                                lst_chapters.append(lesson)
                        lst_chapters.append(" + Ajouter un chapitre + ")
                        lst_chapters.append(" - Supprimer un chapitre - ")  
                        combobox.config(values = lst_chapters) 
                        window.after(5000, window.destroy)

            
            yes_img = PhotoImage(master = window, file="graphics/oui.png").subsample(2)
            yes_btn = Button(sure, image = yes_img, command=lambda:answer(True))
            no_img = PhotoImage(master = window, file="graphics/non.png").subsample(2)
            no_btn = Button(sure, image = no_img, command=lambda:answer(False))

            label_title_.pack(pady=50)
            yes_btn.pack(pady=big_font)
            no_btn.pack()

            sure.mainloop()
        

    enter_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    enter_btn = Button(window, image=enter_img, command=enter)
    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window,image= quit_img, command=window.destroy)

    label_title.pack(pady=50)
    chapter_txt.pack()
    chapter_entry.pack(pady=big_font)
    lesson_txt.pack(pady=5)
    lesson_entry.pack()
    error_txt.pack(pady=10)
    enter_btn.pack(pady=0)
    quit_btn.pack(side=BOTTOM, fill=X)

    window.mainloop()

def add_chapter_menu(master, combobox):
    window = Toplevel(master=master, bg="black")
    window.geometry("1000x600")
    window.minsize(1000,600)
    window.maxsize(1000,600)
    window.title("Ajouter un chapitre")
    window.attributes("-topmost", True)
    set_background("graphics/bg.png", window)

    label_title = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Ajouter un chapitre")
    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Insérer le nom du chapitre à ajouter")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", big_font), text="")

    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Le chapitre a été ajoutée avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")


    def enter():
        if chapter_entry.get() in get_all_chapters():
            error_txt.config(text="Ce chapitre existe déjà !", fg="red")
        elif chapter_entry.get() == "":
            error_txt.config(text="Veuillez insérer un nom de chapitre valide !", fg="red")
        else:
            res = add_chapter(chapter_entry.get())
            if res is False:
                error_txt.config(text="Il y'a eu un problème... Il faut recommencer", fg = "red")
            else:
                error_txt.config(fg="black")
                res_txt.pack(pady=15)
                lst_chapters = ["Veuillez choisir un chapitre"]
                for chap in get_all_chapters():
                        lst_chapters.append(chap)
                lst_chapters.append(" + Ajouter un chapitre + ")
                lst_chapters.append(" - Supprimer un chapitre - ")  
                combobox.config(values = lst_chapters) 
                window.after(5000, window.destroy)

    enter_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    enter_btn = Button(window, image=enter_img, command=enter)
    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window,image= quit_img, command=window.destroy)

    label_title.pack(pady=50)
    chapter_txt.pack()
    chapter_entry.pack(pady=big_font)
    error_txt.pack(pady=5)
    enter_btn.pack(pady=0)
    quit_btn.pack(side=BOTTOM, fill=X)

    window.mainloop()

def del_chapter_menu(master, combobox):
    window = Toplevel(master=master, bg="black")
    window.geometry("1000x600")
    window.minsize(1000,600)
    window.maxsize(1000,600)
    window.title("Supprimer un chapitre")
    window.attributes("-topmost", True)
    set_background("graphics/bg.png", window)

    label_title = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Supprimer un chapitre")
    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Insérer le nom du chapitre à supprimer")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", big_font), text="")

    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Le chapitre a été supprimé avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")


    def enter():
        if chapter_entry.get() not in get_all_chapters():
            error_txt.config(text="Ce chapitre n'existe pas !", fg="red")
        elif chapter_entry.get() == "":
            error_txt.config(text="Veuillez insérer un nom de chapitre valide !", fg="red")
        else:
            sure = Toplevel(master=window, bg="black")
            sure.geometry("1000x600")
            sure.minsize(1000,300)
            sure.maxsize(1000,300)
            sure.title("En êtes vous sûr ?")
            sure.attributes("-topmost",True)

            label_title_ = Label(sure, bg="black", fg="White", font=("Cascadia Code", big_font), text=f"Voulez vous vraiment supprimer le chapitre: {chapter_entry.get()} ?\n cela entraînera la suppression de toutes les leçons et exercices")

            def answer(x):
                if not x :
                    sure.destroy()
                else:
                    sure.destroy()
                    res = delete_chapter(chapter_entry.get())
                    if res is False:
                        error_txt.config(text="Il y'a eu un problème... Il faut recommencer", fg = "red")
                    else:
                        error_txt.config(fg="black")
                        res_txt.pack(pady=15)
                        lst_chapters = ["Veuillez choisir un chapitre"]
                        for chap in get_all_chapters():
                                lst_chapters.append(chap)
                        lst_chapters.append(" + Ajouter un chapitre + ")
                        lst_chapters.append(" - Supprimer un chapitre - ")  
                        combobox.config(values = lst_chapters) 
                        window.after(5000, window.destroy)

            yes_img = PhotoImage(master = window, file="graphics/oui.png").subsample(2)
            yes_btn = Button(sure, image = yes_img, command=lambda:answer(True))
            no_img = PhotoImage(master = window, file="graphics/non.png").subsample(2)
            no_btn = Button(sure, image = no_img, command=lambda:answer(False))

            label_title_.pack(pady=50)
            yes_btn.pack(pady=big_font)
            no_btn.pack()

            sure.mainloop()

    enter_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    enter_btn = Button(window, image=enter_img, command=enter)
    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window,image= quit_img, command=window.destroy)

    label_title.pack(pady=50)
    chapter_txt.pack()
    chapter_entry.pack(pady=big_font)
    error_txt.pack(pady=5)
    enter_btn.pack(pady=0)
    quit_btn.pack(side=BOTTOM, fill=X)

    window.mainloop()

def add_exercice_menu(master, combobox, chapter_selected, lesson_selected):
    global path
    window = Toplevel(master=master, bg="black")
    window.geometry("1000x600")
    window.minsize(1000,600)
    window.maxsize(1000,600)
    window.title("Ajouter un exercice")
    window.attributes("-topmost", True)
    path = ""
    set_background("graphics/bg.png", window)

    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 16), text="Insérer le nom du chapitre")
    
    lesson_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 16), text="Insérer le nom de la leçon")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", 16), text="")
    path_txt = Label(window, bg="black", fg="white", font=("Cascadia Code", 16), text="Veuillez renseigner le fichier python de la correction")
    selected_path = Label(window, bg="black", fg="black", font=("Cascadia Code", 16))
    exercice_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 16), text="Insérer le nom de votre nouvel exercice")
    exercice_enonce = Label(window, bg="black", fg="White", font=("Cascadia Code", 16), text="Insérer l'énoncé de l'exercice")
    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 16), text="L'exercice a été ajouté avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=chapter_selected), highlightbackground="white")
    lesson_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=lesson_selected), highlightbackground="white")
    exercice_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")
    enonce_entry = Text(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white", state="normal", height=5)

    def recup_path_bis():
        global path
        window.attributes("-topmost", False)
        path = recup_path_py()
        window.attributes("-topmost", True)
        selected_path.config(fg="white", text=path)
        select_path_btn.config(text="Changer le chemin du fichier")

    def enter(): 
        global path
        if chapter_entry.get() not in get_all_chapters():
            error_txt.config(text="Ce chapitre n'existe pas !", fg="red")
        elif lesson_entry.get() not in get_name_lessons(chapter_entry.get()) or lesson_entry.get() == "":
            error_txt.config(text="Cette leçon existe déjà ou ne convient pas!", fg = "red")
        elif exercice_entry.get() in get_name_exercices(chapter_entry.get(), lesson_entry.get()) or exercice_entry == "":
            error_txt.config(text="Cet exercice existe déjà ou ne convient pas!", fg = "red")
        elif path == "":
            error_txt.config(text="Votre chemin de fichier ne convient pas", fg = "red")
        else:
            path = copy_file(path)
            res = add_exercice(chapter_entry.get(), lesson_entry.get(), exercice_entry.get(), enonce_entry.get("1.0", "end-1c"), path)
            if res is False:
                delete_file(path)
                error_txt.config(text="Il y'a eu un problème... Il faut recommencer", fg = "red")
            else:
                error_txt.config(fg="black")
                res_txt.pack(pady=15)
                lst_exos = ["Veuillez choisir un exercice"]
                for exo in get_name_exercices(chapter_entry.get(), lesson_entry.get()):
                    lst_exos.append(exo)
                lst_exos.append(" + Ajouter un exercice + ")
                lst_exos.append(" - Supprimer un exercice - ")  
                combobox.config(values = lst_exos) 
                window.after(5000, window.destroy)

    select_img = PhotoImage(master = window, file="graphics/select_file.png").subsample(2)
    select_path_btn = Button(window, image=select_img, command=recup_path_bis)
    
    enter_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    enter_btn = Button(window, image=enter_img, command=enter)
    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window,image= quit_img, command=window.destroy)

    chapter_txt.pack()
    chapter_entry.pack(pady=0)
    path_txt.pack()
    select_path_btn.pack(pady=0)
    selected_path.pack()
    lesson_txt.pack(pady=0)
    lesson_entry.pack()
    exercice_txt.pack()
    exercice_entry.pack()
    exercice_enonce.pack()
    enonce_entry.pack()
    error_txt.pack(pady=0)
    enter_btn.pack(pady=0)
    quit_btn.pack(side=BOTTOM, fill=X)

    window.mainloop()

def del_exercice_menu(master, combobox, chapter_selected, lesson_selected):
    window = Toplevel(master=master, bg="black")
    window.geometry("1000x600")
    window.minsize(1000,600)
    window.maxsize(1000,600)
    window.title("Supprimer un exercice")
    window.attributes("-topmost", True)
    set_background("graphics/bg.png", window)

    label_title = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Supprimer un exercice")
    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Insérer le nom du chapitre")
    
    lesson_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Insérer le nom de la leçon")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", big_font), text="")
    exercice_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Insérer le nom de votre exercice à supprimer")
    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="L'exercice a été supprimé avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=chapter_selected), highlightbackground="white")
    lesson_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=lesson_selected), highlightbackground="white")
    exercice_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")

    def enter(): 
        if chapter_entry.get() not in get_all_chapters():
            error_txt.config(text="Ce chapitre n'existe pas !", fg="red")
        elif lesson_entry.get() not in get_name_lessons(chapter_entry.get()) or lesson_entry.get() == "":
            error_txt.config(text="Cette leçon existe déjà ou ne convient pas!", fg = "red")
        elif exercice_entry.get() not in get_name_exercices(chapter_entry.get(), lesson_entry.get()) or exercice_entry == "":
            error_txt.config(text="Cet exercice n'existe pas ou ne convient pas!", fg = "red")
        else:
            sure = Toplevel(master=window, bg="black")
            sure.geometry("1000x600")
            sure.minsize(1000,300)
            sure.maxsize(1000,300)
            sure.title("En êtes vous sûr ?")
            sure.attributes("-topmost",True)

            label_title_ = Label(sure, bg="black", fg="White", font=("Cascadia Code", big_font), text=f"Voulez vous vraiment supprimer l'exercice: {exercice_entry.get()} ?\n Cela entraînera la suppression de l'exercice, de la correction et de tous les indices", wraplength=1000)

            def answer(x):
                if not x :
                    sure.destroy()
                else:
                    sure.destroy()
                    res = delete_exo(chapter_entry.get(), lesson_entry.get(), exercice_entry.get())
                    if res is False:
                        error_txt.config(text="Il y'a eu un problème... Il faut recommencer", fg = "red")
                    else:
                        error_txt.config(fg="black")
                        res_txt.pack(pady=15)
                        lst_exos = ["Veuillez choisir un exercice"]
                        for exo in get_name_exercices(chapter_entry.get(), lesson_entry.get()):
                                lst_exos.append(exo)
                        lst_exos.append(" + Ajouter un exercice + ")
                        lst_exos.append(" - Supprimer un exercice - ")  
                        combobox.config(values = lst_exos) 
                        window.after(5000, window.destroy)


            yes_img = PhotoImage(master = window, file="graphics/oui.png").subsample(2)
            yes_btn = Button(sure, image = yes_img, command=lambda:answer(True))
            no_img = PhotoImage(master = window, file="graphics/non.png").subsample(2)
            no_btn = Button(sure, image = no_img, command=lambda:answer(False))

            label_title_.pack(pady=50)
            yes_btn.pack(pady=big_font)
            no_btn.pack()

            sure.mainloop()

    enter_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    enter_btn = Button(window, image=enter_img, command=enter)
    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window,image= quit_img, command=window.destroy)

    label_title.pack(pady=0)
    chapter_txt.pack()
    chapter_entry.pack(pady=0)

    lesson_txt.pack(pady=0)
    lesson_entry.pack()
    exercice_txt.pack()
    exercice_entry.pack()
    error_txt.pack(pady=0)
    enter_btn.pack(pady=0)
    quit_btn.pack(side=BOTTOM, fill=X)


    window.mainloop()

def modif_hint_menu(master,chapitre,lesson,exercice):
    window = Toplevel(master = master, bg="black")
    window.geometry("1000x600")
    window.minsize(1000,600)
    window.maxsize(1000,600)
    window.title("Modifier un indice")
    window.attributes("-topmost", True)
    set_background("graphics/bg.png", window)

    label_title = Label(master = window, bg="black", text="Modifier un indice",font=("Cascadia Code", big_font))
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", big_font), text="")
    hint_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Ii vous souhaitez supprimer un indice, séléctionné")
    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="")

    hint_add_label = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Si vous souhaitez ajouter un indice, rensignez le ici:")
    hint_add_entry = Entry(window, font = ("Cascadia Code", big_font), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")

    info_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", big_font), text="Cliquez sur l'action correspondante:")
    
    def enter(command, combobox = None):
        if command == "supprimé":
            hint_selected = hint_suppr.get()
            sure = Toplevel(master=window, bg="black")
            sure.geometry("1000x600")
            sure.minsize(1000,300)
            sure.maxsize(1000,300)
            sure.title("En êtes vous sûr ?")
            sure.attributes("-topmost",True)

            label_title_ = Label(sure, bg="black", fg="White", font=("Cascadia Code", big_font), text=f"Voulez vous vraiment supprimer l'indice ?", wraplength=1000)

            def answer(x):
                if not x :
                    sure.destroy()
                else:
                    sure.destroy()
                    res = delete_hint(chapter=chapitre, lesson=lesson, exercice=exercice, txt = hint_selected)
                    if res is False:
                        error_txt.config(text="Il y'a eu un problème... Il faut recommencer", fg = "red")
                    else:
                        error_txt.config(fg="black")
                        res_txt.config(text=f"L'indice a été supprimé avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
                        res_txt.pack(pady=15)
                        lst_hint = ["Veuillez choisir un indice"]
                        for hint in get_hint(chapitre,lesson,exercice):
                                lst_hint.append(hint)
                        combobox.config(values = lst_hint) 
                        window.after(5000, window.destroy)
                        
            yes_img = PhotoImage(master = window, file="graphics/oui.png").subsample(2)
            yes_btn = Button(sure, image = yes_img, command=lambda:answer(True))
            no_img = PhotoImage(master = window, file="graphics/non.png").subsample(2)
            no_btn = Button(sure, image = no_img, command=lambda:answer(False))

            label_title_.pack(pady=50)
            yes_btn.pack(pady=big_font)
            no_btn.pack()

            sure.mainloop()

        if command == "ajouté":
            if hint_add_entry.get() == "":
                error_txt.config(text= "Veuillez renseigner un indice valable", fg="red")
                error_txt.pack(pady=3)
            else:
                res = add_hint(hint_add_entry.get(), chapitre, lesson, exercice)
                if res is False:
                    error_txt.config(text="Il y'a eu un problème... Il faut recommencer", fg = "red")
                else:
                    error_txt.config(fg="black")
                    res_txt.config(text=f"L'indice a été ajouté avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
                    res_txt.pack(pady=15)
                    window.after(5000, window.destroy)

    lst_hint = ["Veuillez choisir un indice à supprimer"]
    for hint in get_hint(chapitre,lesson,exercice):
        lst_hint.append(hint)
    hint_suppr = ttk.Combobox(window,values=lst_hint, width = 40)
    hint_suppr.current(0)
    hint_suppr.bind("<<ComboboxSelected>>",None)

    add_img = PhotoImage(master = window, file="graphics/ajouter.png").subsample(2)
    add_btn = Button(window, image=add_img, command=lambda:enter("ajouté"))
    del_img = PhotoImage(master = window, file="graphics/supprimer.png").subsample(2)
    del_btn = Button(window,image = del_img, command=lambda:enter("supprimé", hint_suppr))

    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window,image= quit_img, command=window.destroy)

    label_title.pack(pady = 10)
    hint_txt.pack(pady=10)
    hint_suppr.pack(pady=10)
    hint_add_label.pack(pady = 10)
    hint_add_entry.pack(pady = 10)
    error_txt.pack(pady=3)
    info_txt.pack(pady=10)
    add_btn.pack(pady=10)
    del_btn.pack(pady = 10)

    quit_btn.pack(side=BOTTOM, fill=X)

    window.mainloop()