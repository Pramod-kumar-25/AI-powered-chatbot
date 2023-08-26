from flask import Flask, render_template, request, jsonify
from chatbot import get_chatbot_response, initialize_chat

app = Flask(__name__)
messages = initialize_chat()

@app.route('/')
def index():
    return render_template('index.html', initial_message=messages[0]['content'])

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    bot_response, global_messages = get_chatbot_response(messages, user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)