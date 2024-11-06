import subprocess
import sys

def install_package(package):
    """Instala el paquete especificado usando pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Lista de dependencias necesarias
dependencies = ["spotipy"]

for package in dependencies:
    install_package(package)
