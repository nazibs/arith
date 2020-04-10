# Building a simple interpreter https://ruslanspivak.com/lsbasi-part1/
# Token types

INTEGER, PLUS, MINUS, MUL, DIV, SPACE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'SPACE', 'EOF'

class Token():
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer():
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error in parsing the input')

    def skip_whitespaces(self):
        while self.current_char is not None and self.current_char.isspace():
            self.next_character()

    def next_character(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def get_complete_integer(self):
        integer_value = ''
        while self.current_char is not None and self.current_char.isdigit():
            integer_value += self.current_char
            self.next_character()
        return int(integer_value)

    def get_next_token(self):
        text = self.text

        if self.pos > len(text)-1:
            return Token(EOF, None)

        while self.current_char is not None:
            if self.current_char.isdigit():
                token = Token(INTEGER, self.get_complete_integer())
                return token
            if self.current_char.isspace():
                self.skip_whitespaces()
                continue
            if self.current_char == '+':
                token = Token(PLUS, self.current_char)
                self.next_character()
                return token
            if self.current_char == '-':
                token = Token(MINUS, self.current_char)
                self.next_character()
                return token
            if self.current_char == '*':
                token = Token(MUL, self.current_char)
                self.next_character()
                return token
            if self.current_char == '/':
                token = Token(DIV, self.current_char)
                self.next_character()
                return token

            self.error()
        return Token(EOF, None)


class Interpreter():
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Error in parsing the input')

    def eat(self, token_type):
        print('eat:: token_type:', token_type)
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()


    def compute_mul_div(self):
        print('inside compute_mul_div')

        result = self.current_token.value
        self.eat(INTEGER)

        while self.current_token.type in (MUL, DIV):
            if self.current_token.type == MUL:
                self.eat(self.current_token.type)
                result = result * self.current_token.value
                self.eat(INTEGER)
            elif self.current_token.type == DIV:
                self.eat(self.current_token.type)
                result = result / self.current_token.value
                self.eat(INTEGER)

        print('returning from compute_mul_div:', result)
        return result


    def compute_add_sub(self):
        print('inside compute_add_sub')
        result = self.compute_mul_div()

        print('computing add sub')
        while self.current_token.type in (PLUS, MINUS):
            if self.current_token.type == PLUS:
                self.eat(self.current_token.type)
                result = result + self.compute_mul_div()
                # self.eat(INTEGER)
            elif self.current_token.type == MINUS:
                self.eat(self.current_token.type)
                result = result - self.compute_mul_div()
                # self.eat(INTEGER)

        print('returning from compute_add_sub')
        return result

def main():
    while True:
        try:
            text = input()
            print('Input: ', text)
        except EOFError:
            break
        if not text:
            continue

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.compute_add_sub()
        print('Result:', result)

if __name__ == '__main__':
    main()






