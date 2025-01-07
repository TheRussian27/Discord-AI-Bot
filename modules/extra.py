import os
from pathlib import Path as p

class extra():
    def readToken(token_file):
        path = p(__file__).resolve().parent.parent
        token = os.path.join(path,token_file)
        try:
            with open(token, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"Fehler: Die Datei '{token}' wurde nicht gefunden.")
            print(token)
            exit(1)
        except Exception as e:
            print(f"Fehler beim Lesen der Datei '{token}': {e}")
            exit(1)