import enum

class DefineToken(enum.Enum):
  LEFTPAREN = 1
  RIGHTPAREN = 2
  ADDITION = 3
  MINUS = 4
  TIMES = 5
  DIVISION = 6
  IDENT = 7
  WHOLE_NUM = 8
  EOF = -1