from dfa import DFA
from functions import lerarquivo
from nfa import NFA

states, initial, accepting, alphabet, transitions = lerarquivo()
dfa = DFA(states, alphabet, transitions,
          initial[0], accepting, "abcb")


print(lerarquivo())
print(dfa.lerTeste())
