from _ast import If


class MathRequest:

    def __init__ (self, ope1, operator, ope2):
        self.ope1 = ope1
        self.operator = operator
        self.ope2 = ope2
        self.res = None

    def get_ope1(self):
        return self.ope1

    def get_operator(self):
        return self.operator

    def get_ope2(self):
        return self.ope2

    def get_res(self, res=None):
        if res is not None:
            self.res = res
        return self.res

    def to_string(self, res=None):
        return f"{self.ope1} {self.operator} {self.ope2} = {self.res}"