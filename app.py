from flask import Flask, jsonify
import os

app = Flask(__name__)

# Простое "хранилище" задач в памяти
tasks = [{"id": 1, "title": "Изучить Docker"}, {"id": 2, "title": "Настроить CI/CD"}, {"id": 3, "title": "Проверить авто-деплой"}]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
