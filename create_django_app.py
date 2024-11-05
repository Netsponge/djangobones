import os
import sys
import subprocess

# Définir le nom du projet Django et de l'application
yourproject = "my_django_project"  # Remplacez par le nom souhaité pour votre projet
app_name = "myapp"  # Nom de l'application Django
python_executable = sys.executable

# Chemin du dossier de l'environnement virtuel
venv_path = ".venv"

# Créer un environnement virtuel pour Python
subprocess.run([python_executable, "-m", "venv", venv_path])

# Chemin vers le pip de l'environnement virtuel
pip_path = os.path.join(venv_path, "Scripts", "pip") if os.name == 'nt' else os.path.join(venv_path, "bin", "pip")
django_admin_path = os.path.join(venv_path, "Scripts", "django-admin") if os.name == 'nt' else os.path.join(venv_path, "bin", "django-admin")

# Installer Django et d'autres packages nécessaires
subprocess.run([pip_path, "install", "django", "djangorestframework", "django-environ"])

# Créer le projet Django
subprocess.run([django_admin_path, "startproject", yourproject])

