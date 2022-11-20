from LexicalAnalyzer import *
from DefineToken import *


def main():

    input = "(sum + 45)*(num-26) / total"
    lexer = Lexer(input)
    print("Input Token==>", end="")
    print(input)
    while True:
        t = lexer.lex()
        if t.get_token().value == DefineToken.EOF.value:
            break
main()
