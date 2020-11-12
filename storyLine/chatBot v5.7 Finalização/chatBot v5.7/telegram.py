import telepot #importação dos recursos do Telegram
from chatBot import ChatBot

telegram = telepot.Bot("")  #variável "telegram" recebe token
                            #de acesso para controle do bot
bot = ChatBot("Auzio")

def recebendoMsg(msg):
    frase = bot.escuta(frase = msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, resp)

telegram.message_loop(recebendoMsg)

while True:
    pass
