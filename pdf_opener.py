import platform
import os
from tkinter import filedialog
import shutil
import subprocess

def open_pdf() -> None:
    """Ouvre la fenetre pour choisir un fichier PDF et l'ouvre dans le lecteur par defaut de l'OS
    """
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])
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
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])
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
