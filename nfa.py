from itertools import combinations


class NFA():
    def __init__(self, graph, alphabet, initial, accepting, states):
        self.__graph = graph
        self.__alphabet = alphabet
        self.__initial = initial
        self.__accepting = accepting
        self.__states = states
