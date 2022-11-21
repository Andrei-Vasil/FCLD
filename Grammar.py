class Grammar:
    @staticmethod
    def parseLine(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

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
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            rhs = [value.strip() for value in rhs.split('|')]

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

    def __str__(self):
        return 'N = { ' + ', '.join(self.N) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'P = { ' + ', '.join([' -> '.join(prod) for prod in self.P]) + ' }\n' \
               + 'S = ' + str(self.S) + '\n'


if __name__ == '__main__':
    print(Grammar.fromFile('input/g1.in'))
