import Grammar
import Item

# TODO: lr(0)

class Parser:
    # TODO: lr(0)

    def __init__(self, grammar: Grammar):
        self.grammar = grammar

    def closure(self, item: Item):
        oldClosure = {}
        currentClosure = item
        while True:
            oldClosure = currentClosure.toMutableSet()
            newClosure = currentClosure.toMutableSet()
            for it in currentClosure:
                nonTerminal = getDotPrecededNonTerminal(it)
                for production in grammar.getProductionsFor(nonTerminal):
                    currentItem = Item(nonTerminal, production, 0)
                    newClosure.add(currentItem)
            currentClosure = newClosure
            if oldClosure == currentClosure:
                break

        return P

    # private fun goTo(state: State, element: String): State {
    #     val result = mutableSetOf<Item>()
    #     for (item in state.items) {
    #         val nonTerminal = item.rhs.getOrNull(item.dotPosition)
    #         if (nonTerminal == element) {
    #             val nextItem = Item(item.lhs, item.rhs, item.dotPosition + 1)
    #             result.addAll(closure(nextItem).items)
    #         }
    #     }
    #     return State(result)
    # }

    def goTo(self, state, element: str):
        pass

    def canonicalCollection(self):
        res = []
        res.add(closure(""))
        ok = True

        while ok:
            ok = False
