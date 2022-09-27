class DFA():
    def __init__(self, states, alphabet, transitions, initial, accept, test):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial = initial
        self.accept = accept
        self.test = test

    def lerTeste(self):
        for i in self.test:
            if not self.verificaTransicao(i):
                return False
        if self.initial in self.accept:
            return True
        return False

    def verificaTransicao(self, valor):
        for i in self.transitions:
            if i[0] == self.initial and valor in i:
                self.initial = i[-1]
                return True
        return False
