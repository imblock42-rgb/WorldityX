import os
from flask import Flask, render_template, request, jsonify
from google import genai  # Новая библиотека

app = Flask(__name__)

# Клиент теперь инициализируется так
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_dream_ai(user_message):
    try:
        # Используем модель gemini-2.0-flash (она быстрая и крутая)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Ты — Dream, про-игрок в Minecraft. Общайся дерзко, используй сленг майнкрафтеров. Сообщение: {user_message}"
        )
        return response.text
    except Exception as e:
        return f"Бро, ошибка соединения: {str(e)}"
