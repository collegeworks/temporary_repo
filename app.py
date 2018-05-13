from flask import Flask, render_template, request
import sqlite3
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")

connection=sqlite3.connect('chatbot.sqlite')
cursor=connection.cursor()
create_table_request_list=['CREATE TABLE words(sentence Sentence)']
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chato(userText))

def chato(k):
    return "hii dristi,"+str(k)

if __name__ == "__main__":
    app.run()
