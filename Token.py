from DefineToken import *


class Token:

    def __init__(self, tok, value):
        self._t = tok
        self._c = value

    def __str__(self):
        if self._t.value == DefineToken.IDENT.value:
            return "<" + self._t + ":" + self._c + ">"
        elif self._t.value == DefineToken.WHOLE_NUM.value:
            return "<" + self._c + ">"
        else:
            return self._t

    def get_token(self):
        return self._t

    def get_value(self):
        return self._c