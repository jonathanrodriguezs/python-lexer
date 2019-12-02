from lexer_rules import tokens

# We must define a function for every production
# Non terminals are in lowercase
# Terminals are in uppercase (tokens)


def p_program_statements(p):
    'program: statements .'
    p[0] = p[1]


def p_statements_statements(p):
    '''
        statements: statements ";" statement
                  | statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_statement_curly(p):
    'statement: "{" statements "}"'
    p[0] = p[2]


def p_statements_statement(p):
    '''
      statements: statement
                | assign-stat
                | if-stat
                | while-stat
                | input-stat
                | output-stat
                | var-statement
    '''
    p[0] = p[1]


def p_var_statement_colon_ident(p):
    'var-statement: var-statement "," IDENT'


def p_var_statement_ident(p):
    'var-statement: "var" IDENT'


def p_assin_stat(p):
    'assign-stat: IDENT "=" expr'


def p_expr_parens(p):
    'expr: "(" expr ")"'
    p[0] = p[2]


def p_expr_arith_operation(p):
    '''
      expr: expr "+" value
          | expr "-" value
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expr_signed_value(p):
    '''
      expr: "+" value
          | "-" value
    '''
    if p[1] == '+':
        p[0] = p[2]
    elif p[2] == '-':
        p[0] = - p[2]


def p_expr_value(p):
    'expr: value'
    p[0] = p[1]


def p_value_ident(p):
    '''
      value: IDENT
           | CONST
    '''
    p[0] = p[1]


def p_if_statement(p):
    '''
      if-statement: if-then
                  | if-then-else
    '''
    p[0] = p[1]


def p_if_then(p):
    'if-then: if-part THEN statement'


def p_if_then_else(p):
    'if-then-else: if-then ELSE statement'


def p_if_part(p):
    'if-part: IF log-expr'


def p_log_expr(p):
    '''
      log-expr: expr ">" expr
              | expr "<" expr
              | expr "==" expr
    '''
    if p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[2]


def p_while_stat(p):
    'while-stat: while-part do-expr'


def p_while_part(p):
    'while-part: WHILE log-expr'


def p_do_expr(p):
    'do-expr: DO statement'


def p_input_statement(p):
    'input-stat: INPUT IDENT'


def p_output_statement(p):
    'output-stat: OUTPUT expr'


def p_error(expr):
    print(expr)
    raise Exception("Syntax error.")
