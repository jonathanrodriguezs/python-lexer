import re

variables = {}
# Create the environment upon which we will store and retreive variables from.


def binary_operation(operation):
    pass


def evaluate(p):
    p = list(p)
    if type(p[2]) == tuple:
        p[2] = evaluate(p[2])
    if p[0] == "+":
        return p[1] + p[2]


def run_line(p):
    'Recursive function that "walks" the tree generated by the parser'
    global variables
    # for p in lines:
    if p[0] == 'VAR':
        variables[p[1]] = None
    elif p[0] == 'INPUT':
        value = input("Valor de la variable " + p[1] + ": ")
        variables[p[1]] = value
        # elif p[0] == '=':


def run(program):
    for p in program:
        run_line(p)
    print(variables)
