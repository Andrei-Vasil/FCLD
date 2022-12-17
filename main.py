from Grammar import Grammar
from Parser import Parser

if __name__ == '__main__':
    # input_file = 'input/g1.in'
    # input_file = 'input/g2.in'
    input_file = 'input/g3.in'
    grammar = Grammar.fromFile(input_file)
    
    # print(grammar)
    # print(grammar.checkIfCFG())
    # print('[===================================]\n\n')

    parser = Parser(grammar)
    canonicalCollection = parser.canonicalCollection()
    print('states:')
    for i, s in enumerate(canonicalCollection.states):
        print(f'#{i} {s}')
    print(f'state transitions: {canonicalCollection.adjacencyList}')
    print('[===================================]\n\n')

    print(grammar.getEnrichedGrammar().getOrderedProductions())
    print('parsing table:')
    print(parser.getParsingTable())

    result = []
    # try:
    parseTree = parser.parse(['a', 'b', 'b', 'c'])

    for row in parseTree:
        result.append(f'{row.index}: {row.info}, {row.parent}, {row.rightSibling}')
    result.sort()
    for r in result:
        print(r)
    # File("out.txt").writeText(result)
    # except Exception as e:
    #     print(e)
