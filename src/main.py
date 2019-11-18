from ply.lex import lex
import lexer_rules
from os import path
from helpers import print_lexer_table

script_dir = path.dirname(__file__)
source_code = path.join(script_dir, 'program.txt')

f = open(source_code, 'r')

text = f.read()
lexer = lex(module=lexer_rules)
lexer.input(text)

print_lexer_table(lexer)
