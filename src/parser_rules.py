from lexer_rules import tokens
from operator import add
from expressions import BinaryOperation, Number


# We must define a funct. like this for every production
# Non terminals are in lowercase
# Terminals are in uppercase (tokens)


def p_expression_plus(expr):
    'expression : term PLUS term'
    expr[0] = BinaryOperation(expr[1], expr[3], add)


def p_term_number(expr):
    'term : CONST'
    expr[0] = Number(expr[1])


def p_error(expr):
    raise Exception("Syntax error.")
