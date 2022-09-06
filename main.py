dado = open("automato.txt", "r")
listaAutomato = []
automatos = dado.readlines()

for automato in automatos:
    listaAutomato.append(automato.split('\n')[0])
    dado.close()

print(listaAutomato)
