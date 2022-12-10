# TODO: lr(0)
from State import State
from CannonicalCollection import CanonicalCollection

class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.workingGrammar = grammar

    def closure(self, input):
        P = {}

        return P

    def goTo(self, state: State, element: str) -> State:
        result = set()
        for item in state.items:
            nonTerminal = item.rhs.getOrNull(item.dotPosition)
            if nonTerminal == element:
                nextItem = Item(item.lhs, item.rhs, item.dotPosition + 1)
                result.addAll(self.closure(nextItem).items)
        return State(result)

    def canonicalCollection(self) -> CanonicalCollection:
        canonicalCollection = CanonicalCollection()
        canonicalCollection.addState(
            self.closure(
                Item(
                    self.workingGrammar.startingSymbol,
                    self.workingGrammar.productionSet.getProductionsOf(self.workingGrammar.startingSymbol)[0],  # TODO: make this line work with our current architecture
                    0
                )
            )
        )
        i = 0
        while i < canonicalCollection.states.size:
            pass