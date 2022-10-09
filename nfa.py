from itertools import combinations


class NFA():
    def __init__(self, graph, alphabet, initial, accepting, states):
        self.__graph = graph
        self.__alphabet = alphabet
        self.__initial = initial
        self.__accepting = accepting
        self.__states = states

    def tableOfAllStates(self):
        statesTable = []
        statesCombination = self.allStatesCombinations()
        alphabet = self.__alphabet
        alphabetSize = len(alphabet)
        statesCombinationSize = len(statesCombination)
        increment = 0

        for i in range(statesCombinationSize*alphabetSize):
            statesTable.append([])

        for i in range(statesCombinationSize):
            for j in range(alphabetSize):
                for c in range(0, len(self.__graph), 2):
                    vertix = self.__graph[c]
                    adj = self.__graph[c+1][0]
                    peso = self.__graph[c+1][1]

                if vertix in statesCombination[i] and peso == alphabet[j]:
                    statesTable[increment].append(adj)
                increment += 1

        return statesTable, alphabet, statesCombination

    def validateWord(self, word):
        graph = self.tableofValidStates()
        currentState = self.__initial
        for letter in word:
            for peso, adj in graph[currentState].items():
                if peso == letter:
                    currentState = adj

        for fState in self.__accepting:
            if fState in currentState:
                return True, graph

        return False, graph

    def tableofValidStates(self):
        graph = self.generateGraph()

        validGraph = {}
        visited = []
        queue = [self.__initial]

        while queue:
            validGraph[queue[0]] = {}
            for peso, adj in graph[queue[0]].items():
                validGraph[queue[0]][peso] = adj
                if adj not in visited:
                    queue.append(adj)
        visited.append(queue.pop(0))

        return validGraph

    def generateGraph(self):
        statesTable, alphabet, statesCombination = self.tableOfAllStates()
        stringStatesCombination = []
        stringStatesTable = []
        graph = {}

        for i in range(len(statesCombination)):
            stringStatesCombination.append("")

        for i in range(len(statesTable)):
            stringStatesTable.append("")

        for i in range(len(statesCombination)):
            for j in statesCombination[i]:
                stringStatesCombination[i] += j

        for i in range(len(statesTable)):
            for state in statesTable[i]:
                stringStatesTable[i] += state

        count = 0
        for i in range(len(statesCombination)):
            state = stringStatesCombination[i]
            graph[state] = {}
        for letter in alphabet:
            graph[state][letter] = stringStatesTable[count]
            count += 1
        return graph

    def allStatesCombinations(self):
        statesSize = len(self.__states)
        combinationStates = []
        for i in range(statesSize):
            for combination in combinations(self.__states, i+1):
                combinationStates.append(combination)
        return combinationStates
