import speech_recognition as sr
import os
import answers
import pygame
import webbrowser as browser
import sys
import requests
import json
import urllib
import importlib
from translate import Translator
from colors_on_terminal import colorir
from playsound import playsound
from gtts import gTTS
from datetime import datetime

contador = 0

def Menu(msg):
    '''
    Cria um menu personalizado com o texto centralizado
    '''
    print("="*60)
    print(msg.center(60))
    print("="*60)


def MessageFormatted(msg):
    '''
    Cria uma mensagem formatada, com o texto em azul. Utilizei para mostrar as mensagens da assistente
    '''
    print("="*60)
    colorir(msg, texto="Blue")
    print("="*60)


def Speak(audio, message, lang="pt-br"):
    '''
    Função para fazer a assistente falar.
    :param audio: Nome do áudio que será criado.
    :param message: Texto que a assistente irá falar.
    :param lang: (opcional)Idioma que a assistente irá falar.
    '''
    tts = gTTS(message, lang = lang)
    tts.save(audio)
    playsound(audio)
    os.remove(audio)	


def Recognize():
    '''
    Função para reconhecimento de voz.
    '''
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        if contador > 0:
            ShutDonwAssistent()
        Speak("ouvindo.mp3", "Estou ouvindo...")
        while True:
            colorir("Estou ouvindo...", texto="Blue")
            rec.adjust_for_ambient_noise(mic, duration=1)
            voice_data = rec.listen(mic)
            try:
                text = rec.recognize_google(voice_data, language="pt-BR")
                text = str(text).lower()
                colorir(f'Você disse: {text}', texto="Green")
                ExecuteComands(text)
                break
            except:
                pass
            

def RecognizeTranslater():
    '''
    Função para reconhecimento de voz, porém apenas para a função Translater().
    '''
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        Speak("ouvindo.mp3", "Estou ouvindo...")
        while True:
            colorir("Estou ouvindo...", texto="Blue")
            rec.adjust_for_ambient_noise(mic, duration=1)
            voice_data = rec.listen(mic)
            try:
                text = rec.recognize_google(voice_data, language="pt-BR")
                text = str(text).lower()
                colorir(f'Você disse: {text}', texto="Green")
                break
            except:
                pass
        return text


def Weather(city_name):
    '''
    Função que verifica o clima(temperatura e descrição) do lugar pedido.
    :param city_name: Nome da cidade que foi pedida para ser analisada. Ex: Rio de Janeiro, Curitiba, Roma...
    '''
    api_key = "<coloque sua chave API>"
    link = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=pt_br'
    weather = requests.get(link)
    dic = weather.json()
    temperature = dic['main']['temp'] - 273.15
    description = str(dic['weather'][0]['description']).title()
    return f"Em{str(city_name).title()} a temperatura está a {temperature:.2f}°C e {description}"


def Translater(txt):
    '''
    Função que traduz o que foi pedido.
    :param txt: Serve para saber qual será o idioma traduzido.
    '''
    if 'inglês' in txt:
        MessageFormatted('O que você gostaria de traduzir para o inglês?')
        Speak('traducao.mp3', 'O que você gostaria de traduzir para o inglês?')
        message = RecognizeTranslater()
        translation = Translator(to_lang='en', from_lang="pt-br").translate(message)
        MessageFormatted(f'A tradução de "{message}" em português para o inglês é: ')
        Speak('traducao.mp3', f'A tradução de {message} em português para o inglês é: ')
        MessageFormatted(f'>>>>> {translation}')
        Speak('traducao.mp3', translation, lang='en')
    elif 'português' in txt:
        MessageFormatted('O que você gostaria de traduzir para o português?')
        Speak('traducao.mp3', 'O que você gostaria de traduzir para o português?')
        message = RecognizeTranslater()
        translation = Translator(to_lang='pt-br', from_lang="en").translate(message)
        MessageFormatted(f'A tradução de "{message}" em inglês para o português é: ')
        Speak('traducao.mp3', f'A tradução de {message} em inglês para o português é: ')
        MessageFormatted(f'>>>>> {translation}')
        Speak('traducao.mp3', translation)


def Quotation(Coin):
    '''
    Função para saber a cotação do USD, EUR ou BTC em BRL
    :param Coin: Parâmetro passado para saber qual moeda analisar.
    '''
    url = 'https://economia.awesomeapi.com.br/json/last/'+ Coin[0:3] +'-'+ Coin[3:6]
    cotacao = requests.get(url).content
    dic = json.loads(cotacao)
    return dic[Coin]["bid"]


def BestMoviesMoment():
    '''
    Função para ver qual os melhores 5 filmes do momento.
    '''
    api_key = "<coloque sua chave API"
    url = f'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key={api_key}'
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    filmes = json.loads(dados)['results']
    print('='*60)
    contador = 1
    for filme in filmes[:5]:
        colorir(f"{contador}º - {filme['title']}", texto='Blue')
        Speak('filmes.mp3', filme['title'])
        contador += 1
    print('='*60)


def ExecuteComands(txt):
    '''
    Função que executa um comando baseado no que foi falado.
    :param txt: Parâmetro recebido para saber qual comando executar.
    '''
    global contador

    #Analisa qual pesquisa irá ser feita, no Google ou no Youtube.
    if "pesquisar" in txt and "google" in txt or 'pesquisa' in txt and 'google' in txt:
        txt = txt.replace("pesquisar no", "")
        txt = txt.replace("pesquisa no", "")
        txt = txt.replace("pesquisar", "")
        txt = txt.replace("pesquisa", "")
        txt = txt.replace("google", "")
        browser.open(f'https://google.com/search?q={txt}')
    elif "pesquisar" in txt and "youtube" in txt or "pesquisa" in txt and 'youtube' in txt:
        txt = txt.replace("pesquisar no", "")
        txt = txt.replace("pesquisa no", "")
        txt = txt.replace("pesquisar", "")
        txt = txt.replace("pesquisa", "")
        txt = txt.replace("youtube", "")
        browser.open(f'https://youtube.com/results?search_query={txt}')

    #Diz as horas ou a data atual.
    elif "horas" in txt:
        MessageFormatted(f"São {datetime.now().strftime('%H:%M')}")
        Speak("horas.mp3", f"São {datetime.now().strftime('%H:%M')}")
    elif "data" in txt or 'dia' in txt and 'hoje' in txt:
        MessageFormatted(f"Hoje é {datetime.now().strftime('%d/%m/%Y')}")
        Speak("data.mp3", f"Hoje é {datetime.now().strftime('%d/%m/%Y')}")

    #Fecha/Desliga a assistente.
    elif "fechar assistente" in txt or 'desligar assistente' in txt:
        MessageFormatted("Até logo. Desligando assistente.")
        Speak("desligando.mp3", "Até logo. Desligando assistente.")
        contador += 1

    #Diz a cotação das moedas presentes para o Real.
    elif "cotação" in txt:
        if 'dólar' in txt:
            MessageFormatted(f'O dólar está R${float(Quotation("USDBRL")):.2f}')
            Speak('cotacao.mp3', f'O dólar está R${float(Quotation("USDBRL")):.2f}')
        elif 'euro' in txt:
            MessageFormatted(f'O dólar está R${float(Quotation("EURBRL")):.2f}')
            Speak('cotacao.mp3', f'O euro está R${float(Quotation("EURBRL")):.2f}')
        elif 'bitcoin' in txt:
            MessageFormatted(f'O dólar está R${float(Quotation("BTCBRL")):.2f}')
            Speak('cotacao.mp3', f'O bitcoin está R${float(Quotation("BTCBRL")):.2f}')

    #Diz o clima da cidade pedida.
    elif 'clima' in txt:
        txt = txt.replace('qual é o clima em', '')
        txt = txt.replace('como está o clima em', '')
        txt = txt.replace('como está o clima no', '')
        txt = txt.replace('como está o clima na', '')
        txt = txt.replace('clima', '')
        MessageFormatted(Weather(txt))
        Speak("clima.mp3", Weather(txt))

    #Abre o arquivo pedido:
    elif 'abrir' in txt:
        if 'spotify' in txt:
            os.startfile(r"<caminho do arquivo do seu computado")
        elif 'steam' in txt:
            os.startfile(r"<caminho do arquivo do seu computado")
        elif 'visual studio code' in txt or 'vscode' in txt:
            os.startfile(r"<caminho do arquivo do seu computado")
        elif 'google' in txt or 'chrome' in txt or 'google chrome' in txt:
            os.startfile(r"<caminho do arquivo do seu computado")
        elif 'anotações' in txt or 'notepad' in txt:
            os.startfile(r'notepad.exe')

    #Traduz do PT-BR para o EN ou vice e versa.
    elif 'traduzir' in txt or 'traduza' in txt or 'tradutor' in txt:
            txt = txt.replace('traduzir', '')
            txt = txt.replace('traduza', '')
            txt = txt.replace('tradutor', '')
            Translater(txt)

    #Abre o site do spotify mostrando a melhor música, banda ou playlist. 
    elif 'melhor música' in txt:
        browser.open('https://open.spotify.com/intl-pt/track/7H7NyZ3G075GqPx2evsfeb?si=9c8bdab6cae94e46')
        MessageFormatted('Melhor música do mundo: Chamber of Reflection')
        Speak('musica.mp3', 'Melhor música do mundo: Chamber of Reflection')
    elif 'melhor playlist' in txt and 'rock' in txt:
        browser.open('https://open.spotify.com/playlist/6527f2OnyQ6EpQUFnmn6Bv?si=268ca001b37d450a')
        MessageFormatted('Melhor playlist de rock: Pedras Rolantes by Arthur Faturini')
        Speak('musica.mp3', 'Melhor playlist de rock: Pedras Rolantes by Arthur Faturini')
    elif 'melhor playlist' in txt and 'rap' in txt:
        browser.open('https://open.spotify.com/playlist/5i8lK1ft24IYQtipTrb2xF?si=cef96c851d764d2b')
        MessageFormatted('Melhor playlist de rap: Pensantes by Arthur Faturini')
        Speak('musica.mp3', 'Melhor playlist de rap: Pensantes by Arthur Faturini')
    elif 'melhor banda' in txt and 'rock' in txt:
        browser.open('https://open.spotify.com/intl-pt/artist/0k17h0D3J5VfsdmQ1iZtE9?si=e8ef4db2a2e043f4')
        MessageFormatted('Melhor banda de rock: Pink FLoyd')
        Speak('musica.mp3', 'Melhor banda de rock: Pink FLoyd')

    #Diz os 5 melhores filmes do momento.
    elif 'melhores filmes' in txt:
        BestMoviesMoment()

    #Caso nenhuma das funções anteriores rode, nesse caso irá considerar alguma forma de cumprimento.
    #Exemplo: Bom dia. Retornando: Bom dia!
    #Exemplo: Muito obrigado. Retornando: De nada!
    #Entre outras coisas...
    else:
        importlib.reload(answers)
        MessageFormatted(answers.cumprimentos[str(txt).lower()])
        Speak("cumprimentos.mp3", answers.cumprimentos[str(txt).lower()])


def ShutDonwAssistent():
    '''
    Função para desligar a assistente.
    '''
    sys.exit(0)


def Main():
    '''
    Função que roda o programa. 
    '''
    Menu("MENU PRINCIPAL")
    Speak("ola.mp3", "Olá, eu sou a Lena. Seja muito bem vindo!")
    while True:
        Recognize()


Main()
