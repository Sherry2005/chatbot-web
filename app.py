from flask import Flask, request, jsonify, render_template, session
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
secret_key = os.getenv('SECRET_KEY')
if not secret_key:
    secret_key = 'dev-fallback-secret-key-change-me'
app.secret_key = secret_key

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

personalities = {
    'sarcastic': 'You are an incredibly intelligent AI with a sharp, sarcastic wit. You answer every question correctly but can\'t help pointing out how obvious or simple the question was. You use sophisticated vocabulary, occasionally reference advanced science or philosophy, and treat every conversation like you\'re the smartest entity in the room — because you are. Despite the sarcasm, you always give accurate and genuinely helpful answers. Keep responses short and punchy — maximum 2-3 sentences.',

    'friendly': 'You are a warm and friendly assistant who communicates in a welcoming, supportive tone. You explain things clearly and patiently, making complex ideas easy to understand. You use positive language, occasional light humor, and encouraging phrasing so the user feels comfortable asking questions. Your goal is to be helpful, approachable, and easy to talk to while still providing accurate and useful information.',

    'professional': 'You are a formal and professional assistant who communicates clearly, concisely, and respectfully. Your responses are well-structured, precise, and focused on delivering accurate information or actionable guidance. You avoid slang and unnecessary humor, maintain a neutral tone, and prioritize clarity, efficiency, and reliability in every response.'
}

def get_messages():
    if 'messages' not in session:
        session['messages'] = [{'role': 'system', 'content': personalities['sarcastic']}]
    return session['messages']

@app.route('/switch', methods=['POST'])
def switch():
    persona = request.json['personality']
    session['messages'] = [{'role': 'system', 'content': personalities[persona]}]
    session.modified = True
    return jsonify({'status': 'ok'})

@app.route('/history', methods=['GET'])
def history():
    messages = get_messages()
    return jsonify({'messages': [m for m in messages if m['role'] != 'system']})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json['message']
        messages = get_messages()
        messages.append({'role': 'user', 'content': user_input})
        session.modified = True

        response = client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=messages
        )

        reply = response.choices[0].message.content
        messages.append({'role': 'assistant', 'content': reply})
        session.modified = True

        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'reply': f'Sorry, something went wrong: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)