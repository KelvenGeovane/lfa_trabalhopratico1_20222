def add_lista(list_, nome):
    list_return = []
    for i in list_:
        if i.strip("\n") == nome:
            break
        list_return.append(i.strip("\n"))
    return list_return


def split_list(list_transitions):
    list_return = []
    for i in list_transitions:
        list_ = []
        list_.append(i.split(":")[0])
        split = i.split(":")[1].split(">")[0]
        for a in split.split(","):
            list_.append(a)
        list_.append(i.split(":")[1].split(">")[1])
        list_return.append(list_)
    return list_return


def lerarquivo():

    dado = open("automato.txt", "r")
    automatos = dado.readlines()

    for i in range(len(automatos)):

        if automatos[i] == "#states\n":
            states = add_lista(automatos[1+1:], "#initial")

        elif automatos[i] == "#initial\n":
            initial = add_lista(automatos[i+1:], "#accepting")

        elif automatos[i] == "#accepting\n":
            accepting = add_lista(automatos[i+1:], "#alphabet")

        elif automatos[i] == "#alphabet\n":
            alphabet = add_lista(automatos[i+1:], "#transitions")

        elif automatos[i] == "#transitions\n":

            transitions = add_lista(automatos[i+1:], "")
        dado.close()
    separar = split_list(transitions)

    # print(states)
    # print(initial)

    # print(separar)

    # print(accepting)

    # print(alphabet)

    return states, initial, accepting, alphabet, separar


states, initial, accepting, alphabet, transitions = lerarquivo()
