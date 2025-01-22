class MathRequest:

    def __init__ (self, ope1, operator, ope2):
        raise NotImplementedError

    def get_ope1(self):
        raise NotImplementedError

    def get_operator(self):
        raise NotImplementedError

    def get_ope2(self):
        raise NotImplementedError

    def get_res(self):
        raise NotImplementedError

    def set_res(self, value):
        raise NotImplementedError

    def to_string(self):
        raise NotImplementedError