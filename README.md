# ARITH
This work is a part of the course homework for Programming Languages. The task is to create an interpreter for the ARITH language that allows addition and multiplication of integers.

### Requirements:
1. Python 3
2. PyInstaller 3.6


Following are the requirements of the homework assignment:
1. An Abstract Syntax Tree (AST) of ARITH.
2. A parser for ARITH.
3. Interpreter for the AST.


Below is the flow and description of the python code:
1. The script will take the input from the standard input and give the output result via standard output.
2. Lexer will go through the input string and tokenize it.
3. Parser will create the Abstract Syntax Tree based on the Grammar of the ARITH.
4. Interpreter will evaluate the created AST and output the result.


### Features added:
Below are the additional features that I have added on top of the basic requirements:
1. There is no restriction of assuming exactly 1 whitespace between characters. The script will remove/ignore any number of whitespaces between each character.
2. The script also allows subtraction and division on top of the addition and multiplication. Although I haven't handled the special cases for the division like divide by 0. The script will return float when the division operand is involved in the input string.


### References:
I started with the class slides on the ARITH and mainly followed the blog 'Let’s Build A Simple Interpreter' by Ruslan Spivak.

1. Class slides: https://canvas.ucsc.edu/courses/32489/files/2090037
2. Blog's part 1 helped me to get started: https://ruslanspivak.com/lsbasi-part1/
3. Blog's part 4 helped me with precedence for multiplication and division: https://ruslanspivak.com/lsbasi-part4/
4. Blog's part 7 helped me in building the AST: https://ruslanspivak.com/lsbasi-part7/

