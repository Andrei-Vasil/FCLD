# TODO: lr(0)

class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def closure(self, input):
        P = {}

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
