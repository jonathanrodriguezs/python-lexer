from ply.lex import lex
from ply.yacc import yacc
import lexer_rules
import parser_rules
from os import path
from helpers import find_column

script_dir = path.dirname(__file__)
source_code = path.join(script_dir, 'program.txt')

f = open(source_code, 'r')

text = f.read()
lexer = lex(module=lexer_rules)

parser = yacc(module=parser_rules)

expression = parser.parse(text)
print(expression.evaluate())
