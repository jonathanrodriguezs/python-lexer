from lexer_rules import tokens
from operator import add, sub
from expressions import BinaryOperation, Number


# We must define a function for every production
# Non terminals are in lowercase
# Terminals are in uppercase (tokens)

def p_expr_plus(p):
    'expr : expr PLUS term'
    p[0] = BinaryOperation(p[1], p[3], add)


def p_expr_minus(p):
    'expr : expr MINUS term'
    p[0] = BinaryOperation(p[1], p[3], sub)


def p_expr_term(p):
    'expr : term'
    p[0] = p[1]


def p_term_number(expr):
    'term : CONST'
    expr[0] = Number(expr[1])


def p_error(expr):
    raise Exception("Syntax error.")
