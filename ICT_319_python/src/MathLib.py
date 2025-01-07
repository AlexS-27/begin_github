from src.Math_Request import MathRequest

class MathLib:

    def __init__(self, math_request, res=0):
        if not isinstance(math_request, MathRequest):
            raise TypeError('MathLib constructor must be of type MathRequest')
        self.math_request = math_request
        self.res = res

    def calculate(self):
        # Perform the operation based on the operator
        ope1 = self.math_request.ope1
        oper = self.math_request.oper
        ope2 = self.math_request.ope2

        match oper:
            case '+':
                self.res = ope1 + ope2
            case '-':
                self.res = ope1 - ope2
            case '*':
                self.res = ope1 * ope2
            case '/':
                if ope2 == 0:
                    print("Error: Division by zero is undefined.")
                    return
                self.res = ope1 / ope2
            case '^':
                self.res = ope1 ** ope2
            case _:
                print("Invalid operator.")
                return None
        return self.res

    def verification_oper(self):
        valid_operators = ['+', '-', '*', '/', '^']

        while self.math_request.oper not in valid_operators:
            print("Invalid operator. Please enter one of: +,-,*,/,^")
            new_oper = self.math_request.get_oper()

            if new_oper.lower() == "exit":
                print("Exiting...")
                return False

            self.math_request.oper = new_oper

        return True

