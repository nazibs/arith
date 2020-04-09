# Building a simple interpreter https://ruslanspivak.com/lsbasi-part1/
# Token types

INTEGER, PLUS, MINUS, MUL, SPACE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'SPACE', 'EOF'

class Token():
    def __init__(self, type, value):
        self.type = type
        self.value = value


class Interpreter():
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
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
        print('inside get_complete_integer')
        integer_value = ''
        while self.current_char is not None and self.current_char.isdigit():
            print('self.current_char:',self.current_char)
            integer_value += self.current_char
            self.next_character()
        print('returning complete integer:',integer_value)
        return int(integer_value)

    def get_next_token(self):
        text = self.text

        # print('get_next_token :: text:', text)

        if self.pos > len(text)-1:
            return Token(EOF, None)

        # current_char = text[self.pos]
        while self.current_char is not None:
            print('get_next_token :: current_char:', self.current_char)
            if self.current_char.isdigit():
                token = Token(INTEGER, self.get_complete_integer())
                # self.next_character()
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

            self.error()
        return Token(EOF, None)

    def eat(self, token_type):
        print('eat:: token_type:', token_type)
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        result = 0
        left = self.current_token
        print('left.type:', left.type, ' left.value:', left.value)
        self.eat(INTEGER)

        while self.current_token.type is not EOF:

            # print('self.current_token type:', self.current_token.type)

            op = self.current_token
            print('op.type:', op.type, ' op.value:', op.value)
            self.eat(self.current_token.type)

            # if self.current_token.type == SPACE:
            #     self.current_token = self.get_next_token()

            right = self.current_token
            print('right.type:', right.type, ' right.value:', right.value)
            self.eat(INTEGER)

            if op.value == '+':
                result = left.value + right.value
            elif op.value == '-':
                result = left.value - right.value
            else:
                result = left.value * right.value

            left = Token(INTEGER, result)

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

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print('Result:', result)

if __name__ == '__main__':
    main()


