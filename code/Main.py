from tkinter import *
from tkinter import ttk
from sauvegarde_ import nouvelle_sauvegarde, verif_sauvegarde, verifpseudo, user_is_admin
from pdf_opener import open_given_file
from import_csv import get_all_chapters, get_name_exercices, get_name_lessons, get_path_lesson, get_enonce_exercice, get_correction
from add_and_supr_menus import add_chapter_menu, add_exercice_menu, add_lesson_menu, del_chapter_menu, del_lesson_menu, del_exercice_menu
from test_git import *
from datetime import datetime

#git_update()

#Création de la fenètre de base
root = Tk()
root.geometry("1000x600")
root.config(bg="black")
root.minsize(1000,600)
root.maxsize(1000,600)
username = ""
usermdp = ""
is_admin = False

#Permet de reset une page sans la détruire
widget_lst: list = []
def destroy_widgets(special_widget = None) -> None: 
    """Permet de détruire tous les widgets de la fenetre actuelle"""
    if special_widget is None:
        for widget in widget_lst:
            widget.destroy()
    else:
        for widget in widget_lst:
            if widget == special_widget:
                widget.destroy()
                break

def start_menu() -> None:
    """Creer le menu de démarrage"""
    root.title("Authentification")
    #On reset la fenètre
    destroy_widgets()

    #On créé des widgets
    txt = Label(text="__NameError__", bg="Black", fg="White", font=("Arial", 20))
    quit_btn = Button(text="Quitter", command=root.destroy)
    btn_connect = Button(text="     Connexion     ", command=connection_menu, font=("Arial", 17))
    btn_create = Button(text=" Créer un compte ", command=lambda:connection_menu('create'), font=("Arial", 17))

    #On récupère les widgets dans la liste afin de pouvoir les détruire
    widget_lst.append(btn_connect)
    widget_lst.append(quit_btn)
    widget_lst.append(btn_create)
    widget_lst.append(txt)

    #On fait apparaître les widgets sur l'écran
    txt.pack(pady=50)
    btn_connect.pack(pady=100)
    btn_create.pack(pady=0)
    quit_btn.pack(side=BOTTOM, fill=X)

    root.mainloop()
    
def connection_menu(menu:str = 'load') -> None:

    """Creer le menu de connection (soit connection soit charger)"""
    #On reset la fenètre
    destroy_widgets()
    
    def entry_load() -> None:
        global username, is_admin, usermdp
        """systeme de verification d'une sauvegarde à charger"""
        username = pseudo_joueur.get() #On récupère le pseudo et le mdp
        is_admin = user_is_admin(username,"csv_data/csvfile.csv")
        usermdp = mdp_joueur.get()
        error = verif_sauvegarde(str(username), str(usermdp), 'csv_data/csvfile.csv') #on verrifie si le pseudo existe déjà
        if error: #dans le cas d'une erreur
            error_text.config(fg='red', text= "Le nom d'utilisateur ou mot de passe est incorrect !")
            error_text.pack(pady=2)
        else:
            main_menu()

    def entry_create() -> None: 
        global username, is_admin, usermdp
        """systeme de verification/creation d'une nouvelle sauvegarde"""
        username = pseudo_joueur.get()#On récupère le pseudo et le mdp
        usermdp = mdp_joueur.get()
        verification = verifpseudo(username, 'csv_data/csvfile.csv')
        if verification:#dans le cas d'une erreur
            error_text.config(fg ='red', text='Ce pseudo existe déjà !')
        else:
            if len(username) == 0:
                error_text.config(fg='red',  text = "Vous devez utiliser un mot de passe et un pseudo")
            else:
                nouvelle_sauvegarde(username, usermdp, 'csv_data/csvfile.csv')
                is_admin = user_is_admin(username,"csv_data/csvfile.csv")
                main_menu()
    
    #On créé les widgets puis on les récupère dans la liste afin de pouvoir les détruire
    label_titel = Label(root, font = ("Helvetica", 20), bg = 'black', fg='white')
    widget_lst.append(label_titel)

    label_pseudo = Label(root, text = "Votre Pseudo:", font = ("Helvetica", 20),bg = 'black', fg='white')
    widget_lst.append(label_pseudo)

    pseudo_joueur = Entry(root,font = ("Helvetica", 20), bg="black", fg='white', insertbackground='white', width=30, highlightbackground="white")
    widget_lst.append(pseudo_joueur)

    label_mdp = Label(root, text = "Mot de Passe:", font = ("Helvetica", 20), bg="black", fg='white')
    widget_lst.append(label_mdp)

    mdp_joueur = Entry(root,font = ("Helvetica", 20),bg ='black', fg='white', insertbackground='white', width=30, show="*", highlightbackground="white")
    widget_lst.append(mdp_joueur)

    def show()-> None:
        """Permet d'afficher le mot de passe"""
        mdp_joueur.config(show="")
        see_mdp.config(command=hide)

    def hide()-> None:
        """Permet de cacher le mot de passe"""
        mdp_joueur.config(show="*")
        see_mdp.config(command=show)

    see_mdp_bool = BooleanVar()
    see_mdp = Checkbutton(root, fg="black", bg="black",variable=see_mdp_bool,command=show)
    widget_lst.append(see_mdp)

    see_mdp_txt = Label(root,text="Voir Mot de passe:", fg="white", bg="black", font=("Arial",13))
    widget_lst.append(see_mdp_txt)

    error_text = Label(root, text="message erreur", font = ("Helvetica", 20), bg="black", fg='black')
    widget_lst.append(error_text)

    entrer_button = Button(root, text= 'Entrer',font = ("Helvetica", 20))
    widget_lst.append(entrer_button)

    back_btn = Button(text="Retour", command=start_menu)
    widget_lst.append(back_btn)

    
    #Permet la modification entre le menu de connection et de création de compte
    if menu=='create':  #Menu création compte
        root.title("Création d'un compte")
        label_titel.config(text="Veuillez créer un compte:")
        label_pseudo.config(text='Votre pseudo (original):')
        entrer_button.config(command=entry_create)
    else:   #Menu connection
        root.title('Connection')
        label_titel.config(text='Veuillez vous identifier:')
        entrer_button.config(command=entry_load)
    
    #On fait apparaître les widgets sur l'écran
    label_titel.pack(pady=25)
    label_pseudo.pack()
    pseudo_joueur.pack( pady=10)
    label_mdp.pack()
    see_mdp.place(relx=0.75,rely=0.47)
    mdp_joueur.pack(pady= 10)
    see_mdp_txt.place(relx=0.6,rely=0.47)
    entrer_button.pack(pady=10)
    error_text.pack(pady=2)
    back_btn.pack(side=BOTTOM, fill=X)

def main_menu() -> None:
    """On créé la fenêtre du menu principal"""
    global username
    global is_admin
    global has_spawned
    #On reset la fenètre
    root.title("Menu Principal")
    destroy_widgets()
    
    #On créé les widgets
    txt = Label(text="Menu principal", bg="Black", fg="White", font=("Arial", 20))
    quit_btn = Button(text="Quitter", command=root.destroy)

    has_spawned = False

    def lessons(nom: str) -> None:
        global has_spawned
        """On créé le bouton pour accéder aux leçons du chapitre"""

        def access_to_lesson(event) -> None:
            """Permet à l'utilisateur d'acceder à la leçon choisie"""
            select = lessons_btn.get()    #Récupère le nom de l'élément séléctionné
            if select == " + Ajouter une leçon + ": #Si ajouter une leçon
                add_lesson_menu(root, lessons_btn, chapters_btn.get())
            elif select == " - Supprimer une leçon - ": #Si supprimer une leçon
                del_lesson_menu(root, lessons_btn, chapters_btn.get())
            elif not "Veuillez choisir un" in select: #Si pas élément de base
                lesson(get_path_lesson(nom, select),nom,select)
        
        #On crée le bouton de séléction des leçons
        lessons_lst : list = ["Veuillez choisir une leçon :"]
        for lecon in get_name_lessons(nom):
            lessons_lst.append(lecon)
        if is_admin:
            lessons_lst.append(" + Ajouter une leçon + ")
            lessons_lst.append(" - Supprimer une leçon - ")
        lessons_btn = ttk.Combobox(root,values=lessons_lst)
        lessons_btn.current(0)
        lessons_btn.bind("<<ComboboxSelected>>",access_to_lesson)

        #On met en place le bouton
        if not has_spawned:
            widget_lst.append(lessons_btn)
            lessons_btn.pack(pady=50)
            has_spawned = True
    
    def access_to_btn_lessons(_) -> None:
        """Permet de faire apparaitre le bouton pour séléctionner une leçon du chapitre"""
        global has_spawned
        select : str= chapters_btn.get()    #Récupère le nom de l'élément séléctionné
        if select == " + Ajouter un chapitre + ":
            if has_spawned:
                widget_lst.pop().destroy()
                has_spawned = False
            add_chapter_menu(root, chapters_btn)
        elif select == " - Supprimer un chapitre - ":
            if has_spawned:
                widget_lst.pop().destroy()
                has_spawned = False
            del_chapter_menu(root, chapters_btn)
        elif not "Veuillez choisir un " in select:
            if has_spawned:
                x = widget_lst.pop()
                lst_lesons_ = ["Veuillez choisir un chapitre"]
                for chap in get_name_lessons(select):
                    lst_lesons_.append(chap)
                if is_admin:
                    lst_lesons_.append(" + Ajouter un chapitre + ")
                    lst_lesons_.append(" - Supprimer un chapitre - ")
                x.config(values = lst_lesons_)
                widget_lst.append(x)
            lessons(select)
        
    #On crée le bouton de séléction des chapitres
    lst_chapters = ["Veuillez choisir un chapitre"]
    for chap in get_all_chapters():
        lst_chapters.append(chap)
    if is_admin:
        lst_chapters.append(" + Ajouter un chapitre + ")
        lst_chapters.append(" - Supprimer un chapitre - ")
    chapters_btn = ttk.Combobox(root,values=lst_chapters)
    chapters_btn.current(0)
    chapters_btn.bind("<<ComboboxSelected>>", access_to_btn_lessons)
    btn_account = Button(text='Compte (pour le moment ne sert a rien)', font=("Arial", 17))

    #On récupère les widgets dans la liste afin de pouvoir les détruire
    widget_lst.append(chapters_btn)
    widget_lst.append(btn_account)
    widget_lst.append(quit_btn)
    widget_lst.append(txt)

    #On fait apparaître les widgets sur l'écran
    txt.pack(pady=50)
    btn_account.place(anchor=NW)
    chapters_btn.pack(pady=50)
    quit_btn.pack(side=BOTTOM, fill=X)
    
def lesson(lesson_pdf:str ,chapter_name: str, lesson_name: str) -> None:
    """On créé la fenêtre pour accéder aux cours en PDF"""
    #On reset la fenètre
    destroy_widgets()
    root.title(f"Cours {chapter_name}, {lesson_name}")

    #On créé les widgets
    back_btn = Button(text="Retour", command=main_menu)
    btn_open_pdf = Button(text=f"Cours: {chapter_name} {lesson_name}",command=lambda:open_given_file(lesson_pdf))

    def access_to_ex(_) -> None:
        """Permet d'acceder à l'exercice choisi"""
        select = btn_exos.get()    #Récupère le nom de l'élément séléctionné
        if select == " + Ajouter un exercice + ":
            add_exercice_menu(root, btn_exos, chapter_name, lesson_name)
        elif select == " - Supprimer un exercice - ":
            del_exercice_menu(root, btn_exos, chapter_name, lesson_name)
        elif not "Veuillez choisir un" in select: # Si l'élément n'est pas celui de base alors l'utilsateur accede a l'exo
            exercice(get_enonce_exercice(chapter_name, lesson_name, select),chapter_name,lesson_pdf,lesson_name, select)

    lst_exos : list= ["Veuillez choisir un exercice :"]
    for exo in get_name_exercices(chapter_name, lesson_name):
        lst_exos.append(exo)
    if is_admin:
        lst_exos.append(" + Ajouter un exercice + ")
        lst_exos.append(" - Supprimer un exercice - ")
    btn_exos = ttk.Combobox(root,values=lst_exos)
    btn_exos.current(0)
    btn_exos.bind("<<ComboboxSelected>>", access_to_ex)

    #On récupère les widgets dans la liste afin de pouvoir les détruire
    widget_lst.append(back_btn)
    widget_lst.append(btn_open_pdf)
    widget_lst.append(btn_exos)

    #On fait apparaître les widgets sur l'écran
    btn_open_pdf.pack(pady=100)
    btn_exos.pack(pady=50)
    back_btn.pack(side=BOTTOM, fill=X)

def exercice(enonce: str, chapter_name: str, lesson_pdf:str, lesson_name:str, nom_exo) -> None:
    """On créé la fenêtre pour accéder aux exercices en PDF"""
    #On reset la fenètre
    destroy_widgets()
    root.title("Exercice")
    nb_indices_depenses = 0

    def execute_code():
        code = code_entry.get("1.0", "end-1c")
        try:
            a = exec(code)
            result_text.configure(state="normal")
            result_text.delete("1.0", "end")
            result_text.insert("end", "Test reussi!")
        except Exception as e:
            result_text.configure(state="normal")
            result_text.delete("1.0", "end")
            result_text.insert("end", f"Une erreur s'est produite : {e}")
            result_text.configure(state="disabled")

    #Frame 1
    frame_1 = Frame(root, width=850, bg = "black")
    frame_1.grid(row=0, column=0, rowspan=9, columnspan=4, sticky="nsew")

    # Zone de texte pour l'ennonce
    enonce_txt = Label(master = frame_1, text=f"{enonce}", bg="Black", fg="White", font=("Arial", 20), wraplength=300)
    enonce_txt.pack(fill=X, expand=True, pady=10)

    # Zone de texte pour saisir le code
    code_entry = Text(frame_1, height=15)
    code_entry.pack(fill=X, expand=True)

    # Bouton pour exécuter le code
    execute_button = Button(frame_1, text="Exécuter", command=execute_code)
    execute_button.pack(pady=10)

    # Zone de texte pour afficher le résultat
    result_text = Text(frame_1, height=15,state="disabled")
    result_text.pack(fill=X, expand=True)

    frame_2 = Frame(root, width=150, bg="black")
    frame_2.grid(row=0, column=5, rowspan=9, columnspan=1, sticky="nsew")

    #Bouton pour acceder aux indices
    indices_btn = Button(frame_2, text="Indices", bg="Black", fg="black", font=("Arial", 20), height=4)
    indices_btn.pack(pady=50,fill=X, expand=True)    

    if is_admin:
        add_suppr_hint_btn = Button(frame_2, text="Ajouter / supprimer indices", bg="Black", fg="black", font=("Arial", 20), height=4)
        add_suppr_hint_btn.pack(pady=20,fill=X, expand=True)    

    #Bouton pour accéder à la correction
    correction_btn = Button(frame_2,height=6, text="Accéder à la correction", command=lambda:open_given_file(get_correction(chapter_name, lesson_name, nom_exo)), state=DISABLED, font=("Arial", 20), fg="black")
    if nb_indices_depenses >=3:
        correction_btn.config(state=ACTIVE)
    correction_btn.pack(pady=50,fill=X, expand=True)

    frame_3 = Frame(root, bg="black")
    back_btn = Button(frame_3,text="Retour", command=lambda:lesson(lesson_pdf,chapter_name,lesson_name))
    back_btn.pack(fill=X, expand=True)
    frame_3.grid(row=10, column=0, rowspan=1, columnspan=6, sticky="nsew")


    #On récupère les widgets dans la liste afin de pouvoir les détruire
    widget_lst.append(back_btn)
    widget_lst.append(code_entry)
    widget_lst.append(enonce_txt)
    widget_lst.append(result_text)
    widget_lst.append(execute_button)
    widget_lst.append(correction_btn)
    widget_lst.append(indices_btn)
    widget_lst.append(add_suppr_hint_btn)
    widget_lst.append(frame_1)
    widget_lst.append(frame_2)
    widget_lst.append(frame_3)

    #On configure la grille de la fenetre
    for row in range(10):
        root.grid_rowconfigure(row, weight=1)
    for column in range (5): 
        root.grid_columnconfigure(column, weight=1)

#On lance l'application au menu de démarrage
start_menu()
if is_admin:
    git_add_commit_push(["PDF", "csv_data"], f"Mise à jour des fichiers -{datetime.now().date()}")