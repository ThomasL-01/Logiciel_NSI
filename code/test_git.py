from git import Repo
import os
from datetime import datetime

def get_current_date():
    current_date = datetime.now().date()
    return current_date

# Utilisation de la fonction get_current_date pour obtenir la date actuelle
date = get_current_date()
print(date)


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

def git_add_commit_push(directory_names: list, commit_message: list, branch: str ='master',repo_path: str =os.getcwd()) -> None:
    """Pour l'admin
    Permet de mettre à jour le dépot git avec tout les PDF et autres cours/exercices ajoutés ou supprimés par l'admin"""
    repo = Repo(repo_path)
    repo.git.checkout(branch)

    for directory_name in directory_names:
        directory_path = os.path.join(repo_path, directory_name)
        if directory_name == "PDF":

            # Comparer les fichiers dans le répertoire spécifié avec ceux du dépôt
            diff = repo.index.diff(None, paths=[directory_name])

            # Ajouter les fichiers manquants dans l'index
            for root, _, files in os.walk(directory_path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    relative_path = os.path.relpath(file_path, repo_path)
                    if relative_path not in [diff_file.a_path for diff_file in diff]:
                        repo.git.add(relative_path)

            # Supprimer les fichiers manquants de l'index
            for diff_file in diff:
                if diff_file.a_path.startswith(directory_name):
                    file_path = os.path.join(repo_path, diff_file.a_path)
                    if not os.path.exists(file_path):
                        repo.git.rm(diff_file.a_path)
        if directory_name == "csv_data":
            repo.git.add(directory_path, update=True)

    # Effectuer le commit et le push
    repo.index.commit(commit_message)
    repo.git.push('origin', branch)

def git_update(repo_path: str = os.getcwd(), branch: str ='master') -> None:
    """Pour l'utilisateur. Permet de mettre à jour sa version du logiciel avec tous les cours etc que l'admin a pu ajouter"""
    repo = Repo(repo_path)
    
    # Réinitialiser le dépôt au commit de la branche distante
    origin = repo.remotes.origin
    origin.fetch()
    repo.head.reset(commit=f'origin/{branch}', working_tree=True)
    
    # Effectuer le pull pour récupérer les dernières modifications
    origin.pull()

