from tkinter import *
from import_csv import get_all_chapters, add_lesson, get_name_exercices, get_name_lessons, delete_lesson, add_chapter, delete_chapter, add_exercice, delete_exo, add_hint, delete_hint, get_hint
from pdf_opener import recup_path, copy_file, delete_file, recup_path_py

def add_lesson_menu(master, combobox, chapter_selected):
    global path
    window = Toplevel(master=master, bg="black")
    window.geometry("1000x600")
    window.minsize(1000,600)
    window.maxsize(1000,600)
    window.title("Ajouter une leçon")
    window.attributes("-topmost", True)
    path = ""

    label_title = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="Ajouter une leçon")
    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom du chapitre")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", 17), text="")
    path_txt = Label(window, bg="black", fg="white", font=("Cascadia Code", 17), text="Veuillez rensigner le fichier PDF")
    selected_path = Label(window, bg="black", fg="black", font=("Cascadia Code", 17))
    lesson_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom de votre nouvelle leçon")
    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="La leçon a été ajoutée avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=chapter_selected), highlightbackground="white")
    lesson_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")

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


    select_path_btn = Button(window, text="séléctionner le PDF du cours", command=recup_path_bis)
    enter_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    enter_btn = Button(window, image=enter_img, command=enter)
    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window, image= quit_img, command=window.destroy)

    label_title.pack(pady=50)
    chapter_txt.pack()
    chapter_entry.pack(pady=20)
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

    label_title = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="Supprmier une leçon")
    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom du chapitre")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", 17), text="")

    lesson_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom de la leçon à supprimer")
    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="La leçon a été supprimée avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=chapter_selected), highlightbackground="white")
    lesson_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")

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

            label_title_ = Label(sure, bg="black", fg="White", font=("Cascadia Code", 20), text=f"Voulez vous vraiment supprimer la leçon: {lesson_entry.get()} ?\n cela entraînera la suppression de tous les exercices")

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
            
            yes_btn = Button(sure, text="OUI", command=lambda:answer(True))
            no_btn = Button(sure, text="NON", command=lambda:answer(False))

            label_title_.pack(pady=50)
            yes_btn.pack(pady=20)
            no_btn.pack()
        

    enter_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    enter_btn = Button(window, image=enter_img, command=enter)
    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window,image= quit_img, command=window.destroy)

    label_title.pack(pady=50)
    chapter_txt.pack()
    chapter_entry.pack(pady=20)
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

    label_title = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="Ajouter un chapitre")
    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom du chapitre à ajouter")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", 17), text="")

    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="Le chapitre a été ajoutée avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")


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
    chapter_entry.pack(pady=20)
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

    label_title = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="Supprimer un chapitre")
    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom du chapitre à supprimer")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", 17), text="")

    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="Le chapitre a été supprimé avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")


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

            label_title_ = Label(sure, bg="black", fg="White", font=("Cascadia Code", 20), text=f"Voulez vous vraiment supprimer le chapitre: {chapter_entry.get()} ?\n cela entraînera la suppression de toutes les leçons et exercices")

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


            yes_btn = Button(sure, text="OUI", command=lambda:answer(True))
            no_btn = Button(sure, text="NON", command=lambda:answer(False))

            label_title_.pack(pady=50)
            yes_btn.pack(pady=20)
            no_btn.pack()

    enter_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    enter_btn = Button(window, image=enter_img, command=enter)
    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window,image= quit_img, command=window.destroy)

    label_title.pack(pady=50)
    chapter_txt.pack()
    chapter_entry.pack(pady=20)
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

    label_title = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="Ajouter un exercice")
    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom du chapitre")
    
    lesson_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom de la leçon")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", 17), text="")
    path_txt = Label(window, bg="black", fg="white", font=("Cascadia Code", 17), text="Veuillez renseigner le fichier python de la correction")
    selected_path = Label(window, bg="black", fg="black", font=("Cascadia Code", 17))
    exercice_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom de votre nouvel exercice")
    exercice_enonce = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer l'énoncé de l'exercice")
    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="L'exercice a été ajouté avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=chapter_selected), highlightbackground="white")
    lesson_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=lesson_selected), highlightbackground="white")
    exercice_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")
    enonce_entry = Text(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white", state="normal", height=6)

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
            res = add_exercice(chapter_entry.get(), lesson_entry.get(), exercice_entry.get(), enonce_entry.get(), path)
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


    select_path_btn = Button(window, text="Séléctionner le fichier python de la correction", command=recup_path_bis)
    
    enter_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    enter_btn = Button(window, image=enter_img, command=enter)
    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window,image= quit_img, command=window.destroy)

    label_title.pack(pady=0)
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

    label_title = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="Supprimer un exercice")
    chapter_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom du chapitre")
    
    lesson_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom de la leçon")
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", 17), text="")
    exercice_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom de votre exercice à supprimer")
    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="L'exercice a été supprimé avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
    
    chapter_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=chapter_selected), highlightbackground="white")
    lesson_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, textvariable=StringVar(value=lesson_selected), highlightbackground="white")
    exercice_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")

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

            label_title_ = Label(sure, bg="black", fg="White", font=("Cascadia Code", 20), text=f"Voulez vous vraiment supprimer l'exercice: {exercice_entry.get()} ?\n Cela entraînera la suppression de l'exercice, de la correction et de tous les indices", wraplength=1000)

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


            yes_btn = Button(sure, text="OUI", command=lambda:answer(True))
            no_btn = Button(sure, text="NON", command=lambda:answer(False))

            label_title_.pack(pady=50)
            yes_btn.pack(pady=20)
            no_btn.pack()

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


    label_title = Label(master = window, bg="black", text="Modifier un indice",font=("Cascadia Code", 17))
    error_txt = Label(window, bg="black", fg="black", font=("Cascadia Code", 17), text="")
    hint_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 17), text="Insérer le nom de votre indice à jouter ou supprimer:")
    res_txt = Label(window, bg="black", fg="White", font=("Cascadia Code", 20), text="L'indice a été supprimé avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")


    hint_entry = Entry(window, font = ("Cascadia Code", 20), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")

    def enter(command):
        if command == "supprimé":
            if hint_entry.get() not in get_hint(chapitre,lesson,exercice):
                error_txt.config(fg="red", text="Cet indice n'existe pas")
                error_txt.pack(padx=3)
            else:
                sure = Toplevel(master=window, bg="black")
                sure.geometry("1000x600")
                sure.minsize(1000,300)
                sure.maxsize(1000,300)
                sure.title("En êtes vous sûr ?")
                sure.attributes("-topmost",True)

                label_title_ = Label(sure, bg="black", fg="White", font=("Cascadia Code", 20), text=f"Voulez vous vraiment supprimer l'indice: {hint_entry.get()} ?", wraplength=1000)

                def answer(x):
                    if not x :
                        sure.destroy()
                    else:
                        sure.destroy()
                        res = delete_hint(chapter=chapitre, lesson=lesson, exercice=exercice)
                        if res is False:
                            error_txt.config(text="Il y'a eu un problème... Il faut recommencer", fg = "red")
                        else:
                            error_txt.config(fg="black")
                            res_txt.config(text=f"L'indice a été {command} avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
                            res_txt.pack(pady=15)
                yes_btn = Button(sure, text="OUI", command=lambda:answer(True))
                no_btn = Button(sure, text="NON", command=lambda:answer(False))

                label_title_.pack(pady=50)
                yes_btn.pack(pady=20)
                no_btn.pack()

        elif command == "ajouté":
            if hint_entry.get() is "":
                error_txt.config(text= "Veuillez renseigner un indice valable", fg="red")
                error_txt.pack(pady=3)
            else:

                res = add_hint(hint_entry.get(), chapitre, lesson, exercice)
                if res is False:
                    error_txt.config(text="Il y'a eu un problème... Il faut recommencer", fg = "red")
                else:
                    error_txt.config(fg="black")
                    res_txt.config(text=f"L'indice a été {command} avec succès !\n Vous pouvez fermer cette fenêtre, elle se fermera dans 5 secondes")
                    res_txt.pack(pady=15)
    
    add_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    add_btn = Button(window, text="ajouter", command=lambda:enter("ajouté"))
    del_img = PhotoImage(master = window, file="graphics/enter.png").subsample(2)
    del_btn = Button(window, text="supprimer", command=lambda:enter("supprimé"))

    quit_img = PhotoImage(master = window, file="graphics/quitter.png")
    quit_btn = Button(master = window,image= quit_img, command=window.destroy)

    label_title.pack(pady = 20)
    hint_txt.pack(pady=10)
    hint_entry.pack()
    error_txt.pack(pady=3)
    add_btn.pack(pady=10)
    del_btn.pack(pady=10)

    quit_btn.pack(side=BOTTOM, fill=X)

    window.mainloop()