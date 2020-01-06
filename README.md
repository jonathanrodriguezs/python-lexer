# Python LMC

## Considerations

This project is a parser based on the grammar described in the file lmc_syntax.txt, just consider that it ONLY HOLDS variables with NUMERIC values.

## Run the project

### Native

You must have Python 3+ installed in your machine. To install the required dependency ("ply") and run the script write the following in your command line:

```bash
pip install ply
python src/main.py
```

### Docker

Run the following comand to build and run the image:

```bash
docker build -t python-lmc .
docker run python-lmc
```

### Optimized version

If you want to run the main script in optimized mode (python -o), you must change the lexer construction line to:

```python
  lexer = lex(module=lexer_rules, optimized=1)
```

Then a file with the name lextab.py will be generated, containing all the regular expression attached to the docstring functions for complex lexical rules.

## Program example
An implementation of the Fibonacci sequence.
```
var iteration, i, x, y, z;
input iteration;
x = 0;
y = 1;
i = 0;
while iteration > i do {
  output x;
  z = x + y;
  # Modify values
  x = y;
  y = z;
  i = i + 1
}.
```
