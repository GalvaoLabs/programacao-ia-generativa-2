from google import genai
from dotenv import load_dotenv
import pygame
from gtts import gTTS
import os

#Carrega as variáveis do arquivo .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Cria o client Gemini
client = genai.Client(api_key=API_KEY)

def speak(texto):
    tts = gTTS(text=texto, lang='pt-br')
    arquivo = "voz.mp3"
    try:
        os.remove(arquivo)
    except OSError:
        pass
    tts.save(arquivo)

    pygame.mixer.init()
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

    pygame.mixer.music.unload()

# CHATBOT Gemini

print("=" * 50)
print("🤖 CHATBOT GEMINI")
print("Digite 'sair' para encerrar.")
print("=" * 50)

historico = []

while True:

    pergunta = input('\nVocê: ')

    if pergunta.lower() == "sair":
        print("\n🤖 Até logo!")
        break

    # Armazena a mensagem do usuário
    historico.append(
        {
            "role": "user",
            "parts": [{"text" : pergunta}]
        }
    )

    # Envia todo o histórico
    resposta = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=historico
    )

    texto = resposta.text

    # Armazena a resposta da IA para manter o contexto
    historico.append(
        {
            "role": "model",
            "parts": [{"text": texto}]
        }
    )

    print(f'🤖: {texto}')

print(speak(texto))