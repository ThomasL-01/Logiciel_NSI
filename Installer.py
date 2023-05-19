import platform
import subprocess
from tkinter import *
import os
import sys

system = platform.system()  # Système d'exploitation
th_to_install = "git"

def install_git()-> None:
    global th_to_install, set_command
    if system == 'Windows':
        try:
            # Vérifier si Git est déjà installé
            subprocess.run('git --version', check=True, shell=True)
        except subprocess.CalledProcessError:
            # Télécharger et exécuter l'installateur Git pour Windows
            git_installer_url = 'https://github.com/git-for-windows/git/releases/latest/download/Git-2.33.0-64-bit.exe'
            subprocess.run(['powershell', 'Start-BitsTransfer', '-Source', git_installer_url, '-Destination', 'GitInstaller.exe'])
            subprocess.run(['cmd', '/c', 'start', 'GitInstaller.exe'])
            # Attendez que l'installation soit terminée

    elif system == 'Darwin':  # macOS
        try:
            # Vérifier si Git est déjà installé
            subprocess.run('git --version', check=True, shell=True)
        except subprocess.CalledProcessError:
            # Installer Git en utilisant Homebrew
            subprocess.run(['brew', 'install', 'git'])

    elif system == 'Linux':
        # Selon la distribution Linux, utilisez le gestionnaire de paquets approprié
        # par exemple, 'apt', 'yum', 'dnf', 'zypper', etc.

        # Exemple avec apt pour Debian et Ubuntu
        try:
            # Vérifier si Git est déjà installé
            subprocess.run('git --version', check=True, shell=True)
        except subprocess.CalledProcessError:
            # Installer Git en utilisant apt
            subprocess.run(['sudo', 'apt', 'install', '-y', 'git'])
    th_to_install = "GitPython"
    set_command()

def install_gitpython():
    """installe Gitpython"""
    global th_to_install, set_command

    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'GitPython'])
        print("GitPython installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install GitPython.")

    th_to_install = "Logiciel"
    set_command()

def clone_repository(repo_url: str = "https://github.com/ThomasL-01/Logiciel_NSI.git", destination_path: str = os.path.expanduser('~/Documents/Logiciel'))-> None:
    global th_to_install
    try:
        from git import Repo
        Repo.clone_from(repo_url, destination_path)
        print("Le dépôt a été cloné avec succès.")
    except Exception as e:
        print("Une erreur s'est produite lors du clonage du dépôt :", e)
    th_to_install = None
    set_command()

root = Tk()
root.title("Installation du Logiciel")
root.config(bg="black")
root.geometry("500x500")
root.maxsize(500,500)
root.minsize(500,500)

info_txt = Label(text="Pour installer le logiciel, \nnous allons devoir installer plusieurs chose.", bg="Black", fg="White", font=("Arial", 20))
th_to_install_txt = Label(text=f"Nous devons installer {th_to_install}", bg="Black", fg="White", font=("Arial", 20))

install_button = Button(text="Installer", command=None, font=("Arial", 17))

def start_logiciel():
    root.destroy()
    script_path = os.path.expanduser('~/Documents/Logiciel/code/Main.py')
    subprocess.run(['python3', script_path])

def set_command():
    th_to_install_txt.config(text=f"Nous devons installer {th_to_install}")
    if th_to_install == "git":
        install_button.config(command=install_git)
        info_txt.pack(pady= 20)
        th_to_install_txt.pack(pady=20)
        install_button.pack(pady=20)
    elif th_to_install == "GitPython":
        install_button.config(command=install_gitpython)
        info_txt.pack(pady= 20)
        th_to_install_txt.pack(pady=20)
        install_button.pack(pady=20)
    elif th_to_install == "Logiciel":
        th_to_install_txt.config(text=f"Nous devons installer {th_to_install}, il sera installé \n dans votre dossier Documents")
        install_button.config(command=clone_repository)
        info_txt.pack(pady= 20)
        th_to_install_txt.pack(pady=20)
        install_button.pack(pady=20)
    else:
        info_txt.config(text="C'est terminé, nous avons installé tout\n ce dont nous avions besoin ! \n Vous pouvez fermer cette fenètre")
        info_txt.pack(ipady= 20 )
        th_to_install_txt.config(text="Voulez vous lancer le logiciel maintenant ?")
        th_to_install_txt.pack(pady=20)
        install_button.config(text="Démarrer le Logiciel", command=start_logiciel)
        install_button.pack(pady=20)
set_command()

root.mainloop()