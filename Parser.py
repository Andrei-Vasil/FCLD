# TODO: lr(0)
from Grammar import Grammar
from Item import Item
from State import State
from CannonicalCollection import CanonicalCollection
import copy

# TODO: lr(0)
class Parser:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.workingGrammar = grammar

    def closure(self, item: Item) -> State: 
        oldClosure = dict()
        currentClosure = {item.deepCopy():None}
        while True:
            oldClosure = copy.deepcopy(currentClosure)
            newClosure = copy.deepcopy(currentClosure)
            for it in currentClosure:
                nonTerminal = self.getDotPrecededNonTerminal(it)
                for production in self.grammar.getProductionsFor(nonTerminal):
                    currentItem = Item(nonTerminal, production, 0)
                    newClosure.add(currentItem)
            currentClosure = newClosure
            if oldClosure == currentClosure:
                break
        return State(currentClosure)

    def getDotPrecededNonTerminal(self, item: Item):
        if item.dotPos >= len(item.rhs) or item.dotPos < 0 :
            return None
        term = item.rhs[item.dotPos]
        if term not in self.grammar.nonTerminals:
            return None
        return term

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
