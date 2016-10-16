#!/usr/bin/python3

import os

import telebot

"""Autenticação do bot"""
try:
    token = open('token.txt')
    hash = token.readline()
    bot = telebot.TeleBot(hash)
    token.close()
except IOError:
    print("Não foi possível ler o arquivo token.txt")
    exit()

idGrupo = 265159574 # O id do grupo deve vir aqui.

def autenticar_grupo(idChat):
    global idGrupo
    return idGrupo == idChat


def exec_bash():
    saidaComando = os.popen("netstat -n | egrep '443' | wc -l").read()
    return saidaComando

@bot.message_handler(commands=['EHIConectados', 'ehiconectados', 'Ehiconectados'])
def executar_comando(message):
    if autenticar_grupo(message.chat.id):
        bot.send_message(message.chat.id, "Números de usuário conectados: "+exec_bash())
    else:
        bot.send_message(message.chat.id, "Você não tem permissão para acessar este bot.")


@bot.message_handler(commands=['idgrupo'])
def idgrupo(message):
    bot.send_message(message.chat.id, 'O id desse grupo é: {}.'.format(message.chat.id))


@bot.message_handler(commands=['help', 'ajuda'])
def ajuda(message):
    bot.send_message(message.chat.id, "Comandos /ajuda, /idgrupo, /EHIConectados")

print("Bot executando...")
bot.polling()
