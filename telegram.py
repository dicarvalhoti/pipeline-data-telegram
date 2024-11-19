# Verificando se o Telegram está disponível via API

from getpass import getpass
import json
import requests

token = getpass()

base_url = f'https://api.telegram.org/bot{token}'

response = requests.get(url=f'{base_url}/getMe')
print(f'{base_url}/getMe')

print(json.dumps(json.loads(response.text), indent=2))



# Recuperando os dados Usando a Api do Telegram
data = json.loads(response.text)

for update in data["result"]:
    message = update.get("message", {})
    chat_info = message.get("chat", {})
    info_from = message.get("from",{})
    chat_user = info_from.get("first_name", "Usuário Desconhecido")

    print(f"Chat User: {chat_user}, Chat ID: {chat_info.get('id')}, Chat Tipo: {chat_info.get('type')}")

    media_types = ["text", "photo", "voice", "video"]

    for media_type in media_types:
        if media_type in message:
            if media_type == "text":
                print(f"Mensagem de texto: {message['text']}")
            else:
                file_id = message[media_type][-1]["file_id"] if media_type == "photo" else message[media_type]["file_id"]
                print(f"{media_type.capitalize()} recebido - File ID: {file_id}")
                if "caption" in message:
                    print(f"Legenda do {media_type}: {message['caption']}")


# Setando o Telegram para executar o WebHook e enviar 

aws_api_gateway_url = getpass()

base_url = f'https://api.telegram.org/bot{token}'

response = requests.get(url=f'{base_url}/setWebhook?url={aws_api_gateway_url}')

print(json.dumps(json.loads(response.text), indent=2))