import platform
import os
from tkinter.filedialog import askopenfilename
import shutil
import subprocess

def open_pdf() -> None:
    """Ouvre la fenetre pour choisir un fichier PDF et l'ouvre dans le lecteur par defaut de l'OS
    """
    file_path = askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])
    if "macOS" in platform.platform():
        subprocess.run(["open", file_path])

    elif "Windows" in platform.platform():
        subprocess.run(["cmd", "/c", "start", "", file_path], shell=True)

    elif "Linux" in platform.platform():
        subprocess.run(["xdg-open", file_path])

def open_given_pdf(file_path: str)-> None:
    """Ouvre un fichier PDF donné dans le lecteur par defaut de l'OS
    """
    if "macOS" in platform.platform():
        subprocess.run(["open", file_path])

    elif "Windows" in platform.platform():
        subprocess.run(["cmd", "/c", "start", "", file_path], shell=True)

    elif "Linux" in platform.platform():
        subprocess.run(["xdg-open", file_path])

def recup_path() -> str:
    """Renvoie le path du fichier séléctionné"""
    file_path = askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])
    return file_path

def copy_file(file_path):
    # Obtenir le chemin absolu du répertoire parent du fichier actuel
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    # Créer un dossier "Copies" dans le répertoire parent s'il n'existe pas déjà
    target_folder = os.path.join(parent_dir, "PDF")
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Obtenir le nom de fichier à partir du chemin absolu
    filename = os.path.basename(file_path)
    
    # Construire le chemin de destination du fichier copié
    destination = os.path.join(target_folder, filename)
    
    # Vérifier si le fichier existe déjà dans le dossier cible
    if os.path.exists(destination):
        print("Le fichier est déjà copié.")
        return os.path.relpath(destination, os.getcwd())
    
    # Copier le fichier dans le dossier cible
    shutil.copyfile(file_path, destination)
    
    # Obtenir le chemin relatif du fichier copié par rapport au répertoire actuel
    relative_path = os.path.relpath(destination, os.getcwd())
    
    return relative_path



def delete_file(file_path: str) -> str:
    """Supprime le fichier correspondant"""
    try:
        os.remove(file_path)
    except OSError as e:
        pass


"""import git

# Cloner un dépôt
repo_url = 'git@github.com:ThomasL-01/Logiciel_NSI.git'
local_dir = '/Users/Mistigris/Documents/clone'

git.Repo.clone_from(repo_url, local_dir)"""
