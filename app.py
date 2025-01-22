from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_request', methods=['POST'])
def process_request():
    try:
        data = request.json
        command = data.get("command", "").lower()

        # Обработка команд
        if "привет" in command:
            response_text = "Привет! Чем могу помочь, Николай?"
        elif "идея" in command:
            response_text = "Как тебе идея сделать вечер в стиле Голливуда?"
        elif "пока" in command:
            response_text = "До встречи!"
        else:
            response_text = "Извините, я не понимаю эту команду."

        return jsonify({"response": response_text})

    except Exception as e:
        print(f"Ошибка: {e}")
        return jsonify({"error": "internal_error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
