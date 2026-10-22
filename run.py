import socket
import subprocess
import sys
import threading
import time
import webbrowser
from pathlib import Path

RACINE = Path(__file__).resolve().parent
PORT = 8765
DELAI_MAX = 60


def port_ouvert(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex(("127.0.0.1", port)) == 0


def ouvrir_navigateur(processus, port):
    url = f"http://localhost:{port}/"
    debut = time.time()
    while time.time() - debut < DELAI_MAX:
        if processus.poll() is not None:
            return
        if port_ouvert(port):
            webbrowser.open(url)
            return
        time.sleep(0.3)
    print(f"Serveur non joignable sur {url} apres {DELAI_MAX} s.")


def main():
    if not (RACINE / "node_modules").exists():
        print("Installation des dependances (npm install)...")
        if subprocess.call("npm install", cwd=RACINE, shell=True) != 0:
            sys.exit(1)

    if port_ouvert(PORT):
        print(f"Le port {PORT} est deja utilise. Arretez le processus concerne puis relancez.")
        sys.exit(1)

    print(f"Serveur sur http://localhost:{PORT}/")
    processus = subprocess.Popen(f"npx eleventy --serve --port={PORT}", cwd=RACINE, shell=True)
    threading.Thread(target=ouvrir_navigateur, args=(processus, PORT), daemon=True).start()
    try:
        sys.exit(processus.wait())
    except KeyboardInterrupt:
        processus.terminate()
        processus.wait()


if __name__ == "__main__":
    main()
