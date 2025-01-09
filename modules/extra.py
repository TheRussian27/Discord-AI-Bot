import os
from pathlib import Path as p
import yt_dlp

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

    def y_link(self, link):
        dpath = str(p(__file__).parent.parent)
        dpath = os.path.join(dpath, "media/audio")
        os.makedirs(dpath, exist_ok=True)

        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(dpath, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            print("Download abgeschlossen!")
        except Exception as err:
            print(f"Fehler aufgetreten: {err}")

if __name__ == "__main__":
    e = extra()
    e.y_link("https://www.youtube.com/watch?v=n6B5gQXlB-0")