# TODO: lr(0)
from Grammar import Grammar
from Item import Item
from State import State
from CannonicalCollection import CanonicalCollection
import copy

class Parser:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.enrichedGrammar = grammar.getEnrichedGrammar()

    def closure(self, item: Item) -> State: 
        oldClosure = dict()
        currentClosure = {item.deepCopy(): None}
        while True:
            oldClosure = copy.deepcopy(currentClosure)
            newClosure = copy.deepcopy(currentClosure)
            for it in currentClosure.keys():
                nonTerminal = self.getDotPrecededNonTerminal(it)
                if nonTerminal is None:
                    continue
                for production in self.grammar.getProductionsFor(nonTerminal):
                    currentItem = Item(nonTerminal, production, 0)
                    newClosure[currentItem] = None
            currentClosure = newClosure
            if str(list(oldClosure.keys())[0]) == str(list(currentClosure.keys())[0]):
                break
        return State(currentClosure)

    def getDotPrecededNonTerminal(self, item: Item):
        if not (0 <= item.dotPos < len(item.rhs)):
            return None
        term = item.rhs[item.dotPos]
        if term not in self.grammar.N:
            return None
        return term

    def goTo(self, state: State, element: str) -> State:
        result = dict()
        for item in state.items:
            print(f'debug {item}')
            nonTerminal = None
            if 0 <= item.dotPos < len(item.rhs):
                nonTerminal = item.rhs[item.dotPos]
            if nonTerminal == element:
                nextItem = Item(item.lhs, item.rhs, item.dotPos + 1)
                for item in self.closure(nextItem).items:
                    result[item] = None
        return State(result)

    def canonicalCollection(self) -> CanonicalCollection:
        canonicalCollection = CanonicalCollection()
        canonicalCollection.addState(
            self.closure(
                Item(
                    self.enrichedGrammar.S,
                    self.enrichedGrammar.getProductionsFor(self.enrichedGrammar.S)[0][1][0],
                    0
                )
            )
        )
        print('==================================================')
        item = Item(
                    self.enrichedGrammar.S,
                    self.enrichedGrammar.getProductionsFor(self.enrichedGrammar.S)[0][1][0],
                    0
                )
        print(item)
        print(item.lhs)
        print(item.rhs)
        print(item.dotPos)
        print('==================================================')
        print(self.closure(
                Item(
                    self.enrichedGrammar.S,
                    self.enrichedGrammar.getProductionsFor(self.enrichedGrammar.S)[0][1][0][0],
                    0
                )
            ))
        print('==================================================')
        i = 0
        while i < len(canonicalCollection.states):
            for symbol in canonicalCollection.states[i].getSymbolsSucceedingTheDot():
                newState = self.goTo(canonicalCollection.states[i], symbol)
                try:
                    indexInStates = canonicalCollection.states.index(newState)
                except ValueError:
                    indexInStates = -1
                if indexInStates == -1:
                    canonicalCollection.addState(newState)
                    indexInStates = len(canonicalCollection.states) - 1
                canonicalCollection.connectStates(i, symbol, indexInStates)
            i += 1
        return canonicalCollection
