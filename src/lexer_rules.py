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
tokens = ['EQUAL', 'CONST', 'IDENT'] + list(reserved.values())

# Simple lexical rules and literals
t_EQUAL = r'=='
literals = ['.', ';', '{', '}', '(', ')', '=', '+', '-', '<', '>', ',']


# A string containing ignored characters (spaces, tabs and new lines)
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'


def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value, 'IDENT')
    return t


# Complex lexical rules
def t_CONST(token):
    r'[0-9][0-9]*'
    token.value = int(token.value)
    return token


def t_NEWLINE(token):
    r'\n+'
    token.lexer.lineno += len(token.value)


def t_error(token):
    message = 'Unknown token:'
    message = '\nType: ' + token.type
    message += '\nValue: ' + str(token.value)
    message += '\nLine: ' + str(token.lineno)
    message += '\nPosition: ' + str(token.lexpos)
    raise Exception(message)
