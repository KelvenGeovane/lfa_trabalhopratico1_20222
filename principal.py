from dfa import DFA
from functions import lerarquivo
from nfa import NFA

states, initial, accepting, alphabet, transitions = lerarquivo()
dfa = DFA(states, alphabet, transitions,
          initial[0], accepting, "01010")


print(lerarquivo())
print(dfa.lerTeste())
print()


# automaton = NFA(transitions, alphabet, initial[0], accepting, states)
# validWord, graph = automaton.validateWord("0010101")
# print(validWord)
# print(graph)
