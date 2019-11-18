from prettytable import PrettyTable


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def print_lexer_table(lexer):
    lexer_table = PrettyTable()
    lexer_table.field_names = ['Line', 'Token', 'Associated value']

    for token in lexer:
        lexer_table.add_row([token.lineno, token.type, token.value])
    print(lexer_table)

    f = open('lexer_table.txt', 'w')
    f.write(lexer_table.get_string())
    f.close()
