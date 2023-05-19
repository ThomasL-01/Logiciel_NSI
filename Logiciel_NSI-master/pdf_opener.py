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

def open_given_file(file_path: str)-> None:
    """Ouvre un fichier PDF ou python donné dans le lecteur par defaut de l'OS
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

def recup_path_py() ->str:
    file_path = askopenfilename(filetypes=[("Fichiers python", "*.py")])
    return file_path

def copy_file(file_path: str) -> str:
    """Copie le fichier donné dans le répertoire PDF"""
    cwd = os.getcwd()

    target_folder = os.path.join(cwd, 'PDF')

    # Copier le fichier dans le dossier cible
    if file_path and target_folder:
        filename = os.path.basename(file_path)
        destination = os.path.join(target_folder, filename)

        if os.path.exists(destination):
            return os.path.relpath(destination)
            
        else:
            shutil.copyfile(file_path, destination)
            return os.path.relpath(destination)

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
