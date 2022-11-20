import sys
from DefineToken import *
from Token import *
# Lexical analyzer for arithmetic expressions which
# include variable names and  integer literals
# Input: (sum + 45)*(num-26) / total


class Lexer:

    def __init__(self, s):
        self._index = 0
        self._tokens = self.tokenize(s)

    def tokenize(self, s):
        result = []
        i = 0
        while i < len(s):
          c = s[i]
          if c == '(':
            result.append(Token(DefineToken.LEFTPAREN, "("))
            i = i + 1
          elif c == ')':
            result.append(Token(DefineToken.RIGHTPAREN, ")"))
            i = i + 1
          elif c == '+':
              result.append(Token(DefineToken.ADDITION, "+"))
              i = i + 1
          elif c == '-':
              result.append(Token(DefineToken.MINUS, "-"))
              i = i + 1
          elif c == '*':
              result.append(Token(DefineToken.TIMES, "*"))
              i = i + 1
          elif c == '/':
              result.append(Token(DefineToken.DIVISION, "/"))
              i = i + 1
          elif c in ' \r\n\t':
              i = i + 1
              continue
          elif c.isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                  j = j + 1
                result.append(Token(DefineToken.WHOLE_NUM, s[i:j]))
                i = j
          elif c.isalpha():
                j = i
                while j < len(s) and s[j].isalnum():
                    j = j + 1
                result.append(Token(DefineToken.IDENT, s[i:j]))
                i = j
          else:
                print("UNEXPECTED CHARACTER ENCOUNTERED: "+c)
                sys.exit(-1)
        result.append(Token(DefineToken.EOF, "EOF"))
        return result

    def lex(self):
        t = None
        if self._index < len(self._tokens):
            t = self._tokens[self._index]
            self._index = self._index + 1
        print("Next Token: "+str(t.get_token().name)+" "+str(t.get_token().value)+
              ", Next Lexeme: "+t.get_value())
        return t
