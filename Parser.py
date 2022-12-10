import copy
import Grammar
import Item

# TODO: lr(0)

class Parser:
    # TODO: lr(0)

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
        oldClosure = {}
        currentClosure = item
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
        return 

    def goTo(self, state, element: str):
        pass

    def canonicalCollection(self):
        res = []
        res.add(closure(""))
        ok = True

        while ok:
            ok = False
