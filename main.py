import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Настройка API через переменную, которую ты добавишь в Railway
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_dream_ai(user_message):
    try:
        model = genai.GenerativeModel('gemini-pro')
        # Личность Дрима
        prompt = (
            "Ты — Dream, профессиональный игрок в Minecraft. "
            "Отвечай дерзко, используй сленг майнкрафтеров (MLG, спидран, manhunt), "
            "будь уверенным в себе. Общайся кратко."
        )
        response = model.generate_content(prompt + " Сообщение пользователя: " + user_message)
        return response.text
    except Exception as e:
        return "Бро, сервер лагает, перепрыгни в другой биом и попробуй снова!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    message = data.get('message', '')
    ai_response = ask_dream_ai(message)
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    # Railway динамически назначает порт
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
