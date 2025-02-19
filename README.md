# Assistente Virtual com Python
Fala pessoal, essa é a Lena, uma assistente virtual que executa os seus comandos de voz.

Features:\n
⌚ Horário atual: "Que horas são?"
🔎 Pesquisa no Google: "Pesquisar objeto no Google"
📺 Pesquisa no Youtube: "Pesquisar receita de macarrão no Youtube"
🤑Cotação de dólar, euro e bitcoin: "Qual a cotação do dólar no momento?"
📽️ 5 filmes mais populares do momento: "Quais os filmes mais populares no momento?"
🎧 Abrir a melhor música, banda e álbum do mundo no Spotify: "Qual a melhor música do mundo?"
⛅ Clima/tempo: "Qual é o Clima no Rio de Janeiro"
🔃 Tradutor para inglês e português: "Traduzir para o inglês"
💻 Abrir programar na sua máquina: "Abrir Spotify"
🙋🏽‍♀️ Fechar a assistente: "Fechar assistente"

Tecnologia utilizadas:\n
Python: Linguagem de programação
Speech Recognition: reconhecimento de voz
gTTS: Sintetização de voz
Playsound: Executador de áudio
Translate: Traduz o que foi pedido
Outras: os, sys, webbrowser, urllib.request, json, datetime, requests

Como executar:

1. Instale Python na sua máquina, por meio deste link

2. Faça um clone desse repositório na sua máquina:
Crie uma pasta no seu computador para esse programa, recomendo colocar o nome Assistente Virtual
Abra o git bash ou terminal dentro dessa pasta
Copie a URL do repositório
Digite git clone <URL copiada> e pressione enter

3. Instale as bibliotecas necessárias pelo terminal, dentro dessa pasta criada:
gTTS: pip install gTTS
playsound: pip install playsound
speech recognition: pip install SpeechRecognition
translate: pip install translate 
#Caso apareça algum erro referente a alguma das bibliotecas importadas no programa, jogue o nome dela no Google e faça a instalação e passo a passo necessários.

4. Crie sua chave para as APIs:

API de filmes:
Acesse o The Movie DataBase e faça seu cadastro
Em configurações, acesse API e crie uma nova chave
Copie a chave e cole na variável da função BestMoviesMoment(), substituindo a frase <coloque sua chave API>

API de clima:
Acesse o Open Wheather Map e faça seu cadastro
Confirme o email recebido e em configurações, acesse suas API Keys
Copie a chave e cole na variável da função Weather(), substituindo a frase <coloque sua chave API>

5. Preencha os caminhos dos programas na sua máquina:
Pesquise os caminhos dos seguintes programas executáveis na sua máquina: Google Chrome, Visual Studio Code, Steam e Spotify
Abaixo do comentário abrir programas do computador, cole o respectivo caminho em cada chamada de função
Exemplo: os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
Caso queira adicionar ou deletar algum programa, faça isso utilizando o padrão do código.
