from dfa import DFA
from functions import lerarquivo

states, initial, accepting, alphabet, transitions = lerarquivo()
dfa = DFA(states, alphabet, transitions,
          initial[0], accepting, "bcbacabcbcbbbabb")


print(dfa.lerTeste())
