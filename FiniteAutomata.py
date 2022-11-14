class FiniteAutomata:
    def __init__(self):
        self.alphabet = set()
        self.states = dict()
    
    def add_state(self, state):
        self.states[state.token] = state

    def get_state(self, token):
        return self.states[token] if token in self.states else None

    def alphabet_append(self, char):
        self.alphabet.add(char)

    def add_transition(self, src, dest, how):
        if how not in self.alphabet:
            print('invalid char: {how} does not exist in alphabet')
            return
        self.get_state(src).add_transition(self.get_state(dest), how)
        
    def is_DFA(self):
        for state in self.states.values():
            if not state.is_DFA():
                return False
        return True

    def accept(self, word):
        now = None
        for state in self.states.values():
            if state.is_initial:
                now = state
                break
        idx = 0
        while idx < len(word):
            edges = now.transitions
            if word[idx] in edges.keys():
                now = edges[word[idx]][0]
                idx += 1 
            else:
                return False
        return idx == len(word) and now.is_final
