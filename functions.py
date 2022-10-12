def adiciona_lista(list_, nome):
    retorno = []
    for i in list_:
        if i.strip("\n") == nome:
            break
        retorno.append(i.strip("\n"))
    return retorno


def separa_lista(transicoes):
    retorno = []
    for i in transicoes:
        list_ = []
        list_.append(i.split(":")[0])
        split = i.split(":")[1].split(">")[0]
        for a in split.split(","):
            list_.append(a)
        list_.append(i.split(":")[1].split(">")[1])
        retorno.append(list_)
    return retorno


def lerarquivo():

    dado = open("automato.txt", "r")
    automatos = dado.readlines()

    for i in range(len(automatos)):

        if automatos[i] == "#states\n":
            states = adiciona_lista(automatos[1+1:], "#initial")

        elif automatos[i] == "#initial\n":
            initial = adiciona_lista(automatos[i+1:], "#accepting")

        elif automatos[i] == "#accepting\n":
            accepting = adiciona_lista(automatos[i+1:], "#alphabet")

        elif automatos[i] == "#alphabet\n":
            alphabet = adiciona_lista(automatos[i+1:], "#transitions")

        elif automatos[i] == "#transitions\n":

            transitions = adiciona_lista(automatos[i+1:], "")
        dado.close()
    separar = separa_lista(transitions)

    return states, initial, accepting, alphabet, separar


states, initial, accepting, alphabet, transitions = lerarquivo()
