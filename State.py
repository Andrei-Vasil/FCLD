class State:
    def __init__(self, token, initial=False, final=False):
        self.transitions = dict()
        self.token = token
        self.is_final = final
        self.is_initial = initial

    def add_transition(self, state, char):
        self.transitions[char].append(state)
    
    def is_DFA(self):
        for _, value in self.__transitions.items():
            if len(value) > 1:
                return False
        return True

    def __str__(self):
        return "{self.token} is_initial: {self.initial} is_final: {self.final}\n"
