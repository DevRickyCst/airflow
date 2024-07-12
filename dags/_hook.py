from airflow.hooks.base import BaseHook
import requests
import json

bot_name = 'airflowrickybot'

class TelegramBotsHook(BaseHook):
    def __init__(self, http_conn_id = 'telegramBots'):
        super().__init__()
        self.http_conn_id = http_conn_id
        self.conn = self.get_connection(http_conn_id)
        self.url = f"https://ia6orftg8f.execute-api.eu-central-1.amazonaws.com/api/{bot_name}"


    def send_message(self, message, headers=None):
        payload = json.dumps({
        "texte": message,
        "chat_id": 426680033
        })
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.post(
            self.url + '/send_message', 
            headers=headers, 
            data=payload,
            
            )
        print(response.url)
        return response.json()