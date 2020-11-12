from chatBot import ChatBot #importação das definições (funções)
                            #do arquivo "chatBot.py"

bot = ChatBot("Auzio")  #o nome passado aqui como parâmetro criará um arquivo
                        #.json diferente, sendo cada .json um bot diferente com
                        #memórias diferentes

print ('Conectando com '+bot.nome+'...')
print ('Conectado, diga "Oi"!')
print ('Você pode digitar "Aprende", para ensinar algo ao(a) '+bot.nome+'!')
while True:
    frase = bot.escuta()    #variável "frase" recebe o que o usuário enviou
                            #ao bot, por isso, bot "escuta"
    resp = bot.pensa(frase) #"pensa" é uma definição onde acontece o processamento
                            #do bot, por isso "pensa", e a variável "resp" recebe ela
    bot.fala(resp) #definição "fala" exibe na tela o resultado do processamento
                            #da fase anterior, tanto no site quanto no Telegram
    if resp == 'tchau':
        break
    
