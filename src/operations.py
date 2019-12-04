import re
import numbers

# Create the environment to store and retreive variables from
variables = {}


def convert_ident_value(s):
    s = float(variables[s]) if s in list(variables.keys()) else s
    return s


def convert_variables(p):
    p[1] = convert_ident_value(p[1])
    p[2] = convert_ident_value(p[2])
    return p


def evaluate(p):
    if type(p) == tuple and len(p) == 3:
        p = list(p)
        p = convert_variables(p)
        if type(p[2]) == tuple:
            p[2] = evaluate(p[2])
        if p[0] == "+":
            return p[1] + p[2]
        elif p[0] == '-':
            return p[1] - p[2]
        elif p[0] == '>':
            return p[1] > p[2]
        elif p[0] == '<':
            return p[1] < p[2]
        elif p[0] == '==':
            return p[1] == p[2]
    elif isinstance(p, numbers.Number):
        return float(p)
    else:
        return convert_ident_value(p)


def run_line(p):
    'Recursive function that "walks" the tree generated by the parser'
    global variables
    if p[0] == 'VAR':
        variables[p[1]] = 0
    elif p[0] == 'INPUT':
        value = input("Valor de la variable " + p[1] + ": ")
        variables[p[1]] = float(value)
    elif p[0] == 'OUTPUT':
        value = evaluate(p[1])
        print(value)
    elif p[0] in '=':
        variables[p[1]] = evaluate(p[2])
    elif p[0] == 'IF':
        condition = evaluate(p[1])
        if condition:
            print(p[2])
            for subline in list(p[2]):
                run_line(subline)


def run(program):
    for p in program:
        run_line(p)
    print(variables)
