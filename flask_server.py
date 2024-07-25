from flask import Flask, request, jsonify
import chatbot
app=Flask(__name__)
@app.route('/',methods=['GET'])
def index():
    return "Hello World"

@app.route('/chat',methods=['POST'])
def chat():
    user_input=request.json.get('message')
    response=chatbot.it_service_chatbot()
    return jsonify({'response':response})

app.run(host="0.0.0.0",port=8080,debug=False)
