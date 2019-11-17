from ply.lex import lex
import lexer_rules
from os import path

from helpers import find_column

script_dir = path.dirname(__file__)
source_code = path.join(script_dir, 'program.txt')

f = open(source_code, 'r')

text = f.read()
lexer = lex(module=lexer_rules)
lexer.input(text)

for token in lexer:
    print('{}: {}'.format(token.type, token.value))
    # print(token)
