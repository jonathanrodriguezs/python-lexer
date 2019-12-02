from lexer_rules import tokens

# We must define a function for every production
# Non terminals are in lowercase
# Terminals are in uppercase (tokens)


def p_program_statements(p):
    'program: statements .'
    p[0] = p[1]


def p_statements_statements(p):
    'statements: statements ";" statement'


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
    'var-statement: var-statement "," ident'


def p_var_statement_ident(p):
    'var-statement: "var" ident'


def p_assin_stat(p):
    'assign-stat: ident "=" expr'


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
      value: ident
           | const
    '''
    p[0] = p[1]


def p_if_statement(p):
    '''
      if-statement: if-then
                  | if-then-else
    '''
    p[0] = p[1]


def p_if_then(p):
    'if-then: if-part "then" statement'


def p_if_then_else(p):
    'if-then-else: if-then "else" statement'


def p_if_part(p):
    'if-part: "if" log-expr'


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
    'while-part: "while" log-expr'


def p_do_expr(p):
    'do-expr: "do" statement'


def p_input_statement(p):
    'input-stat: "input" ident'


def p_output_statement(p):
    'output-stat: "output" expr'


def p_error(expr):
    print(expr)
    raise Exception("Syntax error.")
