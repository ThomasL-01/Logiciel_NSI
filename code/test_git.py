from git import Repo, GitCommandError
import os
from datetime import datetime

def get_current_date():
    current_date = datetime.now().date()
    return current_date

# Utilisation de la fonction get_current_date pour obtenir la date actuelle
date = get_current_date()

def get_files_in_directory() -> list:
    """Renvoie la liste de tous les fichiers dans PDF"""
    current_directory = os.getcwd()
    directory = os.path.join(current_directory, "PDF")

    files = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            rel_path = os.path.relpath(file_path, current_directory)
            files.append(rel_path)
    return files

def obtenir_dossier_parent():
    dossier_courant = os.path.abspath(os.getcwd())
    dossier_parent = os.path.dirname(dossier_courant)
    return dossier_parent

def git_add_commit_push(repo_path = obtenir_dossier_parent()):
    repo = Repo(repo_path)
    
    # Vérifier si le dépôt est à jour
    if repo.is_dirty() or repo.untracked_files:
        # Ajouter tous les fichiers modifiés ou non suivis
        repo.git.add(all=True)
        
        # Créer un nouvel objet commit
        repo.index.commit("Mise à jour du dépôt")
        
        # Pousser les modifications vers le dépôt distant (origin)
        repo.remotes.origin.push()
        
        print("Le dépôt a été mis à jour avec succès.")
    else:
        print("Le dépôt est déjà à jour.")

def git_update(repo_path: str = os.getcwd(), branch: str = 'master') -> None:
    """Pour l'utilisateur: Permet de mettre à jour sa version du logiciel avec tous les cours etc que l'admin a pu ajouter"""
    repo = Repo(os.path.dirname(repo_path))
    origin = repo.remotes.origin

    if repo.is_dirty():
        # Réinitialiser le répertoire au commit de la branche distante
        origin.fetch()
        repo.head.reset(commit=f'origin/{branch}', working_tree=True)
        # Effectuer le pull pour récupérer les dernières modifications
        origin.pull()
    
    # Revenir au répertoire de départ
    os.chdir(repo_path)