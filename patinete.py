print("Este programa calcula a velocidade média de um patinete elétrico")

#Informando a distância e o tempo

distancia = input("Qual a distância em metros percorrida pelo patinete? : ")
tempo = input("Quantos minutos o patinete demorou para percorrer essa distância? : ")

#Fazendo o cálculo da distância e do tempo

velocidade_media = float(distancia) / float(tempo)

#Exibindo o resultado final

print("O patinete atingiu uma velocidade de {} m/min".format(velocidade_media))