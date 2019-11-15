import lexer_rules
from ply.lex import lex

f = open('program.txt', 'r')

text = f.read()
lexer = lex(module = lexer_rules)
lexer.input(text)
token = lexer.token()

while token is not None:
  print('{}: {}'.format(token.type, token.value))
  token = lexer.token()
