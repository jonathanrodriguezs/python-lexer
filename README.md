# Python LMC

Dependencies: [ply](https://www.dabeaz.com/ply/)
To install please run in a terminal:

```bash
python install ply
```

## Run the project

### Native

You must have Python 3+ installed in your machine. To install the libraries and run the script write the following in your command line if you don't have "ply":

```bash
pip install -r requirements.txt
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
