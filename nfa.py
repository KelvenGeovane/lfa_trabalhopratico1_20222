class NFA():
    def __init__(self, states, alphabet, transitions, initial, accepting, test):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial = initial
        self.accepting = accepting
        self.test = test
        self.listNos = []


# verificar loops

    # def estadosLoop(self):
    #     for i in self.states:

    def estadosIguais(self):
        for i in self.transitions:
            if i[0] == i[-1]:
                self.listNos.append(i)
