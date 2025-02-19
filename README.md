# Assistente Virtual com Python
Fala pessoal, essa é a Lena, uma assistente virtual que executa os seus comandos de voz.

##Features:
* ** Horário atual:** "Que horas são?"<br>
* ** Pesquisa no Google:** "Pesquisar objeto no Google"<br>
* ** Pesquisa no Youtube:** "Pesquisar receita de macarrão no Youtube"<br>
* ** Cotação de dólar, euro e bitcoin:** "Qual a cotação do dólar no momento?"<br>
* ** 5 filmes mais populares do momento:** "Quais os filmes mais populares no momento?"<br>
* ** Abrir a melhor música, banda e álbum do mundo no Spotify:** "Qual a melhor música do mundo?"<br>
* ** Clima/tempo:** "Qual é o Clima no Rio de Janeiro"<br>
* ** Tradutor para inglês e português:** "Traduzir para o inglês"<br>
* ** Abrir programar na sua máquina:** "Abrir Spotify"<br>
* ** Fechar a assistente:** "Fechar assistente"<br>

##Tecnologia utilizadas:
* [Python](https://www.python.org/): Linguagem de programação
* [Speech Recognition](https://pypi.org/project/SpeechRecognition/): reconhecimento de voz
* [gTTS](https://pypi.org/project/gTTS/): Sintetização de voz
* [Playsound](https://pypi.org/project/playsound/): Executador de áudio
* [Translate](https://pypi.org/project/translate/): Traduz o que foi pedido
* Outras: os, sys, webbrowser, urllib.request, json, datetime, requests

## Como executar:

## **1. Instale `Python` na sua máquina, por meio [deste link](https://www.python.org/)**

### **2. Faça um clone [desse repositório](https://github.com/ArthurFaturini/Assistente-Virtual) na sua máquina:**
* Crie uma pasta no seu computador para esse programa, recomendo colocar o nome **Assistente Virtual**
* Abra o `git bash` ou `terminal` dentro dessa pasta
* Copie a [URL](https://github.com/ArthurFaturini/Assistente-Virtual) do repositório
* Digite `git clone <URL copiada>` e pressione `enter`

### **3. Instale as bibliotecas necessárias pelo terminal, dentro dessa pasta criada:**

* gTTS: `pip install gTTS`
* Playsound: `pip install playsound`
* Speech recognition: `pip install SpeechRecognition`
* Translate: `pip install translate`
#Caso apareça algum erro referente a alguma das bibliotecas importadas no programa, jogue o nome dela no Google e faça a instalação e passo a passo necessários

### **4. Crie sua chave para as APIs:**

**API de filmes:**
* Acesse o [The Movie DataBase](https://www.themoviedb.org/) e faça seu cadastro
* Em configurações, acesse API e crie uma nova chave
* Copie a chave e cole na `variável` da função `BestMoviesMoment()`, substituindo a frase `<coloque sua chave API>`

**API de clima:**
* Acesse o [Open Wheather Map](https://openweathermap.org/) e faça seu cadastro
* Confirme o email recebido e em configurações, acesse suas API Keys
* Copie a chave e cole na `variável` da função `Weather()`, substituindo a frase `<coloque sua chave API>`

### **5. Preencha os caminhos dos programas na sua máquina:**
* Pesquise os caminhos dos seguintes programas executáveis na sua máquina: Google Chrome, Visual Studio Code, Steam e Spotify
* Abaixo do comentário `abrir programas do computador`, cole o respectivo caminho em cada chamada de função
* Exemplo: `os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")`
* Caso queira adicionar ou deletar algum programa, faça isso utilizando o padrão do código
