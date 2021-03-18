# Convertendo de graus Celsius para Fahremheit

celsius = input("Coloque a temperatura de hoje em graus Celsius: ")

convertFah = float(celsius) * 1.8 + 32


print("A temperatura de {}°C ficou convertida em {}°F".format(celsius, convertFah))


#Convertendo de Fahremheit para Celsius

fahremheit = input("Coloque a temperatura de hoje em Fahremheit: ")

convertCel = (float(fahremheit) - 32) / 1.8

print("A temperatura de {}°F ficou convertida em {}°C".format(fahremheit, convertCel))