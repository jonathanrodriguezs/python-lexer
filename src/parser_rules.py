from lexer_rules import tokens
from operations import run

# We must define a function for every production
# Non terminals are in lowercase
# Terminals are in uppercase (tokens)


def p_program_statements(p):
    '''
        program : statements "."
                | empty
    '''
    p[0] = p[1]
    run(p[0])


def p_statements_statements(p):
    'statements : statements ";" statement'
    p[0] = p[1] + (p[3],)


def p_statement_curly(p):
    'statement : "{" statements "}"'
    p[0] = p[2]


def p_statements_stat(p):
    'statements : statement'
    p[0] = (p[1],)


def p_statements_statement(p):
    '''
      statement : assign-stat
                | if-stat
                | while-stat
                | input-stat
                | output-stat
                | var-statement
    '''
    p[0] = p[1]


def p_var_statement_colon_ident(p):
    'var-statement : var-statement "," IDENT'
    p[0] = p[1] + (p[3],)


def p_var_statement_ident(p):
    'var-statement : VAR IDENT'
    p[0] = ('VAR', p[2])


def p_assin_stat(p):
    'assign-stat : IDENT "=" expr'
    p[0] = ('=', p[1], p[3])


def p_expr_parens(p):
    'expr : "(" expr ")"'
    p[0] = p[2]


def p_expr_arith_operation(p):
    '''
      expr : expr "+" value
           | expr "-" value
    '''
    p[0] = (p[2], p[1], p[3])


def p_expr_signed_value(p):
    '''
      expr : "+" value
           | "-" value
    '''
    p[0] = (p[1], p[2])


def p_expr_value(p):
    'expr : value'
    p[0] = p[1]


def p_value_const(p):
    'value : CONST'
    p[0] = p[1]


def p_value_ident(p):
    'value : IDENT'
    p[0] = p[1]


def p_if_statement(p):
    '''
      if-stat : if-then
              | if-then-else
    '''
    p[0] = p[1]


def p_if_then(p):
    'if-then : if-part THEN statement'
    p[0] = ('IF', p[1], p[3])


def p_if_then_else(p):
    'if-then-else : if-then ELSE statement'
    p[0] = p[1] + ('ELSE', p[3])


def p_if_part(p):
    'if-part : IF log-expr'
    p[0] = p[2]


def p_log_expr(p):
    '''
      log-expr : expr ">" expr
               | expr "<" expr
               | expr EQUAL expr
    '''
    p[0] = (p[2], p[1], p[3])


def p_while_stat(p):
    'while-stat : while-part do-expr'
    p[0] = ('WHILE', p[1]) + p[2]


def p_while_part(p):
    'while-part : WHILE log-expr'
    p[0] = p[2]


def p_do_expr(p):
    'do-expr : DO statement'
    p[0] = ('DO', p[2])


def p_input_statement(p):
    'input-stat : INPUT IDENT'
    p[0] = ('INPUT', p[2])


def p_output_statement(p):
    'output-stat : OUTPUT expr'
    p[0] = ('OUTPUT', p[2])


def p_empty(p):
    'empty :'
    p[0] = None


def p_error(p):
    print("Syntax error found! {}".format(p))
