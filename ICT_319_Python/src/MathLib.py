class MathLib:

    @classmethod
    def execute(cls, math_request):
        operator = None

        match operator:
            case 'add':
                raise NotImplementedError
            case 'sub':
                raise NotImplementedError
            case 'mul':
                raise NotImplementedError
            case 'div':
                raise NotImplementedError
            case 'pow':
                raise NotImplementedError
            case 'root':
                raise NotImplementedError
            case _:
                raise NotImplementedError

    @staticmethod
    def __root(ope1, ope2):
        raise NotImplementedError

class MathLibException(Exception):
    pass

class OperatorNotSupportedException(MathLibException):
    pass