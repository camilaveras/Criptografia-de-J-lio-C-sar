import requests
import json
import hashlib

def main():
  url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=9ac708cb4ca674c0be7118355b9009cc64369e19'
  
  setMensage()
  decoder()
  sha1()
  arquivo = setAnswer()
  files = {"answer": open("answer.json", "rb")}
  response = requests.post(url, files=files)
  print(response.text)

def setMensage():
  url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=9ac708cb4ca674c0be7118355b9009cc64369e19"
  resposta = requests.get(url)
  dado = resposta.json()
  dado = json.dumps(dado, indent=4)
  arquivo = open("answer.json", "w")#abrindo o arquivo para escrita
  arquivo.write(dado)#escrevendo no arquivo
  arquivo.close()#fechando o arquivo

def getMensage():

    arquivo = open("answer.json", "r")#abrindo o arquivo para leitura

    data = json.load(arquivo)#converte e lê

    menCrip = data['cifrado']

    return data


def decoder():

  data = getMensage() 
  menCrip = data['cifrado'].lower()

  numero_casas = data['numero_casas']

  alfa = 'abcdefghijklmnopqrstuvwxyz'
  x = 0
  menDescrip = ''
  
  return menDescrip

def sha1():
  mensage = decoder()
  resul = hashlib.sha1(mensage.encode())#converte no equivalente de byte
  resCrip = resul.hexdigest()#gera sequencia equivalente hexadecimal
  return resCrip

def setAnswer():

  decifrado = decoder()

  resumo_crip = sha1()
  numero_casas = getMensage()['numero_casas']

  dado = {

    "numero_casas": numero_casas,

    "token": "9ac708cb4ca674c0be7118355b9009cc64369e19",

    "cifrado": getMensage()['cifrado'],

    "decifrado":decifrado,

    "resumo_criptografico": resumo_crip

  }

  dado = json.dumps(dado, indent=4)
  arquivo = open("answer.json", "w")
  arquivo.write(dado)
  arquivo.close()

  return arquivo

if __name__=="__main__":
  main()
