class Grammar:
    @staticmethod
    def parseLine(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split('\n')]

    @staticmethod
    def fromFile(fileName):
        with open(fileName) as file:
            N = Grammar.parseLine(file.readline())
            E = Grammar.parseLine(file.readline())
            S = file.readline().split('=')[1].strip()
            P = Grammar.parseRules(Grammar.parseLine(''.join([line for line in file])))

            return Grammar(N, E, P, S)

    @staticmethod
    def parseRules(rules):
        result = []

        for rule in rules:
            print(rule)
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            rhs = [filter(lambda c: c != '', (value.split(' '))) for value in rhs.split('|')]

            for value in rhs:
                result.append((lhs, value))

        return result

    def __init__(self, N, E, P, S):
        self.N = N
        self.E = E
        self.P = P
        self.S = S

    def isNonTerminal(self, value):
        return value in self.N

    def isTerminal(self, value):
        return value in self.E

    def getProductionsFor(self, nonTerminal):
        if not self.isNonTerminal(nonTerminal):
            raise Exception('Can only show productions for non-terminals')
        return [prod for prod in self.P if prod[0] == nonTerminal]

    def showProductionsFor(self, nonTerminal):
        productions = self.getProductionsFor(nonTerminal)
        print(', '.join([' -> '.join(prod) for prod in productions]))

    def checkIfCFG(self):
        checkStartingSymbol = False

        for rule in self.P:
            lhs, rhs = rule
            if self.S == lhs:
                checkStartingSymbol = True
                break

        if not checkStartingSymbol:
            return False

        for rule in self.P:
            lhs, rhs = rule
            if len(lhs) > 1:
                return False
            elif lhs not in self.N:
                return False

            for r in rhs:
                if not (r in self.N or r in self.E or r == 'e'):
                    return False

        return True

    def __str__(self):
        return 'N = { ' + ', '.join(self.N) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'P = { ' + ', '.join([(prod[0] + ' -> ' + " ".join(prod[1])) for prod in self.P]) + ' }\n' \
               + 'S = ' + str(self.S) + '\n'


if __name__ == '__main__':
    print(Grammar.fromFile('input/gl.in'))
    print(Grammar.fromFile('input/gl.in').checkIfCFG())
