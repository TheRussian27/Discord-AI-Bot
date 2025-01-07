import requests
import json
from datetime import datetime
import os

class ollama():
    def __init__(self):
        self.__reset_url()
        self.chat_history = []

    def __attachurl(self,url):
        self.__reset_url()
        self.url = self.url + url

    def __reset_url(self):
        self.url = "http://192.168.178.61:11434/"
    
    def ask(self, q):
        self.__attachurl(f"v1/chat/completions")
        
        # Neue Nachricht des Benutzers speichern
        self.chat_history.append({"role": "user", "content": q})
        
        json_body = {
            "messages": self.chat_history,
            "model": "llama3.2",
            "stream": False
            }

        
        # Sende die Anfrage
        response = requests.post(url=self.url, json=json_body)

        data = response.json()
        choices = data.get("choices")
        message = choices[0]["message"]["content"]
        self.chat_history.append({"role":"assistant", "content": message})        
        return message
