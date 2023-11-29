# Implementation of the recursive descent parser
class ArithmeticParser:
    def __init__(self, expression):
        self.tokens = self.tokenize(expression)
        self.current_token_index = 0

    def tokenize(self, expression):
        # Simple tokenizer to split the expression into numbers and operators
        tokens = []
        value = ''
        for char in expression:
            if char.isdigit() or char == '.':
                value += char  # Build up the number
            else:
                if value:
                    tokens.append(float(value))  # End of a number
                    value = ''
                if char in '+-*/^':
                    tokens.append(char)  # Operator
        if value:
            tokens.append(float(value))  # Last number, if any
        return tokens

    def parse(self):
        return self.expression()

    def expression(self):
        # Parse an expression (with + or -)
        result = self.term()
        while self.current_token() in ('+', '-'):
            if self.current_token() == '+':
                self.eat('+')
                result += self.term()
            elif self.current_token() == '-':
                self.eat('-')
                result -= self.term()
        return result

    def term(self):
        # Parse a term (with * or /)
        result = self.factor()
        while self.current_token() in ('*', '/'):
            if self.current_token() == '*':
                self.eat('*')
                result *= self.factor()
            elif self.current_token() == '/':
                self.eat('/')
                divisor = self.factor()
                if divisor == 0:
                    raise ValueError("Division by zero")
                result /= divisor
        return result

    def factor(self):
        # Parse a factor (with ^ for exponentiation)
        result = self.base()
        if self.current_token() == '^':
            self.eat('^')
            result **= self.factor()
        return result

    def base(self):
        # Parse a base (number)
        token = self.current_token()
        self.eat(token)
        return token

    def current_token(self):
        # Get the current token or None if at the end
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None

    def eat(self, token):
        # Consume a token if it's the expected one, or raise an error
        if self.current_token() == token:
            self.current_token_index += 1
        else:
            raise ValueError(f"Unexpected token: {self.current_token()}")


def evaluate_expression(expression):
    parser = ArithmeticParser(expression)
    return parser.parse()


# Example usage:
expression = "3 + 5 * 2 ^ 3"
result = evaluate_expression(expression)
print(f"The result of '{expression}' is {result}")
