# Reserved words
reserved = {
  'var': 'VAR',
  'if': 'IF',
  'then': 'THEN',
  'else': 'ELSE',
  'while': 'WHILE',
  'do': 'DO',
  'input': 'INPUT',
  'output': 'OUTPUT'
}

# List of tokens (characters and symbolss)
tokens = [
  'DOT',
  'SEMICOLON',
  'LCURLY',
  'RCURLY',
  'LPAREN',
  'RPAREN',
  'ASSIGN',
  'PLUS',
  'MINUS',
  'LESSTHAN',
  'GREATHERTHAN',
  'EQUAL',
  'COLON',
  'IDENT',
  'CONST',
  'ID'
] + list(reserved.values())

# Simple lexical rules
t_DOT = r'\.'
t_SEMICOLON = r';'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_LESSTHAN = r'<'
t_GREATHERTHAN = r'>'
t_EQUAL = r'=='
t_COLON = r','
t_IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'

# A string containing ignored characters (spaces, tabs and new lines)
t_ignore  = ' \t'

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  # Check for reserved words
  t.type = reserved.get(t.value,'IDENT')
  return t

# Complex lexical rules
def t_CONST(token):
  r'[1-9][0-9]*'
  token.value = int(token.value)
  return token

def t_NEWLINE(token):
  r'\n+'
  token.lexer.lineno += len(token.value)

def t_error(token):
  message = 'Token desconocido:'
  message = '\nType: ' + token.type
  message += '\nValue: ' + str(token.value)
  message += '\nLine: ' + str(token.lineno)
  message += '\nPosition: ' + str(token.lexpos)
  raise Exception(message)
