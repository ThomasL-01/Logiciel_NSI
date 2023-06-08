import platform
import subprocess
from tkinter import *
import os
import sys
import shutil

system = platform.system()  # Système d'exploitation
th_to_install = "git"

def install_git()-> None:
    """installe git sur le PC"""
    global th_to_install, set_command
    if system == 'Windows':
        try:
            # Vérifier si Git est déjà installé
            subprocess.run('git --version', check=True, shell=True)
        except subprocess.CalledProcessError:
            # Télécharger et exécuter l'installateur Git pour Windows
            git_installer_url = 'https://github.com/git-for-windows/git/releases/latest/download/Git-2.41.0-64-bit.exe'
            subprocess.run(['powershell', 'Start-BitsTransfer', '-Source', git_installer_url, '-Destination', 'GitInstaller.exe'])
            subprocess.run(['cmd', '/c', 'start', 'GitInstaller.exe'])

    elif system == 'Darwin':  # macOS
        try:
            # Vérifier si Git est déjà installé
            subprocess.run('git --version', check=True, shell=True)
        except subprocess.CalledProcessError:
            # Installer Git en utilisant Homebrew
            subprocess.run(['brew', 'install', 'git'])

    elif system == 'Linux': #Fonctionne pour Debian et Ubuntu
        try:
            # Vérifier si Git est déjà installé
            subprocess.run('git --version', check=True, shell=True)
        except subprocess.CalledProcessError:
            # Installer Git en utilisant apt
            subprocess.run(['sudo', 'apt', 'install', '-y', 'git'])
    th_to_install = "GitPython"
    set_command()

def install_gitpython():
    """installe Gitpython dans python"""
    global th_to_install, set_command

    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'GitPython'])
        print("GitPython installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install GitPython.")

    th_to_install = "Logiciel"
    set_command()

def clone_repository(repo_url: str = "https://github.com/ThomasL-01/Logiciel_NSI.git", destination_path: str = os.path.expanduser('~/Documents/Logiciel')) -> None:
    global th_to_install
    from git import Repo
    # On supprime le dossier de destination s'il existe déjà
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)

    # On clone le répertoire dans le nouveau dossier
    try:
        print(destination_path)
        if system == "Windows":
            destination_path = os.path.expanduser('C:\\Users\\Programmes\\Logiciel_NSI')
        Repo.clone_from(repo_url, destination_path)
        print("Le dépôt a été cloné avec succès.")
    except Exception as e:
        print("Une erreur s'est produite lors du clonage du dépôt :", e)
        if os.path.exists(destination_path):
            th_to_install = "Failed"
    th_to_install = None
    set_command()

root = Tk()
root.title("Installation du Logiciel")
root.config(bg="black")
root.geometry("500x500")
root.maxsize(500,500)
root.minsize(500,500)

info_txt = Label(text="Pour installer le logiciel, nous allons devoir installer plusieurs chose.", bg="Black", fg="White", font=("Cascadia Code", 20), wraplength=500)
th_to_install_txt = Label(text=f"Nous devons installer {th_to_install}, cliquez pour installer.", bg="Black", fg="White", font=("Cascadia Code", 20), wraplength=500)

install_button = Button(text="Installer", command=None, font=("Cascadia Code", 17))

def set_command():
    th_to_install_txt.config(text=f"Nous devons installer {th_to_install}, cliquez pour installer.")
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
    elif th_to_install == "Failed":
        install_button.config(command=None, state=DISABLED, text="Erreur")
        th_to_install_txt.config(text="Il y a eu une erreur, veuillez recommencer. Si l'erreur persiste, veuillez contacter le staff.")
        info_txt.pack(pady= 20)
        th_to_install_txt.pack(pady=20)
        install_button.pack(pady=20)
    elif th_to_install == "Logiciel":
        if system == "Windows":
            th_to_install_txt.config(text=f"Nous devons installer le {th_to_install}, il sera installé  dans votre dossier Programmes sur votre PC (vous pourrez  toujours le changer de place après)")
        else:
            th_to_install_txt.config(text=f"Nous devons installer le {th_to_install}, il sera installé  dans votre dossier Documents (vous pourrez  toujours le changer de place après)")
        install_button.config(command=clone_repository)
        info_txt.pack(pady= 20)
        th_to_install_txt.pack(pady=20)
        install_button.pack(pady=20)
    else:
        info_txt.config(text="C'est terminé, nous avons installé tout ce dont nous avions besoin !  Vous pouvez fermer cette fenètre")
        info_txt.pack(ipady= 20 )
        if system == "Windows":
            th_to_install_txt.config(text="Vous pouvez démarrer le logiciel en lançant Main.py dans le dossier code de Logiciel_NSI de votre dossier Programmes sur votre PC")
        else:
            th_to_install_txt.config(text="Vous pouvez démarrer le logiciel en lançant Main.py dans le dossier code de Logiciel_NSI de votre dossier Documents")
        th_to_install_txt.pack(pady=20)
        install_button.config(text="C'est fini !", command=None, state=DISABLED)
        install_button.pack(pady=20)
set_command()

root.mainloop()