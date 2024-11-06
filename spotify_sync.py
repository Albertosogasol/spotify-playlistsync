# Archivo principal

import json
import subprocess
import sys
import os


def chk_spotipy():
    try:
        import spotipy
    except ImportError:
        print("Dependencia faltante. Ejecutando setup.py para instalar dependencias...")
        # Ejecuta setup.py desde la carpeta Dependencies
        subprocess.check_call([sys.executable, os.path.join("Dependencies", "setup.py")])
        # Intenta importar spotipy nuevamente después de la instalación
        import spotipy

def get_credentials():
    with open ("conf.json") as f:
        config = json.load(f)
        return config

# Configura la autenticación con los datos de tu aplicación
def set_auth(CLIENT_ID,CLIENT_SECRET):
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://localhost:8888/callback",
    scope = "playlist-modify-private playlist-modify-public"
    ))

    return sp


# Buscar la playlist por nombre
def search_playlist(sp, playlist_name, track_uri):
    # Buscar todas las playlist del usuario
    playlists = sp.current_user_playlists()

    # Buscar la playlist por nombre
    playlist_id = None
    for playlist in playlists['items']:
        if playlist['name'].lower() == playlist_name.lower():
            playlist_id = playlist['id']
            break

    if playlist_id is None:
        print(f"No se encontró la playlist '{playlist_name}'.")
        return
    
    # Añadir la canción a la playlist 
    sp.playlist_add_items(playlist_id, [track_uri])
    print(f"Canción añadida a la playlist '{playlist_name}'.")

def main():
    chk_spotipy()
    config = get_credentials()
    CLIENT_ID = config["CLIENT_ID"]
    CLIENT_SECRET = config["CLIENT_SECRET"]

    sp = set_auth(CLIENT_ID,CLIENT_SECRET)
    user_profile = sp.current_user()
    print(user_profile)

    track_uri = "spotify:track:5wwYFxRblHS6eb93JARo1f" # TRACK DE PRUEBA

    # Añadir una canción a la playlist llamada "Test Playlist"
    search_playlist(sp, "Test Playlist", track_uri)


if __name__ == '__main__':
    main()