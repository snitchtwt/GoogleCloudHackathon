from flask import Flask, render_template, request

app = Flask(__name__)

# conversation history
history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def chatbot_response():
    user_input = request.args.get('msg')
    # add user input to conversation history
    history.append({'user_input': user_input, 'bot_response': 'Bot response'})
    return 'Bot response'

@app.route('/history')
def conversation_history():
    return render_template('history.html', conversations=history)

if __name__ == '__main__':
    app.run(debug=True)
