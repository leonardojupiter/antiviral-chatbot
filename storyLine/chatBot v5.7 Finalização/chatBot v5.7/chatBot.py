import json
import sys
import os
import subprocess

class ChatBot():
        def __init__(self, nome):
                self.nome = nome
                try:
                        memoria = open(nome+'.json','r')
                except FileNotFoundError:
                        memoria = open(nome+'.json','w')
                        memoria.write('[["Alan Turing","Katie Bouman"],{"voltar": "Olá, meu nome é '+self.nome+', qual é o seu?","tchau": "Tchau!","ha quanto tempo": "Olá, meu nome é '+self.nome+', qual é o seu?","ola": "Olá, meu nome é '+self.nome+', qual é o seu?","oi": "Olá, meu nome é '+self.nome+', qual é o seu?","opa": "Olá, meu nome é '+self.nome+', qual é o seu?","fala ai": "Olá, meu nome é '+self.nome+', qual é o seu?","fala": "Olá, meu nome é '+self.nome+', qual é o seu?","saudacoes": "Olá, meu nome é '+self.nome+', qual é o seu?","oi tudo bem": "Olá, meu nome é '+self.nome+', qual é o seu?","e ae": "Olá, meu nome é '+self.nome+', qual é o seu?","e ai": "Olá, meu nome é '+self.nome+', qual é o seu?","eae": "Olá, meu nome é '+self.nome+', qual é o seu?","oi, tudo bem": "Olá, meu nome é '+self.nome+', qual é o seu?"}]')
                        memoria.close()
                        memoria = open(nome+'.json','r')
                self.conhecidos, self.frases = json.load(memoria)
                memoria.close()
                self.historico = [None,]

        def recoloca(self, frase):
                frase = frase.lower()
                frase = frase.replace ('á','a')
                frase = frase.replace ('ç','c')
                frase = frase.replace ('?','')
                frase = frase.replace ('!','')
                frase = frase.replace ('í','i')
                frase = frase.replace ('´','')
                frase = frase.replace ('`','')
                frase = frase.replace ('{','')
                frase = frase.replace ('[','')
                frase = frase.replace ('~','')
                frase = frase.replace ('ã','a')
                frase = frase.replace ('õ','o')
                frase = frase.replace ('}','')
                frase = frase.replace (']','')
                frase = frase.replace ('ª','')
                frase = frase.replace ('º','')
                frase = frase.replace (',','')
                frase = frase.replace ('<','')
                frase = frase.replace ('.','')
                frase = frase.replace ('>','')
                frase = frase.replace (';','')
                frase = frase.replace (':','')
                frase = frase.replace ('°','')
                frase = frase.replace ('|','')
                frase = frase.replace ('"','')
                frase = frase.replace ("'",'')
                frase = frase.replace ('@','')
                frase = frase.replace ('#','')
                frase = frase.replace ('$','')
                frase = frase.replace ('%','')
                frase = frase.replace ('¨','')
                frase = frase.replace ('&','')
                frase = frase.replace ('*','')
                frase = frase.replace ('(','')
                frase = frase.replace (')','')
                frase = frase.replace ('-','')
                frase = frase.replace ('_','')
                frase = frase.replace ('+','')
                frase = frase.replace ('=','')
                return frase
                
        def escuta(self, frase=None):
                if frase == None:
                        frase = input('>: ')
                frase = str(frase)
                frase = self.recoloca(frase)
                return frase
        
        def pensa(self, frase):
                try:
                        ultFrase = self.historico[-1]
                        if frase == '/start':
                                return 'Conectando com Auzio... Conectado, diga "Oi"! Você pode digitar "Aprende", para ensinar algo ao(a) Auzio!'
                        if frase in self.frases:
                                return self.frases[frase]
                        if frase == 'aprende' or frase =='aprenda':
                                return 'Digite a frase: '
                        if ultFrase == 'Olá, meu nome é '+self.nome+', qual é o seu?':
                                nome = self.pegaNome(frase)
                                frase = self.reconheceNome(nome)
                                return frase
                        if ultFrase == 'Digite a frase: ':
                                self.chave = frase
                                return 'Digite a resposta: '
                        if ultFrase == 'Digite a resposta: ':
                                resp = frase
                                self.frases[self.chave] = resp
                                self.gravaMemoria()
                                return 'Aprendi!'
                        try:
                                resp = str(eval(frase))
                                return resp
                        except:
                                pass
                        return 'Não entendi'
                except:
                        return 'Não entendi'

        def pegaNome(self, nome):
                if 'porque' in nome or 'por que' in nome or 'porquê' in nome or 'por quê' in nome or 'pq' in nome or 'não' in nome or 'nao' in nome:
                        nome = 'Usuário'
                if 'meu nome é ' in nome or 'meu nome e ' in nome:
                        nome = nome [11:]
                if 'é ' in nome or 'e ' in nome:
                        nome = nome [2:]
                nome = nome.title()
                return nome

        def reconheceNome(self, nome):
                if nome in self.conhecidos:
                        frase = 'Oi '
                else:
                        frase = 'Muito prazer '
                        self.conhecidos.append(nome)
                        self.gravaMemoria()
                        return frase+nome+', me pergunta alguma coisa!'
                        
                return frase+nome+', me ensina alguma coisa!'

        def fala(self, frase):
                print(frase)
                self.historico.append(frase)

        def gravaMemoria(self):
                memoria = open(self.nome+'.json','w')
                json.dump([self.conhecidos,self.frases],memoria)
                memoria.close()
                
