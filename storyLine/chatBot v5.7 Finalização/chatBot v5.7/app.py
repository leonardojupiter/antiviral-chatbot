from chatBot import ChatBot
from flask import Flask, render_template, request   #importação
                                                    #dos recursos do Flask

bot = ChatBot("Auzio")

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    frase = bot.escuta(request.args.get('msg'))
    resp = bot.pensa(frase)
    bot.fala(resp)
    return resp

if __name__ == "__main__":
    app.run()

#o Flask irá hospedar no localhost o index.html apontado
#na definição "home" (http://localhost:5000/)

#comando abaixo irá gerar um link e hospedar o seu localhost na web:
#ngrok http 5000
#lembre-se o link muda sempre que você fechar o ngrok
    
