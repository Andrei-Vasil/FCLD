import copy
import Grammar
import Item
import State

# TODO: lr(0)
class Parser:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar

    def getDotPrecededNonTerminal(self, item:Item):
        if item.dotPos >= len(item.rhs) or item.dotPos < 0 :
            return None
        term = item.rhs[item.dotPos]
        if term not in self.grammar.nonTerminals:
            return None
        return term

    def closure(self, item: Item):
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

    def goTo(self, state, element: str):
        pass

    def canonicalCollection(self):
        pass
