print("PROGRAMANDO EM PYTHON - LET'S ROCK")

print("Calculando as notas bimestrais")

notaA = input("Digite a nota do 1° semestre: ")

notaB = input("Digite a nota do 2° semestre: ")

notaC = input("Digite a nota do 3° semestre: ")

notaD = input("Digite a nota do 4° semestre: ")


#Soma das notas

somaDasNotas = float(notaA) + float(notaB) + float(notaC) + float(notaD)

#Calculando a media das notas

media = somaDasNotas / 4

print(media)

#Passando mensagem de aprovado ou reprovado

if media < 6:
    print("Que pena, você foi reprovado")
elif media == 6:
    print("Parabéns, você passou, mas sempre pode melhorar mais!")
else:
    print("Wow, que notas incríveis!! Parabéns, you're Rock!!!")
