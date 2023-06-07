import csv
from pdf_opener import delete_file
from sauvegarde_ import add_user
#Module permettant tout ce qu'il doit se passer au niveau de la sauvegarde des chapitres, exercices, corrections, leçons et indices.
#Tu trouveras forcément ton bonheur !

def get_all_chapters() -> list: 
    """Permet de récupérer la liste de tous les chapitres"""
    f = open("csv_data/chapitres.csv", "r", encoding= "utf-8")
    table = list(csv.DictReader(f,delimiter=";")) #Preciser que le delimiter est ; et non ,
    val = []
    for e in table:
        val.append(e["chapitres"])
    return val 

def get_lessons(chapter: str) -> list:
    """Renvoie une liste composée de couples (path,nom_leçon)"""
    f = open("csv_data/chapitres.csv", "r", encoding= "utf-8")
    table = list(csv.DictReader(f,delimiter=";")) #Preciser que le delimiter est ; et non ,
    val = []
    for e in table:
        if e["chapitres"] == chapter:
            val =e["lst_lecons"]
    return eval(val) 

def get_enonce_exercice(chapter: str, lesson: str, nom: str) -> list:
    """Renvoie une liste composée de couples (path,nom_leçon)"""
    f = open("csv_data/exercices.csv", "r", encoding= "utf-8")
    table = list(csv.DictReader(f)) 
    val = ""
    for e in table:
        if e["chapitre"] == chapter and e["lecon"] == lesson and e["nom_exo"] == nom:
            val = e["enonce"]
    return val 

def get_hint(chapter: str, lesson: str, name_exo: str) -> list:
    """Renvoie la liste des indices pour l'exercice donné"""
    f = open("csv_data/indices.csv", "r", encoding= "utf-8")
    r = list(csv.DictReader(f))
    lst = []
    for exo in r:
        if exo["chapitre"] == chapter and exo["lecon"] == lesson and exo["exercice"] == name_exo:
            lst.append(exo["text"])
    f.close()
    return lst

def get_correction(chapter: str, lesson: str, name_exercice: str) -> str:
    """Renvoie le path de la correction de l'exercice donné"""
    f = open("csv_data/exercices.csv", "r", encoding= "utf-8")
    r = list(csv.DictReader(f))
    for exo in r:
        if exo["chapitre"] == chapter and exo["lecon"] == lesson and exo["nom_exo"] == name_exercice:
            return exo["correction"]
    f.close()

def get_name_lessons(chapter: str) -> list:
    """Renvoie la liste des noms de leçons du chapitre"""
    lst = get_lessons(chapter)
    res = []
    for chap in range(len(lst)):
        res.append(lst[chap][1])
    return res

def get_name_exercices(chapter: str, lesson: str) -> list:
    """Permet de récupérer la liste de tous les exercices d'un chapter et d'une leçon données"""
    f = open("csv_data/exercices.csv", "r", encoding= "utf-8")
    table = list(csv.DictReader(f)) #Preciser que le delimiter est ; et non ,
    val = []
    for e in table:
        if e["chapitre"] == chapter and e["lecon"] == lesson:
            val.append(e["nom_exo"])
    return val 

def add_chapter(chapter: str) -> bool:
    """Ajoute le chapter dans le csv et renvoie true si l'opération a eu lieu, False sinon"""
    if not chapter in get_all_chapters():
        f = open("csv_data/chapitres.csv", "a", encoding= "utf-8")
        table = csv.DictWriter(f, ["chapitres", "lst_lecons"], delimiter=";")
        table.writerow({"chapitres":chapter, "lst_lecons":[]})
        f.close()
        return True #L'action a été faite
    return False

def delete_user(user: str) -> bool:
    """Supprime l'utilisateur dont le pseudo est donné en argument. Renvoie True si tout c'est bien passé, False sinon"""
    with open('csv_data/csvfile.csv', 'r', encoding= "utf-8") as fr:
        # reading line by line
        lines = fr.readlines()
        line_to_delete = _find_line(user, "pseudo", 'csv_data/csvfile.csv')
        acc = 0
        # opening in writing mode
        with open('csv_data/csvfile.csv', 'w', encoding= "utf-8") as fw:
            for line in lines:
                if acc != line_to_delete:
                    fw.write(line)
                acc += 1

        if line_to_delete == 1:
            return False
        return True
    
def _find_line(value: str, key: str, file: str ,delimiter: str= ",") -> int or None:
    """Renvoie la ligne correspondant à la valeur de l'élément 'value' de clé 'key' dans le fichier 'file' ayant pour séparation 'delimiter'"""
    with open(file, 'r', encoding= "utf-8") as f:
        test = list(csv.DictReader(f,delimiter= delimiter))
        line_to_delete = 0
        for e in test:
            line_to_delete += 1
            if e[key] == value:
                f.close()
                return line_to_delete
        f.close()

def add_lesson(chapter: str ,path_lecon: str ,nom_lecon: str) -> bool:
    """Ajoute la leçon dans le csv et renvoie True si l'opération a eu lieu, False sinon\n
    ATTENTION: Doit suivre la syntaxe suivante : "'path'" et " 'nom'" (l'espace est important)"""
    if chapter in get_all_chapters():
        with open("csv_data/chapitres.csv",'r', encoding= "utf-8") as fr:
            lines = fr.readlines()
            line_to_modifiy = _find_line(chapter,"chapitres","csv_data/chapitres.csv",";") 
            line_to_update = _add_lesson_bis(chapter,path_lecon,nom_lecon)
            acc = 0
            a_marché = False
            with open("csv_data/chapitres.csv", 'w', encoding= "utf-8") as fw:
                for line in lines:
                    if acc != line_to_modifiy:
                        fw.write(line)
                    else:
                        if line_to_update is None:
                            fw.write(line) 
                        elif line_to_update is not None:
                            fw.write(line_to_update+"\n")
                            a_marché = True
                    acc += 1
            if line_to_modifiy == 0 or not a_marché:
                return False
            return True
    return False

def _add_lesson_bis(chapter: str ,path: str ,nom_lecon: str) -> None or str :
    """Renvoie la ligne changée ou None si le changement n'a pas pu avoir lieu"""
    with open("csv_data/chapitres.csv", 'r', encoding= "utf-8") as f:
        test = list(csv.DictReader(f, delimiter=";"))
        for e in test:
            if e["chapitres"] == chapter and not nom_lecon in e["lst_lecons"]:
                lecon_lst = str(e["lst_lecons"])
                res = _change_txt(lecon_lst, "(" + path + "," + nom_lecon + ")")
                return str(chapter) + ";" + res

def _change_txt(base_txt: str, what_to_add: str) -> str:
    "renvoie une nouvelle chaine de caractères à partir de celles envoyées"
    res = ""
    for ch in base_txt:
        if ch == "]":
            if base_txt == "[]":
                ch = what_to_add + "]"
            else:
                ch = ", " + what_to_add + "]"
        res += ch
    return res

def add_exercice(chapter:str ,lesson: str, nom: str, enonce: str, correction: str)-> bool:
    """Ajoute l'exercice dans le csv suivant les paramètres donnés. Renvoie True si l'action a eu lieu, false sinon."""
    if chapter in get_all_chapters() and lesson in get_name_lessons(chapter) and not nom in get_name_exercices(chapter,lesson):
        with open("csv_data/exercices.csv","a", encoding= "utf-8") as f:
            w = csv.DictWriter(f, ["chapitre", "lecon", "nom_exo", "enonce", "correction"])
            w.writerow({"chapitre": chapter, "lecon": lesson, "nom_exo": nom, "enonce": enonce, "correction": correction})
            return True      
    return False
    
def delete_exo(chapter: str, lesson: str = None, nom: str = None)-> bool:
    """Supprime l'exercice avec les infos données en argument. Renvoie True si tout c'est bien passé, False sinon"""
    if nom in get_name_exercices(chapter,lesson):
        with open('csv_data/exercices.csv', 'r', encoding= "utf-8") as fr:
            # reading line by line
            lines = fr.readlines()
            lines_to_delete = _find_line_exo(chapter, lesson, nom)
            acc = 0
            file_to_delete = get_correction(chapter,lesson,nom)
            # opening in writing mode
            with open('csv_data/exercices.csv', 'w', encoding= "utf-8") as fw:
                for line in lines:
                    if lines_to_delete is None or acc not in lines_to_delete:
                        fw.write(line)
                    acc += 1
            if lines_to_delete is None:
                return False
            else:
                delete_hint(chapter,lesson,nom)
                delete_file(file_to_delete)
                return True
    return False

def _find_line_exo(chapter: str, lesson: str, nom: str)-> int or None:
    with open("csv_data/exercices.csv", 'r', encoding= "utf-8") as f:
        test = list(csv.DictReader(f))
        line_to_delete = 0
        res = []
        for e in test:
            line_to_delete += 1
            if e["chapitre"] == chapter and lesson is None and nom is None:
                res.append(line_to_delete)
            elif e["chapitre"] == chapter and lesson == e["lecon"] and nom is None:
                res.append(line_to_delete)
            elif e["chapitre"] == chapter and e["lecon"] == lesson and e["nom_exo"] == nom:
                res.append(line_to_delete)
        f.close()
        return res
       
def delete_chapter(chapter: str) -> bool: 
    """Supprime le chapter donné en argument (et donc les leçons et exos qu'il y'avait). Renvoie True si tout c'est bien passé, False sinon"""
    with open('csv_data/chapitres.csv', 'r', encoding= "utf-8") as fr:
        # reading line by line
        lines = fr.readlines()
        line_to_delete = _find_line(chapter, "chapitres", 'csv_data/chapitres.csv',";")
        acc = 0
        # opening in writing mode
        with open('csv_data/chapitres.csv', 'w', encoding= "utf-8") as fw:
            for line in lines:
                if acc != line_to_delete:
                    fw.write(line)
                acc += 1
        if line_to_delete is None:
            return False
        else:
            delete_exo(chapter)
            return True

def delete_lesson(chapter: str,lesson_name: str) -> bool:
    """Supprime la lecon du chapter dans le csv et renvoie True si tout a marché False sinon """
    if lesson_name in get_name_lessons(chapter):
        lst = get_lessons(chapter)
        res = []
        for chap in lst:
            if chap[1] != lesson_name:
                res.append(chap)
            else:
                delete_file(chap[0])
        if res == lst:
            return False
        else:
            delete_exo(chapter, lesson_name)
            return _modif_line(str(res), str(lst), "lst_lecons", "csv_data/chapitres.csv", ";")
    return False

def _modif_line(new_val: str, previous_val: str, key: str, file: str, delimiter: str = ",") -> bool:
    """Permet de remplacer la valeur 'previous_val' par 'new_val' de clé 'key' dans le fichier 'file' ayant pour séparateur 'delimiter'
    Renvoie True si tout c'est bien passé, False sinon
    """
    with open(file,'r', encoding= "utf-8") as fr:
        lines = fr.readlines()
        line_to_modifiy = _find_line(previous_val,key,file,delimiter) 
        acc = 0
        with open(file, 'w', encoding= "utf-8") as fw:
            for line in lines:
                if acc != line_to_modifiy:
                    fw.write(line)
                else:
                    string = line.replace(previous_val,new_val)
                    fw.writelines(string)
                acc += 1
        if line_to_modifiy is None:
            return False
        return True
    
def get_path_lesson(chapter: str, lesson: str) -> str or None:
    """Renvoie le path de la leçon donnée en arguments, None sinon"""
    lst = get_lessons(chapter)
    for l in lst:
        if l[1] == lesson:
            return str(l[0])
        
def add_hint(text: str, chapter: str, lesson: str, exercice: str)-> bool:
    """Ajoute un indice en fonction des paramtètres donnés. renvoie True si tout c'est bien passé, False sinon"""
    if not text in get_hint(chapter,lesson,exercice):
        f = open("csv_data/indices.csv", "a", encoding= "utf-8")
        w = csv.DictWriter(f, ["chapitre","lecon","exercice","text"])
        w.writerow({"chapitre": chapter, "lecon": lesson, "exercice": exercice, "text": text})
        f.close()
        return True
    return False

def delete_hint(chapter: str, lesson: str = None, exercice: str = None, txt = "") -> bool:
    """Supprime l'indice avec les infos données en argument. Renvoie True si tout c'est bien passé, False sinon"""
    with open('csv_data/indices.csv', 'r', encoding= "utf-8") as fr:
        # reading line by line
        lines = fr.readlines()
        lines_to_delete = _find_line_hint(chapter, lesson,exercice)
        acc = 0
        # opening in writing mode
        with open('csv_data/indices.csv', 'w', encoding= "utf-8") as fw:
            for line in lines:
                if lines_to_delete is None or acc not in lines_to_delete:
                    fw.write(line)
                acc += 1
        if lines_to_delete is None:
            return False
        return True   

def _find_line_hint(chapter: str, lesson: str, exercice: str, txt) -> int:
    """Renvoie la ligne correspondant à la valeur de l'indice"""
    with open("csv_data/indices.csv", 'r', encoding= "utf-8") as f:
        test = list(csv.DictReader(f))
        line_to_delete = 0
        res = []
        for e in test:
            line_to_delete += 1
            if e["chapitre"] == chapter and lesson is None and exercice is None and txt is None:
                res.append(line_to_delete)
            elif e["chapitre"] == chapter and e["lecon"] == lesson and exercice is None and txt is None:
                res.append(line_to_delete)
            elif e["chapitre"] == chapter and e["lecon"] == lesson and e["exercice"] == exercice and txt is None:
                res.append(line_to_delete)
            elif e["chapitre"] == chapter and e["lecon"] == lesson and e["exercice"] == exercice and txt == e["text"]:
                res.append(line_to_delete)
        f.close()
        return res

def get_user():
    """Renvoie la liste de tous les utilisateurs"""
    f = open("csv_data/csvfile.csv", "r", encoding= "utf-8")
    table = list(csv.DictReader(f,delimiter=",")) #Preciser que le delimiter est ; et non ,
    val = []
    for e in table:
        val.append(e["pseudo"])
    return val 

def modif_mdp_admin(new_mdp):
    delete_user("Admin")
    add_user("Admin", new_mdp,True)
