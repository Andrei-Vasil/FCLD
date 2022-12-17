from dataclasses import dataclass

from State import StateType


@dataclass
class Row:
    def __init__(self, stateType: StateType, goTo: dict[str, int] or None, reductionIndex: int or None):
        self.stateType = stateType
        self.goTo = goTo
        self.reductionIndex = reductionIndex

    def __str__(self):
        if self.stateType == StateType.REDUCE:
            return f'REDUCE {self.reductionIndex}'
        elif self.stateType == StateType.ACCEPT:
            return 'ACCEPT'
        elif self.stateType == StateType.SHIFT:
            return f'SHIFT {self.reductionIndex}'
        else:
            raise Exception("No other states allowed")
