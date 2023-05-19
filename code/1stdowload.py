import platform
import subprocess

system = platform.system()  # Système d'exploitation

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

# Continuer avec le reste du processus de téléchargement et d'installation de votre logiciel
