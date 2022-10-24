import re

class Scanner:
    def __init__(self):
        self.reserved_expressions = re.compile('^(if|while|print|int|bool|print|read)$')
        self.number = re.compile('^-{,1}[1-9]+[0-9]*$')
        self.string = re.compile('^(\'|\")( a-zA-Z.;:?!)*(\'|\")$')
        self.identifier = re.compile('^[a-zA-Z]+[a-zA-Z0-9_-]*$')
        self.operator = re.compile('^(\+|-|/|\*|=|==|!=|<|>|<=|>=|&&|\|\|)$')
        self.deliminator = re.compile('^(;|\{|\}| |\n|,|\(|\))$')
        self.comment = re.compile('^//$')

    def read_file(self, input_path: str):
        file = open(input_path, 'r')
        
        expression = ''
        while file:
            byte = file.read(1)
            if byte == '':
                return
            if self.comment.match(expression + byte):
                print("comment")
                file.readline()
                expression = ''
            elif self.deliminator.match(byte):
                if expression == '':
                    continue
                elif self.reserved_expressions.match(expression) is not None:
                    print('reserved expr')
                elif self.number.match(expression) is not None:
                    print('number')
                elif self.string.match(expression) is not None:
                    print('string')
                elif self.identifier.match(expression) is not None:
                    print('id')
                elif self.operator.match(expression) is not None:
                    print('operator')
                else:
                    print(expression)
                    print('lexical error')
                    exit(1)
                print(expression)
                expression = ''
            else:
                expression += byte

if __name__ == "__main__":
    Scanner().read_file('input/p1err.in')
