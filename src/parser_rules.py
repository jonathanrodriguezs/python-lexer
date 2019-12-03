from lexer_rules import tokens

# We must define a function for every production
# Non terminals are in lowercase
# Terminals are in uppercase (tokens)

variables = {}


def p_program_statements(p):
    'program : statements "."'
    p[0] = p[1]
    print(variables)


def p_statements_statements(p):
    'statements : statements ";" statement'
    p[0] = p[1] + [p[3]]


def p_statement_curly(p):
    'statement : "{" statements "}"'
    p[0] = p[2]


def p_statements_stat(p):
    'statements : statement'
    p[0] = p[1]


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
    p[0] = [p[1] + [p[3]]]


def p_var_statement_ident(p):
    'var-statement : VAR IDENT'
    p[0] = ['VAR', p[2]]
    variables[p[2]] = 0


def p_assin_stat(p):
    'assign-stat : IDENT "=" expr'
    print("+ Assigning variable", p[1], "to", p[3])
    variables[p[1]] = p[3]


def p_expr_parens(p):
    'expr : "(" expr ")"'
    p[0] = p[2]


def p_expr_arith_operation(p):
    '''
      expr : expr "+" value
           | expr "-" value
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expr_signed_value(p):
    '''
      expr : "+" value
           | "-" value
    '''
    if p[1] == '+':
        p[0] = p[2]
    elif p[2] == '-':
        p[0] = - p[2]


def p_expr_value(p):
    'expr : value'
    p[0] = p[1]


def p_value_const(p):
    'value : CONST'
    p[0] = p[1]


def p_value_ident(p):
    'value : IDENT'
    p[0] = variables[p[1]]


def p_if_statement(p):
    '''
      if-stat : if-then
              | if-then-else
    '''
    p[0] = p[1]


def p_if_then(p):
    'if-then : if-part THEN statement'


def p_if_then_else(p):
    'if-then-else : if-then ELSE statement'


def p_if_part(p):
    'if-part : IF log-expr'


def p_log_expr(p):
    '''
      log-expr : expr ">" expr
               | expr "<" expr
               | expr EQUAL expr
    '''
    if p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[2]


def p_while_stat(p):
    'while-stat : while-part do-expr'


def p_while_part(p):
    'while-part : WHILE log-expr'


def p_do_expr(p):
    'do-expr : DO statement'


def p_input_statement(p):
    'input-stat : INPUT IDENT'
    p[0] = ['INPUT', p[2]]


def p_output_statement(p):
    'output-stat : OUTPUT expr'
    print(p[2])
    p[0] = ['OUTPUT', p[2]]


def p_error(expr):
    print(expr)
    raise Exception("Syntax error.")
