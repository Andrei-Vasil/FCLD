from State import State

class CanonicalCollection:
    states = []
    adjacencyList = dict()  # {(int, string): int}

    def addState(self, state: State):
        self.states.add(state)

    def connectStates(self, indexFirstState: int, symbol: str, indexSecondState: int):
        self.adjacencyList[(indexFirstState, symbol)] = indexSecondState
